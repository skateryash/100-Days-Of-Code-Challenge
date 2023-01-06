from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

CHROME_WEB_DRIVER = "C:\Developement\chromedriver.exe"
TARGET_ACCOUNT = "filmygags"
INSTAGRAM_USERNAME = os.getenv('USERNAME')
INSTAGRAM_PASSWORD = os.getenv('PASSWORD')


class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_WEB_DRIVER))
        self.followers_list = None

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        sleep(5)

        followers = self.driver.find_element(By.XPATH, f'//a[@href="/{TARGET_ACCOUNT}/followers/"]')
        followers.click()
        sleep(3)

        self.followers_list = self.driver.find_element(By.XPATH, '//div[@class="_aano"]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight + arguments[0].offsetHeight;"
                                       , self.followers_list)
            sleep(3)

    def follow(self):
        follow_buttons = self.followers_list.find_elements(By.CSS_SELECTOR, "div button")
        sleep(2)
        for button in follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                sleep(1)
                cancel = self.driver.find_element(By.XPATH, '//button[@class="_a9-- _a9_1"]')
                cancel.click()


bot = InstaFollowers()
bot.login()
bot.find_followers()
bot.follow()
