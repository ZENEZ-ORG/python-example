#_*_ coding:utf-8 _*_  
fd = open("test.txt")  
  
spaces = 0
char_cnt = 0
word_cnt=0 
  
for line_cnt, line in enumerate(fd):  
    spaces += line.count(' ')
    char_cnt += line.__len__()
    word_cnt += len(line.split(" "))
    print (line_cnt, line.replace('\n',''))
  
fd.close()
  
print ('빈칸 : %d'%spaces)
print ('글자 : %d'%char_cnt)
print ('단어 : %d'%word_cnt)
print ('문단 : %d'%(line_cnt+1))