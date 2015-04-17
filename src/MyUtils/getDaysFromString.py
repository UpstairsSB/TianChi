# coding=utf-8
'''
Created on 2015年4月12日
Creatd at 2015年4月12日 下午1:58:05
@author: zhanghb   mail:zhb_bupt@163.com
'''
import datetime
def getDaysString (dateScope):
    dateScope=dateScope.strip()
    tempDay=[]
    tempDay=dateScope.split("-")
    if(len(tempDay)==1):
        return '"'+dateScope+'"'
    if(len(tempDay)!=2):
        print("您输入的日期范围有误，请重新输入")
        return ""
    dateStart=datetime.datetime.strptime(tempDay[0],"%Y%m%d")
    dateEnd=datetime.datetime.strptime(tempDay[1],"%Y%m%d")
    i=datetime.timedelta(days=0)
    days=[]
    while i<((dateEnd-dateStart+datetime.timedelta(days=1))):
        days.append('"'+(dateStart+i).strftime('%Y%m%d')+'"')
        i+=datetime.timedelta(days=1)
    tempDaysString=",".join(days)
    return tempDaysString
def getDays (dateScope):
    dateScope=dateScope.strip()
    tempDay=[]
    tempDay=dateScope.split("-")
    if(len(tempDay)==1):
        return tempDay.append('"'+dateScope+'"')
    if(len(tempDay)!=2):
        print("您输入的日期范围有误，请重新输入")
        return ""
    dateStart=datetime.datetime.strptime(tempDay[0],"%Y%m%d")
    dateEnd=datetime.datetime.strptime(tempDay[1],"%Y%m%d")
    i=datetime.timedelta(days=0)
    days=[]
    while i<((dateEnd-dateStart+datetime.timedelta(days=1))):
        days.append((dateStart+i).strftime('%Y%m%d'))
        i+=datetime.timedelta(days=1)
    return days
def getDaysNum (dateScope):
    dateScope=dateScope.strip()
    tempDay=[]
    tempDay=dateScope.split("-")
    if(len(tempDay)==1):
        return 1
    if(len(tempDay)!=2):
        print("您输入的日期范围有误，请重新输入")
        return ""
    dateStart=datetime.datetime.strptime(tempDay[0],"%Y%m%d")
    dateEnd=datetime.datetime.strptime(tempDay[1],"%Y%m%d")
    i=datetime.timedelta(days=0)
    days=[]
    while i<((dateEnd-dateStart+datetime.timedelta(days=1))):
        days.append((dateStart+i).strftime('%Y%m%d'))
        i+=datetime.timedelta(days=1)
    return len(days)
    
# 以下为测试代码          
# test=getDaysString("20141122-20141127")
# test2=getDays("20141122-20141127")