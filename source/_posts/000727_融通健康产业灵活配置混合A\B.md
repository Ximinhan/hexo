---
title: 产品详情
date: 2021-09-05 15:26:05
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
- 近一个月涨跌幅：-5.38%
- 近三个月涨跌幅: -13.07%
- 近六个月涨跌幅: -8.77%

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
["2021/07/06",3.025],
["2021/07/05",3.083],
["2021/07/02",3.099],
["2021/07/01",3.145],
["2021/06/30",3.141],
["2021/06/29",3.158],
["2021/06/28",3.191],
["2021/06/25",3.085],
["2021/06/24",3.078],
["2021/06/23",3.085],
["2021/06/22",3.063],
["2021/06/21",3.044],
["2021/06/18",2.973],
["2021/06/17",2.949],
["2021/06/16",2.951],
["2021/06/15",3.013],
["2021/06/11",3.063],
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-09-03|2.746|<font color=red>1.07%</font>|0.46|0|1|<font color=green>-11.3%</font>|<font color=green>-3.99%</font>|<font color=red>16.01%</font>|-5.46|12.89|
|2021-09-02|2.717|<font color=green>-1.74%</font>|0.47|1|0|<font color=green>-9.73%</font>|<font color=green>-3.89%</font>|<font color=red>16.01%</font>|-4.7|12.91|
|2021-09-01|2.765|<font color=red>1.51%</font>|0.46|0|4|<font color=green>-11.07%</font>|<font color=green>-3.76%</font>|<font color=red>16.01%</font>|-5.35|12.9|
|2021-08-31|2.724|<font color=green>-0.4%</font>|0.46|0|3|<font color=green>-10.71%</font>|<font color=green>-3.64%</font>|<font color=red>16.01%</font>|-5.18|13.02|
|2021-08-30|2.735|<font color=green>-1.01%</font>|0.47|0|2|<font color=green>-9.79%</font>|<font color=green>-3.52%</font>|<font color=red>16.01%</font>|-4.73|13.11|
|2021-08-27|2.763|<font color=green>-0.97%</font>|0.48|0|1|<font color=green>-8.91%</font>|<font color=green>-3.42%</font>|<font color=red>16.01%</font>|-4.31|13.2|
|2021-08-26|2.79|<font color=green>-3.36%</font>|0.49|3|0|<font color=green>-5.75%</font>|<font color=green>-3.38%</font>|<font color=red>16.01%</font>|-2.78|12.88|
|2021-08-25|2.887|<font color=red>0.52%</font>|0.48|2|0|<font color=green>-6.24%</font>|<font color=green>-3.33%</font>|<font color=red>16.01%</font>|-3.02|12.99|
|2021-08-24|2.872|<font color=red>0.24%</font>|0.47|1|0|<font color=green>-6.46%</font>|<font color=green>-3.26%</font>|<font color=red>16.01%</font>|-3.12|13.11|
|2021-08-23|2.865|<font color=red>1.96%</font>|0.46|0|2|<font color=green>-8.26%</font>|<font color=green>-3.16%</font>|<font color=red>16.01%</font>|-3.99|13.03|
|2021-08-20|2.81|<font color=green>-2.94%</font>|0.47|0|1|<font color=green>-5.48%</font>|<font color=green>-3.12%</font>|<font color=red>16.01%</font>|-2.65|12.8|
|2021-08-19|2.895|<font color=green>-0.69%</font>|0.48|1|0|<font color=green>-4.83%</font>|<font color=green>-3.08%</font>|<font color=red>16.01%</font>|-2.34|12.92|
|2021-08-18|2.915|<font color=red>1.6%</font>|0.47|0|1|<font color=green>-6.33%</font>|<font color=green>-3.01%</font>|<font color=red>16.01%</font>|-3.06|12.91|
|2021-08-17|2.869|<font color=green>-2.38%</font>|0.48|2|0|<font color=green>-4.05%</font>|<font color=green>-2.99%</font>|<font color=red>16.01%</font>|-1.96|12.79|
|2021-08-16|2.939|<font color=red>1.14%</font>|0.47|1|0|<font color=green>-5.13%</font>|<font color=green>-2.94%</font>|<font color=red>16.01%</font>|-2.48|12.85|
|2021-08-13|2.906|<font color=red>0.87%</font>|0.45|0|2|<font color=green>-5.94%</font>|<font color=green>-2.87%</font>|<font color=red>16.01%</font>|-2.87|12.94|
|2021-08-12|2.881|<font color=green>-0.93%</font>|0.47|0|1|<font color=green>-5.06%</font>|<font color=green>-2.82%</font>|<font color=red>16.01%</font>|-2.45|13.06|
|2021-08-11|2.908|<font color=green>-1.05%</font>|0.48|2|0|<font color=green>-4.05%</font>|<font color=green>-2.79%</font>|<font color=red>16.01%</font>|-1.96|13.17|
|2021-08-10|2.939|<font color=red>2.12%</font>|0.46|1|0|<font color=green>-6.04%</font>|<font color=green>-2.71%</font>|<font color=red>16.01%</font>|-2.92|13.04|
|2021-08-09|2.878|<font color=red>3.23%</font>|0.45|0|3|<font color=green>-8.98%</font>|<font color=green>-2.56%</font>|<font color=red>16.01%</font>|-4.34|12.51|
|2021-08-06|2.788|<font color=green>-2.35%</font>|0.46|0|2|<font color=green>-6.79%</font>|<font color=green>-2.45%</font>|<font color=red>16.01%</font>|-3.28|12.4|
|2021-08-05|2.855|<font color=green>-0.73%</font>|0.47|0|1|<font color=green>-6.11%</font>|<font color=green>-2.35%</font>|<font color=red>16.01%</font>|-2.95|12.54|
|2021-08-04|2.876|<font color=green>-0.9%</font>|0.49|4|0|<font color=green>-5.26%</font>|<font color=green>-2.27%</font>|<font color=red>16.01%</font>|-2.54|12.68|
|2021-08-03|2.902|<font color=red>4.16%</font>|0.47|3|0|<font color=green>-9.04%</font>|<font color=green>-2.09%</font>|<font color=red>16.01%</font>|-4.37|11.54|
|2021-08-02|2.786|<font color=red>1.46%</font>|0.46|2|0|<font color=green>-10.35%</font>|<font color=green>-1.85%</font>|<font color=red>16.01%</font>|-5.0|11.47|
|2021-07-30|2.746|<font color=red>1.63%</font>|0.44|1|0|<font color=green>-11.79%</font>|<font color=green>-1.56%</font>|<font color=red>16.01%</font>|-5.7|11.33|
|2021-07-29|2.702|<font color=red>0.82%</font>|0.42|0|5|<font color=green>-12.5%</font>|<font color=green>-1.23%</font>|<font color=red>16.01%</font>|-6.04|11.37|
|2021-07-28|2.68|<font color=green>-0.3%</font>|0.44|0|4|<font color=green>-12.24%</font>|<font color=green>-0.88%</font>|<font color=red>15.76%</font>|-6.01|11.55|
|2021-07-27|2.688|<font color=green>-2.89%</font>|0.45|0|3|<font color=green>-9.63%</font>|<font color=green>-0.6%</font>|<font color=red>13.26%</font>|-5.62|11.21|
|2021-07-26|2.768|<font color=green>-3.22%</font>|0.47|0|2|<font color=green>-6.63%</font>|<font color=green>-0.4%</font>|<font color=red>10.37%</font>|-4.95|10.63|
|2021-07-23|2.86|<font color=green>-2.95%</font>|0.48|0|1|<font color=green>-3.79%</font>|<font color=green>-0.28%</font>|<font color=red>7.65%</font>|-3.83|10.08|
|2021-07-22|2.947|<font color=green>-2.03%</font>|0.5|2|0|<font color=green>-1.8%</font>|<font color=green>-0.23%</font>|<font color=red>6.3%</font>|-2.21|9.88|
|2021-07-21|3.008|<font color=red>0.17%</font>|0.48|1|0|<font color=green>-1.96%</font>|<font color=green>-0.16%</font>|<font color=red>6.3%</font>|-2.41|10.05|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.46|0|3|<font color=green>-2.38%</font>|<font color=green>-0.08%</font>|<font color=red>6.3%</font>|-2.92|10.21|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.48|0|2|<font color=green>-2.25%</font>|<font color=red>0.01%</font>|<font color=red>6.17%</font>|-2.82|10.41|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.5|0|1|<font color=green>-1.08%</font>|<font color=red>0.05%</font>|<font color=red>5.42%</font>|-1.54|10.49|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.52|4|0|<font color=red>0.91%</font>|<font color=red>0.02%</font>|<font color=red>5.42%</font>|1.3|10.26|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.5|3|0|<font color=red>0.88%</font>|<font color=green>-0.02%</font>|<font color=red>5.42%</font>|1.26|10.49|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.48|2|0|<font color=green>-0.26%</font>|<font color=green>-0.01%</font>|<font color=red>5.42%</font>|-0.37|10.55|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.45|1|0|<font color=green>-1.04%</font>|<font color=red>0.04%</font>|<font color=red>5.42%</font>|-1.49|10.7|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.42|0|1|<font color=green>-1.47%</font>|<font color=red>0.12%</font>|<font color=red>5.42%</font>|-2.1|10.93|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.44|1|0|<font color=green>-0.2%</font>|<font color=red>0.14%</font>|<font color=red>5.2%</font>|-0.3|11.03|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.41|0|3|<font color=green>-1.24%</font>|<font color=red>0.22%</font>|<font color=red>5.2%</font>|-1.85|11.13|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.44|0|2|<font color=red>0.65%</font>|<font color=red>0.19%</font>|<font color=red>3.72%</font>|1.35|10.94|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.47|0|1|<font color=red>1.18%</font>|<font color=red>0.12%</font>|<font color=red>3.72%</font>|2.46|11.26|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.5|1|0|<font color=red>2.68%</font>|<font color=green>-0.06%</font>|<font color=red>3.72%</font>|5.58|11.23|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.46|0|2|<font color=red>2.55%</font>|<font color=green>-0.26%</font>|<font color=red>3.72%</font>|5.31|11.65|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.5|0|1|<font color=red>3.1%</font>|<font color=green>-0.54%</font>|<font color=red>3.72%</font>|6.45|12.04|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.55|2|0|<font color=red>4.18%</font>|<font color=green>-0.97%</font>|<font color=red>3.72%</font>|8.7|12.24|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.5|1|0|<font color=red>0.72%</font>|<font color=green>-1.14%</font>|<font color=red>3.72%</font>|1.5|9.89|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.44|0|1|<font color=red>0.49%</font>|<font color=green>-1.32%</font>|<font color=red>3.72%</font>|1.02|10.4|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.5|4|0|<font color=red>0.72%</font>|<font color=green>-1.57%</font>|<font color=red>3.72%</font>|1.5|11.02|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.43|3|0|<font color=red>0.0%</font>|<font color=green>-1.8%</font>|<font color=red>3.72%</font>|0.0|11.51|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.33|2|0|<font color=green>-0.62%</font>|<font color=green>-1.99%</font>|<font color=red>3.72%</font>|-1.29|12.12|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.2|1|0|<font color=green>-2.94%</font>|<font color=green>-1.8%</font>|<font color=red>3.72%</font>|-6.12|8.33|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.0|0|3|<font color=green>-3.72%</font>|<font color=green>-1.32%</font>|<font color=red>3.72%</font>|-7.74|5.77|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.0|0|2|<font color=green>-3.66%</font>|<font color=green>-0.54%</font>|<font color=red>3.66%</font>|-7.74|1.98|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.0|0|1|<font color=green>-1.63%</font>|<font color=red>0.0%</font>|<font color=red>1.63%</font>|-7.74|0.7|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
