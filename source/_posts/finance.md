---
title: 使用travis自动部署hexo笔记
date: 2021-01-23 19:25:49
tags:
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

# 配置 \.Travis.yml文件

# 配置token与github pages

# 检查部署
向main分支可以触发travis build并部署到gh-pages分支

# 配置atom
markdown插件preview
github插件授权


编写shell脚本更新post内容
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
