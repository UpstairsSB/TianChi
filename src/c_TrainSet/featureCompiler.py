# coding=utf-8
'''
Created on 2015年4月14日
Creatd at 2015年4月14日 上午11:05:19
@author: zhanghb   mail:zhb_bupt@163.com
'''
from MyUtils import MySQL
import Conf
from MyUtils.getDaysFromString import getDaysString
def getTrainset(dateScope,labeldate,tempTrainsetFile):
#     outputPath=Conf.trainsetTempPath+"\\"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"""
        select a.user_id,a.item_id,a.item_category,if(b.user_id is null,0,1)
        from
        (select
        distinct user_id, item_id,item_category
        from useritem
        where date_format(usertime,'%%Y%%m%%d') in (%s)
        group by user_id, item_id,item_category) a
        left join
        (select
        distinct user_id, item_id,item_category
        from useritem
        where behavior_type=4 and date_format(usertime,'%%Y%%m%%d') in (%s)
        group by user_id, item_id,item_category) b
        on a.user_id=b.user_id and a.item_id=b.item_id
        ; 
        """%(dateString,labeldate)
    #print(SQL)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo3(Result,tempTrainsetFile)
def FeatureCompiler(SourceFilePath,FeaturePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,outputPath):
    userFeatureDict={}
    itemFeatureDict={}
    CateFeatureDict={}
    DemandFeatureDict={}
    featureFile=""
    for tempFeatureName in userFeatureList:
        featureFile=FeaturePath+"\\"+tempFeatureName+".csv"
        featureReader=open(featureFile,'r')
        userFeatureDict[tempFeatureName]={}
        tempLineData=""
        tempLineData=featureReader.readline()
        while(tempLineData!=""):
            tempLineData=tempLineData.strip()
            userFeatureDict[tempFeatureName][tempLineData.split("\t")[0]]=tempLineData.split("\t")[1]
            tempLineData=featureReader.readline()
    for tempFeatureName in itemFeatureList:
        featureFile=FeaturePath+"\\"+tempFeatureName+".csv"
        featureReader=open(featureFile,'r')
        itemFeatureDict[tempFeatureName]={}
        tempLineData=""
        tempLineData=featureReader.readline()
        while(tempLineData!=""):
            tempLineData=tempLineData.strip()
            itemFeatureDict[tempFeatureName][tempLineData.split("\t")[0]]=tempLineData.split("\t")[1]
            tempLineData=featureReader.readline()
    for tempFeatureName in CateFeatureList:
        featureFile=FeaturePath+"\\"+tempFeatureName+".csv"
        featureReader=open(featureFile,'r')
        CateFeatureDict[tempFeatureName]={}
        tempLineData=""
        tempLineData=featureReader.readline()
        while(tempLineData!=""):
            tempLineData=tempLineData.strip()
            CateFeatureDict[tempFeatureName][tempLineData.split("\t")[0]]=tempLineData.split("\t")[1]
            tempLineData=featureReader.readline()
    for tempFeatureName in DemandFeatureList:
        featureFile=FeaturePath+"\\"+tempFeatureName+".csv"
        featureReader=open(featureFile,'r')
        DemandFeatureDict[tempFeatureName]={}
        tempLineData=""
        tempLineData=featureReader.readline()
        while(tempLineData!=""):
            tempLineData=tempLineData.strip()
            DemandFeatureDict[tempFeatureName][tempLineData.split("\t",1)[0]]=tempLineData.split("\t",1)[1]
            tempLineData=featureReader.readline()

    sourceFileReader=open(SourceFilePath,'r')
    trainsetWritter=open(outputPath,'w+')
    tempLineData=""
    tempLineData=sourceFileReader.readline()
    while(tempLineData!=""):
        tempLineData=tempLineData.strip()
        Demand_id=tempLineData.split("\t")[0]
        tempInfoList=Demand_id.split("|")
        user_id=tempInfoList[0]
        item_id=tempInfoList[1]
        Cate_id=tempInfoList[2]
        tempBuyInfo=tempLineData.split("\t")[1]
        tempout=tempBuyInfo+"\t"
        for tempFeatureName in userFeatureList:
            if user_id in userFeatureDict[tempFeatureName].keys():
                tempout+=(userFeatureDict[tempFeatureName][user_id]+"\t")
        for tempFeatureName in itemFeatureList:
            if item_id in itemFeatureDict[tempFeatureName].keys():
                tempout+=(itemFeatureDict[tempFeatureName][item_id]+"\t")
        for tempFeatureName in CateFeatureList:
            if Cate_id in CateFeatureDict[tempFeatureName].keys():
                tempout+=(CateFeatureDict[tempFeatureName][Cate_id]+"\t")
        for tempFeatureName in DemandFeatureList:
            if Demand_id in DemandFeatureDict[tempFeatureName].keys():
                tempout+=(DemandFeatureDict[tempFeatureName][Demand_id]+"\t")
        tempout=tempout.strip("\t")+"\n"
        trainsetWritter.write(tempout)
        tempLineData=sourceFileReader.readline()
        
         
#以下为测试代码
#featureName=["400","401","402","403"]
# tempTrainssetFile=Conf.trainsetTempPath+"\\"+"tempTrainset.csv"
# getTrainset("20141128",tempTrainssetFile)
# SourceFilePath=Conf.trainsetTempPath+"\\"+"tempTrainset.csv"
# FeaturePath=Conf.featureExtractPath+"\\"+"1122_1127"
# userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate"]
# itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
# CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
# DemandFeatureList=["DemandFeature"]
# outputPath=Conf.trainsetOutputPath+"\\"+"1128_Trainset.csv"
# FeatureCompiler(SourceFilePath,FeaturePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,outputPath)

if __name__=="__main__":
    tempTrainssetFile=Conf.trainsetTempPath+"\\"+"20141218_tempTrainset.csv"
    getTrainset("20141211-20141217",'"20141218"',tempTrainssetFile)
    SourceFilePath=r"D:\TianChi\TrainWorkSpace\c_TrainSet\temp\20141218_tempTrainset.csv"
    FeaturePath=r"D:\TianChi\TrainWorkSpace\b_FeatureExtract\20141211-20141217"
    userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate"]
    itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
    CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
    DemandFeatureList=["DemandFeature"]
    outputPath=r"D:\TianChi\TrainWorkSpace\c_TrainSet"+"\\"+"20141211-20141217_20141218_Trainset.csv"
    FeatureCompiler(SourceFilePath,FeaturePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,outputPath)