# coding=utf-8
'''
Created on 2015年4月22日

@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
#把没有找回率低的提交结果的user-item给过滤掉
def filter2(sourcefile,inputfile,outputfile):
    sourceReader=open(sourcefile,"r")
    inputReader=open(inputfile,"r")
    outputWriter=open(outputfile,"w")
    tempLineData=""
    
    useritemDict={}
    tempLineData=inputReader.readline()
    tempLineData=inputReader.readline()
    
    count=0
    
    while(tempLineData!=""):
        
        count+=1
        print(count)
        
        tempLineData=tempLineData.strip()
        useritemDict[tempLineData]=""
        tempLineData=inputReader.readline()
    tempLineData=""
    tempLineData=sourceReader.readline()
    
    count=0
    
    while(tempLineData!=""):
        
        count+=1
        print(count)
        
        tempLineData=tempLineData.strip()
        tempLineDataList=tempLineData.split("\t")[0].split("|")
        if useritemDict.__contains__(tempLineDataList[0]+","+tempLineDataList[1]):
            tempLineData=sourceReader.readline()
            continue
        else:
            outputWriter.write(tempLineData+"\n")
            tempLineData=sourceReader.readline()
#以下为测试代码
if __name__=="__main__":
    sourcefile=Conf.StrategyPath+"\\"+r"filiter2\predictsetResult_20150422.csv"
    inputfile=Conf.StrategyPath+"\\"+r"filiter2\filter2.csv"
    outputfile=Conf.StrategyPath+"\\"+r"filiter2\predictsetResult_20150422_filter2.csv"
    filter2(sourcefile,inputfile,outputfile) 