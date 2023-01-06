from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
PROMISED_DOWN = 150
PROMISED_UP = 100
CHROME_WEB_DRIVER = "C:\Developement\chromedriver.exe"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_WEB_DRIVER))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start.click()
        sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Down: {self.down}, Up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        self.driver.maximize_window()
        print(self.driver.title)
        sleep(5)
        email = self.driver.find_element(By.XPATH, '//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet = self.driver.find_element(By.XPATH, '//div[@aria-label="Tweet text"]')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}Down/{self.up}Up when I pay for {PROMISED_DOWN}Down/{PROMISED_UP}Up?")
        post_tweet = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        post_tweet.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
