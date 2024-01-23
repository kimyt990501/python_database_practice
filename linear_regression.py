#%%
import warnings
warnings.filterwarnings('ignore')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

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

# 데이터 중 필요한 데이터만 불러오기 및 정제 (타율에 영향 끼치는 것 같은 데이터만 가져온다)
dataset = df.drop(['순'], axis = 1)
dataset = dataset[['연도', '타율', '득점', '루타', '타점']]
dataset = dataset.sort_values(by = ['연도'], ascending=[True], ignore_index= True)
dataset = dataset.astype({'타율':'float', '득점':'int', '루타':'int', '타점':'int'})

# 종속변수와 독립변수 설정 후 트레인, 테스트 데이터 설정
y = dataset[['타율']]
X = dataset[['득점', '루타', '타점']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형회귀 모델 불러와 다중 선형회귀 분석 진행
lr = LinearRegression()
model_linear = lr.fit(X_train, y_train)
y_pred = model_linear.predict(X_test)

# 한글 폰트 설정
plt.rc('font',family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 다중 선형회귀 결과를 scatter 그래프로 표시 
plt.scatter(y_test, y_pred, alpha=0.4)
plt.xlabel("실제 타율")
plt.ylabel("예측 타율")
plt.title("회귀분석")

print("학습 데이터 점수 : {:.2f}".format(model_linear.score(X_train, y_train)))
print("검증 데이터 점수 : {:.2f}".format(model_linear.score(X_test, y_test)))

# 회귀분석의 결정계수
print('R2 : {:.2f}'.format(r2_score(y_test, y_pred)))

# 안타수, 타점, 득점을 직접 입력 받아 타율 예측

# 사용자로부터 입력 받기
user_input_hits = int(input("안타수를 입력하세요 (대략 1300 ~ 2300): "))
user_input_runs = int(input("득점을 입력하세요 (대략 400 ~ 900): "))
user_input_rbi = int(input("타점을 입력하세요 (대략 400 ~ 800): "))

# 입력된 값을 이용하여 타율 예측
user_input_data = np.array([[user_input_runs, user_input_rbi, user_input_hits]])
predicted_batting_average = model_linear.predict(user_input_data)

# 결과 출력
print(f"입력한 안타수, 득점, 타점에 대한 예측 타율: {predicted_batting_average[0][0]:.3f}")
# %%
