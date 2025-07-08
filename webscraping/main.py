from bs4 import BeautifulSoup
import requests

# User-Agent header ekleyerek gerçek browser gibi görünmeye çalışalım
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

job_cards = soup.find_all('div', class_ = 'srp-listing  clearfix ')

print(f'Toplam {len(job_cards)} iş ilanı bulundu.')


    
