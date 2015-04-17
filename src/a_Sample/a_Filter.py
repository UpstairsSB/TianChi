# coding=utf-8
'''
Created on 2015年4月12日
Creatd at 2015年4月12日 上午10:20:58
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf;
def ExistItemFilter(originalSampleName,filterName):
    existItemList=[]
    readLine=""
    
    count=0
    
    for tempfileName in filterName:
        try:
            temppath=Conf.filterPath+"/"+tempfileName
            tempReader=open(temppath,'r')
            readLine=tempReader.readline()
            while readLine!="" :
                
                count+=1
                print(count)
                
                readLine=readLine.strip()
                if readLine not in existItemList:
                    existItemList.append(readLine)
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
            
    count=0        
    
    for tempfileName in originalSampleName:
        try:
            temppath=Conf.originalSamplePath+"/"+tempfileName
            tempReader=open(temppath,'r')
            temppath=Conf.sampleOutputPath+"/"+tempfileName
            tempOutputWriter=open(temppath,'a')
            readLine=tempReader.readline()
            tempreadLine=[]
            while readLine!="" :
                
                count+=1
                print(count)
                
                readLine=readLine.strip()
                tempreadLine=readLine.split(",")
                if tempreadLine[1] in existItemList:
                    tempOutputWriter.write(readLine+"\n")
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
def ExistUserFilter(originalSampleName,filterName):
    existUserList=[]
    readLine=""
    for tempfileName in filterName:
        try:
            temppath=Conf.filterPath+"/"+tempfileName
            tempReader=open(temppath,'r')
            readLine=tempReader.readline()
            while readLine!="" :
                readLine=readLine.strip()
                if readLine not in existUserList:
                    existUserList.append(readLine)
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
    for tempfileName in originalSampleName:
        try:
            temppath=Conf.originalSamplePath+"/"+tempfileName
            tempReader=open(temppath,'r')
            temppath=Conf.sampleOutputPath+"/"+tempfileName
            tempOutputWriter=open(temppath,'a')
            readLine=tempReader.readline()
            tempreadLine=[]
            while readLine!="" :
                readLine=readLine.strip()
                tempreadLine=readLine.split(",")
                if tempreadLine[0] in existUserList:
                    tempOutputWriter.write(readLine+"\n")
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
def ExistUserItemFilter_1(originalSampleName,filterName):
    existUserItemList=[]
    readLine=""
    for tempfileName in filterName:
        try:
            temppath=Conf.filterPath+"/"+tempfileName
            tempReader=open(temppath,'r')
            readLine=tempReader.readline()
            while readLine!="" :
                readLine=readLine.strip()
                if readLine not in existUserItemList:
                    existUserItemList.append(readLine)
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
    for tempfileName in originalSampleName:
        try:
            temppath=Conf.originalSamplePath+"/"+tempfileName
            tempReader=open(temppath,'r')
            temppath=Conf.sampleOutputPath+"/"+tempfileName
            tempOutputWriter=open(temppath,'a')
            readLine=tempReader.readline()
            while readLine!="" :
                readLine=readLine.strip()
                if readLine in existUserItemList:
                    tempOutputWriter.write(readLine+"\n")
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
def ExistUserItemFilter_2(originalSampleName,userFilterName,itemFilterName):
    existUserList=[]
    existItemList=[]
    readLine=""
    for tempfileName in userFilterName:
        try:
            temppath=Conf.filterPath+"/"+tempfileName
            tempReader=open(temppath,'r')
            readLine=tempReader.readline()
            while readLine!="" :
                readLine=readLine.strip()
                if readLine not in existUserList:
                    existUserList.append(readLine)
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
    for tempfileName in itemFilterName:
        try:
            temppath=Conf.filterPath+"/"+tempfileName
            tempReader=open(temppath,'r')
            readLine=tempReader.readline()
            while readLine!="" :
                readLine=readLine.strip()
                if readLine not in existItemList:
                    existItemList.append(readLine)
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
    for tempfileName in originalSampleName:
        try:
            temppath=Conf.originalSamplePath+"/"+tempfileName
            tempReader=open(temppath,'r')
            temppath=Conf.sampleOutputPath+"/"+tempfileName
            tempOutputWriter=open(temppath,'a')
            readLine=tempReader.readline()
            tempreadLine=[]
            while readLine!="" :
                readLine=readLine.strip()
                tempreadLine=readLine.split(",")
                if tempreadLine[0] in existUserList:
                    if tempreadLine[1] in existItemList:
                        tempOutputWriter.write(readLine+"\n")
                readLine=tempReader.readline()
            tempReader.close()
        except:
            print(tempfileName+"不存在")
        