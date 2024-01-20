#%%
import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
#2018년 데이터
csv181 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 1월.csv", encoding='euc-kr')
csv182 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 2월.csv", encoding='euc-kr')
csv183 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 3월.csv", encoding='euc-kr')
csv184 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 4월.csv", encoding='euc-kr')
csv185 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 5월.csv", encoding='euc-kr')
csv186 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 6월.csv", encoding='euc-kr')
csv187 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 7월.csv", encoding='euc-kr')
csv188 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 8월.csv", encoding='euc-kr')
csv189 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 9월.csv", encoding='euc-kr')
csv1810 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 10월.csv", encoding='euc-kr')
csv1811 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 11월.csv", encoding='euc-kr')
csv1812 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2018년 12월.csv", encoding='euc-kr')

#2019년 데이터
csv191 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 01월.csv", encoding='euc-kr')
csv192 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 02월.csv", encoding='euc-kr')
csv193 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 03월.csv", encoding='euc-kr')
csv194 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 04월.csv", encoding='euc-kr')
csv195 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 05월.csv", encoding='euc-kr')
csv196 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 06월.csv", encoding='euc-kr')
csv197 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 07월.csv", encoding='euc-kr')
csv198 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 08월.csv", encoding='euc-kr')
csv199 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 09월.csv", encoding='euc-kr')
csv1910 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 10월.csv", encoding='euc-kr')
csv1911 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 11월.csv", encoding='euc-kr')
csv1912 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2019년 12월.csv", encoding='euc-kr')

#2020년 데이터
csv201 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 1월.csv", encoding='euc-kr')
csv202 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 2월.csv", encoding='euc-kr')
csv203 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 3월.csv", encoding='euc-kr')
csv204 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 4월.csv", encoding='euc-kr')
csv205 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 5월.csv", encoding='euc-kr')
csv206 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 6월.csv", encoding='euc-kr')
csv207 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 7월.csv", encoding='euc-kr')
csv208 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 8월.csv", encoding='euc-kr')
csv209 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 9월.csv", encoding='euc-kr')
csv2010 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 10월.csv", encoding='euc-kr')
csv2011 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 11월.csv", encoding='euc-kr')
csv2012 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2020년 12월.csv", encoding='euc-kr')

#2021년 데이터
csv211 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 1월.csv", encoding='euc-kr')
csv212 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 2월.csv", encoding='euc-kr')
csv213 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 3월.csv", encoding='euc-kr')
csv214 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 4월.csv", encoding='euc-kr')
csv215 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 5월.csv", encoding='euc-kr')
csv216 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 6월.csv", encoding='euc-kr')
csv217 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 7월.csv", encoding='euc-kr')
csv218 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 8월.csv", encoding='euc-kr')
csv219 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 9월.csv", encoding='euc-kr')
csv2110 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 10월.csv", encoding='euc-kr')
csv2111 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 11월.csv", encoding='euc-kr')
csv2112 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2021년 12월.csv", encoding='euc-kr')

#2022년 데이터
csv221 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 1월.csv", encoding='euc-kr')
csv222 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 2월.csv", encoding='euc-kr')
csv223 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 3월.csv", encoding='euc-kr')
csv224 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 4월.csv", encoding='euc-kr')
csv225 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 5월.csv", encoding='euc-kr')
csv226 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 6월.csv", encoding='euc-kr')
csv227 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 7월.csv", encoding='euc-kr')
csv228 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 8월.csv", encoding='euc-kr')
csv229 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 9월.csv", encoding='euc-kr')
csv2210 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 10월.csv", encoding='euc-kr')
csv2211 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 11월.csv", encoding='euc-kr')
csv2212 = pd.read_csv("C:\\Users\\user\\Desktop\\resources\\mp10_pm25_2018_2022\\2022년 12월.csv", encoding='euc-kr')

#각 년도 별 데이터 합치기
#18년 데이터 합치기
csv18 = pd.concat([csv181, csv182, csv183, csv184, csv185, csv186, csv187, csv188, csv189, csv1810, csv1811, csv1812], ignore_index = True)
#csv18.drop(["Unnamed: 0"], axis=1, inplace =True)
#print(csv18.head())

#19년 데이터 합치기
csv19 = pd.concat([csv191, csv192, csv193, csv194, csv195, csv196, csv197, csv198, csv199, csv1910, csv1911, csv1912], ignore_index = True)
#csv19.drop(["Unnamed: 0"], axis=1, inplace =True)
#print(csv19.head())

#20년 데이터 합치기
csv20 = pd.concat([csv201, csv202, csv203, csv204, csv205, csv206, csv207, csv208, csv209, csv2010, csv2011, csv2012], ignore_index = True)
#csv20.drop(["Unnamed: 0"], axis=1, inplace =True)
#print(csv20.head())

#21년 데이터 합치기
csv21 = pd.concat([csv211, csv212, csv213, csv214, csv215, csv216, csv217, csv218, csv219, csv2110, csv2111, csv2112], ignore_index = True)
#csv21.drop(["Unnamed: 0"], axis=1, inplace =True)
#print(csv21.head())

