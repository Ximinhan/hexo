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
      trigger: 'none',
      axisPointer: {
          type: 'cross'
      }
  },
  legend: {
      data:['2015 降水量', '2016 降水量']
  },
  grid: {
      top: 70,
      bottom: 50
  },
  xAxis: [
      {
          type: 'category',
          axisTick: {
              alignWithLabel: true
          },
          axisLine: {
              onZero: false,
          },
          axisPointer: {
              label: {
                  formatter: function (params) {
                      return '降水量  ' + params.value
                          + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                  }
              }
          },
          data: ['2016-1', '2016-2', '2016-3', '2016-4', '2016-5', '2016-6', '2016-7', '2016-8', '2016-9', '2016-10', '2016-11', '2016-12']
      },
      {
          type: 'category',
          axisTick: {
              alignWithLabel: true
          },
          axisLine: {
              onZero: false,
          },
          axisPointer: {
              label: {
                  formatter: function (params) {
                      return '降水量  ' + params.value
                          + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                  }
              }
          },
          data: ['2015-1', '2015-2', '2015-3', '2015-4', '2015-5', '2015-6', '2015-7', '2015-8', '2015-9', '2015-10', '2015-11', '2015-12']
      }
  ],
  yAxis: [
      {
          type: 'value'
      }
  ],
  series: [
      {
          name: '2015 降水量',
          type: 'line',
          xAxisIndex: 1,
          smooth: true,
          emphasis: {
              focus: 'series'
          },
          data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
      },
      {
          name: '2016 降水量',
          type: 'line',
          smooth: true,
          emphasis: {
              focus: 'series'
          },
          data: [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
      }
  ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 |
| --- | --- | --- |
|2021-01-25|1.9425|+2.81%|
