# coding=utf-8
'''
Created on 2015年4月12日
Creatd at 2015年4月12日 下午10:10:40
@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString 
def userBuyClickRate(dateScope,outputPath):
    featureSid="1"
#     outputPath=Conf.featureExtractPath+"/"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"""
        select 
        user_id,ceil(100*((sum(if(behavior_type=4,1,0))+1)/(sum(if(behavior_type=1,1,0))+1))) as BuyClickRate 
        from useritem 
        where date_format(usertime,'%%Y%%m%%d') in (%s) 
        group by user_id 
        order by BuyClickRate desc;
        """%(dateString)
    #SQL=SQL.replace("\n", "")
    Result=MySQL.getData(SQL)
    MySQL.OutputTo(Result, outputPath,featureSid)
#以下为测试代码
if __name__=="__main__":
    userBuyClickRate("20141122-20141127",r"\1122_1127\userBuyClickRate.csv")
    