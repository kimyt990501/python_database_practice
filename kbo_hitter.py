#%%
import warnings
import pandas as pd
import seaborn as sns

warnings.filterwarnings('ignore')

# 한글 사용하기 위해 폰트 불러옴
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# 저장해둔 타자 데이터 읽어오기
'''
hitter_data = pd.read_csv('C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_1982.csv', encoding='euc-kr')
years = range(1983, 2024)
for year in years:
    path = 'C:\\Users\\user\\Desktop\\resources\\baseball_player\\kbo_hitter_data_%d.csv' %year
    old = pd.read_csv(path, encoding='euc-kr')
    new = pd.concat([hitter_data, old], ignore_index=True)
    hitter_data = new
#print(hitter_data)
'''
hitter_data = pd.read_csv('data\\hitter_data.csv', encoding='euc-kr')

# 선수의 수준과 상관 없는 칼럼, 중복된 칼럼, 결측치가 존재하는 칼럼을 삭제
hitter_data = hitter_data.drop(['팀명', '선수명', 'WPA', 'WAR2'], axis=1)

# 모든 칼럼 데이터의 타입을 float형으로 변경
hitter_data = hitter_data.astype('float')
print(hitter_data)

'''
# 상관 행렬 만들어 히트맵 만들기
hitter_cor = hitter_data.corr()
hitter_cor = round(hitter_cor,2)

plt.rcParams.update({'figure.dpi' : '120',	#해상도 설정
                    'figure.figsize' : [7.5,5.5]}) # 가로세로크기
sns.heatmap(hitter_cor,
           annot=True,	# 상관계수 표시
           cmap='RdBu') # 컬러맵
'''
# %%
