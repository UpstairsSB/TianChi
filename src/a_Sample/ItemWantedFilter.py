# coding=utf-8
'''
Created on 2015年4月12日
Creatd at 2015年4月12日 下午9:32:01
@author: zhanghb   mail:zhb_bupt@163.com
'''
from MyUtils import MySQL
import Conf
def ItemWantedFilter():
    SQL=r'select distinct item_id from item'
    result=MySQL.getData(SQL)
    outputPath=Conf.filterPath+"/"+"ItemWanted.csv"
    MySQL.OutputTo(result, outputPath)
ItemWantedFilter()