#22년 데이터 합치기
csv22 = pd.concat([csv221, csv222, csv223, csv224, csv225, csv226, csv227, csv228, csv229, csv2210, csv2211, csv2212], ignore_index = True)
csv22.drop(["Unnamed: 12"], axis=1, inplace =True)
csv22.drop(["Unnamed: 13"], axis=1, inplace =True)
#print(csv22.head())

#원하는 지역만 불러오기
csv18 = csv18[csv18['지역'].str.contains('서울')]
csv19 = csv19[csv19['지역'].str.contains('서울')]
csv20 = csv20[csv20['지역'].str.contains('서울')]
csv21 = csv21[csv21['지역'].str.contains('서울')]
csv22 = csv22[csv22['지역'].str.contains('서울')]

#기존의 인덱스 삭제
csv18.reset_index(drop = True, inplace=True)
csv19.reset_index(drop = True, inplace=True)
csv20.reset_index(drop = True, inplace=True)
csv21.reset_index(drop = True, inplace=True)
csv22.reset_index(drop = True, inplace=True)

#미세먼지
csv18_PM10 = csv18[["지역", "측정일시", "PM10"]]
csv19_PM10 = csv19[["지역", "측정일시", "PM10"]]
csv20_PM10 = csv20[["지역", "측정일시", "PM10"]]
csv21_PM10 = csv21[["지역", "측정일시", "PM10"]]
csv22_PM10 = csv22[["지역", "측정일시", "PM10"]]

#초미세먼지
csv18_PM25 = csv18[["지역", "측정일시", "PM25"]]
csv19_PM25 = csv19[["지역", "측정일시", "PM25"]]
csv20_PM25 = csv20[["지역", "측정일시", "PM25"]]
csv21_PM25 = csv21[["지역", "측정일시", "PM25"]]
csv22_PM25 = csv22[["지역", "측정일시", "PM25"]]

#잘 추출되었는지 테스트
#print(csv22.head())

# 서울에 구와 군이 몇개 있는지 추출
csv_18_seoul_PM10 = csv18_PM10["지역"].unique()
csv_19_seoul_PM10 = csv19_PM10["지역"].unique()
csv_20_seoul_PM10 = csv20_PM10["지역"].unique()
csv_21_seoul_PM10 = csv21_PM10["지역"].unique()
csv_22_seoul_PM10 = csv22_PM10["지역"].unique()

csv_18_seoul_PM25 = csv18_PM25["지역"].unique()
csv_19_seoul_PM25 = csv19_PM25["지역"].unique()
csv_20_seoul_PM25 = csv20_PM25["지역"].unique()
csv_21_seoul_PM25 = csv21_PM25["지역"].unique()
csv_22_seoul_PM25 = csv22_PM25["지역"].unique()

#잘 추출됐는지 확인
'''
print(len(csv_18_seoul_PM10))
print(len(csv_19_seoul_PM10))
print(len(csv_20_seoul_PM10))
print(len(csv_21_seoul_PM10))
print(len(csv_22_seoul_PM10))

print(len(csv_18_seoul_PM25))
print(len(csv_19_seoul_PM25))
print(len(csv_20_seoul_PM25))
print(len(csv_21_seoul_PM25))
print(len(csv_22_seoul_PM25))
'''

# 각 연도별 결측값 확인 후 삭제

# 결측값 삭제 전
'''
print("미세먼지 데이터")
print("2018년 서울데이터")
print(csv18_PM10.isnull().sum())
print("")
print("2019년 서울데이터")
print(csv19_PM10.isnull().sum())
print("")
print("2020년 서울데이터")
print(csv20_PM10.isnull().sum())
print("")
print("2021년 서울데이터")
print(csv21_PM10.isnull().sum())
print("")
print("2022년 서울데이터")
print(csv22_PM10.isnull().sum())
print("")
print("")

print("초미세먼지 데이터")
print("2018년 서울데이터")
print(csv18_PM25.isnull().sum())
print("")
print("2019년 서울데이터")
print(csv19_PM25.isnull().sum())
print("")
print("2020년 서울데이터")
print(csv20_PM25.isnull().sum())
print("")
print("2021년 서울데이터")
print(csv21_PM25.isnull().sum())
print("")
print("2022년 서울데이터")
print(csv22_PM25.isnull().sum())
print("")
'''
# 결측값 삭제
csv18_PM10.dropna(axis=0, inplace = True)
csv19_PM10.dropna(axis=0, inplace = True)
csv20_PM10.dropna(axis=0, inplace = True)
csv21_PM10.dropna(axis=0, inplace = True)
csv22_PM10.dropna(axis=0, inplace = True)

csv18_PM25.dropna(axis=0, inplace = True)
csv19_PM25.dropna(axis=0, inplace = True)
csv20_PM25.dropna(axis=0, inplace = True)
csv21_PM25.dropna(axis=0, inplace = True)
csv22_PM25.dropna(axis=0, inplace = True)

