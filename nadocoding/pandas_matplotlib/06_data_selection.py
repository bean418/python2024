# -*- coding: utf-8 -*-
"""06_Data_Selection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xczCq1ZRU0S-am3FT0_8D4t1tMb48lUm
"""

import pandas as pd
import numpy as np

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', np.nan, np.nan, 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index = ["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번"])
df.index.name = "지원번호"

"""## Column 선택 (Using label)"""

df['이름']

df['키']

df[['이름', '키']]

"""## Column 선택 (Using integer index)"""