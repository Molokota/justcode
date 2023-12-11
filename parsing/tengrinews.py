import requests
from bs4 import BeautifulSoup

url = "https://tengrinews.kz/news/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
quotes2 = soup.find_all("span", class_="tn-article-title")
for i in quotes2:
    print(i.text)


