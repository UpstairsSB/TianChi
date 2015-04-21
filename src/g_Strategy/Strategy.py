# coding=utf-8
'''
Created on 2015年4月21日

@author: zhanghb   mail:zhb_bupt@163.com
'''
import Conf
#策略1删除不活跃用户
def Strategy_1(sourcefile,inputfile,outputfile,*tempcount):
    sourceReader=open(sourcefile,"r")
    inputReader=open(inputfile,"r")
    outputWriter=open(outputfile,"w")
    tempLineData=""
    
    userDict={}
    count=3000
    if tempcount!=():
        count=tempcount[0]
    i=0
    tempLineData=inputReader.readline()
    while(tempLineData!=""):
        tempLineData=tempLineData.strip()
        if i<count :
            userDict[tempLineData.split(",")[0]]=""
            i+=1
            tempLineData=inputReader.readline()
        else:
            break
    tempLineData=""
    tempLineData=sourceReader.readline()
    while(tempLineData!=""):
        tempLineData=tempLineData.strip()
        if userDict.__contains__(tempLineData.split(",")[0]):
            tempLineData=sourceReader.readline()
            continue
        else:
            outputWriter.write(tempLineData.replace(",", "|")+"\t\n")
            tempLineData=sourceReader.readline()
#策略2删除不活跃item
def Strategy_2(sourcefile,inputfile,outputfile,*tempcount):
    sourceReader=open(sourcefile,"r")
    inputReader=open(inputfile,"r")
    outputWriter=open(outputfile,"w")
    tempLineData=""
    
    itemDict={}
    count=3000
    if tempcount!=():
        count=tempcount[0]
    i=0
    tempLineData=inputReader.readline()
    while(tempLineData!=""):
        tempLineData=tempLineData.strip()
        if i<count :
            itemDict[tempLineData.split(",")[0]]=""
            i+=1
            tempLineData=inputReader.readline()
        else:
            break
    tempLineData=""
    tempLineData=sourceReader.readline()
    while(tempLineData!=""):
        tempLineData=tempLineData.strip()
        if itemDict.__contains__(tempLineData.split(",")[1]):
            tempLineData=sourceReader.readline()
            continue
        else:
            outputWriter.write(tempLineData.replace(",", "|")+"\t\n")
            tempLineData=sourceReader.readline()
#以下为测试代码
if __name__=="__main__":
#     sourcefile=Conf.StrategyPath+"\\"+r"20141218_cart.csv"
#     inputfile=Conf.StrategyPath+"\\"+r"1213-1218_user_Active.csv"
#     outputfile=Conf.StrategyPath+"\\"+r"20141218_cart_afterdeleteNegative.csv"
#     Strategy_1(sourcefile,inputfile,outputfile,3000)
#     sourcefile=outputfile
#     inputfile=Conf.StrategyPath+"\\"+r"1213-1218_user_BuyCartRate.csv"
#     outputfile=Conf.StrategyPath+"\\"+r"20141218_cart_afterDelete.csv"
#     Strategy_1(sourcefile,inputfile,outputfile,3000)
    sourcefile=Conf.StrategyPath+"\\"+r"20141218_cart_ItemWanted.csv"
    inputfile=Conf.StrategyPath+"\\"+r"itemBuyCartRate_afterFliter.csv"
    outputfile=Conf.StrategyPath+"\\"+r"20141218_cart_itemBuyCartRate.csv"
    Strategy_2(sourcefile,inputfile,outputfile,1000)        
        
    
        