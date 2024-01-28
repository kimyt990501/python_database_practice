import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font', family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 각 연도별 경기가 있었던 기간 (월별)
# 01, 02, 03, 04, 06, 07, 11, 12, 16, 21, 22, 23
m_4_10 = range(4, 11)

# 05, 09
m_4_9 = range(4, 10)

# 10, 19
m_3_9 = range(3, 10)

# 08, 13, 14, 15, 17, 18
m_3_10 = range(3, 11)

# 20
m_5_10 = range(5, 11)

# 데이터 불러오기
wr_list = []
for month in m_5_10:
    match = pd.read_csv('samsung_matchdata_mine\\data\\samsung_match_data\\2020\\samsung_2020_' + str(month) + '_match_result.csv', encoding='euc-kr')
    
    # 승률 구해서 리스트에 저장
    res = match['결과'].count()
    wins = len(match.loc[match['결과'] == 'win'])
    wr = '%0.3f' % float(wins / res)
    temp = [str(month), wr]
    wr_list.append(temp)

# 데이터프레임 만들어서 월별 승률 저장
wr_2020 = pd.DataFrame(wr_list)
wr_2020.columns = ['월', '승률']
wr_2020 = wr_2020.set_index('월')
print(wr_2020)
wr_2020.to_csv('samsung_matchdata_mine\\data\\samsung_winning_rate\\wr_2020.csv', encoding='euc-kr')