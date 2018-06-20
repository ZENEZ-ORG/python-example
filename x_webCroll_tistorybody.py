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
f = open("test.txt", 'w')

for i in range(0, len(res)) :
    pst = BeautifulSoup(str(res[i]), 'lxml')
    title = pst.find_all("strong", class_="tit_post")
    context = pst.find_all("p", class_="txt_post")
    category = pst.find_all("a", class_="link_cate")
    print('분류 : ' + category[0].text, '\n')
    f.write(category[0].text+'\n')
    print('제목 : ' + title[0].text, '\n')
    f.write(title[0].text+'\n')
    print('요약 : ' + context[0].text+'\n')
    f.write(context[0].text+'\n')
    
f.close()

#단어수세기
fp = open("test.txt")
spaces = 0
char_cnt = 0
word_cnt=0 

for line_cnt, line in enumerate(fp):  
    spaces += line.count(' ')
    char_cnt += line.__len__()
    word_cnt += len(line.split(" "))
    print (line_cnt, line.replace('\n',''))
  
fp.close()

#print ("*" * 50)  
print ('빈칸 : %d'%spaces)
print ('글자 : %d'%char_cnt)
print ('단어 : %d'%word_cnt)
print ('문단 : %d'%(line_cnt+1))