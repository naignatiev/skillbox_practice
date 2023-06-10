import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    for page_name in 'Java', 'Python', 'C++':
        url = 'https://ru.wikipedia.org/wiki/' + page_name
        response = requests.get(url)
        soup = BeautifulSoup(response.content)
        for tr in soup.find('table', class_='infobox').find_all('tr')[::-1]:
            link = tr.find('a', class_='external text')
            if link:
                print(link.text)
                break
