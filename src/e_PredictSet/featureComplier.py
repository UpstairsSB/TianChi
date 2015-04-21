# coding=utf-8
'''
Created on 2015年4月17日

@author: zhanghb   mail:zhb_bupt@163.com
'''
def featureCompiler(SourceFilePath,FeaturePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,outputPath):
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
    
    count=0
    
    while(tempLineData!=""):
        
        count+=1
        print(count)
        
        tempLineData=tempLineData.strip()
        Demand_id=tempLineData
        tempInfoList=Demand_id.split("|")
        user_id=tempInfoList[0]
        item_id=tempInfoList[1]
        Cate_id=tempInfoList[2]
        tempout=tempLineData+"\t"
        for tempFeatureName in userFeatureList:
            if userFeatureDict[tempFeatureName].__contains__(user_id):
                tempout+=(userFeatureDict[tempFeatureName][user_id]+"\t")
        for tempFeatureName in itemFeatureList:
            if  itemFeatureDict[tempFeatureName].__contains__(item_id):
                tempout+=(itemFeatureDict[tempFeatureName][item_id]+"\t")
        for tempFeatureName in CateFeatureList:
            if  CateFeatureDict[tempFeatureName].__contains__(Cate_id):
                tempout+=(CateFeatureDict[tempFeatureName][Cate_id]+"\t")
        for tempFeatureName in DemandFeatureList:
            if  DemandFeatureDict[tempFeatureName].__contains__(Demand_id):
                tempout+=(DemandFeatureDict[tempFeatureName][Demand_id]+"\t")
        tempout=tempout.strip("\t")+"\n"
        trainsetWritter.write(tempout)
        tempLineData=sourceFileReader.readline()
        
#以下为测试代码
#featureName=["400","401","402","403"]
# tempTrainssetFile=Conf.trainsetTempPath+"\\"+"tempTrainset.csv"
# getTrainset("20141128",tempTrainssetFile)
SourceFilePath=r"D:\TianChi\TrainWorkSpace\Gao\temp_predictset"+"\\"+"20141212-20141218_tempPredictset.csv"
FeaturePath=r"D:\TianChi\TrainWorkSpace\Gao\temp_featureset"
userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate","GaoCateItemNum"]
itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
DemandFeatureList=["DemandFeature"]
outputPath=r"D:\TianChi\TrainWorkSpace\Gao\20141212-20141218.csv"
featureCompiler(SourceFilePath,FeaturePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,outputPath)
