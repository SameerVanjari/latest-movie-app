import requests
from bs4 import BeautifulSoup

URL = 'https://www.freejobalert.com/upcoming-exam-dates-of-various-jobs/1835/'
req = requests.get(URL)

soup = BeautifulSoup(req.content, 'html5lib')

with open("index22.html", "w", encoding='utf-8') as fp:
    fp.write(soup.prettify())
