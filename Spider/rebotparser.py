# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:29:36 2019

@author: yuy15
"""

import urllib.robotparser as urobot
import requests
#url="https://www.bilibili.com"
url="https://www.taobao.com"
rp=urobot.RobotFileParser()
rp.set_url(url+"/robots.txt")
rp.read()
user_agent='Baiduspider'
if rp.can_fetch(user_agent,'https://www.taobao.com/article/'):
#if rp.can_fetch(user_agent,'https://www.bilibili.com'):
    site=requests.get(url)
#    print(site)
#   200 返回值    
    print('seems good')
else:
    print("Cannot scrap because robot.txt bans")
    
"""
To test mutiple websites
for webs in weblist:
    try:
        if rp.can_fetch("*",newweb):
            site=requests.get(url)
    except:
        print("Banned by robots.txt")
"""