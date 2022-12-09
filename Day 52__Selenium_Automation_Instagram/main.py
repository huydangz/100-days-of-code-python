import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
INSTA_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "brisbane"
INSTA_USERNAME = "lamasia40@gmail.com"
INSTA_PASSWORD = "Dng@2022"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))

    def login(self):
        self.driver.get(INSTA_URL)

        time.sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(INSTA_USERNAME)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(5)
        for a in self.driver.find_elements(By.TAG_NAME, "a"):
            if "followers" in a.get_attribute("href"):
                a.click()
                break
        #
        # time.sleep(2)
        # modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)


    def follow(self):
        time.sleep(5)
        dialog = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        all_buttons = dialog.find_elements(By.TAG_NAME, "button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                continue
                # cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                # cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
