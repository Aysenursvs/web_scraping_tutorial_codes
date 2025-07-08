from bs4 import BeautifulSoup
import requests

response = requests.get('http://localhost').text

soup = BeautifulSoup(response, 'lxml')
print(soup.prettify())