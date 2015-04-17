# coding=utf-8
'''
Created on 2015年4月13日
Creatd at 2015年4月13日 下午5:03:12
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

#选定代码,ctrl+'/'注释所有代码

 #计算20141122-20141127之间所有用户 购买/(点击+1) 当不发生购买行为时为0，不提取
userBuyClickRate("20141122-20141127",r"\1122_1127\userBuyClickRate.csv")
 #计算20141122-20141127之间所有用户 购买/(收藏+1) 当不发生购买行为时为0，不提取
userBuyFavRate("20141122-20141127",r"\1122_1127\userBuyFavRate.csv")
 #计算20141122-20141127之间所有用户 购买/(加购物车+1) 当不发生购买行为时为0，不提取
userBuyCartRate("20141122-20141127",r"\1122_1127\userBuyCartRate.csv")
 #计算20141122-20141127之间所有用户 购买/(交互次数+1) 当不发生购买行为时为0，不提取
userBuyTotalRate("20141122-20141127",r"\1122_1127\userBuyTotalRate.csv")
  
# 计算20141122-20141127之间所有商品 购买/(点击+1) 当不发生购买行为时为0，不提取
itemBuyClickRate("20141122-20141127",r"\1122_1127\itemBuyClickRate.csv")
 #计算20141122-20141127之间所有商品 购买/(收藏+1) 当不发生购买行为时为0，不提取
itemBuyFavRate("20141122-20141127",r"\1122_1127\itemBuyFavRate.csv")
 #计算20141122-20141127之间所有商品 购买/(加购物车+1) 当不发生购买行为时为0，不提取
itemBuyCartRate("20141122-20141127",r"\1122_1127\itemBuyCartRate.csv")
 #计算20141122-20141127之间所有商品 购买/(交互次数+1) 当不发生购买行为时为0，不提取
itemBuyTotalRate("20141122-20141127",r"\1122_1127\itemBuyTotalRate.csv")
 #计算20141122-20141127之间所有商品 日均交互次数
itemVisitPerDay("20141122-20141127",r"\1122_1127\itemVisitPerDay.csv")

 #计算20141122-20141127之间所有类目 购买/(点击+1) 当不发生购买行为时为0，不提取
CateBuyClickRate("20141122-20141127",r"\1122_1127\CateBuyClickRate.csv")
 #计算20141122-20141127之间所有类目 购买/(收藏+1) 当不发生购买行为时为0，不提取
CateBuyFavRate("20141122-20141127",r"\1122_1127\CateBuyFavRate.csv")
 #计算20141122-20141127之间所有类目 购买/(加购物车+1) 当不发生购买行为时为0，不提取
CateBuyCartRate("20141122-20141127",r"\1122_1127\CateBuyCartRate.csv")
 #计算20141122-20141127之间所有类目 购买/(交互次数+1) 当不发生购买行为时为0，不提取
CateBuyTotalRate("20141122-20141127",r"\1122_1127\CateBuyTotalRate.csv")
# 计算20141122-20141127之间所有类目 日均交互次数
CateVisitPerDay("20141122-20141127",r"\1122_1127\CateVisitPerDay.csv")

# 计算20141122-20141127之间user-item需求特征
DemandFeature("20141122-20141127",r"1122_1127\DemandFeature.csv")
