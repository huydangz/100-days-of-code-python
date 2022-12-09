import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
URL = "https://tinder.com/"

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get(URL)

time.sleep(5)
tags = driver.find_elements(By.CLASS_NAME, "c1p6lbu0")
for tag in tags:
    if tag.text == "Log in":
        tag.click()
        break

time.sleep(4)
tags = driver.find_elements(By.CLASS_NAME, "button")
for tag in tags:
    if tag.text == "LOG IN WITH PHONE NUMBER":
        tag.click()
        break

time.sleep(4)
phone_tag = driver.find_element(By.NAME, "phone_number")
phone_tag.send_keys("977201771")
# driver.quit()

# =========================================================================
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# from time import sleep
#
# FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
# FB_PASSWORD = YOUR FACEBOOK PASSWORD
#
# chrome_driver_path = YOUR CHROME DRIVER PATH
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("http://www.tinder.com")
#
# sleep(2)
# login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
# login_button.click()
#
# sleep(2)
# fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
# fb_login.click()
#
# sleep(2)
# base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(fb_login_window)
# print(driver.title)
#
# email = driver.find_element_by_xpath('//*[@id="email"]')
# password = driver.find_element_by_xpath('//*[@id="pass"]')
#
# email.send_keys(FB_EMAIL)
# password.send_keys(FB_PASSWORD)
# password.send_keys(Keys.ENTER)
#
# driver.switch_to.window(base_window)
# print(driver.title)
#
# sleep(5)
# allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
# allow_location_button.click()
# notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
# notifications_button.click()
# cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
# cookies.click()
#
# for n in range(100):
#     sleep(1)
#     try:
#         print("called")
#         like_button = driver.find_element_by_xpath(
#             '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
#         like_button.click()
#     except ElementClickInterceptedException:
#         try:
#             match_popup = driver.find_element_by_css_selector(".itsAMatch a")
#             match_popup.click()
#         except NoSuchElementException:
#             sleep(2)
#
# driver.quit()