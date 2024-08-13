# -*- coding: utf-8 -*-
"""Movie_Recommendation_System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dgLIJM2lQixBBgf9x4-jEetSEbAiShoz

# Load data
"""

import pandas as pd
import numpy as np
df1 = pd.read_csv("https://github.com/bean0418/python2024/blob/main/nadocoding/data/tmdb_5000_credits.csv?raw=true")
df2 = pd.read_csv("https://github.com/bean0418/python2024/blob/main/nadocoding/data/tmdb_5000_movies.csv?raw=true")

# data가 있는 url + "?raw=true"를 통해서 바로 불러오기

df1.head()

df2.head()

"""# 1. Demographic Filtering"""

df1['title'].equals(df2['title'])

# 두 데이터의 값이 같다.
# -> df1의 title은 없애고 id를 기준으로 두 데이터프레임을 병합한다.

df1.columns

df1.columns = ['id', 'title', 'cast', 'crew']
df1.head()

# rename columns (movie_id -> id)

df1[['id', 'title', 'cast', 'crew']]

df = df2.merge(df1[['id', 'cast', 'crew']], on = 'id')
df.head()

# df의 id, cast, crew를 id를 기준으로 merge (title은 제외)

C = df["vote_average"].mean()
C

m = df["vote_count"].quantile(0.9) # 상위 10%
m

q_movies = df2.copy().loc[df["vote_count"] >= m]
q_movies.shape

q_movies["vote_count"].sort_values() # 상위 10%가 1838이었으므로 데이터가 잘 인덱싱된 것을 확인.

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m) * R) + (m / (m + v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis = 1) # q_movies의 모든 데이터들에 대해 weighted_rating 함수를 적용시킴.
q_movies.head()

q_movies = q_movies.sort_values("score", ascending = False) # 오름차순 = false -> 내림차순
q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10)

# 기존 데이터에서 영화의 인기도를 측정하는 측도인 popularity를 기준으로 시각화

pop= df.sort_values('popularity', ascending=False)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(10),pop['popularity'].head(10), align='center',
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")

"""# 2. Content Based Filtering"""

df['overview'].head()

# 목적: overview의 글을 분석하여 유사 콘텐츠를 추천하는 방식

"""## Bag Of Words - BOW
### I am a boy
### I am a girl
### I(2), am(2), a(2), boy(1), girl(1)로 분리 (횟수)

###        I   am  a   boy   girl
### 문장1:  1    1  1    1     0
### 문장2:  1    1  1    0     1
### 문서 100개, 모든 문서에서 나온 단어가 10,000개라면
### 100 x 10,000 의 행렬으로 표현

1. TfidVectorizer (TF-IDF 기반의 벡터화)
-> 중요도가 낮은 a, the와 같은 관사에 가중치를 적게 지정함으로써
학습의 정확도를 높임
2. CountVectorizer
"""

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words = "english")

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
ENGLISH_STOP_WORDS

# stop_words = 중요도가 낮은 단어들

df['overview'].isnull().values.any()

df['overview'] = df['overview'].fillna("")

df['overview'].isnull().values.any()

tfidf_matrix = tfidf.fit_transform(df['overview'])
tfidf_matrix.shape

# 4803개의 문서들이 20978개의 단어들로 이루어져있다. stop_words 제외

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim # cosine similarity -> symmetric matrix

cosine_sim.shape

indices = pd.Series(df.index, index = df['title']).drop_duplicates()
indices

indices["Spectre"]

df.iloc[[2]]

"""### 영화의 제목을 입력하면 코사인 유사도를 통해 가장 유사도가 높은 상위 10개 영화 목록 반환하는 함수"""

def get_recommendations(title, cosine_sim = cosine_sim):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = indices[title]

    # 코사인 유사도 매트릭스(cosine_sim)에서 idx에 해당하는 데이터를 [idx, 유사도] 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

    # 자기 자신(코사인 유사도 = 1)을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]

    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]

    # 인덱스 정보를 통해 영화 제목 추출
    return(df['title'].iloc[movie_indices])

# test_idx = indices["The Dark Knight Rises"] # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
# test_idx -> 3

