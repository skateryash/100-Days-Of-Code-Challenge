from time import sleep
from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.nobroker.in/property/rent/mumbai/Mumbai/?searchParam=W3sibGF0IjoxOS4xMjMyNjI2MTEzMzc1LCJsb24iOjcyLjg3NzE3MDcyNjA1MzgsInBsYWNlSWQiOiJDaElKd2UxRVpqREc1enNSYVl4a2pZX3RwRjAiLCJwbGFjZU5hbWUiOiJNdW1iYWkiLCJzaG93TWFwIjpmYWxzZX1d&sharedAccomodation=0&rent=0,10000&type=BHK1"
header = {
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,mr;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
GOOGLE_FORM = "https://forms.gle/hM3WjzDjGnEihpYe8"
CHROME_WEB_DRIVER = "C:\Developement\chromedriver.exe"

response = requests.get(URL, headers=header)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

driver = webdriver.Chrome(service=Service(executable_path=CHROME_WEB_DRIVER))

address = [add.getText() for add in soup.select(selector="div article section div div div")]
rents = [rent.getText() for rent in soup.select(selector="div article #minimumRent")]
deposits = [rent.getText() for rent in soup.select(selector="div article #roomType")]
links = ["https://www.nobroker.in" + link.__getitem__("href") for link in soup.select(selector="div article h2 a")]

print("Data from No Broker Scrapped Successfully")

for i in range(len(address)):
    driver.get(GOOGLE_FORM)
    driver.maximize_window()
    sleep(1)
    address_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_entry.send_keys(address[i])

    rent_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_entry.send_keys(rents[i])

    deposit_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    deposit_entry.send_keys(deposits[i])

    link_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

print("Data Added to Excel Sheet")
