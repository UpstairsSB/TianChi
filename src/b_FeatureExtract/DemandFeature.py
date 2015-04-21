# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午9:40:21
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDays
def DemandFeature(dateScope,outputPath):
    featureSid=["400","401","402","403","404","405","406","408","409","410","411","412"]
#     outputPath=Conf.featureExtractPath+"\\"+outputName
    date_7=getDays(dateScope)
    date_3=date_7[-3:]
    
    dateString_7=",".join(date_7)
    dateString_3=",".join(date_3)
    dateString_1=date_7[-1]
    SQL=r"""
        select a.user_id,a.item_id,a.item_category,
        a.Click,a.Fav,a.Cart,a.Buy,
        ifnull(b.Click,0),ifnull(b.Fav,0),ifnull(b.Cart,0),ifnull(b.Buy,0), 
        ifnull(c.Click,0),ifnull(c.Fav,0),ifnull(c.Cart,0),ifnull(c.Buy,0)
        from
        (select
        user_id, item_id,item_category,
        sum(if(behavior_type=1,1,0)) as Click,sum(if(behavior_type=2,1,0)) as Fav,
        sum(if(behavior_type=3,1,0)) as Cart,sum(if(behavior_type=4,1,0)) as Buy
        from useritem
        where date_format(usertime,'%%Y%%m%%d') in (%s)
        group by user_id, item_id,item_category) a
        left join
        (select
        user_id, item_id,item_category,
        sum(if(behavior_type=1,1,0)) as Click,sum(if(behavior_type=2,1,0)) as Fav,
        sum(if(behavior_type=3,1,0)) as Cart,sum(if(behavior_type=4,1,0)) as Buy
        from useritem
        where date_format(usertime,'%%Y%%m%%d') in (%s)
        group by user_id, item_id,item_category) b
        on a.user_id=b.user_id and a.item_id=b.item_id
        left join
        (select
        user_id, item_id,item_category,
        sum(if(behavior_type=1,1,0)) as Click,sum(if(behavior_type=2,1,0)) as Fav,
        sum(if(behavior_type=3,1,0)) as Cart,sum(if(behavior_type=4,1,0)) as Buy
        from useritem
        where date_format(usertime,'%%Y%%m%%d') in (%s)
        group by user_id, item_id,item_category) c
        on a.user_id=c.user_id and a.item_id=c.item_id
        ;
        """%(dateString_7,dateString_3,dateString_1)
    #print(SQL)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo2(Result,outputPath,featureSid)
#以下为测试代码

#DemandFeature("20141122-20141127",r"1122_1127\DemandFeature.csv")
if __name__=="__main__":
    DemandFeature("20141122-20141127",r"D:\TianChi\TrainWorkSpace\test\DemandFeature.csv")