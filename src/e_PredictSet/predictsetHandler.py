# coding=utf-8
'''
Created on 2015年4月17日

@author: zhanghb   mail:zhb_bupt@163.com
'''
def handler(inputpath,outputpath):
    FileReader=open(inputpath,"r")
    tempLineData=""
    tempLineData=FileReader.readline()
    FileWriter=open(outputpath,"w",-1,"utf-8")
    
    count=0
    FileWriter.write("user_id"+","+"item_id"+"\n")
    while(tempLineData!=""):
        
        count+=1
        print(count)
        
        tempLineData=tempLineData.strip()
        templist=tempLineData.split("|")
        tempout=""
        tempout+=(templist[0]+","+templist[1]+"\n")
        FileWriter.write(tempout)
        tempLineData=FileReader.readline()
    FileWriter.close
#以下为测试代码
if __name__=="__main__":
    inputpath=r"D:\TianChi\TrainWorkSpace\f_PredictResult\20150419_1.csv"
    outputpath=r"D:\TianChi\TrainWorkSpace\f_PredictResult\20150419_1_o.csv"
    handler(inputpath,outputpath)
    