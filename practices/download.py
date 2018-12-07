# -*- coding: UTF-8 -*-

import tkinter as tk
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
import urllib
import requests

url = 'https://www.mzitu.com/160548'
ua = UserAgent()

# 添加前置0
def addZero(n):
	if n<=9:
		return '0'+str(n)
	else:
		return ''+str(n)

r = requests.get(url).content
soup = BeautifulSoup(r, 'lxml')

title = soup.title.string[0:-12]
imgAddress = soup.find_all('div', 'main-image')[0].p.a.img.get('src')[0:-6]
allPage = soup.find_all('span', 'dots')[0].next_sibling.span.string

# 创建文件夹并进入
if(os.path.exists(title)):
	os.rmdir(title)
else:
	os.mkdir(title)
	os.chdir(title)

num = 1
for i in range(1,int(allPage)+1):
	f = imgAddress+addZero(i)+'.jpg'
	print(f)
	header = {'user-agent': ua.random}
	r1 = requests.get(f, headers=header)
	f = open(str(i)+'.jpg', 'wb')
	f.write(r1.content)
	f.close()

	# with open(str(i)+'.jpg', 'wb') as j:
	# 	j.write(r1.content)