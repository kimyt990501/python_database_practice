#%%
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np

import warnings
warnings.filterwarnings('ignore')

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

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

# 데이터 표준화 (Standardization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 신경망 모델 정의
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# 모델 컴파일
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 학습
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_data=(X_test_scaled, y_test))

# 테스트 데이터에 대한 예측
y_pred_nn = model.predict(X_test_scaled)

# 성능 평가
mse_nn = mean_squared_error(y_test, y_pred_nn)
r2_nn = r2_score(y_test, y_pred_nn)
print(f'Mean Squared Error (Neural Network): {mse_nn}')
print(f'R2 Score (Neural Network): {r2_nn}')
# %%
