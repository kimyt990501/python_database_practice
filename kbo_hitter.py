import warnings
import pandas as pd

warnings.filterwarnings('ignore')

# 저장해둔 타자 데이터 읽어오기
hitter_data = pd.read_csv('C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_1982.csv', encoding='euc-kr')
years = range(1983, 2024)
for year in years:
    path = 'C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_%d.csv' %year
    old = pd.read_csv(path, encoding='euc-kr')
    new = pd.concat([hitter_data, old], ignore_index=True)
    hitter_data = new
print(hitter_data)
