from collections import *
a=[]
letter=[]
c=[]
СharacterData = ""

with open(r"8.txt",'r',encoding="utf-8") as File:
    for line in File:
        letter = list(map(str,line.split()))
#Нахождение самого популярного в шифре символа
c = {letter.count(i): i for i in letter};
a = sorted(c.items(),reverse = True)
k = int(a[0][1],16)^ord('e')

for i in letter:
    print(chr(int(i, 16)^int(k)),end="")

