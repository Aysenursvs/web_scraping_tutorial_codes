from bs4 import BeautifulSoup
import requests

# User-Agent header ekleyerek gerçek browser gibi görünmeye çalışalım
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

html_text = requests.get('https://tr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=0a4c06f1e7e8166f', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')

job_cards = soup.find_all('li', class_='css-1ac2h1w eu4oa1w0')

print(f'Toplam {len(job_cards)} iş ilanı bulundu.')

if len(job_cards) == 0:
    print("İş ilanı bulunamadı.")
else:   
    for job in job_cards:
        print(job.prettify())
        print('**************************************************')

    
