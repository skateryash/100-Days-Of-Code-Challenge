from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

chrome_web_driver = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_web_driver))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://www.appbrewery.co/p/newsletter")

# no_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(no_of_articles.text)
# no_of_articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, "other Wikipedias are available")
# all_portals.click()

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(os.getenv("MY_EMAIL"))
email_input.send_keys(Keys.ENTER)

driver.close()



