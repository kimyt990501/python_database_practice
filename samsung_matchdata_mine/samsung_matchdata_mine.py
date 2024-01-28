#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font', family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 2001년부터 2023년까지의 승률 데이터 합친 csv 파일 불러오기
wr_01_23 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_01_23.csv', encoding='euc-kr').astype({'월':'int'})

wr_month = []

# 각 월별 승률끼리 평균구하기 
# (10월엔 경기수가 적기 때문에 결과에 영향을 줄수도 있기 때문에 생략)
for month in range(3, 10):
    is_month = wr_01_23['월'] == month
    wr = wr_01_23[is_month]
    wr.drop(["Unnamed: 0"], axis=1, inplace =True)
    wr = wr.set_index('월')
    temp = [month, '%0.3f' % wr['승률'].mean()]
    wr_month.append(temp)

wr_final = pd.DataFrame(wr_month)
wr_final.columns = ['월', '승률']
wr_final = wr_final.astype({'승률':'float'})

# 선 그래프로 시각화 하기
plt.figure(figsize = (12,10))

sns.lineplot(x='월',y='승률',data = wr_final, label = "종합")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=90)

# %%
