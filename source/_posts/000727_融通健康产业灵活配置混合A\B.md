---
title: 产品详情
date: 2021-10-01 15:59:44
tags:
- atom
- github
- hexo
- travis
categories:
- Diary
---

# 基本信息
## 000727-融通健康产业灵活配置混合A\B
- 近一个月涨跌幅：4.07%
- 近三个月涨跌幅: -9.74%
- 近六个月涨跌幅: -3.34%

# 重仓股票
- 002727 深证 一心堂
- 603883 上证 老百姓
- 300406 创业 九强生物
- 300633 创业 开立医疗
- 002044 深证 美年健康
- 300149 创业 睿智医药
- 603658 上证 安图生物
- 
- 300122 创业 智飞生物
- 300639 创业 凯普生物
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
        min: 2,
        max: 4,
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
["2021/09/30",2.835],
["2021/09/29",2.795],
["2021/09/28",2.85],
["2021/09/27",2.863],
["2021/09/24",2.818],
["2021/09/23",2.817],
["2021/09/22",2.815],
["2021/09/17",2.793],
["2021/09/16",2.713],
["2021/09/15",2.721],
["2021/09/14",2.767],
["2021/09/13",2.743],
["2021/09/10",2.754],
["2021/09/09",2.785],
["2021/09/08",2.795],
["2021/09/07",2.793],
["2021/09/06",2.821],
["2021/09/03",2.746],
["2021/09/02",2.717],
["2021/09/01",2.765],
["2021/08/31",2.724],
["2021/08/30",2.735],
["2021/08/27",2.763],
["2021/08/26",2.79],
["2021/08/25",2.887],
["2021/08/24",2.872],
["2021/08/23",2.865],
["2021/08/20",2.81],
["2021/08/19",2.895],
["2021/08/18",2.915],
["2021/08/17",2.869],
["2021/08/16",2.939],
["2021/08/13",2.906],
["2021/08/12",2.881],
["2021/08/11",2.908],
["2021/08/10",2.939],
["2021/08/09",2.878],
["2021/08/06",2.788],
["2021/08/05",2.855],
["2021/08/04",2.876],
["2021/08/03",2.902],
["2021/08/02",2.786],
["2021/07/30",2.746],
["2021/07/29",2.702],
["2021/07/28",2.68],
["2021/07/27",2.688],
["2021/07/26",2.768],
["2021/07/23",2.86],
["2021/07/22",2.947],
["2021/07/21",3.008],
["2021/07/20",3.003],
["2021/07/19",2.99],
["2021/07/16",2.994],
["2021/07/15",3.03],
["2021/07/14",3.091],
["2021/07/13",3.09],
["2021/07/12",3.055],
["2021/07/09",3.031],
["2021/07/08",3.018],
["2021/07/07",3.057],
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-09-30|2.835|<font color=red>1.43%</font>|0.49|0|2|<font color=green>-8.57%</font>|<font color=green>-6.48%</font>|<font color=red>13.3%</font>|-4.99|12.77|
|2021-09-29|2.795|<font color=green>-1.93%</font>|0.5|0|1|<font color=green>-6.77%</font>|<font color=green>-6.48%</font>|<font color=red>13.3%</font>|-3.94|12.74|
|2021-09-28|2.85|<font color=green>-0.45%</font>|0.51|5|0|<font color=green>-6.35%</font>|<font color=green>-6.48%</font>|<font color=red>13.3%</font>|-3.7|12.85|
|2021-09-27|2.863|<font color=red>1.6%</font>|0.5|4|0|<font color=green>-7.82%</font>|<font color=green>-6.45%</font>|<font color=red>13.3%</font>|-4.55|12.84|
|2021-09-24|2.818|<font color=red>0.04%</font>|0.49|3|0|<font color=green>-7.85%</font>|<font color=green>-6.43%</font>|<font color=red>13.3%</font>|-4.57|12.96|
|2021-09-23|2.817|<font color=red>0.07%</font>|0.48|2|0|<font color=green>-7.92%</font>|<font color=green>-6.4%</font>|<font color=red>13.3%</font>|-4.61|13.08|
|2021-09-22|2.815|<font color=red>0.79%</font>|0.47|1|0|<font color=green>-8.64%</font>|<font color=green>-6.36%</font>|<font color=red>13.3%</font>|-5.03|13.16|
|2021-09-17|2.793|<font color=red>2.95%</font>|0.46|0|2|<font color=green>-11.25%</font>|<font color=green>-6.26%</font>|<font color=red>13.3%</font>|-6.55|12.86|
|2021-09-16|2.713|<font color=green>-0.29%</font>|0.47|0|1|<font color=green>-10.99%</font>|<font color=green>-6.17%</font>|<font color=red>13.3%</font>|-6.4|12.99|
|2021-09-15|2.721|<font color=green>-1.66%</font>|0.48|1|0|<font color=green>-9.49%</font>|<font color=green>-6.11%</font>|<font color=red>13.3%</font>|-5.52|13.02|
|2021-09-14|2.767|<font color=red>0.87%</font>|0.47|0|3|<font color=green>-10.27%</font>|<font color=green>-6.02%</font>|<font color=red>13.3%</font>|-5.98|13.1|
|2021-09-13|2.743|<font color=green>-0.4%</font>|0.48|0|2|<font color=green>-9.91%</font>|<font color=green>-5.94%</font>|<font color=red>13.3%</font>|-5.77|13.23|
|2021-09-10|2.754|<font color=green>-1.11%</font>|0.49|0|1|<font color=green>-8.9%</font>|<font color=green>-5.88%</font>|<font color=red>13.3%</font>|-5.18|13.33|
|2021-09-09|2.785|<font color=green>-0.36%</font>|0.5|1|0|<font color=green>-8.57%</font>|<font color=green>-5.82%</font>|<font color=red>13.3%</font>|-4.99|13.47|
|2021-09-08|2.795|<font color=red>0.07%</font>|0.49|0|1|<font color=green>-8.64%</font>|<font color=green>-5.76%</font>|<font color=red>13.3%</font>|-5.03|13.62|
|2021-09-07|2.793|<font color=green>-0.99%</font>|0.5|2|0|<font color=green>-7.72%</font>|<font color=green>-5.71%</font>|<font color=red>13.3%</font>|-4.49|13.74|
|2021-09-06|2.821|<font color=red>2.73%</font>|0.49|1|0|<font color=green>-10.17%</font>|<font color=green>-5.61%</font>|<font color=red>13.3%</font>|-5.92|13.46|
|2021-09-03|2.746|<font color=red>1.07%</font>|0.48|0|1|<font color=green>-11.12%</font>|<font color=green>-5.48%</font>|<font color=red>13.3%</font>|-6.47|13.54|
|2021-09-02|2.717|<font color=green>-1.74%</font>|0.49|1|0|<font color=green>-9.55%</font>|<font color=green>-5.38%</font>|<font color=red>13.3%</font>|-5.56|13.58|
|2021-09-01|2.765|<font color=red>1.51%</font>|0.47|0|4|<font color=green>-10.89%</font>|<font color=green>-5.24%</font>|<font color=red>13.3%</font>|-6.34|13.58|
|2021-08-31|2.724|<font color=green>-0.4%</font>|0.49|0|3|<font color=green>-10.53%</font>|<font color=green>-5.1%</font>|<font color=red>13.3%</font>|-6.13|13.75|
|2021-08-30|2.735|<font color=green>-1.01%</font>|0.5|0|2|<font color=green>-9.62%</font>|<font color=green>-4.98%</font>|<font color=red>13.3%</font>|-5.6|13.9|
|2021-08-27|2.763|<font color=green>-0.97%</font>|0.51|0|1|<font color=green>-8.73%</font>|<font color=green>-4.88%</font>|<font color=red>13.3%</font>|-5.08|14.05|
|2021-08-26|2.79|<font color=green>-3.36%</font>|0.53|3|0|<font color=green>-5.56%</font>|<font color=green>-4.86%</font>|<font color=red>13.3%</font>|-3.24|13.63|
|2021-08-25|2.887|<font color=red>0.52%</font>|0.51|2|0|<font color=green>-6.05%</font>|<font color=green>-4.83%</font>|<font color=red>13.3%</font>|-3.52|13.8|
|2021-08-24|2.872|<font color=red>0.24%</font>|0.5|1|0|<font color=green>-6.28%</font>|<font color=green>-4.79%</font>|<font color=red>13.3%</font>|-3.65|13.99|
|2021-08-23|2.865|<font color=red>1.96%</font>|0.48|0|2|<font color=green>-8.08%</font>|<font color=green>-4.69%</font>|<font color=red>13.3%</font>|-4.7|13.91|
|2021-08-20|2.81|<font color=green>-2.94%</font>|0.5|0|1|<font color=green>-5.3%</font>|<font color=green>-4.67%</font>|<font color=red>13.3%</font>|-3.08|13.6|
|2021-08-19|2.895|<font color=green>-0.69%</font>|0.52|1|0|<font color=green>-4.65%</font>|<font color=green>-4.67%</font>|<font color=red>13.3%</font>|-2.71|13.8|
|2021-08-18|2.915|<font color=red>1.6%</font>|0.5|0|1|<font color=green>-6.15%</font>|<font color=green>-4.62%</font>|<font color=red>13.3%</font>|-3.58|13.81|
|2021-08-17|2.869|<font color=green>-2.38%</font>|0.52|2|0|<font color=green>-3.86%</font>|<font color=green>-4.65%</font>|<font color=red>13.3%</font>|-2.25|13.67|
|2021-08-16|2.939|<font color=red>1.14%</font>|0.5|1|0|<font color=green>-4.94%</font>|<font color=green>-4.64%</font>|<font color=red>13.3%</font>|-2.87|13.79|
|2021-08-13|2.906|<font color=red>0.87%</font>|0.48|0|2|<font color=green>-5.76%</font>|<font color=green>-4.59%</font>|<font color=red>13.3%</font>|-3.35|13.96|
|2021-08-12|2.881|<font color=green>-0.93%</font>|0.5|0|1|<font color=green>-4.87%</font>|<font color=green>-4.58%</font>|<font color=red>13.3%</font>|-2.83|14.18|
|2021-08-11|2.908|<font color=green>-1.05%</font>|0.52|2|0|<font color=green>-3.86%</font>|<font color=green>-4.61%</font>|<font color=red>13.3%</font>|-2.25|14.39|
|2021-08-10|2.939|<font color=red>2.12%</font>|0.5|1|0|<font color=green>-5.86%</font>|<font color=green>-4.56%</font>|<font color=red>13.3%</font>|-3.41|14.24|
|2021-08-09|2.878|<font color=red>3.23%</font>|0.48|0|3|<font color=green>-8.8%</font>|<font color=green>-4.38%</font>|<font color=red>13.3%</font>|-5.12|13.41|
|2021-08-06|2.788|<font color=green>-2.35%</font>|0.5|0|2|<font color=green>-6.61%</font>|<font color=green>-4.27%</font>|<font color=red>13.3%</font>|-3.85|13.28|
|2021-08-05|2.855|<font color=green>-0.73%</font>|0.52|0|1|<font color=green>-5.92%</font>|<font color=green>-4.2%</font>|<font color=red>13.3%</font>|-3.45|13.57|
|2021-08-04|2.876|<font color=green>-0.9%</font>|0.55|4|0|<font color=green>-5.07%</font>|<font color=green>-4.15%</font>|<font color=red>13.3%</font>|-2.95|13.86|
|2021-08-03|2.902|<font color=red>4.16%</font>|0.53|3|0|<font color=green>-8.86%</font>|<font color=green>-3.9%</font>|<font color=red>13.3%</font>|-5.16|11.8|
|2021-08-02|2.786|<font color=red>1.46%</font>|0.5|2|0|<font color=green>-10.17%</font>|<font color=green>-3.56%</font>|<font color=red>13.3%</font>|-5.92|11.6|
|2021-07-30|2.746|<font color=red>1.63%</font>|0.47|1|0|<font color=green>-11.61%</font>|<font color=green>-3.08%</font>|<font color=red>13.3%</font>|-6.76|11.19|
|2021-07-29|2.702|<font color=red>0.82%</font>|0.44|0|5|<font color=green>-12.33%</font>|<font color=green>-2.5%</font>|<font color=red>13.3%</font>|-7.18|11.15|
|2021-07-28|2.68|<font color=green>-0.3%</font>|0.47|0|4|<font color=green>-12.07%</font>|<font color=green>-1.87%</font>|<font color=red>13.04%</font>|-7.16|11.48|
|2021-07-27|2.688|<font color=green>-2.89%</font>|0.5|0|3|<font color=green>-9.45%</font>|<font color=green>-1.32%</font>|<font color=red>10.45%</font>|-7.0|10.98|
|2021-07-26|2.768|<font color=green>-3.22%</font>|0.54|0|2|<font color=green>-6.44%</font>|<font color=green>-0.93%</font>|<font color=red>7.47%</font>|-6.67|9.82|
|2021-07-23|2.86|<font color=green>-2.95%</font>|0.58|0|1|<font color=green>-3.6%</font>|<font color=green>-0.71%</font>|<font color=red>4.66%</font>|-5.98|8.36|
|2021-07-22|2.947|<font color=green>-2.03%</font>|0.64|2|0|<font color=green>-1.6%</font>|<font color=green>-0.63%</font>|<font color=red>3.27%</font>|-3.79|7.53|
|2021-07-21|3.008|<font color=red>0.17%</font>|0.6|1|0|<font color=green>-1.77%</font>|<font color=green>-0.51%</font>|<font color=red>3.27%</font>|-4.19|7.87|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.56|0|3|<font color=green>-2.19%</font>|<font color=green>-0.33%</font>|<font color=red>3.27%</font>|-5.18|8.19|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.62|0|2|<font color=green>-2.06%</font>|<font color=green>-0.11%</font>|<font color=red>3.14%</font>|-5.08|8.68|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.71|0|1|<font color=green>-0.88%</font>|<font color=red>-0.0%</font>|<font color=red>1.97%</font>|-3.46|8.66|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.83|4|0|<font color=red>1.11%</font>|<font color=green>-0.19%</font>|<font color=red>1.28%</font>|6.71|6.4|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.8|3|0|<font color=red>1.08%</font>|<font color=green>-0.44%</font>|<font color=red>1.28%</font>|6.53|6.9|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.75|2|0|<font color=green>-0.07%</font>|<font color=green>-0.53%</font>|<font color=red>1.28%</font>|-0.42|7.05|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.67|1|0|<font color=green>-0.85%</font>|<font color=green>-0.43%</font>|<font color=red>1.28%</font>|-5.14|7.65|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.5|0|1|<font color=green>-1.28%</font>|<font color=red>0.0%</font>|<font color=red>1.28%</font>|-7.74|9.06|
|2021-07-08|3.018|<font color=green>-1.28%</font>|1.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-07-07|3.057|<font color=red>1.06%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
