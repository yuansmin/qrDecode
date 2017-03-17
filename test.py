# -*- coding: utf-8 -*-
# @Date    : 2016-11-30 11:27:06
# @Author  : fancy (fancy@thecover.cn)

import requests

# URL = 'http://192.168.64.14:8002/decode'
URL = 'http://localhost:8002/decode'

def decode_img_with_file(file_name):
    f = open(file_name, 'r')
    files = {'file': f}
    resp = requests.get(URL, files=files)#, params=params)
    f.close()
    print resp.content

def decode_img_with_url(img_url):
    params = {'url': img_url}
    resp = requests.get(URL, params=params)
    print resp.content


if __name__ == '__main__':
    file_name = 'test.jpg'
    decode_img_with_file(file_name)
    url = 'http://mp.weixin.qq.com/mp/qrcode?scene=10000004&size=102&__biz=MjM5NjAwNzI0MA==&mid=2651948307&idx=3&sn=a5fa67242f7bbb7ebe97f5e38bd1be85'
    decode_img_with_url(url)
