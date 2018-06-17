import sys
import requests
import time
from bs4 import BeautifulSoup
import urllib

'''
Given a starting url of ant wikipedia page, work if it possible to get to https://en.wikipedia.org/wiki/Philosophy
by only clicking on the first link of each article. Ensure not to get stuck in loop i.e visiting the same
page twice , which should return false. Give a max number of visited pages to 25 if not specified by user.
Ensure not to over load server with lots of requests.
'''

# pseudo code
# get starting url string.
# get url web page.
# add to search history
# while most current url in search history not equal target
#    if list size = limit
#        exit program
#
#   get web page of most current in search history
#   get first link element in article
#   if url not in list
#       add url in link element to search history
#    else
#        exit program


def continue_crawl(search_history, limit):
    '''

    :param search_history:
    :param target_url:
    :return:
    '''

    print(f'{search_history[-1]} appears {search_history.count(search_history[-1])} in list')
    if len(search_history) >= limit or (search_history.count(search_history[-1]) > 1):
        return False
    return True

def get_next_url(next_url):

    # get the HTML from "url", use the requests library
    # feed the HTML into Beautiful Soup
    # find the first link in the article
    # return the first link as a string, or return None if there is no link
    web_page = requests.get(next_url)
    html = web_page.text
    soup = BeautifulSoup(html, "html.parser")

    # TODO: find the first link in the article, or set to None if
    # there is no link in the article.
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if article_link:
        return urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return None

def get_input(starting_url, limit=25):
    print(f'Main file: {sys.argv[0]}')
    if len(sys.argv) < 1:
        # a starting url must be provided.
        return None
    else:
        starting_url = sys.argv[1]
        print(f'Starting URL is: {starting_url}')
        try:
            limit = sys.argv[2]
        except IndexError:
            # limit is not required. Default is 25
            pass

    return starting_url, limit

def main():
    # get the starting url from user
    # must have a starting url
    # testing vars will removed when get_input is used.
    target_url = 'https://en.wikipedia.org/wiki/Philosophy'
    starting_url = 'https://en.wikipedia.org/wiki/Blow_(film)'
    limit = 25
    count = 1

    search_history = list()
    search_history.append(starting_url)
    print(f'{count}: {starting_url}')

    while continue_crawl(search_history, limit):
        count = count + 1
        if len(search_history) > 1:
            # wait for seconds after first and subsequant calls before next request.
            time.sleep(2)

        # get the next url out of search history
        next_url = get_next_url(search_history[-1])

        if next_url == target_url:
            # infrom user of target reached
            print(f'The target url {target_url} has been reached.')
        else:
            search_history.append(next_url)


if __name__ == '__main__':
    main()
