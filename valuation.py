############
# virtual env : value
############

# pip install undetected-chromedriver
# pip install pyperclip
# pyautogui

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
import pyperclip, pyautogui
import pandas as pd
import numpy as np
import undetected_chromedriver as uc


from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
options.add_argument("--headless")

# driver = webdriver.Chrome('chromedriver.exe', options=options)
#driver = webdriver.Chrome('chromedriver.exe', options=options)

# url = input('url 을 입력하세요: ') 

# url = input('url 을 입력하세요: ') 
url = 'https://seekingalpha.com/symbol/BA/earnings/estimates'

# driver = uc.Chrome()
# subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')

# option = Options()
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# driver.maximize_window()
# driver.get(url)

driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)
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
time.sleep(5)


# # 다른계정으로 로그인 버튼 누르기

differ_acc_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div/div[2]'
differ_signin_button = driver.find_element(By.XPATH, differ_acc_xpath)
actions = webdriver.ActionChains(driver).move_to_element(differ_signin_button).click(on_element = None)
# 체인을 실행합니다.
actions.perform()

# actions
print('다른 계정으로 로그인 버튼을 눌렀습니다.')
time.sleep(5)


#######################################
# id/pw 입력


user_id = 'n3figo@gmail.com'
user_pw = 'Romeo123'


# /html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[1]/input
id = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
driver.find_element(By.XPATH, id).click()
pyperclip.copy(user_id)
driver.find_element(By.XPATH, id).send_keys(Keys.CONTROL,'v')
time.sleep(2)

# 다음버튼 클릭 
next_button = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
driver.find_element(By.XPATH, next_button).click()

# pw 입력
time.sleep(3)
pw = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
driver.find_element(By.XPATH, pw).click()
pyperclip.copy(user_pw)
driver.find_element(By.XPATH, pw).send_keys(Keys.CONTROL,'v')

# 다음버튼 클릭 
next_button_2 = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
driver.find_element(By.XPATH, next_button_2).click()

wait = WebDriverWait(driver, 30)
time.sleep(5)

print("="*50)
print("로그인에 성공하였습니다.")
print("="*50)



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