#! PYTHON 3

import csv
import pprint
with open('ICAN_Trans_Count_06_01_2016.csv', newline='') as f:
    reader = csv.reader(f)
    
    lis=[[]]
    for row in reader:
        lis.append(row)
    #print(lis)
    #print(lis[1:4])
    fc=0
    
    prelist=[]
    maxv=0
    resultlist=[]
    for i in range(3,len(lis)):
         listnow=lis[i]
         prelist=lis[i-1]
         if listnow[0] != prelist[0]:
            maxv=0
            fc=fc+1
         elif listnow[0]==prelist[0]:
            if int(listnow[2])> int(maxv):
                maxv=listnow[2]
                resultlist.insert(fc,i)
            if int(prelist[2])> int(maxv):
                maxv=prelist[2]
                resultlist.insert(fc,i-1)
    strin=[]
    #for i in range(len(resultlist)):
    strin.append(lis[1])
    for i in range(1,len(lis)):
        strin.append(lis[resultlist[i]])
    #f=open('ICAN_Trans_Count_06_24_2016-result.xlsx','w')
    pprint.pprint(strin[0:120])
'''print(len(resultlist))
print(len(lis))'''

'''import csv
with open('ICAN_Trans_Count_06_02_2016.csv', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)'''
