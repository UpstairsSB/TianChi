# coding=utf-8
'''
Created on 2015年4月15日
Creatd at 2015年4月15日 上午9:51:45
@author: zhanghb   mail:zhb_bupt@163.com
'''
from b_FeatureExtract.userBuyClickRate import userBuyClickRate
from b_FeatureExtract.userBuyFavRate import userBuyFavRate
from b_FeatureExtract.userBuyCartRate import userBuyCartRate
from b_FeatureExtract.userBuyTotalRate import userBuyTotalRate
from b_FeatureExtract.itemBuyClickRate import itemBuyClickRate
from b_FeatureExtract.itemBuyFavRate import itemBuyFavRate
from b_FeatureExtract.itemBuyCartRate import itemBuyCartRate
from b_FeatureExtract.itemBuyTotalRate import itemBuyTotalRate
from b_FeatureExtract.itemVisitPerDay import itemVisitPerDay
from b_FeatureExtract.CateBuyClickRate import CateBuyClickRate
from b_FeatureExtract.CateBuyFavRate import CateBuyFavRate
from b_FeatureExtract.CateBuyCartRate import CateBuyCartRate
from b_FeatureExtract.CateBuyTotalRate import CateBuyTotalRate
from b_FeatureExtract.CateVisitPerDay import CateVisitPerDay
from b_FeatureExtract.DemandFeature import DemandFeature


def FeatureGenerater(dateScope,outputPath):
#计算dateScope之间所有用户 购买/(点击+1) 当不发生购买行为时为0，不提取
    userBuyClickRate(dateScope,outputPath+r"\userBuyClickRate.csv")
#计算dateScope之间所有用户 购买/(收藏+1) 当不发生购买行为时为0，不提取
    userBuyFavRate(dateScope,outputPath+r"\userBuyFavRate.csv")
#计算dateScope之间所有用户 购买/(加购物车+1) 当不发生购买行为时为0，不提取
    userBuyCartRate(dateScope,outputPath+r"\userBuyCartRate.csv")
#计算dateScope之间所有用户 购买/(交互次数+1) 当不发生购买行为时为0，不提取
    userBuyTotalRate(dateScope,outputPath+r"\userBuyTotalRate.csv")
  
# 计算dateScope之间所有商品 购买/(点击+1) 当不发生购买行为时为0，不提取
    itemBuyClickRate(dateScope,outputPath+r"\itemBuyClickRate.csv")
#计算dateScope之间所有商品 购买/(收藏+1) 当不发生购买行为时为0，不提取
    itemBuyFavRate(dateScope,outputPath+r"\itemBuyFavRate.csv")
#计算dateScope之间所有商品 购买/(加购物车+1) 当不发生购买行为时为0，不提取
    itemBuyCartRate(dateScope,outputPath+r"\itemBuyCartRate.csv")
#计算dateScope之间所有商品 购买/(交互次数+1) 当不发生购买行为时为0，不提取
    itemBuyTotalRate(dateScope,outputPath+r"\itemBuyTotalRate.csv")
#计算dateScope之间所有商品 日均访问人数
    itemVisitPerDay(dateScope,outputPath+r"\itemVisitPerDay.csv")

#计算dateScope之间所有类目 购买/(点击+1) 当不发生购买行为时为0，不提取
    CateBuyClickRate(dateScope,outputPath+r"\CateBuyClickRate.csv")
#计算dateScope之间所有类目 购买/(收藏+1) 当不发生购买行为时为0，不提取
    CateBuyFavRate(dateScope,outputPath+r"\CateBuyFavRate.csv")
#计算dateScope之间所有类目 购买/(加购物车+1) 当不发生购买行为时为0，不提取
    CateBuyCartRate(dateScope,outputPath+r"\CateBuyCartRate.csv")
#计算dateScope之间所有类目 购买/(交互次数+1) 当不发生购买行为时为0，不提取
    CateBuyTotalRate(dateScope,outputPath+r"\CateBuyTotalRate.csv")
# 计算dateScope之间所有类目 日均访问人数
    CateVisitPerDay(dateScope,outputPath+r"\CateVisitPerDay.csv")

# 计算dateScope之间user-item需求特征
    DemandFeature(dateScope,outputPath+r"\DemandFeature.csv")


#以下为测试代码
if __name__=="__main__":
    FeatureGenerater("20141122-20141127")