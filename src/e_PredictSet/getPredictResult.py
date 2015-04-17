# coding=utf-8
'''
Created on 2015年4月17日

@author: zhanghb   mail:zhb_bupt@163.com
'''
from MyUtils.Logistics import logistics
def getPredictResult(ModelFile,predictsetFile,predictResultFile):
    ModelFileReader=open(ModelFile,"r")
    tempLineData=""
    tempLineData=ModelFileReader.readline()
    tempLineDict={}
    while(tempLineData!=""):
        tempLineList=tempLineData.split("\t")
        tempfeatureID=tempLineList[0]+":"+tempLineList[1]
        tempLineDict[tempfeatureID]=float(tempLineList[2])
        tempLineData=ModelFileReader.readline()
    predictsetFileReader=open(predictsetFile,"r")
    predictResultFileWriter=open(predictResultFile,"w+")
    tempLineData=""
    tempLineData=predictsetFileReader.readline()
    tempout=""
    
    count=0
    
    while(tempLineData!=""):
        
        count+=1
        print(count)
        
        wtx=0.0
        tempLineList=tempLineData.split("\t")
        for i in range(1,len(tempLineList)-1,1):
            if tempLineDict.__contains__(tempLineList[i]):
                wtx+=tempLineDict[tempLineList[i]]
        logisticResult=logistics(wtx)
        tempout=tempLineList[0]+"\t"+"%.9f"%(logisticResult)+"\n"
        predictResultFileWriter.write(tempout) 
        tempLineData=predictsetFileReader.readline()
    ModelFileReader.close()
    predictsetFileReader.close()
    predictResultFileWriter.close()
#以下为测试代码
if __name__=="__main__":
    ModelFile=r"D:\TianChi\TrainWorkSpace\d_Model\model_0417_04_01.csv"
    predictsetFile=r"D:\TianChi\TrainWorkSpace\e_PredictSet\predictset\predictset.csv"
    predictResultFile=r"D:\TianChi\TrainWorkSpace\f_PredictResult\predictsetResult.csv"
    getPredictResult(ModelFile,predictsetFile,predictResultFile)
              
        
    