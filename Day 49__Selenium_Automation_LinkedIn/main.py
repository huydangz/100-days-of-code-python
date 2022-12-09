from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
URL = "https://www.linkedin.com/"
USERNAME = "lamasia30@gmail.com"
PASSWORD= "Dng@2022"
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get(URL)
driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
driver.quit()