import requests
import timeit
from bs4 import BeautifulSoup


def main():
    print('working')
    response = requests.get('https://www.bloomberg.com/europe')
    print(response.status_code)
    page = response.text
    print(type(page))

    soup = BeautifulSoup(page, 'html.parser')

    print(soup.title)
    print(soup.find_all('a'))

    print('*\n' *12)
    print(soup.find(id="bb-lazy-img-328028706"))
    #print(soup.prettify())





if __name__ == '__main__':
    main()
