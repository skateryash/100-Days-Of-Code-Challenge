from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

chrome_web_driver = "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_web_driver))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3408464460&f_AL=true&f_WT=2&geoId=102713980&keywords=PYTHON%20WEB%20DEVELOPMENT%20TRAINING%20AND%20INTERNSHIP%20PROGRAM&location=India&refresh=true")
sleep(10)
sign_in = driver.find_element(By.CLASS_NAME, "job-alert-redirect-section__cta")
sign_in.click()
sleep(5)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
submit = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

username.send_keys(os.getenv('MY_EMAIL'))
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))
submit.click()
sleep(10)

job = driver.find_element(By.LINK_TEXT, "Training +internship")
job.click()
sleep(7)

easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
easy_apply.click()

country_code = driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3408464460-9-phoneNumber-country")
country_code.click()
country_code.send_keys("In")
country_code.send_keys(Keys.ENTER)

phone = driver.find_element(By.ID, "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3408464460-9-phoneNumber-nationalNumber")
phone.send_keys(os.getenv("MY_MOBILE_NO"))

resume_div = driver.find_element(By.CLASS_NAME, "jobs-resume-picker__resume-btn-container")
resume = resume_div.find_element(By.CSS_SELECTOR, "span")
resume.click()

submit_application = driver.find_element(By.CSS_SELECTOR, "footer button span")
submit_application.click()

print("Successful")


