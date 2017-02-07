# coding: utf-8
import tushare as ts
import pandas as pd

#获取所有股票代码
stock_total=ts.get_stock_basics()

#初始化历史股票数据
stock_hist_list=pd.DataFrame()

#遍历前20只股票，添加插入股票代码，并且拼接到stock_hist_list中
'''for i in stock_total.index[:20]:
    single_stock_hist=ts.get_hist_data(i)
    single_stock_hist.insert(0,'num',i)
    stock_hist_list=pd.concat([stock_hist_list,single_stock_hist],ignore_index=False)    
'''
for i in stock_total.index:
    single_stock_hist=ts.get_hist_data(i)
    single_stock_hist.insert(0,'num',i)
    stock_hist_list=pd.concat([stock_hist_list,single_stock_hist],ignore_index=False)    

#数据库写入    
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://ncp:ncp@192.168.1.175/hdata?charset=utf8')
stock_hist_list.to_sql('h_data3',engine,if_exists='append')
