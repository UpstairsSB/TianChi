# coding=utf-8
'''
Created on 2015年4月17日

@author: zhanghb   mail:zhb_bupt@163.com
'''
from math import exp
def logistics(z):
    result=1/(1+exp(-z))
    return result
#以下为测试代码
if __name__=="__main__":
   result= logistics(5)
   print(result)