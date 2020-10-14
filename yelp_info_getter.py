#! /usr/bin/python3


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import re

""""
#S1 Insert search results page link
#S2 get links from page
#S3 iterate over each link obtaine and get title, website, link, Rating, total reviews
#S4 insert into csv file for export

"""

url = "https://www.yelp.com/search?find_desc=Dentist%20Endodontist&find_loc=Herndon%2C%20VA&cflt=endodontists&l=g%3A-77.38906592130661%2C39.0877365793137%2C-77.44743347167969%2C38.98426629317477&sortby=review_count"
url_yelp = "https://www.yelp.com"
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}

def get_soup(url):
    r = requests.get(url, headers = headers)
    if r.status_code == 200:
        html = r.text
        r.close()
        soup = bs(html, features="html.parser")
        return soup
    else:
        r.close()
        soup = ''
    return soup

def get_soup_result_links(soup):
    soup_a = soup.find_all("a")
    list_result_links = []

    for a in soup_a:
        if a.has_attr('href'):
            if '/biz/' in a['href']:
                a_temp = a['href']
                a_temp = a_temp.split('?')[0]
                list_result_links.append(a_temp)

    set_result_links = set(list_result_links)
    return set_result_links

def get_soup_info(soup):
    for i in soup.body:
        print(i.a.text)


"""

FOR TESTING

import yelp_info_getter as yi
soup = yi.get_soup(yi.url)
result_links = yi.get_soup_result_links(soup)
result_links


"""