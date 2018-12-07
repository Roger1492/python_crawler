# 基本GUI界面

import tkinter as tk
from bs4 import BeautifulSoup
import os
import re
import urllib
import urllib3
import requests

window = tk.Tk()
window.title('my')
window.geometry('500x200')

# 标签
l = tk.Label(window, text='输入地址:', font=('Arial', 12), width=15, height=2)
l.pack()

# Entry
url = tk.StringVar()
e = tk.Entry(window, width=200, show=None)
e.pack()


# 下载功能
def hitme():
	url = e.get()   # 获取下载地址
	r = requests.get(url).content
	soup = BeautifulSoup(r, 'lxml')
	# title = soup.title.string
	img = soup.find_all('div', 'pic')

	# 创建文件夹并进入
	os.mkdir('250')
	os.chdir('250')

	num = 1
	for i in img:
		num += 1
		g = i.a.img.get('src')
		r1 = requests.get(g)

		with open(str(num) + '.jpg', 'wb') as j:
			j.write(r1.content)


# 按钮
b = tk.Button(window, text='开始下载', width=15, height=2, command=hitme)
b.pack()

window.mainloop()
