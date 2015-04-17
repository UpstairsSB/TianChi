# coding=utf-8
'''
Created on 2015年4月15日
Creatd at 2015年4月15日 上午12:13:18
@author: zhanghb   mail:zhb_bupt@163.com
'''
# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午3:09:18
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString 
def itemBuyFavRate(dateScope,outputName):
    featureSid="101"
    outputPath=Conf.featureExtractPath+"/"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"(select b.item_id,ceil(1000*((if(Buy is null,1,Buy+1))/(if(Fav is null,1,Fav+1)))) as BuyFavRate "\
        +"from "\
        +"(( "\
        +"select "\
        +"item_id,count(behavior_type) as Fav "\
        +"from useritem "\
        +"where behavior_type=2 and date_format(usertime,'%%Y%%m%%d') in (%s) "%(dateString)\
        +"group by item_id "\
        +")a right join "\
        +"( "\
        +"select "\
        +"item_id,count(behavior_type) as Buy "\
        +"from useritem "\
        +"where behavior_type=4 and date_format(usertime,'%%Y%%m%%d') in (%s) "%(dateString)\
        +"group by item_id "\
        +")b "\
        +"on a.item_id=b.item_id "\
        +")) "\
        +"union "\
        +"(select a.item_id,ceil(1000*((if(Buy is null,1,Buy+1))/(if(Fav is null,1,Fav+1)))) as BuyFavRate "\
        +"from "\
        +"(( "\
        +"select "\
        +"item_id,count(behavior_type) as Fav "\
        +"from useritem "\
        +"where behavior_type=2 and date_format(usertime,'%%Y%%m%%d') in (%s) "%(dateString)\
        +"group by item_id "\
        +")a left join "\
        +"( "\
        +"select "\
        +"item_id,count(behavior_type) as Buy "\
        +"from useritem "\
        +"where behavior_type=4 and date_format(usertime,'%%Y%%m%%d') in (%s) "%(dateString)\
        +"group by item_id "\
        +")b "\
        +"on a.item_id=b.item_id "\
        +")) "\
        +"order by BuyFavRate desc;"
    Result=MySQL.getData(SQL)
    MySQL.OutputTo(Result, outputPath,featureSid)
#以下为测试代码
itemBuyFavRate("20141122-20141127",r"\1122_1127\itemBuyFavRate0.csv")