import requests
from bs4 import BeautifulSoup

rsp = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(rsp.text, "html.parser")
tags = soup.find_all(name="span", class_="titleline")
article_text = []
article_link = []
for tag in tags:
    article_text.append(tag.find(name="a").getText())
    article_link.append(tag.find(name="a").get("href"))

article_score = []
tags = soup.find_all(name="span", class_="score")
for tag in tags:
    article_score.append(tag.getText())

print(len(article_text))
print(len(article_link))
print(len(article_score))

#####################################################################

# with open(file="website.html", encoding="utf-8", mode="r") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.text)

#####################################################################

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
#
# driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
# driver.get(URL)
#
# for tag in driver.find_elements(By.CSS_SELECTOR, ".listicle-item h3"):
#     print(tag.text)
