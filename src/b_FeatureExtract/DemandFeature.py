# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午9:40:21
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString
def DemandFeature(dateScope,outputPath):
    featureSid=["400","401","402","403"]
#     outputPath=Conf.featureExtractPath+"\\"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"""
        select
        user_id, item_id,item_category,
        sum(if(behavior_type=1,1,0)) as Click,sum(if(behavior_type=2,1,0)) as Fav,
        sum(if(behavior_type=3,1,0)) as Cart,sum(if(behavior_type=4,1,0)) as Buy
        from useritem
        where date_format(usertime,'%%Y%%m%%d') in (%s)
        group by user_id, item_id,item_category;
        """%(dateString)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo2(Result,outputPath,featureSid)
#以下为测试代码

#DemandFeature("20141122-20141127",r"1122_1127\DemandFeature.csv")
