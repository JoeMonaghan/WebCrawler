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

def continue_crawl(search_history, limit):
    '''
    Checks if limit is reached or the current url has been already visited. If either
    is true return false to stop the crawl.
    :param search_history: list of all visited urls.
    :param limit: max number of urls before reaching target.
    :return:
    '''
    if len(search_history) == limit or (search_history.count(search_history[-1]) > 1):
        return False
    return True

def get_next_url(next_url):
    '''
    Returns the first link in the article.
    :param next_url:
    :return: the first link
    '''

    web_page = requests.get(next_url)
    html = web_page.text
    soup = BeautifulSoup(html, "html.parser")

    # there is no link in the article.
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if article_link:
        return urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return None


def get_input(limit):
    '''
    Get the starting url and limit if provided. If limit is not of type int the
    program will exit informing user.
    :param limit:
    :return: starting url and limit if provided.
    '''
    print(f'Main file: {sys.argv[0]}')
    if len(sys.argv) < 1:
        # a starting url must be provided.
        return None
    else:
        starting_url = sys.argv[1]
        print(f'Starting URL is: {starting_url}')
        try:
            limit = int(sys.argv[2])
        except IndexError:
            # limit is not required. Default is 25
            pass
        except TypeError:
            print('Invalid input for limit must be a number')
            sys.exit()

    return starting_url, limit


def main():
    # get the starting url from user
    # must have a starting url
    # testing vars will removed when get_input is used.
    target_url = 'https://en.wikipedia.org/wiki/Philosophy'
    limit = 25

    if get_input() is not None:
        starting_url, limit = get_input(limit)
    else:
        print('A starting url is required!')
        sys.exit()
    count = 1

    search_history = list()
    search_history.append(starting_url)

    while continue_crawl(search_history, limit):
        print(f'{count}: {search_history[-1]}')
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
