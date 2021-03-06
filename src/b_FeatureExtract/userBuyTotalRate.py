# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午1:55:09
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString 
def userBuyTotalRate(dateScope,outputPath):
    featureSid="4"
#     outputPath=Conf.featureExtractPath+"/"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"""
        select 
        user_id,ceil(100*((sum(if(behavior_type=4,1,0))+1)/(sum(1)+1))) as BuyTotalRate 
        from useritem 
        where date_format(usertime,'%%Y%%m%%d') in (%s) 
        group by user_id 
        order by BuyTotalRate desc;
        """%(dateString)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo(Result, outputPath,featureSid)
#以下为测试代码
#userBuyTotalRate("20141122-20141127",r"\1122_1127\userBuyTotalRate.csv")
