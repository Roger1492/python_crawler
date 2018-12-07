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
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    r = requests.get(url)
    res = BeautifulSoup(r)
    print(res.prettify())

# 按钮
b = tk.Button(window, text='开始下载', width=15, height=2, command=hitme)
b.pack()

window.mainloop()