# test_sim_scores = list(enumerate(cosine_sim[3])) # 코사인 유사도 매트릭스 (cosine_sim)에서 idx에 해당하는 데이터를 [idx, 유사도] 형태로 얻기

# test_sim_scores = sorted(test_sim_scores, key = lambda x: x[1], reverse = True)
# test_sim_scores[1:11] # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
# 인덱스 0에는 자기 자신(추천도가 가장 높음)이 위치해있음.

# lambda 알아보기
# def get_second(x):
#    return x[1]

# lst = ['인덱스', '유사도']
# print(get_second(lst))

# (lambda x : x[1])(lst)

# 추천 영화
# test_movie_indices = [i[0] for i in test_sim_scores[1:11]]
# test_movie_indices

df['title'][:20]

get_recommendations("Avengers: Age of Ultron")

get_recommendations("The Avengers")

get_recommendations("Avatar")

"""# 3. Credits, Genres and Keywords Based Recommender"""

df.head(3)

df.loc[0, 'genres']

s1 = [{"id": 28, "name": "Action"}]
s2 = '[{"id": 28, "name": "Action"}]'

type(s1), type(s2)

from ast import literal_eval
s2 = literal_eval(s2)
s2, type(s2)

print(s1)
print(s2)

# 따라서 literal_eval -> '[{~~}]'처럼 리스트 형태로 입력된 문자열을 리스트로 변환해줌.

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    df[feature] = df[feature].apply(literal_eval)

df.loc[0, 'crew']

# crew에서 job이 director인 사람의 name만 가져오는 함수를 만들어야 함.

def get_director(dic_list):
    for i in dic_list:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

df['director'] = df['crew'].apply(get_director)
df['director']

df[df['director'].isnull()]

df.loc[0, 'cast']

df.loc[0, 'genres']

df.loc[0, 'keywords']

# We are going to build a recommender based on the following metadata:
# the 3 top actors, the director, related genres and the movie plot keywords.

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        if len(names) > 3:
            names = names[:3]
        return names
    return [] # exception

features = ['cast', 'keywords', 'genres']
for feature in features:
    df[feature] = df[feature].apply(get_list)

df[['title', 'cast', 'director', 'keywords', 'genres']].head(3)

'''
The next step would be to convert the names and keyword instances into lowercase
and strip all the spaces between them.
This is done so that our vectorizer doesn't count
the Johnny of "Johnny Depp" and "Johnny Galecki" as the same.
'''

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(' ', '')) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(' ', ''))
        else:
            return ''

features = ['cast', 'keywords','director', 'genres']
for feature in features:
    df[feature] = df[feature].apply(clean_data)

df[['title', 'cast', 'director', 'keywords', 'genres']].head(3)

'''
We are now in a position to create our "metadata soup",
which is a string that contains all the metadata that we want to feed to our vectorizer
(namely actors, director and keywords).

키워드, 캐스트, 감독, 장르 등을 공백으로 구분한 일명 '중요 데이터 잡탕'을 만든다.
'''

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
df['soup'] = df.apply(create_soup, axis=1)

df['soup'][:3]

df['overview'][:3]

# soup은 마치 overview처럼 공백으로 구분된 중요 단어들의 나열처럼 보임.

'''
The next steps are the same as what we did with our plot description based recommender.
One important difference is that we use the CountVectorizer() instead of TF-IDF.
This is because we do not want to down-weight the presence of an actor/director
if he or she has acted or directed in relatively more movies. It doesn't make much intuitive sense.

이전에 했던 것처럼 단어의 개수에 따른 코사인 유사도를 측정하면 된다.
중요한 차이점은 overview와 달리 soup에서 반복되는 단어들은 down-weight해서는 안된다.
overview에서 반복되는 단어들은 주로 a, the, in 등 전치사나 관사(중요하지 않은 단어)이고
soup에서 반복되는 단어들은 배우, 감독 등 중요한 단어들이므로 가중치가 동일해야 한다.
'''

from sklearn.feature_extraction.text import CountVectorizer

cnt = CountVectorizer(stop_words = 'english')
cnt_matrix = cnt.fit_transform(df['soup'])

cnt_matrix

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(cnt_matrix, cnt_matrix)
cosine_sim2

indices[:3]

# Reset index of our main DataFrame and construct reverse mapping as before
df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])