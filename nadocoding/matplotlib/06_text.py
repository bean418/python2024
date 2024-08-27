# -*- coding: utf-8 -*-
"""06_text.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mqN_isPdjU5Bt1fuk19bd4GVM1NJiHGh
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mp

!wget https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Regular.ttf
!wget https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Bold.ttf
!fc-cache -fv
!rm ~/.cache/matplotlib -rf

font_dirs = './'
font_files = fm.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    fm.fontManager.addfont(font_file)
plt.rc('font', family='NanumGothic')

mp.rcParams['font.size'] = 15
mp.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3, 4, 5]
y = [2, 4, 8, 16, 32]

plt.plot(x, y)

plt.plot(x, y, marker='o')

for idx, txt in enumerate(y):
    plt.text()

# 240827
