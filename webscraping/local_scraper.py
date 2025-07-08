from bs4 import BeautifulSoup
import os

# Read the local HTML file
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(current_dir, 'sample_jobs.html')

with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

# Find job postings
job_cards = soup.find_all('div', class_='job-card')

print(f'Total {len(job_cards)} job postings found:')
print('=' * 50)

for index, job in enumerate(job_cards, 1):
    # Job title
    title = job.find('h3', class_='job-title').get_text(strip=True)
    
    # Company name
    company = job.find('p', class_='company-name').get_text(strip=True)
    
    # Location
    location = job.find('span', class_='location').get_text(strip=True)
    
    # Salary
    salary = job.find('p', class_='salary').get_text(strip=True)
    
    # Job description
    description = job.find('div', class_='job-description').get_text(strip=True)
    
    # Post date
    post_date = job.find('span', class_='post-date').get_text(strip=True)
    
    # Job ID (from data attribute)
    job_id = job.get('data-job-id')

    with open(f'results/job_results{index}.txt', 'w', encoding='utf-8') as results_file:
        results_file.write(f"{index}. {title}\n")
        results_file.write(f"   Company: {company}\n")
        results_file.write(f"   Location: {location}\n")
        results_file.write(f"   Salary: {salary}\n")
        results_file.write(f"   Description: {description}\n")
        results_file.write(f"   Post Date: {post_date}\n")
        results_file.write(f"   Job ID: {job_id}\n")
        results_file.write("\n")
    print(f"{index}. {title}")
    print(f"   Company: {company}")
    print(f"   Location: {location}")
    print(f"   Salary: {salary}")
    print(f"   Description: {description}")
    print(f"   Post Date: {post_date}")
    print(f"   Job ID: {job_id}")
    print()

print("=" * 50)
print("Web scraping completed successfully!")

# Bonus: Store data as a dictionary
jobs_data = []
for job in job_cards:
    job_data = {
        'title': job.find('h3', class_='job-title').get_text(strip=True),
        'company': job.find('p', class_='company-name').get_text(strip=True),
        'location': job.find('span', class_='location').get_text(strip=True),
        'salary': job.find('p', class_='salary').get_text(strip=True),
        'description': job.find('div', class_='job-description').get_text(strip=True),
        'post_date': job.find('span', class_='post-date').get_text(strip=True),
        'job_id': job.get('data-job-id')
    }
    jobs_data.append(job_data)

print(f"Data stored in dictionary format. Example: {jobs_data[0]['title']}")
