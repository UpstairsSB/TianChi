# coding=utf-8
'''
Created on 2015年4月19日

@author: zhanghb   mail:zhb_bupt@163.com
'''
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
    userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate","GaoCateItemNum"]
    itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
    CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
    DemandFeatureList=["DemandFeature"]
    userFeatureIdList=["1","2","3","4","1001"]
    itemFeatureIdList=["100","101","102","103","104"]
    CateFeatureIdList=["200","201","202","203","204"]
    DemandFeatureIdList=["400","401","402","403"]
    fealestIdList=userFeatureIdList+itemFeatureIdList+CateFeatureIdList+DemandFeatureIdList
    inputFile=r"D:\TianChi\TrainWorkSpace\Gao\trainset\1212_Trainset.csv"
    outputFile=r"D:\TianChi\TrainWorkSpace\Gao\1212_Trainset.csv"
    ZhangToGao(inputFile,outputFile,fealestIdList)