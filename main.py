#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
reload(sys)
sys.setdefaultencoding('utf8')


result = u"没有"
totalhand = 0
Peoplelist = []

totalzy = 0
totaldt = 0
totalsh = 0
totalsj = 0
totalej = 0
totalyx = 0

totalcjh = 0
totallbh = 0
totallbhei = 0
#当前状元
currentzy  = {1: 0, 2:0, 3:0,4:0,5:0}

zy = 1
dt = 2
sh = 4
sj = 8
ej = 16
yx = 32


class People(object):

    def __init__(self,name,yx,ej,sj,sh,dt,zy):
        self.name = name
        self.yx = yx
        self.ej = ej
        self.sj = sj
        self.sh = sh
        self.dt = dt
        self.zy = zy
    def print_score(self):
        print u'%s: 一秀:%s,二举:%s,四进:%s,三红:%s,对堂%s,状元:%s' % (self.name, self.yx,self.ej,self.sj,self.sh,self.dt,self.zy)

# 取出特定数字
def guolvhanshu(num):
    if num<>4:
        return num


# 判断状元
def countzy(currentzy={}):
    whoiszy = max(currentzy.items(), key=lambda x:x[1])
    Peoplelist[whoiszy[0]].zy = 1
    return 

#判断大小函数
def my_count(hand=[],p=0):
    global Peoplelist
    global yx,zy,dt,sh,sj,ej,result
    global totalzy,totaldt,totalsh,totalsj,totalej,totalyx,totalcjh,totallbh,totallbhei,currentzy
    dic={1:0,2:0,3:0,4:0,5:0,6:0}
    for item in hand:
        dic[item] = dic.get(item, 0) + 1
    #print dic
    if dic[4]==6:
        zy = 0
        totalzy = totalzy + 1
        Peoplelist[p].zy = Peoplelist[p].zy+1
        result =u'六勃红'
        currentzy[p] = 6.1
        totallbh = totallbh+1
        return
    elif dic[1] == 6 or dic[2] == 6 or dic[3] == 6 or dic[5] == 6 or dic[6] == 6:
        zy = 0
        result =u'六勃黑'
        totalzy = totalzy + 1
        Peoplelist[p].zy = Peoplelist[p].zy+1
        currentzy[p] = 6.0
        totallbhei = totallbhei+1
        return
    elif dic[4] == 4 and dic[1] == 2:
        zy = 0
        result =u'状元插金花'
        totalzy = totalzy + 1
        totalcjh = totalcjh+1
        Peoplelist[p].zy = Peoplelist[p].zy+1
        currentzy[p] = 5.9
        return
    elif dic[4] == 5 :
        zy = 0
        result =u'五红'
        totalzy = totalzy + 1
        d = 0
        if dic[1] == 1:
            d =1
        elif dic[2] == 1:
            d =2
        elif dic[3] == 1:
            d =3
        elif dic[4] == 1:
            d =4
        elif dic[5] == 1:
            d =5
        elif dic[1] == 1:
            d =6
        currentzy[p] = 500 + d
        return
    elif dic[1] == 5 or dic[2] == 5 or dic[3] == 5 or dic[5] == 5 or dic[6] == 5:
        zy = 0
        result =u'五子'
        totalzy = totalzy + 1
        # 使用filter函数
        result=filter(guolvhanshu,hand)
        currentzy[p] = 450 + result[0]
        return
    elif dic[4] == 4 :
        zy = 0
        result =u'四红'
        totalzy = totalzy + 1
        # 使用filter函数
        result=filter(guolvhanshu,hand)
        currentzy[p] = 400 + result[0] + result[1]
        return
    elif dic[1] == 1 and dic[2] == 1 and dic[3] == 1 and dic[4] == 1 and dic[5] == 1 and dic[6] == 1:
        if dt >=1:
            dt = dt -1
            Peoplelist[p].dt = Peoplelist[p].dt+1
        result =u'对堂'
        totaldt = totaldt + 1
        return
    elif dic[4] == 3 :
        if sh >=1:
            sh = sh -1
            Peoplelist[p].sh = Peoplelist[p].sh+1
        result =u'三红'
        totalsh = totalsh + 1
        return
    elif dic[1] == 4 or dic[2] == 4 or dic[3] == 4 or dic[5] == 4 or dic[6] == 4:
        if sj >=1:
            sj = sj -1
            Peoplelist[p].sj = Peoplelist[p].sj+1
        result =u'四进'
        totalsj = totalsj + 1
        if dic[4] == 2 :
            if ej >=1:
                ej = ej -1
                Peoplelist[p].ej = Peoplelist[p].ej+1
        result =u'四进带二举'
        totalej = totalej + 1
        if dic[4] == 1 :
            if yx >=1:
                yx = yx -1
                Peoplelist[p].yx = Peoplelist[p].yx+1
        result =u'四进带一秀'
        totalyx = totalyx + 1
        return
    elif dic[4] == 2 :
        if ej >=1:
            ej = ej -1
            Peoplelist[p].ej = Peoplelist[p].ej+1
        result =u'二举'
        totalej = totalej + 1
        return
    elif dic[4] == 1 :
        if yx >=1:
            yx = yx -1
            Peoplelist[p].yx = Peoplelist[p].yx+1
        result =u'一秀'
        totalyx = totalyx + 1
        return


#开始一次博饼
#创建一个随机数组
 
 



class Bobing(object):

    def __init__(self,peoples=5):
        self.peoples = peoples

    def start(self):
        #初始化
        global zy 
        global dt 
        global sh 
        global sj 
        global ej 
        global yx 
        zy = 1
        dt = 2
        sh = 4
        sj = 8
        ej = 16
        yx = 32
        global totalhand 
        global Peoplelist
        global Cheng,Yue,Dolm,TT,Eva
        #创建循环
        Cheng = People("Cheng",0,0,0,0,0,0)
        Yue = People("Yue",0,0,0,0,0,0)
        Dolm = People("Dolm",0,0,0,0,0,0)
        TT = People("TT",0,0,0,0,0,0)
        Eva = People("Eva",0,0,0,0,0,0)

        Peoplelist = [Cheng,Yue,Dolm,TT,Eva]
        Peoples = 5
        #第几个人
        p = 0
        while yx> 0 or zy> 0 or dt> 0 or sh > 0 or sj> 0 or ej> 0 or p< 4:
            hand = []
            n = 1
#随机博一次饼
            while n <= 6:
               hand.append(random.randint(1, 6))
               n = n + 1
#判断大小
            my_count(hand,p)
            p = p + 1
            if p == Peoples:
                p = 0
            totalhand = totalhand +1
            countzy(currentzy)

    def print_score(self):
        print totalzy,totaldt,totalsh,totalsj,totalej,totalyx
        print totalhand
        #Cheng.print_score()
        #Yue.print_score()
        #Dolm.print_score()
        #TT.print_score()
        #Eva.print_score()
#模拟器
class Simulator(object):
    def __init__(self,times,peoples,th):
       self.times = times
       self.peoples = peoples
       self.th = th
    def start(self):
        i = 0
        while i< self.times:
           Mybobing = Bobing(self.peoples)
           Mybobing.start() 
           i = i + 1
        
    def print_score(self):
        print totallbh,totallbhei,totalcjh,totalzy,totaldt,totalsh,totalsj,totalej,totalyx
        print totalhand


myS = Simulator(100000,5,0)
myS.start()
myS.print_score()
#Mybobing.print_score()



