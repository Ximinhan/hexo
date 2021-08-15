#!/usr/bin/python3
from __future__ import division
import subprocess
import sys
import datetime
import csv
num=60
if len(sys.argv)>2:
    num=sys.argv[2]
def main():
    p = subprocess.Popen("curl -s http://fund.eastmoney.com/pingzhongdata/{}.js|sed 's/;/\\n/g'|grep Data_netWorthTrend|grep -Po '(?<=\[).*(?=\])'|sed 's/}}\,{{/\\n/g'|sed 's/[A-Za-z\\\"\:]*//g'|cut -d ',' -f 1,2,3|sed 's/,/|/g'|sed 's/^/|&/g'|sed 's/$/&|/g'|tac|head -n {}".format(sys.argv[1],num),stdout=subprocess.PIPE,shell=True)
    vl=p.stdout.readlines()
    result=[]
    ret=[]
    for line in vl:
        ds = line.decode().strip().split("|")
        #日期，净值，涨跌幅，上涨概率，连续上涨天数，连续下跌天数，区间净收益率，区间累计收益
        result.append([datetime.datetime.fromtimestamp(int(ds[1][0:10])).strftime('%Y-%m-%d'),float(ds[2]),float(ds[3])])
        #print(datetime.datetime.fromtimestamp(int(ds[1][0:10])).strftime('%Y-%m-%d'),ds[2],ds[3])
    result.reverse()
    i=0
    #定投概率
    pickrate=[[],[],[],[],[]]
    #print(result)
    while i < int(num):
        #日期
        d0 = result[i][0]
        #净值
        d1 = result[i][1]
        #涨跌幅
        d2 = result[i][2]
        #上涨概率
        d3 = uprate(result[:i])
        #连续上涨天数
        d4 = keepup(result[:i])
        #连续下跌天数
        d5 = keepdown(result[:i])
        #区间净收益率
        d6 = prate(result[:i])
        #区间累计收益率
        d7 = sumprate(result[:i])
        #最大回撤
        d8 = maxretrace(result[:i])
        #收益回撤比
        d9 = pretrace(d6,d8)
        #波动率
        d10 = wave(result[:i])

        #周几
        #{ mon: up:{},dowm:{}
        wd=datetime.datetime.strptime(d0, "%Y-%m-%d").weekday()
        #mon 0 fir 4
        pickrate[wd].append(d2)

        #print(d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10)
        ret.append([d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,sys.argv[1]])
        i=i+1
   # with open('today.csv','a+') as td:
   #     cw = csv.writer(td)
   #     cw.writerow(ret[-1])

    ret.reverse()
    for item in ret:
        print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
            item[0],#日期
            item[1],#净值
            color(item[2]),#涨跌幅
            item[3],#上涨概率
            item[4],#连续上涨天数
            item[5],#连续下跌天数
            color(item[6]),#区间净收益率
            color(item[7]),#区间累计收益率
            color(item[8]),#最大回撤
            item[9],#收益回撤比
            item[10],#波动率
        ))
    #print(result)
    #print(pickrate)
    #getday(pickrate)

def getday(p):
    for s,i in enumerate(p):
        t=0
        for k in i:
            if k>0:
                t=t+1
        print("day {} up rate is:{}".format(s,t/len(i)))


def color(p):
    ret=""
    if p < 0:
        ret = "<font color=green>{}%</font>".format(p)
    else:
        ret = "<font color=red>{}%</font>".format(p)
    return ret


#收益回撤比
def pretrace(a,b):
    if b == 0:
        return 0
    return round(a*7.74/b,2)


#波动率
def wave(p):
    #print("wave",p)
    if len(p)==0:
        return 0
    s=0
    i=0
    while i < len(p):
        s=s+p[i][2]
        i=i+1
    a=s/len(p)
    t=0
    i=0
    while i < len(p):
        t=t+(p[i][2]-a)*(p[i][2]-a)
        i=i+1
    #print("out wave",p)
    return round((t/len(p))**0.5*7.74,2)

#最大回撤
def maxretrace(p):
    #print("maxretrace",p)
    if len(p)==0:
        return 0
    r=0
    i=0
    while i < len(p):
        k=i+1
        while k < len(p):
            #print(i,k)
            #print((p[i][1]-p[k][1])/p[i][1])
            if r < (p[i][1]-p[k][1])/p[i][1]:
                r = (p[i][1]-p[k][1])/p[i][1]
            k=k+1
        i=i+1
    return round(r*100,2)


#区间累计收益率
def sumprate(p):
    #print("sumprate",p)
    if len(p)==0:
        return 0
    i=1
    t=0
    while i < len(p):
        t=t+prate(p[:i])
        i=i+1
    return round(t/len(p),2)

#区间净收益率
def prate(p):
    #print("prate",p)
    if len(p)==0:
        return 0
    return round(((p[-1][1]-p[0][1])/p[0][1])*100,2)


#连续下跌天数
def keepdown(p):
    #print("keepdown",p)
    if len(p)==0:
        return 0
    i=1
    n=0
    while i < len(p):
        if p[-i][2] <= 0:
            n=n+1
            i=i+1
        else:
            break
    return n
#上涨概率
def uprate(p):
    #print("uprate",p)
    if len(p)==0:
        return 0
    up=0
    down=0
    for i in p:
        #print(i[0],i[1],i[2])
        if float(i[2]) > 0:
            up=up+1
        else:
            down=down+1
    #print(up,down)
    return round(float(up/(up+down)),2)
#连续上涨天数
def keepup(p):
    #print("keepup",p)
    if len(p)==0:
        return 0
    i=1
    n=0
    while i < len(p):
        if p[-i][2] >= 0:
            n=n+1
            i=i+1
        else:
            break
    return n

if __name__ == '__main__':
    main()
