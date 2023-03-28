############
# virtual env : value
############

# pip install undetected-chromedriver

import os, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# import pyperclip, pyautogui


# it

## 
import pandas as pd
import numpy as np
import undetected_chromedriver as uc

# options = webdriver.ChromeOptions()
# options.add_argument('window-size=1920,1080')
# options.add_argument("--headless")

# driver = webdriver.Chrome('chromedriver.exe', options=options)
#driver = webdriver.Chrome('chromedriver.exe', options=options)

# url = input('url 을 입력하세요: ') 

# url = input('url 을 입력하세요: ') 
url = 'https://seekingalpha.com/symbol/BA/earnings/estimates'

driver = uc.Chrome()

# driver = webdriver.Firefox(ChromeDriverManager().install(), options= options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)
driver.get(url)

time.sleep(3)

# sing in 버튼으로 이동
signin_xpath = '/html/body/div[2]/div/div[1]/header/nav/div[1]/div/div[2]/button'
# driver.find_element_by_xpath(signin_xpath).click()
signin_button = driver.find_element(By.XPATH, signin_xpath)
actions = webdriver.ActionChains(driver).move_to_element(signin_button).click(on_element = None)

# 체인을 실행합니다.
actions.perform()

# actions
print('클릭을 눌렀습니다.')
time.sleep(2)


# # 구글로그인 계정 누르기
google_acc_xpath = '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/button'
google_signin_button = driver.find_element(By.XPATH, google_acc_xpath)
actions = webdriver.ActionChains(driver).move_to_element(google_signin_button).click(on_element = None)
# 체인을 실행합니다.
actions.perform()

# actions
print('구글 로그인 버튼을 눌렀습니다.')
time.sleep(2)


print('-'*50)
print('시킹알파 화면에 진입합니다.')
print('-'*50)
# time.sleep(10)

table = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/main/div/div[2]/div/div/div[3]/div/div/section[2]/div/div[2]/div[2]/div[2]/div/table')
print(table)


# Get HTML
html = requests.get(url).text

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Parse first table
# table = soup.select_one('#content > div > div.c-f.O-b5.O-cm.O-cp > div > div > div:nth-child(3) > div > div > section:nth-child(3) > div > div.ev-d > div:nth-child(2) > div.fa-j.fa-uH > div > table')
table = soup.select_one('/html/body/div[2]/div/div[1]/main/div/div[2]/div/div/div[3]/div/div/section[2]/div/div[2]/div[2]/div[2]/div/table')
print(table)
df = pd.read_html(str(table))[0]
print(df)