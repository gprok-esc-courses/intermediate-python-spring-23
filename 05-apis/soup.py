import requests
from bs4 import BeautifulSoup

url = 'https://www.unyp.cz/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link['href'])
