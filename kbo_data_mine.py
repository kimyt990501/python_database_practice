#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns

# KBO 기록 데이터 크롤링
url = 'http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=1982&ye=2023&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&tr=&cv=&ml=1&sn=30&pa=0&si=&cn=&lr=1'

response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find_all("table")[0]

# 빈 데이터 프레임 만들어두기
df = pd.DataFrame(index = range(343), columns = ["순", "이름", "연도", "WAR", "-", "타석", "타수", "득점", "안타", "2루타", "3루타", "홈런", "루타", "타점", 
                                                 "도루", "도루실패", "볼넷", "사구", "고의사구", "삼진", "병살", "희생타", "희생플라이", "타율", "출루", "장타", 
                                                 "OPS", "wOBA", "wRC+", "WAR2", "--"])
# 중간에 추가 돼있는 칼럼을 제외하고 불러오기
l = 0
temp2 = temp.find_all("tr")[3]
for j in range(3,414):
    temp2 = temp.find_all("tr")[j]
    if len(temp2.find_all("td")) == 31:
        for i in range(31):
            temp3 = temp2.find_all("td")[i]
            df.iloc[l,i] = temp3.get_text()
        l += 1

# 삼성의 데이터만 불러오기 및 정제 후 연도 별로 정렬 (클래식 팀이므로 두가지 버전 존재)
samsung_data = df[df['이름'].str.contains('삼성')]
samsung_data = samsung_data.drop(['순'], axis = 1)
samsung_data = samsung_data[['연도', '타율']]
samsung_data = samsung_data.sort_values(by = ['연도'], ascending=[True])
samsung_tayul = samsung_data.iloc[0:24]
samsung_b = samsung_data.iloc[24:43]
samsung_classic_tayul = pd.concat([samsung_b, samsung_tayul], ignore_index= True)
samsung_tayul['타율'] = samsung_tayul['타율'].astype('float')
samsung_classic_tayul['타율'] = samsung_classic_tayul['타율'].astype('float')

# 롯데의 데이터만 불러오기 및 정제 후 연도 별로 정렬 (클래식 팀이므로 두가지 버전 존재)
lotte_data = df[df['이름'].str.contains('롯데')]
lotte_data = lotte_data.drop(['순'], axis = 1)
lotte_data = lotte_data[['연도', '타율']]
lotte_data = lotte_data.sort_values(by = ['연도'], ascending=[True])
lotte_tayul = lotte_data.iloc[0:24]
lotte_b = lotte_data.iloc[24:43]
lotte_classic_tayul = pd.concat([lotte_b, lotte_tayul], ignore_index= True)
lotte_tayul['타율'] = lotte_tayul['타율'].astype('float')
lotte_classic_tayul['타율'] = lotte_classic_tayul['타율'].astype('float')

# LG의 데이터만 불러오기 및 정제 후 연도 별로 정렬
lg_data = df[df['이름'].str.contains('LG')]
lg_data = lg_data.drop(['순'], axis = 1)
lg_data = lg_data[['연도', '타율']]
lg_data = lg_data.sort_values(by = ['연도'], ascending=[True])
lg_tayul = lg_data.iloc[0:24]
lg_tayul['타율'] = lg_tayul['타율'].astype('float')

# 한화의 데이터만 불러오기 및 정제 후 연도 별로 정렬
hanhwa_data = df[df['이름'].str.contains('한화')]
hanhwa_data = hanhwa_data.drop(['순'], axis = 1)
hanhwa_data = hanhwa_data[['연도', '타율']]
hanhwa_data = hanhwa_data.sort_values(by = ['연도'], ascending=[True])
hanhwa_tayul = hanhwa_data.iloc[0:24]
hanhwa_tayul['타율'] = hanhwa_tayul['타율'].astype('float')

# 두산의 데이터만 불러오기 및 정제 후 연도 별로 정렬
doosan_data = df[df['이름'].str.contains('두산')]
doosan_data = doosan_data.drop(['순'], axis = 1)
doosan_data = doosan_data[['연도', '타율']]
doosan_data = doosan_data.sort_values(by = ['연도'], ascending=[True])
doosan_tayul = doosan_data.iloc[0:24]
doosan_tayul['타율'] = doosan_tayul['타율'].astype('float')

# 한글 사용하기 위해 폰트 불러옴
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

'''
# 연도 별 타율 그래프 그리기 (클래식 팀 한정: 삼성, 롯데)
plt.figure(figsize = (15,10))

sns.lineplot(x='연도', y='타율', data = samsung_classic_tayul, label = "삼성")
sns.lineplot(x='연도', y='타율', data = lotte_classic_tayul, label = "롯데")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=90)
'''

# 연도 별 타율 그래프 그리기
plt.figure(figsize = (15,10))

sns.lineplot(x='연도', y='타율', data = samsung_tayul, label = "삼성")
sns.lineplot(x='연도', y='타율', data = lotte_tayul, label = "롯데")
sns.lineplot(x='연도', y='타율', data = lg_tayul, label = "LG")
sns.lineplot(x='연도', y='타율', data = hanhwa_tayul, label = "한화")
sns.lineplot(x='연도', y='타율', data = doosan_tayul, label = "두산")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=90)
# %%
