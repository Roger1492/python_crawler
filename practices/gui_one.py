# 基本GUI界面

import tkinter as tk
from bs4 import BeautifulSoup
import os
import re
import urllib
import urllib3
import requests

window = tk.Tk()
window.title('下载器')
window.geometry('500x200')

# 标签
l = tk.Label(window, text='输入地址:', font=('Arial', 12), width=15, height=2)
l.pack()

# Entry
url = tk.StringVar()
e = tk.Entry(window, width=200, show=None)
e.pack()


# 添加前置0
def addZero(n):
	if n<=9:
		return '0'+str(n)
	else:
		return ''+str(n)

# 下载功能
def hitme():
	url = e.get()   # 获取下载地址
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
		r1 = requests.get(f)

		with open(str(i)+'.jpg', 'wb') as j:
			j.write(r1.content)


# 按钮
b = tk.Button(window, text='开始下载', width=15, height=2, command=hitme)
b.pack()

window.mainloop()