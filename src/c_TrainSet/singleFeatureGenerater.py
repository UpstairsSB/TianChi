# coding=utf-8
'''
Created on 2015年4月16日

@author: zhanghb   mail:zhb_bupt@163.com
'''
from b_FeatureExtract.userBuyClickRate import userBuyClickRate
from b_FeatureExtract.userBuyFavRate import userBuyFavRate
from b_FeatureExtract.userBuyCartRate import userBuyCartRate
from b_FeatureExtract.userBuyTotalRate import userBuyTotalRate
from b_FeatureExtract.itemBuyClickRate import itemBuyClickRate
from b_FeatureExtract.itemBuyFavRate import itemBuyFavRate
from b_FeatureExtract.itemBuyCartRate import itemBuyCartRate
from b_FeatureExtract.itemBuyTotalRate import itemBuyTotalRate
from b_FeatureExtract.itemVisitPerDay import itemVisitPerDay
from b_FeatureExtract.CateBuyClickRate import CateBuyClickRate
from b_FeatureExtract.CateBuyFavRate import CateBuyFavRate
from b_FeatureExtract.CateBuyCartRate import CateBuyCartRate
from b_FeatureExtract.CateBuyTotalRate import CateBuyTotalRate
from b_FeatureExtract.CateVisitPerDay import CateVisitPerDay
from b_FeatureExtract.DemandFeature import DemandFeature
import Conf
from MyUtils.dateDivier import dateDivier, dateDivier_3
def singleFeatureGenerate_0(featureName,dateScope,*tempoutputPath):
    if tempoutputPath==():
        outputPath=Conf.featureExtractPath+"\\"+dateScope
    else:
        outputPath=tempoutputPath[0]+"\\"+dateScope
    
    if featureName=="userBuyClickRate":
        userBuyClickRate(dateScope,outputPath+r"\userBuyClickRate.csv")
    
    if featureName=="userBuyFavRate":
        userBuyFavRate(dateScope,outputPath+r"\userBuyFavRate.csv")
        
    if featureName=="userBuyCartRate":
        userBuyCartRate(dateScope,outputPath+r"\userBuyCartRate.csv")
    
    if featureName=="userBuyTotalRate":
        userBuyTotalRate(dateScope,outputPath+r"\userBuyTotalRate.csv")
    
    if featureName=="itemBuyClickRate":
        itemBuyClickRate(dateScope,outputPath+r"\itemBuyClickRate.csv")
    
    if featureName=="itemBuyFavRate":
        itemBuyFavRate(dateScope,outputPath+r"\itemBuyFavRate.csv")
    
    if featureName=="itemBuyCartRate":
        itemBuyCartRate(dateScope,outputPath+r"\itemBuyCartRate.csv")
    
    if featureName=="itemBuyTotalRate":
        itemBuyTotalRate(dateScope,outputPath+r"\itemBuyTotalRate.csv")
    
    if featureName=="itemVisitPerDay":
        itemVisitPerDay(dateScope,outputPath+r"\itemVisitPerDay.csv")
    
    if featureName=="CateBuyClickRate":
        CateBuyClickRate(dateScope,outputPath+r"\CateBuyClickRate.csv")
        
    if featureName=="CateBuyFavRate":
        CateBuyFavRate(dateScope,outputPath+r"\CateBuyFavRate.csv")
    
    if featureName=="CateBuyCartRate":
        CateBuyCartRate(dateScope,outputPath+r"\CateBuyCartRate.csv")
    
    if featureName=="CateBuyTotalRate":
        CateBuyTotalRate(dateScope,outputPath+r"\CateBuyTotalRate.csv")
    
    if featureName=="CateVisitPerDay":
        CateVisitPerDay(dateScope,outputPath+r"\CateVisitPerDay.csv")
    
    if featureName=="userBuyClickRate":
        DemandFeature(dateScope,outputPath+r"\DemandFeature.csv")
def singleFeatureGenerate(featureName,dateScope,dateDelta,*dateSkipAndtempoutputPath):
    if dateSkipAndtempoutputPath[0]==():
        dateScopeList=dateDivier_3(dateScope,dateDelta)
    else:
        dateScopeList=dateDivier_3(dateScope,dateDelta,dateSkipAndtempoutputPath[0])
    for tempdateScope in dateScopeList:
        singleFeatureGenerate_0(featureName,tempdateScope,dateSkipAndtempoutputPath[1])
def singleFeatureGenerate_2(featureName,dateScope,dateDelta,*dateSkip):
    if dateSkip==():
        dateScopeList=dateDivier_3(dateScope,dateDelta)
    else:
        dateScopeList=dateDivier_3(dateScope,dateDelta,dateSkip[0])
    for tempdateScope in dateScopeList:
        singleFeatureGenerate_0(featureName,tempdateScope)
def singleFeatureGenerate_3(featureName,dateScope,dateDelta,*tempoutputPath):
    dateScopeList=dateDivier_3(dateScope,dateDelta)
    for tempdateScope in dateScopeList:
        singleFeatureGenerate_0(featureName,tempdateScope,tempoutputPath[0])
        
if __name__=="__main__":
#     singleFeatureGenerate("itemVisitPerDay","20141118-20141218",7,1,r"D:\TianChi\TrainWorkSpace\test\temp")
    a=[]
    