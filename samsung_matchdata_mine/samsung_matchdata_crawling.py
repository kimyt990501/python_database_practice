from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

import warnings
warnings.filterwarnings('ignore')

driver = webdriver.Chrome()
url = 'https://www.koreabaseball.com/Schedule/Schedule.aspx'
driver.get(url)

# 정규시즌 선택
driver.find_element(By.XPATH, "//*[@id='ddlSeries']/option[text()='KBO 정규시즌 일정']").click()

# 팀 선택
driver.find_element(By.XPATH, "//*[@id='boxList']/ul/li[@attr-value = 'SS']").click()

# 년도 선택
driver.find_element(By.XPATH, "//*[@id='ddlYear']/option[text()='2001']").click()

for month in range(4, 11):
    # 월 선택
    driver.find_element(By.XPATH, "//*[@id='ddlMonth']/option[" + str(month) + "]").click()
    
    # 파싱
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    schedule = soup.find('table', {'class':'tbl'})
    tr_list = schedule.find_all('tr')
    
    list = []
    for i in range(1, len(tr_list)):
        td_list = tr_list[i].find_all('td')
        span_list = tr_list[i].find_all('span')
        
        if len(td_list) == 9:
            if td_list[8].text != '-':
                if td_list[7].text == '대구':
                    temp = [td_list[0].text.strip(), span_list[0].text.strip(), '-']
                elif td_list[7].text == '포항':
                    temp = [td_list[0].text.strip(), span_list[0].text.strip(), '-']
                else:
                    temp = [td_list[0].text.strip(), span_list[2].text.strip(), '-']
                list.append(temp)
                continue
            elif td_list[8].text == '그라운드사정':
                if td_list[7].text == '대구':
                    temp = [td_list[0].text.strip(), span_list[0].text.strip(), '-']
                elif td_list[7].text == '포항':
                    temp = [td_list[0].text.strip(), span_list[0].text.strip(), '-']
                else:
                    temp = [td_list[0].text.strip(), span_list[2].text.strip(), '-']
                list.append(temp)
                continue
            else:
                #print(span_list[0].text + span_list[4].text)
                if td_list[7].text == '대구':
                    if int(span_list[3].text) > int(span_list[1].text):
                        temp = [td_list[0].text.strip(), span_list[0].text.strip(), 'win']
                    elif int(span_list[3].text) == int(span_list[1].text):
                        temp = [td_list[0].text.strip(), span_list[0].text.strip(), 'draw']
                    else:
                        temp = [td_list[0].text.strip(), span_list[0].text.strip(), 'lose']
                elif td_list[7].text == '포항':
                    if int(span_list[3].text) > int(span_list[1].text):
                        temp = [td_list[0].text.strip(), span_list[0].text.strip(), 'win']
                    elif int(span_list[3].text) == int(span_list[1].text):
                        temp = [td_list[0].text.strip(), span_list[0].text.strip(), 'draw']
                    else:
                        temp = [td_list[0].text.strip(), span_list[0].text.strip(), 'lose']
                else:
                    if int(span_list[3].text) < int(span_list[1].text):
                        temp = [td_list[0].text.strip(), span_list[4].text.strip(), 'win']
                    elif int(span_list[3].text) == int(span_list[1].text):
                        temp = [td_list[0].text.strip(), span_list[4].text.strip(), 'draw']
                    else:
                        temp = [td_list[0].text.strip(), span_list[4].text.strip(), 'lose']
                list.append(temp)
        else:
            if td_list[7].text == '우천취소':
                if td_list[6].text == '대구':
                    temp = ['-', span_list[0].text.strip(), '-']
                elif td_list[6].text == '포항':
                    temp = ['-', span_list[0].text.strip(), '-']
                else:
                    temp = ['-', span_list[2].text.strip(), '-']
                list.append(temp)
                continue
            else:
                #print(span_list[0].text + span_list[4].text)
                if td_list[6].text == '대구':
                    if int(span_list[3].text) > int(span_list[1].text):
                        temp = ['-', span_list[0].text.strip(), 'win']
                    elif int(span_list[3].text) == int(span_list[1].text):
                        temp = ['-', span_list[0].text.strip(), 'draw']
                    else:
                        temp = ['-', span_list[0].text.strip(), 'lose']
                elif td_list[6].text == '포항':
                    if int(span_list[3].text) > int(span_list[1].text):
                        temp = ['-', span_list[0].text.strip(), 'win']
                    elif int(span_list[3].text) == int(span_list[1].text):
                        temp = ['-', span_list[0].text.strip(), 'draw']
                    else:
                        temp = ['-', span_list[0].text.strip(), 'lose']
                else:
                    if int(span_list[3].text) < int(span_list[1].text):
                        temp = ['-', span_list[4].text.strip(), 'win']
                    elif int(span_list[3].text) == int(span_list[1].text):
                        temp = ['-', span_list[4].text.strip(), 'draw']
                    else:
                        temp = ['-', span_list[4].text.strip(), 'lose']
                list.append(temp)
    # 빈 데이터프레임 만들기
    df = pd.DataFrame(list)
    df.columns = ['날짜', '상대팀', '결과']
    df.to_csv('samsung_2001_' + str(month) + '_match_result.csv', index=None, encoding='euc-kr')