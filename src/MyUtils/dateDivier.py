# coding=utf-8
'''
Created on 2015年4月15日
Creatd at 2015年4月15日 上午11:18:49
@author: zhanghb   mail:zhb_bupt@163.com
'''
import datetime
def dateDivier_1(dateScope,dateDelta):
    tempDay=dateScope.split("-")
    dateStart=datetime.datetime.strptime(tempDay[0],"%Y%m%d")
    dateEnd=datetime.datetime.strptime(tempDay[1],"%Y%m%d")
    tempdateStart=dateStart
    tempdateEnd=dateStart
    tempdateScope=[]
    templabelDate=[]
    tempout=[]
    i=datetime.timedelta(days=dateDelta)
    while i<(dateEnd-tempdateStart+datetime.timedelta(days=1)):
        tempdateEnd=tempdateStart+datetime.timedelta(days=(dateDelta-1))
        tempdateScope.append((tempdateStart).strftime('%Y%m%d')+"-"+(tempdateEnd).strftime('%Y%m%d'))
        templabelDate.append((tempdateEnd+datetime.timedelta(days=1)).strftime('%Y%m%d'))
        tempdateStart+=i
    if datetime.timedelta(days=1)<=(dateEnd-tempdateStart):
        print((tempdateStart).strftime('%Y%m%d')+"-"+(dateEnd).strftime('%Y%m%d')+"不足以构成区间，舍弃")
    for i in range(len(tempdateScope)):
        templist=[]
        templist.append(tempdateScope[i])
        templist.append(templabelDate[i])
        tempout.append(templist)
    return tempout
def dateDivier(dateScope,dateDelta,*dateSkip):
    tempDay=dateScope.split("-")
    dateStart=datetime.datetime.strptime(tempDay[0],"%Y%m%d")
    dateEnd=datetime.datetime.strptime(tempDay[1],"%Y%m%d")
    tempdateStart=dateStart
    tempdateEnd=dateStart
    tempdateScope=[]
    templabelDate=[]
    tempout=[]
    i=datetime.timedelta(days=dateDelta)
    if dateSkip==():
        temp_dateSkip=dateDelta
    else:
        temp_dateSkip=dateSkip[0]
    while i<(dateEnd-tempdateStart+datetime.timedelta(days=1)):
        tempdateEnd=tempdateStart+datetime.timedelta(days=(dateDelta-1))
        tempdateScope.append((tempdateStart).strftime('%Y%m%d')+"-"+(tempdateEnd).strftime('%Y%m%d'))
        templabelDate.append((tempdateEnd+datetime.timedelta(days=1)).strftime('%Y%m%d'))
        tempdateStart+=datetime.timedelta(days=temp_dateSkip)
    if datetime.timedelta(days=1)<=(dateEnd-tempdateStart):
        print((tempdateStart).strftime('%Y%m%d')+"-"+(dateEnd).strftime('%Y%m%d')+"不足以构成区间，舍弃")
    for i in range(len(tempdateScope)):
        templist=[]
        templist.append(tempdateScope[i])
        templist.append(templabelDate[i])
        tempout.append(templist)
    return tempout

def dateDivier_3(dateScope,dateDelta,*dateSkip):
    tempDay=dateScope.split("-")
    dateStart=datetime.datetime.strptime(tempDay[0],"%Y%m%d")
    dateEnd=datetime.datetime.strptime(tempDay[1],"%Y%m%d")
    tempdateStart=dateStart
    tempdateEnd=dateStart
    tempdateScope=[]
    i=datetime.timedelta(days=dateDelta)
    if dateSkip==():
        temp_dateSkip=dateDelta
    else:
        temp_dateSkip=dateSkip[0]
    while i<(dateEnd-tempdateStart+datetime.timedelta(days=1)):
        tempdateEnd=tempdateStart+datetime.timedelta(days=(dateDelta-1))
        tempdateScope.append((tempdateStart).strftime('%Y%m%d')+"-"+(tempdateEnd).strftime('%Y%m%d'))
        tempdateStart+=datetime.timedelta(days=temp_dateSkip)
    if datetime.timedelta(days=1)<=(dateEnd-tempdateStart):
        print((tempdateStart).strftime('%Y%m%d')+"-"+(dateEnd).strftime('%Y%m%d')+"不足以构成区间，舍弃")
    return tempdateScope
#以下是测试代码
if __name__=="__main__":
    test1=dateDivier_1("20141112-20141212",3)
    test3=dateDivier_3("20141112-20141212",3,1)
    test2=dateDivier("20141112-20141212",3)
# a=[]