# coding=utf-8
'''
Created on 2015年4月12日
Creatd at 2015年4月12日 下午2:53:17
@author: zhanghb   mail:zhb_bupt@163.com
'''
import pymysql
import Conf
from MyUtils import MySQL
from MyUtils.getDaysFromString import getDaysString
def Sample(dateScope, outputName):
    tempDaysString=getDaysString(dateScope)
    outputPath=Conf.originalSamplePath+"/" + outputName
    sql = ' select '\
        + ' distinct user_id,item_id '\
        + ' from useritem '\
        + ' where date_format(usertime,"%Y%m%d") in '\
        + ' ( '\
        + tempDaysString\
        + ')'\
        + ' group by user_id,item_id '\
        + ' order by user_id '\
        + ";"
    try:
#         MySQLConnect = pymysql.connect(host=Conf.host,port=Conf.port,user=Conf.user,passwd=Conf.password,db=Conf.databaseName)
#         MySQLCursor = MySQLConnect.cursor()
#         MySQLCursor.execute(sql)
#         result=MySQLCursor.fetchall()
        result=MySQL.getData(sql)
        MySQL.OutputTo(result,outputPath)
#         MySQLCursor.close()
#         MySQLConnect.close()
        print("数据提取完毕")
    except :
        print("数据提取有误")
#以下为测试代码
Sample("20141122-20141127","test9.csv")
