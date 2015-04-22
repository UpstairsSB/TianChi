# coding=utf-8
'''
Created on 2015年4月19日

@author: zhanghb   mail:zhb_bupt@163.com
'''
import os

def ZhangToGao(inputFile,outputFile,fealestIdList):
    inputFilereader=open(inputFile,"r")
    outputFileWriter=open(outputFile,"w")
    tempLineData=""
    tempLineData=inputFilereader.readline()
    tempfeatureDict={}
    count =0
    while(tempLineData!=""):
        
        count+=1
        print(count)
        
        for feature in fealestIdList:
            tempfeatureDict[feature]="0"
        tempLineData=tempLineData.strip()
        tempLineList=tempLineData.split("\t")
        i=0
        tempLineOut=""
        tempLineOut+=tempLineList[0]+"\t"
        for i in range(1,len(tempLineList)-1):
            tempfeatureDict[tempLineList[i].split(":")[0]]=tempLineList[i].split(":")[1]
        for tempfeature in fealestIdList:
            tempLineOut+=tempfeatureDict[tempfeature]+"\t"
        tempLineOut=tempLineOut.strip()
        outputFileWriter.write(tempLineOut+"\n")
        tempLineData=inputFilereader.readline()
    inputFilereader.close()
    outputFileWriter.close
                
        
#以下为测试代码
if __name__=="__main__":
    userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate"]
    itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
    CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
    DemandFeatureList=["DemandFeature"]
    userFeatureIdList=["1","2","3","4"]
    itemFeatureIdList=["100","101","102","103","104"]
    CateFeatureIdList=["200","201","202","203","204"]
    DemandFeatureIdList=["400","401","402","403","404","405","406","408","409","410","411","412"]
    fealestIdList=userFeatureIdList+itemFeatureIdList+CateFeatureIdList+DemandFeatureIdList
    
    traininputPath=r"D:\TianChi\TrainWorkSpace\Gao\train_in"
    trainoutputPath=r"D:\TianChi\TrainWorkSpace\Gao\train_out"
    predictinputPath=r"D:\TianChi\TrainWorkSpace\Gao\predict_in"
    predictoutputPath=r"D:\TianChi\TrainWorkSpace\Gao\predict_out"
    for trainFile in os.listdir(traininputPath):        
        trainFile_full_path=os.path.join(traininputPath,trainFile)
        trainoutputFile_full_path=os.path.join(trainoutputPath,trainFile)
        ZhangToGao(trainFile_full_path,trainoutputFile_full_path,fealestIdList)
    for predictFile in os.listdir(predictinputPath):
        predictFile_full_path=os.path.join(predictinputPath,predictFile)
        predictoutputFile_full_path=os.path.join(predictoutputPath,predictFile)
        ZhangToGao(predictFile_full_path,predictoutputFile_full_path,fealestIdList)