# coding=utf-8
'''
Created on 2015年4月17日

@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
import os
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString
from b_FeatureExtract.b_FeatureGenerater import FeatureGenerater
from e_PredictSet.featureComplier import featureCompiler
def gettempPredictset(dateScope,tempPredictsetFile):
    #tempPredictsetFile=Conf.temp_predictsetPath+"\\"+dateScope+"_tempPredictset.csv"
    dateString=getDaysString(dateScope)
    tempPredictsetFile=tempPredictsetFile.replace("\\","/")
    if os.path.exists(tempPredictsetFile):
        os.remove(tempPredictsetFile)
    SQL=r"""
        select
        user_id,item_id,item_category
        from useritem
        where date_format(usertime,'%%Y%%m%%d') in (%s) 
        group by user_id, item_id,item_category
        into outfile 
        "%s"
        fields terminated by '|'
        optionally enclosed by ""
        lines terminated by "\n"; 
        """%(dateString,tempPredictsetFile.replace("\\","/"))
    conn=MySQL.Connect()
    cur=conn.cursor()
    try:
        cur.execute(SQL)
        conn.commit()
        cur.close()
        conn.close()
    except:
        cur.close()
        conn.close()
        print("测试集头信息提取完毕")
def predictsetGenerater(dateScope):
    tempfeaturePath=Conf.temp_featuresetPath
    tempPredictsetFile=Conf.temp_predictsetPath+"\\"+dateScope+"_tempPredictset.csv"
    #生成特征
    FeatureGenerater(dateScope,tempfeaturePath)
    #生成预测集头信息
    gettempPredictset(dateScope,tempPredictsetFile)
    predictsetGenerater_1(dateScope)
    
def predictsetGenerater_1(dateScope):
    tempfeaturePath=Conf.temp_featuresetPath
    tempPredictsetFile=Conf.temp_predictsetPath+"\\"+dateScope+"_tempPredictset.csv"    
    userFeatureList=["userBuyClickRate","userBuyFavRate","userBuyCartRate","userBuyTotalRate"]
    itemFeatureList=["itemBuyClickRate","itemBuyFavRate","itemBuyCartRate","itemBuyTotalRate","itemVisitPerDay"]
    CateFeatureList=["CateBuyClickRate","CateBuyFavRate","CateBuyCartRate","CateBuyTotalRate","CateVisitPerDay"]
    DemandFeatureList=["DemandFeature"]
    #生成最终训练数据
    predictFile=Conf.predictsetPath+"\\"+dateScope+"_predictset.csv"
    featureCompiler(tempPredictsetFile,tempfeaturePath,userFeatureList,itemFeatureList,CateFeatureList,DemandFeatureList,predictFile)
#def predictsetGenerater(deteScope,):
    
#以下为测试代码
if __name__=="__main__":
    dateScope="20141212-20141218"
    tempPredictsetFile=Conf.temp_predictsetPath+"\\"+dateScope+"_tempPredictset.csv"
    #gettempPredictset(dateScope,tempPredictsetFile)
    predictsetGenerater(dateScope)
    #predictsetGenerater_1(dateScope)