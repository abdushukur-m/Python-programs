import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
print(news[0].text)
