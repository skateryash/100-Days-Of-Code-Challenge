from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_web_driver = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_web_driver))
driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME, "_30jeq3")
# print(price.text)

# books = driver.find_element(By.CSS_SELECTOR, ".navFooterMoreOnAmazon a")
# print(books.get_attribute("href"))

# question = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[6]/div[7]/div/div/div[2]/div[2]/div/div[1]/span[2]')
# print(question.text)

# result = {
#     "0": {"time": "", "name": ""},
#     "1": {"time": "", "name": ""},
#     "2": {"time": "", "name": ""},
#     "3": {"time": "", "name": ""},
#     "4": {"time": "", "name": ""},
#     "5": {"time": "", "name": ""}
# }

result = {}

menu = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
name = menu.find_elements(By.CSS_SELECTOR, "a")     #.text
date = menu.find_elements(By.CSS_SELECTOR, "time")

for index in range(len(name)):
    result[index] = {"time": date[index].text, "name": name[index].text}

print(result)

driver.close()  # Closes on current tab
# driver.quit()   # Closes entire browser
