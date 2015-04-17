# coding=utf-8
'''
Created on 2015年4月15日
Creatd at 2015年4月15日 下午3:20:06
@author: zhanghb   mail:zhb_bupt@163.com
'''
def ItemWantedFilter(sourceDataFile,filterFile,outputFile):
    itemWantedDict={}
    sourceDataReader=open(sourceDataFile,"r")
    filterReader=open(filterFile,"r")
    outputWriter=open(outputFile,"w+")
    templinedata=""
    templinedata=filterReader.readline()
    
    count=0
    
    while templinedata!="":
        
        count+=1
        print(count)
        
        templinedata=templinedata.strip()
        itemWantedDict[templinedata]=""
        templinedata=filterReader.readline()
    templinedata=""
    templinedata=sourceDataReader.readline()
    
    count=0
    
    while templinedata!="":
        
        count+=1
        print(count)
        
        templinedata=templinedata.strip()
        if itemWantedDict.__contains__(templinedata.split(",")[1]):
            outputWriter.write(templinedata+"\n")
        templinedata=sourceDataReader.readline()

ItemWantedFilter(r"D:\TianChi\TrainWorkSpace\test\test.csv",r"D:\TianChi\TrainWorkSpace\test\filter.csv", r"D:\TianChi\TrainWorkSpace\test\result.csv")
    
    