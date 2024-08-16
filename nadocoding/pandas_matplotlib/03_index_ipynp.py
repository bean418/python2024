# -*- coding: utf-8 -*-
"""03_Index.ipynp

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OCcHtCXrmgsJmGbnWEBH2NoCa-PGNBBb
"""

import pandas as pd

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
data

df = pd.DataFrame(data, index = ["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번"])

df.head()

df.index

"""## set name of index"""

df.index.name = "지원번호"
df.head()

"""## Initialize name of index"""

df.reset_index()

# 기존의 index 정보는 변수가 된다.

df.reset_index(drop = True)

# 위 함수는 call-by-value이므로 객체를 복사하는 것이다.
# 따라서 다시 값을 할당해주어야 함.

df = df.reset_index(drop = True)
df.head()

# 또는 inplace = True (inplcae: 제자리)

df.index.name = "지원번호"
print(df.head(2), '\n')
df.reset_index(drop = True, inplace = True)
print(df.head(2))

# 값을 할당하지 않아도 인덱스가 사라진 것을 확인

"""## Set Index"""

df.set_index("이름", inplace = True)

# 변수를 인덱스로 설정하기

df.head()

"""## Sort Index"""

df.sort_index(inplace = True) # 인덱스로 '오름차순' 정리

# 내림차순 : ascending = False

df.head()