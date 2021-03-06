---
title: 使用travis自动部署hexo笔记
date: 2021-01-23 19:25:49
tags:
- atom
- github
- hexo
- travis
categories:
- Diary
---

# 工具列表

* atom
* git
* Hexo
* Travis
* Github pages

# 新建项目
# 加载themes主题

git rm -r --cached .  删除git缓存导致的themes文件夹push失败
使用atom git插件授权

# 配置 \_config.yml

deploy部分的repo需要是一个object
repo:
    url:
    branch: gh-pages
    token: $GH_TOKEN

# 配置 \.Travis.yml文件

配置deploy参数
查看build
https://travis-ci.com/github/Ximinhan/hexo/builds


# 配置token与github pages

在project setting中配置github pages的source分支和public url

# 检查部署
向main分支可以触发travis build并部署到gh-pages分支

# 配置atom
markdown插件preview
https://markdown-it.github.io/
github插件授权

可直接clone项目后在atom中打开编辑
然后commit push就行了
用命令的话
可以配置git crendential免密push
git commit -am “update” && git push
git fetch upstream
git checkout master
git merge upstream/master
git push origin master

编写shell脚本更新post内容
1.基金名称
curl -s http://fund.eastmoney.com/pingzhongdata/519150.js|sed 's/;/\n/g'|grep fS_name|grep -Po '(?<=").*(?=")'


2.历史净值
curl -s http://fund.eastmoney.com/pingzhongdata/519150.js|sed 's/;/\n/g'|grep Data_netWorthTrend|grep -Po '(?<=\[).*(?=\])'|sed 's/}\,{/\n/g'|sed "s/[A-Za-z\"\:]*//g"|cut -d ',' -f 1,2,3|sed 's/,/|/g'|sed 's/^/|&/g'|sed 's/$/&|/g'|tac|head -n 10
cat ./test|while read line;
do
    s1=`echo $line|cut -d "|" -f 2`
    s2=`echo $line|cut -d "|" -f 3`
    s3=`echo $line|cut -d "|" -f 4`
    s1=`date -d @${s1:0:10} +'%Y-%m-%d'`
    if [ ${s3:0:1} == "-" ];then
        s3="<font color=green>$s3%</font>"
    else
        s3="<font color=red>$s3%</font>"
    fi
    echo "|$s1|$s2|$s3|";
    #s1=`date -d @${s1:0:10} +'%Y/%m/%d'`;
    #echo "[\"$s1\",$s2],";
done

使用travis script 执行内容并使用cronjob自动部署
markdown list table 列表 echart曲线图

{% echarts 400 '85%' %}
{
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['利润', '支出', '收入']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'value'
        }
    ],
    yAxis : [
        {
            type : 'category',
            axisTick : {show: false},
            data : ['周一','周二','周三','周四','周五','周六','周日']
        }
    ],
    series : [
        {
            name:'利润',
            type:'bar',
            itemStyle : {
                normal: {
                    label: {show: true, position: 'inside'}
                }
            },
            data:[200, 170, 240, 244, 200, 220, 210]
        },
        {
            name:'收入',
            type:'bar',
            stack: '总量',
            itemStyle: {
                normal: {
                    label : {show: true}
                }
            },
            data:[320, 302, 341, 374, 390, 450, 420]
        },
        {
            name:'支出',
            type:'bar',
            stack: '总量',
            itemStyle: {normal: {
                label : {show: true, position: 'left'}
            }},
            data:[-120, -132, -101, -134, -190, -230, -210]
        }
    ]
};
{% endecharts %}

# 折线图

{% echarts 600 '100%' %}
{
    title: {
        text: '折线图堆叠'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 40,
        data:['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一','周二','周三','周四','周五','周六','周日']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'邮件营销',
            type:'line',
            stack: '总量',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'联盟广告',
            type:'line',
            stack: '总量',
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'视频广告',
            type:'line',
            stack: '总量',
            data:[150, 232, 201, 154, 190, 330, 410]
        },
        {
            name:'直接访问',
            type:'line',
            stack: '总量',
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'搜索引擎',
            type:'line',
            stack: '总量',
            data:[820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};
{% endecharts %}

# 表格

| 日期 | Description |
| ------ | ----------- |
| data   | `+2.8`% |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
