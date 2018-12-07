# -*- coding: UTF-8 -*-

# 下载图片

import requests

url = 'http://a.hiphotos.baidu.com/image/pic/item/b999a9014c086e062550d0020f087bf40bd1cbfb.jpg'
r = requests.get(url)

with open('i.jpg', 'wb') as img:
	img.write(r.content)