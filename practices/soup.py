# -*- coding: UTF-8 -*-

import requests
import urllib
import re
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

def getContent():
  res = requests.get(url).content
  soup = BeautifulSoup(res, 'lxml')
  s = soup.findAll('span', 'inq')

  for a in s:
  	print(a.string)

if __name__ == "__main__":
    getContent()