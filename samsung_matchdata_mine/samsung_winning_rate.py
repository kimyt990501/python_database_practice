import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font', family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')
'''
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
'''

# 승률 csv 파일 불러오기
wr_2001 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2001.csv', encoding='euc-kr').astype({'월':'int'})
wr_2002 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2002.csv', encoding='euc-kr').astype({'월':'int'})
wr_2003 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2003.csv', encoding='euc-kr').astype({'월':'int'})
wr_2004 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2004.csv', encoding='euc-kr').astype({'월':'int'})
wr_2005 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2005.csv', encoding='euc-kr').astype({'월':'int'})
wr_2006 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2006.csv', encoding='euc-kr').astype({'월':'int'})
wr_2007 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2007.csv', encoding='euc-kr').astype({'월':'int'})
wr_2008 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2008.csv', encoding='euc-kr').astype({'월':'int'})
wr_2009 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2009.csv', encoding='euc-kr').astype({'월':'int'})
wr_2010 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2010.csv', encoding='euc-kr').astype({'월':'int'})
wr_2011 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2011.csv', encoding='euc-kr').astype({'월':'int'})
wr_2012 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2012.csv', encoding='euc-kr').astype({'월':'int'})
wr_2013 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2013.csv', encoding='euc-kr').astype({'월':'int'})
wr_2014 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2014.csv', encoding='euc-kr').astype({'월':'int'})
wr_2015 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2015.csv', encoding='euc-kr').astype({'월':'int'})
wr_2016 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2016.csv', encoding='euc-kr').astype({'월':'int'})
wr_2017 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2017.csv', encoding='euc-kr').astype({'월':'int'})
wr_2018 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2018.csv', encoding='euc-kr').astype({'월':'int'})
wr_2019 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2019.csv', encoding='euc-kr').astype({'월':'int'})
wr_2020 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2020.csv', encoding='euc-kr').astype({'월':'int'})
wr_2021 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2021.csv', encoding='euc-kr').astype({'월':'int'})
wr_2022 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2022.csv', encoding='euc-kr').astype({'월':'int'})
wr_2023 = pd.read_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_2023.csv', encoding='euc-kr').astype({'월':'int'})

#wr_2001, wr_2002, wr_2003, wr_2004, wr_2005, wr_2006, wr_2007, wr_2008, wr_2009, wr_2010, wr_2011, wr_2012, wr_2013, wr_2014, wr_2015, 
wr_01_23 = pd.concat([wr_2001, wr_2002, wr_2003, wr_2004, wr_2005, wr_2006, wr_2007, wr_2008, wr_2009, wr_2010, wr_2011, wr_2012, wr_2013, wr_2014, wr_2015, wr_2016, wr_2017, wr_2018, wr_2019, wr_2020, wr_2021, wr_2022, wr_2023], ignore_index = True)
#wr_01_23 = wr_01_23.set_index('월')
wr_01_23.to_csv('C:\\Users\\user\\Desktop\\python_database_practice\\python_database_practice\\samsung_matchdata_mine\\data\samsung_winning_rate\\wr_01_23.csv', encoding='euc-kr')
#print(wr_01_23)