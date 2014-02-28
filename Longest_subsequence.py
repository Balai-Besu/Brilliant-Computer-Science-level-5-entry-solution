#!/usr/bin/python

n = int(raw_input())
dic = {'size': 0,'index': -1}
listSize = 1
result = 0
List  = [0] * n
for i in range(0,n):
    List[i] = int(raw_input())
for i in range(0,n-1):
    if List[i] < List[i+1] :
        listSize += 1
    else:
          if listSize > dic['size']:
                  dic['size'] = listSize 
                  dic['index'] = i
          listSize = 1

m = dic['index'] - dic['size'] + 1
for i in range(dic['index'], m-1, -1):
         result = result +  List[i]
if result < 0:
   result = result * -1
print result
  
