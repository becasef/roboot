import argparse
import re
import requests
from urllib.request import quote, unquote
parser = argparse.ArgumentParser(description='聊天机器人 https://github.com/becases/roboot')
parser.add_argument('-q', type=str, default ='你是',help='需要和机器人要说的话')
args = parser.parse_args()
wdd = args.q
url = "http://api.qingyunke.com/api.php?key=free&msg=" + wdd
res1 = quote(url, safe=";/?:@&=+$,", encoding="utf-8")
strhtml = requests.get(res1)
print(re.findall(r"content\":\".*?(.+?)\"}", strhtml.text))