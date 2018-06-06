import requests
from bs4 import BeautifulSoup

'''
Given a starting url of ant wikipedia page, work if it possible to get to https://en.wikipedia.org/wiki/Philosophy
by only clicking on the first link of each article. Ensure not to get stuck in loop i.e visiting the same
page twice , which should return false. Give a max number of visited pages to 25 if not specified by user.
Ensure not to over load server with lots of requests.
'''



def continue_crawl(search_history, target_url):
    '''

    :param search_history:
    :param target_url:
    :return:
    '''
    pass


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
