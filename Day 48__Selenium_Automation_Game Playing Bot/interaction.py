from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH))
driver.get(URL)

# Click:
# driver.find_element(By.CSS_SELECTOR, "#articlecount a").click()
# driver.find_element(By.LINK_TEXT, "Content portals").click()

# Type input:
# driver.find_element(By.CSS_SELECTOR, "#searchInput").send_keys("Python")
# driver.find_element(By.CSS_SELECTOR, "#searchInput").send_keys(Keys.ENTER)

# driver.quit()

driver.find_element(By.NAME, "fName").send_keys("First")
driver.find_element(By.NAME, "lName").send_keys("Last")
driver.find_element(By.NAME, "email").send_keys("email@mail.com")
driver.find_element(By.CSS_SELECTOR, ".btn-block").click()
