---
title: 产品详情
date: 2021-01-26 19:53:25
tags:
- atom
- github
- hexo
- travis
categories:
- Diary
---

# 基本信息
- 当前净值
- 近一周涨跌幅
- 近一个月涨跌幅

# 重仓股票
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10

# 业绩走势

{% echarts 600 '100%' %}
{
  tooltip: {
        trigger: 'axis',
        position: function (pt) {
            return [pt[0], '10%'];
        }
    },
    title: {
        left: 'center',
        text: '基金走势',
    },
    toolbox: {
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'time',
        boundaryGap: false
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%']
    },
    dataZoom: [{
        type: 'inside',
        start: 0,
        end: 20
    }, {
        start: 0,
        end: 20
    }],
    series: [
        {
            name: '模拟数据',
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {},
            data: [[1, 1],[ 2, 2], [3, 3], [4, 4]]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 |
| --- | --- | --- |
|2021-01-25|1.9425|+2.81%|
