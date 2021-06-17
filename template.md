---
title: 产品详情
date: {{ datetime }}
tags:
- atom
- github
- hexo
- travis
categories:
- Diary
---

# 基本信息
## {{ name }}
- 近一个月涨跌幅：{{ m1 }}%
- 近三个月涨跌幅: {{ m3 }}%
- 近六个月涨跌幅: {{ m6 }}%

# 重仓股票
((* for value in stocklist -*))
- {{ value.strip() }}
((* endfor -*))

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
        min: {{ min1 }},
        max: {{ max1 }},
        type: 'value',
        boundaryGap: [0, '100%']
    },
    dataZoom: [{
        type: 'inside',
        start: 50,
        end: 100
    }, {
        start: 0,
        end: 20
    }],
    series: [
        {
            name: '本基金',
            type: 'line',
            data: [
((* for value in linelist -*))
{{ value.strip() }}
((* endfor -*))
            ]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 |
| --- | --- | --- |
((* for value in valuelist -*))
{{ value.strip() }}
((* endfor -*))
