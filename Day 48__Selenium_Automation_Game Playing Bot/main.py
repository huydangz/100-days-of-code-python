import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get(URL)

timeout = time.time() + 120
timeslot = time.time() + 5
bought_items = []
while True:
    driver.find_element(By.CSS_SELECTOR, "#cookie").click()

    if time.time() > timeslot:
        # update money and prices
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        items = [item for item in driver.find_elements(By.CSS_SELECTOR, "#store b") if item.text != ""]
        prices = [int(item.text.split("-")[1].replace(",", "")) for item in items]
        names = [item.text.split("-")[0] for item in items]

        # check which item can buy
        buyable_prices = [price for price in prices if money >= price]
        for n in range(len(prices)):
            if prices[n] == max(buyable_prices) and names[n] not in bought_items:
                print(f'money={money} buy {names[n]} (price={prices[n]})')
                items[n].click()
                bought_items.append(names[n])
                break

        # increase timeslot again
        timeslot = time.time() + 5

    if time.time() > timeout:
        print(driver.find_element(By.ID, "cps").text)
        break

# driver.quit()

# ===========================================================================
# URL = "https://www.python.org/"
#
# driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH))
# driver.get(URL)
#
# dict = {}
# for tag in driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li"):
#     time = tag.find_element(by=By.TAG_NAME, value="time").text
#     event = tag.find_element(by=By.TAG_NAME, value="a").text
#     dict[len(dict)] = {
#         "time": time,
#         "event": event
#     }
#
# print(dict)
#
# driver.quit()
