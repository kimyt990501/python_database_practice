import requests
from bs4 import BeautifulSoup
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# 웹페이지에서 타자 데이터 크롤링
url1 = 'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=0&ys='
url2 = '&ye='
url3 = '&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=30&si=&cn='

# 빈 데이터 프레임 만들어두기
df = pd.DataFrame(index = range(30), columns = ["순위", "선수명", "팀명", "WAR", "경기", "타석", "타수", "득점", "안타", "2루타", "3루타", "홈런", "루타", "타점", 
                                                 "도루", "도루실패", "볼넷", "사구", "고의사구", "삼진", "병살타", "희생타", "희생플라이", "타율", "출루율", "장타율", "OPS", "wOBA", "wRC+", "WAR2", "WPA"])

# 1982 ~ 2023 년까지의 타자 기록 크롤링하여 csv 파일로 저장
for year in range(1982, 2024):
    url = url1 + str(year) + url2 + str(year) + url3
    response = requests.get(url)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find_all("table")[0]
    # 중간에 추가 돼있는 칼럼을 제외하고 불러오기
    l = 0
    temp2 = temp.find_all("tr")[2]
    for j in range(2,36):
        temp2 = temp.find_all("tr")[j]
        if len(temp2.find_all("td")) == 31:
            for i in range(31):
                temp3 = temp2.find_all("td")[i]
                df.iloc[l,i] = temp3.get_text()
            l += 1
    #df = df.insert(1, '연도', str(year))
    df['연도'] = year
    # 만들어낸 데이터프레임을 csv 파일로 저장
    df.to_csv('C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_' + str(year) + '.csv', index=None, encoding='euc-kr')

# 저장해둔 타자 데이터 읽어와 하나의 데이터프레임으로 합친 후 csv로 저장
hitter_data = pd.read_csv('C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_1982.csv', encoding='euc-kr')
years = range(1983, 2024)
for year in years:
    path = 'C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_%d.csv' %year
    old = pd.read_csv(path, encoding='euc-kr')
    new = pd.concat([hitter_data, old], ignore_index=True)
    hitter_data = new
hitter_data.to_csv('data\\hitter_data.csv', index=None, encoding='euc-kr')