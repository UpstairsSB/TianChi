# coding=utf-8
'''
Created on 2015年4月19日

@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString
def GaoCateItemNum(dateScope,outputPath):
    featureSid="1001"
#     outputPath=Conf.featureExtractPath+"/"+outputName
    dateString=getDaysString(dateScope)
    SQL=r"""
        select 
        user_id,ceil(100*((sum(if(behavior_type=4,1,0))+1)/(sum(if(behavior_type=3,1,0))+1))) as BuyCartRate 
        from useritem 
        where date_format(usertime,'%%Y%%m%%d') in (%s) 
        group by user_id 
        order by BuyCartRate desc;
        """%(dateString)
    Result=MySQL.getData(SQL)
    MySQL.OutputTo(Result, outputPath,featureSid)
#以下为测试代码
if __name__=="__main__":
    outputPath=Conf.featureExtractPath+"/"+"test/GaoCateItemNum.csv"
    GaoCateItemNum("20141205-20141211",outputPath)
