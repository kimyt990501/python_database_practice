#%%
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 저장해둔 타자 데이터 읽어오기
hitter_data = pd.read_csv('data\\hitter_data.csv', encoding='euc-kr')

# 선수의 수준과 상관 없는 칼럼, 중복된 칼럼, 결측치가 존재하는 칼럼을 삭제
hitter_data = hitter_data.drop(['팀명', '선수명', 'WPA', 'WAR2'], axis=1)

# 모든 칼럼 데이터의 타입을 float형으로 변경
hitter_data = hitter_data.astype('float')

# 순위가 1위인 선수들의 데이터만 추출
first_hitter_data = hitter_data[hitter_data['순위'] == 1.0]

# 사용할 특징 선택
features_to_predict = ['경기', '타석', '타수', '득점', '안타', '2루타', '3루타', '홈런', 'WAR', 'OPS']

# 선택한 특징만 추출
selected_features_data = first_hitter_data[features_to_predict]

# 데이터 전처리
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_features_data.values)

# 시계열 데이터를 학습용 데이터로 변환
time_steps = 3  # 시계열 데이터를 몇 개의 타임 스텝으로 나눌지 설정
X, y, years = [], [], []
for i in range(len(scaled_data)-time_steps):
    X.append(scaled_data[i:(i+time_steps), :])
    y.append(scaled_data[i + time_steps, :])
    years.append(first_hitter_data['연도'].values[i + time_steps])

X, y, years = np.array(X), np.array(y), np.array(years)

# 데이터셋 분리
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]
years_test = years[train_size:]

# LSTM 모델 구축
model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(y_train.shape[1]))  # 출력 노드 수를 예측하려는 특징 수로 설정
model.compile(optimizer='adam', loss='mse')

# 모델 학습
model.fit(X_train, y_train, epochs=100, batch_size=16, verbose=2)

# 테스트 데이터로 예측
test_predictions = model.predict(X_test)

# 예측 결과를 스케일 역전환
predicted_features = scaler.inverse_transform(test_predictions)

# 예측 결과 확인
predicted_df = pd.DataFrame(predicted_features, columns=features_to_predict)
predicted_df['연도'] = years_test

# 실제 결과 확인
actual_df = pd.DataFrame(selected_features_data.iloc[train_size + time_steps:].values, columns=features_to_predict)
actual_df['연도'] = years_test

# 예측 결과와 실제 결과를 합쳐서 출력
result_df = pd.concat([actual_df, predicted_df], keys=['실제', '예측'], axis=1)
print(result_df)

# 예측 결과의 MSE 계산
mse = mean_squared_error(actual_df[features_to_predict].values, predicted_df[features_to_predict].values)
print(f'Mean Squared Error: {mse}')

# 예측 결과의 R-squared 계산
r2 = r2_score(actual_df[features_to_predict].values, predicted_df[features_to_predict].values)
print(f'R-squared: {r2}')
# %%