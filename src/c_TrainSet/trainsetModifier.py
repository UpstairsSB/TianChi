# coding=utf-8
'''
Created on 2015年4月16日

@author: zhanghb   mail:zhb_bupt@163.com
'''
from c_TrainSet.singleFeatureGenerater import singleFeatureGenerate_0
from MyUtils.dateDivier import dateDivier
from c_TrainSet.featureCompiler import FeatureCompiler
import os
import Conf
def trainModifier_1(featureDict,dateScope,labelDate):
    userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate"]
    itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
    CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
    DemandFeatureList=["DemandFeature"]
    if featureDict.__contains__("User") and (featureDict["User"] not in userFeatureList):
        userFeatureList.append(featureDict["User"])
    if featureDict.__contains__("Item") and (featureDict["Item"] not in itemFeatureList):
        itemFeatureList.append(featureDict["Item"])
    if featureDict.__contains__("Cate") and (featureDict["Cate"] not in CateFeatureList):
        CateFeatureList.append(featureDict["Cate"])
    if featureDict.__contains__("Demand") and (featureDict["Demand"] not in DemandFeatureList):
        DemandFeatureList.append(featureDict["Demand"])
    #特征输出路径
    featurePath=Conf.featureExtractPath+"\\"+dateScope
    if not os.path.exists(featurePath):
        print("特征文件夹不存在:"+featurePath)
        return
    #观测数据路径
    tempTrainsetFile=Conf.trainsetTempPath+"\\"+labelDate+"_tempTrainset.csv"
    if not os.path.exists(Conf.trainsetTempPath):
        print("观测数据文件不存在:"+tempTrainsetFile)
        return
    #生成的最终训练数据
    if not os.path.exists(Conf.trainsetOutputPath):
        print("最终训练数据文件夹不存在:"+Conf.trainsetTempPath)
        return
    trainsetFile=Conf.trainsetOutputPath+"\\"+dateScope+"_"+labelDate+"_Trainset.csv"
    #重新生成特征文件
    for tempFeatureName in featureDict.values():
        singleFeatureGenerate_0(tempFeatureName,dateScope)
    #把重新生成后的特征文件组合成训练文件
    FeatureCompiler(tempTrainsetFile,featurePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,trainsetFile)
#以下为测试代码
if __name__=="__main__":
    featureDict={"Item":"itemVisitPerDay"}
    trainModifier_1(featureDict,"20141118-20141124","20141125")