# 결측값 삭제 후
'''
print("미세먼지 데이터")
print("2018년 서울데이터")
print(csv18_PM10.isnull().sum())
print("")
print("2019년 서울데이터")
print(csv19_PM10.isnull().sum())
print("")
print("2020년 서울데이터")
print(csv20_PM10.isnull().sum())
print("")
print("2021년 서울데이터")
print(csv21_PM10.isnull().sum())
print("")
print("2022년 서울데이터")
print(csv22_PM10.isnull().sum())
print("")
print("")

print("초미세먼지 데이터")
print("2018년 서울데이터")
print(csv18_PM25.isnull().sum())
print("")
print("2019년 서울데이터")
print(csv19_PM25.isnull().sum())
print("")
print("2020년 서울데이터")
print(csv20_PM25.isnull().sum())
print("")
print("2021년 서울데이터")
print(csv21_PM25.isnull().sum())
print("")
print("2022년 서울데이터")
print(csv22_PM25.isnull().sum())
print("")
'''

# 연도별 측정 일시를 월로 바꾸기
# 미세먼지
csv18_PM10["월별"] = csv18_PM10["측정일시"].astype(str)
csv18_PM10["월별"] = csv18_PM10["월별"].str[4:6]
csv18_PM10 = csv18_PM10[["지역","월별","PM10"]]

csv19_PM10["월별"] = csv19_PM10["측정일시"].astype(str)
csv19_PM10["월별"] = csv19_PM10["월별"].str[4:6]
csv19_PM10 = csv19_PM10[["지역","월별","PM10"]]

csv20_PM10["월별"] = csv20_PM10["측정일시"].astype(str)
csv20_PM10["월별"] = csv20_PM10["월별"].str[4:6]
csv20_PM10 = csv20_PM10[["지역","월별","PM10"]]

csv21_PM10["월별"] = csv21_PM10["측정일시"].astype(str)
csv21_PM10["월별"] = csv21_PM10["월별"].str[4:6]
csv21_PM10 = csv21_PM10[["지역","월별","PM10"]]

csv22_PM10["월별"] = csv22_PM10["측정일시"].astype(str)
csv22_PM10["월별"] = csv22_PM10["월별"].str[4:6]
csv22_PM10 = csv22_PM10[["지역","월별","PM10"]]

# 초미세먼지
csv18_PM25["월별"] = csv18_PM25["측정일시"].astype(str)
csv18_PM25["월별"] = csv18_PM25["월별"].str[4:6]
csv18_PM25 = csv18_PM25[["지역","월별","PM25"]]

csv19_PM25["월별"] = csv19_PM25["측정일시"].astype(str)
csv19_PM25["월별"] = csv19_PM25["월별"].str[4:6]
csv19_PM25 = csv19_PM25[["지역","월별","PM25"]]

csv20_PM25["월별"] = csv20_PM25["측정일시"].astype(str)
csv20_PM25["월별"] = csv20_PM25["월별"].str[4:6]
csv20_PM25 = csv20_PM25[["지역","월별","PM25"]]

csv21_PM25["월별"] = csv21_PM25["측정일시"].astype(str)
csv21_PM25["월별"] = csv21_PM25["월별"].str[4:6]
csv21_PM25 = csv21_PM25[["지역","월별","PM25"]]

csv22_PM25["월별"] = csv22_PM25["측정일시"].astype(str)
csv22_PM25["월별"] = csv22_PM25["월별"].str[4:6]
csv22_PM25 = csv22_PM25[["지역","월별","PM25"]]

# 잘 추출됐는지 확인
'''
print(csv18_PM10.head())
print(csv19_PM10.head())
print(csv20_PM10.head())
print(csv21_PM10.head())
print(csv22_PM10.head())

print(csv18_PM25.head())
print(csv19_PM25.head())
print(csv20_PM25.head())
print(csv21_PM25.head())
print(csv22_PM25.head())
'''

# 한글 사용하기 위해 폰트 불러옴
plt.rc('font',family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 미세먼지 월별 데이터를 그래프로 표시

plt.figure(figsize = (12,10))

sns.lineplot(x='월별',y='PM10',data = csv18_PM10, label = "2018")
sns.lineplot(x='월별',y='PM10',data = csv19_PM10, label = "2019")
sns.lineplot(x='월별',y='PM10',data = csv20_PM10, label = "2020")
sns.lineplot(x='월별',y='PM10',data = csv21_PM10, label = "2021")
sns.lineplot(x='월별',y='PM10',data = csv22_PM10, label = "2022")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=90)

# 초미세먼지 월별 데이터를 그래프로 표시

plt.figure(figsize = (12,10))

sns.lineplot(x='월별',y='PM25',data = csv18_PM25, label = "2018")
sns.lineplot(x='월별',y='PM25',data = csv19_PM25, label = "2019")
sns.lineplot(x='월별',y='PM25',data = csv20_PM25, label = "2020")
sns.lineplot(x='월별',y='PM25',data = csv21_PM25, label = "2021")
sns.lineplot(x='월별',y='PM25',data = csv22_PM25, label = "2022")

plt.legend()
sns.set_context('poster', font_scale = 1)

plt.xticks(rotation=90)
# %%
