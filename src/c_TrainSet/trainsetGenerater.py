# coding=utf-8
'''
Created on 2015年4月15日
Creatd at 2015年4月15日 上午9:49:43
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from b_FeatureExtract.b_FeatureGenerater import FeatureGenerater
from c_TrainSet.featureCompiler import getTrainset
from c_TrainSet.featureCompiler import FeatureCompiler
import shutil
import os
import Conf
from MyUtils.dateDivier import dateDivier

def trainsetGenerater_1(dateScope,labelDate):
    #特征输出路径
    featurePath=Conf.featureExtractPath+"\\"+dateScope
    if os.path.exists(featurePath):
        shutil.rmtree(featurePath)
        os.makedirs(featurePath)
    else:
        os.makedirs(featurePath)
    #生成labelDate的观测数据
    if not os.path.exists(Conf.trainsetTempPath):
        os.makedirs(Conf.trainsetTempPath)
    tempTrainsetFile=Conf.trainsetTempPath+"\\"+labelDate+"_tempTrainset.csv"
    #生成的最终训练数据
    if not os.path.exists(Conf.trainsetOutputPath):
        os.makedirs(Conf.trainsetOutputPath)
    trainsetFile=Conf.trainsetOutputPath+"\\"+dateScope+"_"+labelDate+"_Trainset.csv"
    #生成特征
    FeatureGenerater(dateScope,featurePath)
    #生成labelDate的观测数据
    getTrainset(labelDate,tempTrainsetFile)
    userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate"]
    itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
    CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
    DemandFeatureList=["DemandFeature"]
    #生成最终训练数据
    FeatureCompiler(tempTrainsetFile,featurePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,trainsetFile)
def trainsetGenerater_2(dateScope,dateDelta,*dateSkip):
    if dateSkip==():
        dateScopeList=dateDivier(dateScope,dateDelta)
    else:
        dateScopeList=dateDivier(dateScope,dateDelta,dateSkip[0])
    for tempdateScope in dateScopeList:
        trainsetGenerater_1(tempdateScope[0],tempdateScope[1])
    
#以下为测试数据
#trainsetGenerater_1("20141122-20141127","20141128")
trainsetGenerater_2("20141118-20141218",7,1)