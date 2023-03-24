from bs4 import BeautifulSoup
import requests


root = "https://subslikescript.com/"

website = f'{root}movies'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

box = soup.find('article', class_='main-article')
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_="page-item")
last_page = pages[9].text


links = []
for page in range(1, 3):
    website = f'{root}/movies_letter-A?page={page}'
    print(website)
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    box = soup.find('article', class_='main-article')

    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            website = f'{root}{link}'
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, "lxml")
            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcript = box.find(
                'div', class_="full-script").get_text(strip=True, separator=" ")

            with open(title + '.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print('-------Link not working-----------')
            print(link)
