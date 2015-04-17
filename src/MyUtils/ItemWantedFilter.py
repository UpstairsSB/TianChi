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
        if itemWantedDict.__contains__(templinedata.split("\t")[0].split("|")[1]):
            outputWriter.write(templinedata+"\n")
        templinedata=sourceDataReader.readline()
if __name__=="__main__":
    ItemWantedFilter(r"D:\TianChi\TrainWorkSpace\e_PredictSet\predictset\20141212-20141218_predictset.csv",r"D:\TianChi\TrainWorkSpace\e_PredictSet\ItemWantedFilter.csv", r"D:\TianChi\TrainWorkSpace\e_PredictSet\predictset\predictset.csv")
    
    