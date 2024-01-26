# PYTHON DATABASE PRACTICE
파이썬과 데이터베이스를 활용하여 여러가지 작은 프로젝트들을 수행하기 위해 만든 레포지토리이며 연습용으로 쓰는 중이다

## 프로젝트 목록

### 1. 전화번호 관리 프로그램
- 말 그대로 간단한 전화번호 관리 프로그램이며 몇 가지 기능을 포함한다

#### 파일 명
- telbook.py

#### 개발환경
- IDE: Visual Studio Code

#### 기술 스택
- 데이터베이스: MySQL
- 언어: Python

#### 기능
- 새로운 전화번호 입력
  - 새로 추가할 사람의 이름과 전화번호를 입력하면 해당 정보를 연결된 데이터베이스의 테이블로 insert 해준다
- 기존 전화번호 삭제
  - 삭제하고 싶은 사람의 이름을 검색하여 테이블로부터 삭제한다 
- 이름으로 검색
  - 이름을 검색하여 해당 인물의 정보를 출력한다
- 전화번호 전체목록 출력
  - 테이블에 저장되어 있는 모든 인물의 정보를 출력한다
- 전화번호 목록 저장
  - 추가하거나 삭제한 사항들을 저장한다. (저장하지 않을 시 commit되지 않아 그동안 입력하거나 삭제한 사항들은 초기화된다)

### 2. 가위바위보 프로그램
- 컴퓨터와 가위바위보를 하여 승부를 가리는 프로그램이다

#### 파일 명
- RockPaperScissors.py

#### 개발환경
- IDE: Visual Studio Code

#### 기술 스택
- 데이터베이스: MySQL
- 언어: Python

#### 기능
- 컴퓨터와 게임 진행
  - 컴퓨터와 1 대 1로 총 세 판의 가위바위보를 진행한다
- 승수, 패수, 무승부수 통계
  - 프로그램 실행 시 계정을 만들어 사용자의 기록을 데이터베이스 테이블에 저장
- 게임 머니 기능
  - 매 게임마다 100골드씩 할당되며 한 게임 당 최대 20골드씩 걸 수 있다
  - 승리한다면 본인이 걸었던 돈의 두배를 돌려 받지만 패배한다면 전부 잃게 된다 
- 본인 기록 불러오기
  - 데이터베이스에 저장된 본인의 정보를 불러와 게임을 이어서 진행할 수 있다

### 3. 데이터를 활용하여 서울의 미세먼지, 초미세먼지 농도 변화 분석하기 
- 에어코리아에서 데이터를 다운 받아 전처리 후 그래프로 시각화하는 간단한 프로젝트

#### 파일 명
- pm10_pm25_Seoul_2018_2022.ipynb
- PM10_PM25_Seoul_2018_2022_data.py

#### 개발환경
- IDE: Visual Studio Code, Jupyter Notebook

#### 기술 스택
- 언어: Python

#### 절차
- 에어 코리아에서 다운 받은 데이터를 전처리하여 각 변수에 저장한다
- 해당 변수들을 통해 각 연도별 미세먼지, 초미세먼지 농도의 변화가 어떻게 되는지 그래프로 시각화하여 확인 (2018 ~ 2022년)
- 아직 진행 중

- 참고: <https://velog.io/@greendatai/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80-%EC%9B%94%EB%B3%84-%ED%8F%89%EA%B7%A0-%EC%98%88%EC%B8%A12%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%A0%84%EC%B2%98%EB%A6%AC-%EB%B0%8F-%ED%99%95%EC%9D%B8>

### 4. 데이터를 활용하여 역대 KBO 야구 팀들의 기록 분석하기
- 스탯티즈 라는 사이트에서 KBO 야구 팀들의 데이터를 크롤링하여 불러와 분석을 진행하는 프로젝트

#### 파일 명
- kbo_data_graph.ipynb
- kbo_data_mine.py
- linear_regression.py

#### 개발환경
- IDE: Visual Studio Code

#### 기술 스택
- 언어: Python

#### 절차
- 스탯티즈에서 크롤링한 데이터를 불러와 전처리한다
- 전처리한 데이터를 활용하여 다양한 분석 가능
- 진행한 내용들
    - 일부 팀들의 연도 별 타율 데이터만 뽑아와 그래프로 시각화하여 타율 변화 확인
    - 타율 뿐만 아니라 다른 데이터들도 따로 뽑아 각 데이터들이 타율, 출루율, WAR 에 얼마나 영향을 끼쳤는지 확인
    - 상관분석을 통해 어느 요인이 타율, 출루율, WAR 에 가장 영향을 많이 끼쳤는지 확인
    - 상관 행렬을 이용하여 출력한 히트맵을 통해 각 데이터들의 상관 관계를 시각화
    - 선형회귀를 이용하여 몇가지 데이터를 통해 타율을 예측 (루타, 득점, 타점)
    - 만든 선형회귀 모델을 검증
    - 해당 모델을 사용하여 사용자로부터 입력받은 데이터를 토대로 타율 예측
- 아직 진행 중

- 참고: <https://analyst-ggom-chi-kim.tistory.com/9>

### 5. 역대 KBO 타자 데이터를 활용하여 데이터 분석하기
- 스탯티즈 라는 사이트에서 KBO 타자 선수들의 데이터를 크롤링하여 불러와 분석을 진행하는 프로젝트

#### 파일 명
- kbo_hitter.py
- kbo_hitter_crawling.py

#### 개발환경
- IDE: Visual Studio Code
- Version: python 3.7

#### 기술 스택
- 언어: Python

#### 절차
- 스탯티즈에서 역대 kbo 각 시즌 30 순위 안에 들었던 타자 데이터를 크롤링하여 csv 파일로 저장
- csv 파일을 불러와 하나의 데이터프레임으로 결합
- 데이터 전처리 후 여러가지 작업 수행
  - 역대 1위 타자의 OPS 등 여러 데이터를 불러와 연도별로 시계열 데이터 분석 진행하여 데이터 예측 -> mse, r2 score 모두 안 좋게 나온걸 보아 OPS 같은 데이터들은 시계열분석으로 예측하는건 알맞지 않음을 알게 됨

- 아직 진행 중

