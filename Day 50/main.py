from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
chrome_web_driver = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_web_driver))
driver.get("https://bumble.com/en-in/")

join = driver.find_element(By.CLASS_NAME, 'app-entry-points__action')
join.click()

login = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.CSS_SELECTOR, '#email')
email.send_keys(os.getenv('MY_EMAIL'))
password = driver.find_element(By.CSS_SELECTOR, '#pass')
password.send_keys(os.getenv('PASSWORD'))
login_button = driver.find_element(By.CSS_SELECTOR, '#loginbutton')
login_button.click()

driver.switch_to.window(base_window)

right_swipe = driver.find_element(By.CSS_SELECTOR, "body")
for i in range(15):
    sleep(2)
    right_swipe.send_keys(Keys.ARROW_RIGHT)
