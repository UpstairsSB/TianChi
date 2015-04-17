# coding=utf-8
'''
Created on 2015年4月12日
Creatd at 2015年4月12日 下午2:53:46
@author: zhanghb   mail:zhb_bupt@163.com
'''
import pymysql
import Conf
def Connect():
    try:
        conn=pymysql.connect(host=Conf.host,port=Conf.port,user=Conf.dbuser,passwd=Conf.password,db=Conf.databaseName)
        print("数据库连接成功")
        return conn
    except:
        print("数据库连接失败")
def OutputTo(Result,outputPath,featureSid,*tempsplitor):
    outFile=open(outputPath,'w+')
    if tempsplitor==():
        splitor="\t"
    else:
        splitor=tempsplitor[0]
    for tempdata in Result:
        tempout=""
        tempout=tempdata[0]+splitor+featureSid+":"+str(tempdata[1])
        outFile.write(tempout+"\n")
    outFile.close()
def OutputTo2(Result,outputPath,featureSid,*tempsplitor):
    outFile=open(outputPath,'w+')
    if tempsplitor==():
        splitor="\t"
    else:
        splitor=tempsplitor[0]
    for tempdata in Result:
        tempout=""
        tempout+=(tempdata[0]+"|"+tempdata[1]+"|"+tempdata[2]+"\t")
        i=0
        for temp in featureSid:
            i+=1
            tempout+=(temp+":"+str(tempdata[2+i])+"\t")
        tempout=tempout.rstrip(splitor)
        outFile.write(tempout+"\n")
    outFile.close()
def OutputTo3(Result,outputPath,*tempsplitor):
    outFile=open(outputPath,'w+')
    if tempsplitor==():
        splitor="\t"
    else:
        splitor=tempsplitor[0]
    for tempdata in Result:
        tempout=""
        tempout+=(tempdata[0]+"|"+tempdata[1]+"|"+tempdata[2]+splitor+str(tempdata[3])+splitor)
        outFile.write(tempout+"\n")
    outFile.close()
    
def getData(SQL):
    conn=Connect()
    cur=conn.cursor()
    cur.execute(SQL)
    result=cur.fetchall()
    cur.close()
    conn.close()
    return result
#以下为测试代码
# conn=Connect()
# cur=conn.cursor()
# cur.execute('select * from test1')
# temp=[]
# temp=cur.fetchone()
# #cur.execute(r'load data infile "d:/TianChi/data/SourceData/usertest.csv" replace into table usertest character set utf8 fields terminated by "," enclosed by "" lines terminated by "\r\n" IGNORE 1 Lines (user_id,item_id,behavior_type,user_geohash,item_category,usertime);')
# # for r in cur:
# #     print("row_number:"+str(cur.rownumber))
# #     print("user_id:"+str(r[0])+"item_id:"+str(r[1]))
# result=cur.fetchall()
# outputPath=Conf.originalSamplePath+"/"+"test10.csv"
# OutputTo(result,outputPath,"\t")
# cur.close()    
# conn.close()