# -*- coding: utf-8 -*-
"""04_style.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tmo_unpYu0sOdOEMhbHObPDceR5C_UkD
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

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)

"""## Marker

https://matplotlib.org/stable/api/markers_api.html
"""

plt.plot(x, y, linewidth=5)

plt.plot(x, y, marker='o')

plt.plot(x, y, marker='o', linestyle="None")

plt.plot(x, y, marker='v')

plt.plot(x, y, marker='v', markersize=10)

plt.plot(x, y, marker='X', markersize=20)

plt.plot(x, y, marker='X', markersize=20, markeredgecolor='red')

plt.plot(x, y, marker='X', markersize=20, markeredgecolor='red',
         markerfacecolor='yellow')

"""## Line Style"""

plt.plot(x, y, linestyle=':')

plt.plot(x, y, '--') # 생략가능?

plt.plot(x, y, '-.')

"""## Color"""

x2 = [1,2,3,4]
y2 = [2,3,4,5]

plt.plot(x, y, color='pink', label='pink')
plt.plot(x2, y2, color='g', label='green')
plt.legend()

"""## Format"""

plt.plot(x, y, 'ro--') # color, markerstyle, linestyle

plt.plot(x, y, 'gv-.')

plt.plot(x, y, 'go') # linestyle을 None으로 설정한 것과 같은 결과

"""## abbreviation"""

plt.plot(x, y, marker='o', mfc='r', ms=10, mec='b', ls=':')
# markerFaceColor, markerSize, markerEdgeColor, lineStyle

"""## alpha"""

plt.plot(x, y, color='red', label='red')
plt.plot(x2, y2, color='b', label='blue', alpha=0.3) # 투명도
plt.legend()

"""## Size"""

plt.figure(figsize=(10,5))
plt.plot(x, y)

plt.figure(figsize=(10, 5), dpi=200) # dots per inch
plt.plot(x, y)

plt.figure(figsize=(10, 5), dpi=50)
plt.plot(x, y)

"""## Background Color"""

plt.figure(facecolor="yellow")
plt.plot(x, y)

# google에 color picker를 활용하면 원하는 rgb 값을 가져오기 용이함.

plt.figure(facecolor="#0cdde8")
plt.plot(x, y)

# commit 240825
# commit 240826