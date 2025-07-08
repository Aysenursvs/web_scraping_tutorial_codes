from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        #course_name = course.find('h5', class_='card-title').text
        course_price = course.a.text.split()[-1]
        print(f'Course Name: {course_name} | Course Price: {course_price}')
