# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午4:53:32
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString , getDaysNum
def CateVisitPerDay(dateScope,outputPath):
    featureSid="204"
#     outputPath=Conf.featureExtractPath+"/"+outputName
    dateString=getDaysString(dateScope)
    daysNum=str(getDaysNum(dateScope))
    SQL=r"""
        select
        item_category,ceil((100*(count(distinct user_id)/%s))) as VisitPerDay
        from useritem
        where behavior_type in (1,2,3,4) and date_format(usertime,'%%Y%%m%%d') in (%s)
        group by item_category
        order by VisitPerDay desc;
        """%(daysNum,dateString)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo(Result, outputPath,featureSid)
#以下为测试代码
#CateVisitPerDay("20141122-20141127",r"\1122_1127\CateVisitPerDay.csv")
