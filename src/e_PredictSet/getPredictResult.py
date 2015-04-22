# coding=utf-8
'''
Created on 2015年4月17日

@author: zhanghb   mail:zhb_bupt@163.com
'''
from MyUtils.Logistics import logistics
import Conf
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
def getPredictResult_2(ModelFileDict,predictsetFile,predictResultFile):
    
    count=0
    
    tempLineData=""
    tempModelDict={}
    for ModelName in ModelFileDict.keys():
        ModelFile=Conf.ModelPath+"\\"+ModelName+".csv"
        ModelFileReader=open(ModelFile,"r")
        tempLineData=ModelFileReader.readline()
        tempModelDict[ModelName]={}
        while(tempLineData!=""):
            
            count+=1
            print(count)
            
            tempLineList=tempLineData.split("\t")
            tempfeatureID=tempLineList[0]+":"+tempLineList[1]
            tempModelDict[ModelName][tempfeatureID]=float(tempLineList[2])
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
        logisticResult=0.0
        for ModelName in ModelFileDict.keys():
            for i in range(1,len(tempLineList)-1,1):
                if tempModelDict[ModelName].__contains__(tempLineList[i]):
                    wtx+=tempModelDict[ModelName][tempLineList[i]]
            logisticResult+=(logistics(wtx)*float(ModelFileDict[ModelName]))
        tempout=tempLineList[0]+"\t"+"%.9f"%(logisticResult)+"\n"
        predictResultFileWriter.write(tempout) 
        tempLineData=predictsetFileReader.readline()
    ModelFileReader.close()
    predictsetFileReader.close()
    predictResultFileWriter.close()
#以下为测试代码
if __name__=="__main__":
    ModelFile=r"D:\TianChi\TrainWorkSpace\d_Model\model_0422_f.csv"
    predictsetFile=r"D:\TianChi\TrainWorkSpace\e_PredictSet\predictset\predictset.csv"
    predictResultFile=r"D:\TianChi\TrainWorkSpace\f_PredictResult\predictsetResult_20150422.csv"
    getPredictResult(ModelFile,predictsetFile,predictResultFile)
              
    #ModelFileDict={"Model1":0.817,"Model2":0.813,"Model3":0.748,"Model4":0.775} 
    #getPredictResult_2(ModelFileDict,predictsetFile,predictResultFile)   
    