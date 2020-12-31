# -*- coding: utf-8 -*-
import pandas as pd
import datetime as d
import re

class cart():
    #將Input做分類看到底是商品、折價券、當天促銷哪一種
    def __init__(self, input_):
        discount, buy, coupon=[],[],0
        temp = input_.split('\n')
        for i in temp:
            if i == '':
                continue
            elif '|' in i :
                discount.append(i)
            elif '*' in i:
                buy.append(i)
            else:
                coupon=i
        self.total_price(discount, buy, coupon.split(' ')) 
                
    def total_price(self, discount, buy, coupon):
        if discount ==[]:
            discount = ['||']
        discount = pd.DataFrame([dis_sep.split('|') for dis_sep in discount],
                                columns = ['date','off','category'])
        
        if buy == []:
            buy = ['*:']
        buy = pd.DataFrame([ re.split('\*|:',buy_sep) for buy_sep in buy],
                           columns = ['amount','name','price'])
        buy['category'] = buy['name'].apply(self.classify)
        buy = pd.merge(left = buy, right = discount, how = "left", on = 'category')
        buy['off'][buy['date'] != coupon[0]] = 1

        for i in ['amount','price','off']:
            buy[i] = pd.to_numeric(buy[i])
        total_price = sum(buy['amount']*buy['price']*buy['off'])
        
        if len(coupon) > 1: 
            if self.due_(coupon[0],coupon[1]) >= 0 and total_price >= int(coupon[2]):
                total_price -= int(coupon[3])
        
        self.price = float("{:.2f}".format(total_price))
        print(self.price)

    #這裡產品細項我有自行加入"顯示器"(文件內電子類沒有但折扣有算到)和"面包"(文件中只有"麵包")
    def classify(self,value):
        category = {"電子":["ipad","iphone","螢幕","筆記型電腦","鍵盤","顯示器"],
                     "食品":["麵包","餅乾","蛋糕","牛肉","魚","蔬菜","面包"],
                     "日用品":["餐巾紙","收納箱","咖啡杯","雨傘"],
                     "酒類":["啤酒","白酒","伏特加"]}
        for product in category :
            if value in category[product]:
                return product
    #確認折價券日期
    def due_(self,now, exp):
        temp_now = [int(i) for i in now.split('.')]
        temp_exp = [int(i) for i in exp.split('.')]
        d_now = d.datetime(temp_now[0], temp_now[1], temp_now[2])
        d_exp = d.datetime(temp_exp[0], temp_exp[1], temp_exp[2])
        return (d_exp - d_now).days

input_1="2015.11.11|0.7|電子\n1*ipad:2399.00\n1*顯示器:1799.00\n12*啤酒:25.00\n5*麵包:9.00\n2015.11.11 2016.3.2 1000 200"
cart1 = cart(input_1)
input_2 ="\n3*蔬菜:5.98\n8*餐巾紙:3.20\n2015.01.01"
cart2 = cart(input_2)
