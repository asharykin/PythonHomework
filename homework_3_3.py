import requests
from bs4 import BeautifulSoup

url = "https://www.yahoo.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text
    print("Название страницы:", title)
