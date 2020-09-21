#coding=utf-8
import  requests
from urllib.request import quote, unquote
wdd = input("请输入")
url = "http://api.qingyunke.com/api.php?key=free&msg=" + wdd
res1 = quote(url, safe=";/?:@&=+$,", encoding="utf-8") # 编码
response = requests.get(res1)
print(response.content.decode())
input()