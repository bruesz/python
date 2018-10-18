# 导入urllib库，处理网页请求信息
from urllib import request,parse
from bs4 import BeautifulSoup
import re

url = 'https://www.baidu.com/s?wd=python&pn=10'

# 模拟浏览器的header以避过某些网站的反爬策略
agent_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
# 这里的request.Request是一个class，记住第二个Request大写
# request.Request(url,data,headers), 如果当中data没有数据，就传入None
req = request.Request(url,None,agent_headers)
response = request.urlopen(req)
response = response.read().decode('UTF-8')

soup = BeautifulSoup(response,'html.parser')

links = soup.find_all('a', {'data-click':re.compile(r'^{'),'href':re.compile(r'^http://www.baidu.com/link')})

for each_link in links:
    print(each_link.text)
