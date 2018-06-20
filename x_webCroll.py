import json
from bs4 import BeautifulSoup
import requests
## 어쩌나

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
					'Accept-Encoding': 'none',
					'Accept-Language': 'en-US,en;q=0.8',
					'Connection': 'keep-alive'}
url = 'http://www.zenez.org'
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
res = soup.find_all("div", class_="list_content")

f = open("test.html", 'w')
f.write('{0}'.format(res[0]))
f.close()
print(res)