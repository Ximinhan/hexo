---
title: 产品详情
date: 2021-07-20 16:00:34
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
- 近一个月涨跌幅：0.57%
- 近三个月涨跌幅: 1.25%
- 近六个月涨跌幅: 7.44%

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
["2021/06/10",3.108],
["2021/06/09",3.12],
["2021/06/08",3.145],
["2021/06/07",3.181],
["2021/06/04",3.158],
["2021/06/03",3.159],
["2021/06/02",3.213],
["2021/06/01",3.304],
["2021/05/31",3.26],
["2021/05/28",3.206],
["2021/05/27",3.247],
["2021/05/26",3.185],
["2021/05/25",3.169],
["2021/05/24",3.135],
["2021/05/21",3.132],
["2021/05/20",3.144],
["2021/05/19",3.128],
["2021/05/18",3.147],
["2021/05/17",3.159],
["2021/05/14",3.16],
["2021/05/13",3.1],
["2021/05/12",3.071],
["2021/05/11",3.024],
["2021/05/10",2.986],
["2021/05/07",2.974],
["2021/05/06",3.065],
["2021/04/30",3.099],
["2021/04/29",3.103],
["2021/04/28",3.124],
["2021/04/27",3.105],
["2021/04/26",3.081],
["2021/04/23",3.059],
["2021/04/22",3.051],
["2021/04/21",3.0],
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.53|0|2|<font color=green>-0.2%</font>|<font color=red>3.29%</font>|<font color=red>10.74%</font>|-0.14|9.87|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.53|0|1|<font color=red>1.0%</font>|<font color=red>3.33%</font>|<font color=red>10.74%</font>|0.72|9.88|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.54|4|0|<font color=red>3.03%</font>|<font color=red>3.33%</font>|<font color=red>10.74%</font>|2.18|9.74|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.54|3|0|<font color=red>3.0%</font>|<font color=red>3.34%</font>|<font color=red>10.74%</font>|2.16|9.83|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.53|2|0|<font color=red>1.83%</font>|<font color=red>3.37%</font>|<font color=red>10.74%</font>|1.32|9.86|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.52|1|0|<font color=red>1.03%</font>|<font color=red>3.41%</font>|<font color=red>10.74%</font>|0.74|9.92|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.51|0|1|<font color=red>0.6%</font>|<font color=red>3.46%</font>|<font color=red>10.74%</font>|0.43|10.0|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.52|1|0|<font color=red>1.9%</font>|<font color=red>3.49%</font>|<font color=red>10.74%</font>|1.37|9.99|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.51|0|3|<font color=red>0.83%</font>|<font color=red>3.54%</font>|<font color=red>10.74%</font>|0.6|10.03|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.52|0|2|<font color=red>2.77%</font>|<font color=red>3.56%</font>|<font color=red>10.74%</font>|2.0|9.91|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.53|0|1|<font color=red>3.3%</font>|<font color=red>3.57%</font>|<font color=red>10.74%</font>|2.38|9.98|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.54|1|0|<font color=red>4.83%</font>|<font color=red>3.54%</font>|<font color=red>10.74%</font>|3.48|9.93|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.53|0|2|<font color=red>4.7%</font>|<font color=red>3.51%</font>|<font color=red>10.74%</font>|3.39|10.04|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.54|0|1|<font color=red>5.27%</font>|<font color=red>3.48%</font>|<font color=red>10.74%</font>|3.8|10.12|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.56|2|0|<font color=red>6.37%</font>|<font color=red>3.41%</font>|<font color=red>10.74%</font>|4.59|10.14|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.55|1|0|<font color=red>2.83%</font>|<font color=red>3.42%</font>|<font color=red>10.74%</font>|2.04|9.5|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.53|0|1|<font color=red>2.6%</font>|<font color=red>3.44%</font>|<font color=red>10.74%</font>|1.87|9.61|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.55|4|0|<font color=red>2.83%</font>|<font color=red>3.46%</font>|<font color=red>10.74%</font>|2.04|9.71|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.54|3|0|<font color=red>2.1%</font>|<font color=red>3.49%</font>|<font color=red>10.74%</font>|1.51|9.8|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.53|2|0|<font color=red>1.47%</font>|<font color=red>3.54%</font>|<font color=red>10.74%</font>|1.06|9.9|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.51|1|0|<font color=green>-0.9%</font>|<font color=red>3.66%</font>|<font color=red>10.74%</font>|-0.65|9.6|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.5|0|7|<font color=green>-1.7%</font>|<font color=red>3.8%</font>|<font color=red>10.74%</font>|-1.23|9.67|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.51|0|6|<font color=green>-1.63%</font>|<font color=red>3.94%</font>|<font color=red>10.68%</font>|-1.18|9.8|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.53|0|5|<font color=red>0.43%</font>|<font color=red>4.04%</font>|<font color=red>8.81%</font>|0.38|9.56|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.54|0|4|<font color=red>2.1%</font>|<font color=red>4.1%</font>|<font color=red>7.29%</font>|2.23|9.44|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.56|0|3|<font color=red>3.6%</font>|<font color=red>4.11%</font>|<font color=red>5.93%</font>|4.7|9.35|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.58|0|2|<font color=red>4.0%</font>|<font color=red>4.11%</font>|<font color=red>5.57%</font>|5.56|9.46|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.59|0|1|<font color=red>4.83%</font>|<font color=red>4.09%</font>|<font color=red>4.81%</font>|7.77|9.52|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.61|1|0|<font color=red>6.03%</font>|<font color=red>4.03%</font>|<font color=red>4.8%</font>|9.72|9.49|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.6|0|3|<font color=red>5.27%</font>|<font color=red>3.99%</font>|<font color=red>4.8%</font>|8.5|9.62|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.62|0|2|<font color=red>5.3%</font>|<font color=red>3.94%</font>|<font color=red>4.8%</font>|8.55|9.78|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.64|0|1|<font color=red>7.1%</font>|<font color=red>3.83%</font>|<font color=red>4.8%</font>|11.45|9.54|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.67|2|0|<font color=red>10.13%</font>|<font color=red>3.6%</font>|<font color=red>4.8%</font>|16.33|8.55|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.65|1|0|<font color=red>8.67%</font>|<font color=red>3.4%</font>|<font color=red>4.8%</font>|13.98|8.58|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.64|0|1|<font color=red>6.87%</font>|<font color=red>3.26%</font>|<font color=red>4.8%</font>|11.08|8.51|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.67|4|0|<font color=red>8.23%</font>|<font color=red>3.06%</font>|<font color=red>4.8%</font>|13.27|8.3|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.65|3|0|<font color=red>6.17%</font>|<font color=red>2.92%</font>|<font color=red>4.8%</font>|9.95|8.08|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.64|2|0|<font color=red>5.63%</font>|<font color=red>2.8%</font>|<font color=red>4.8%</font>|9.08|8.25|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.62|1|0|<font color=red>4.5%</font>|<font color=red>2.72%</font>|<font color=red>4.8%</font>|7.26|8.34|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.6|0|1|<font color=red>4.4%</font>|<font color=red>2.63%</font>|<font color=red>4.8%</font>|7.1|8.54|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0.63|1|0|<font color=red>4.8%</font>|<font color=red>2.52%</font>|<font color=red>4.8%</font>|7.74|8.68|
|2021-05-20|3.144|<font color=red>0.51%</font>|0.61|0|3|<font color=red>4.27%</font>|<font color=red>2.42%</font>|<font color=red>4.8%</font>|6.89|8.91|
|2021-05-19|3.128|<font color=green>-0.6%</font>|0.65|0|2|<font color=red>4.9%</font>|<font color=red>2.28%</font>|<font color=red>4.8%</font>|7.9|9.0|
|2021-05-18|3.147|<font color=green>-0.38%</font>|0.69|0|1|<font color=red>5.3%</font>|<font color=red>2.09%</font>|<font color=red>4.8%</font>|8.55|9.16|
|2021-05-17|3.159|<font color=green>-0.03%</font>|0.73|5|0|<font color=red>5.33%</font>|<font color=red>1.87%</font>|<font color=red>4.8%</font>|8.59|9.42|
|2021-05-14|3.16|<font color=red>1.94%</font>|0.71|4|0|<font color=red>3.33%</font>|<font color=red>1.77%</font>|<font color=red>4.8%</font>|5.37|9.2|
|2021-05-13|3.1|<font color=red>0.94%</font>|0.69|3|0|<font color=red>2.37%</font>|<font color=red>1.72%</font>|<font color=red>4.8%</font>|3.82|9.44|
|2021-05-12|3.071|<font color=red>1.55%</font>|0.67|2|0|<font color=red>0.8%</font>|<font color=red>1.8%</font>|<font color=red>4.8%</font>|1.29|9.37|
|2021-05-11|3.024|<font color=red>1.27%</font>|0.64|1|0|<font color=green>-0.47%</font>|<font color=red>2.0%</font>|<font color=red>4.8%</font>|-0.76|9.4|
|2021-05-10|2.986|<font color=red>0.4%</font>|0.6|0|4|<font color=green>-0.87%</font>|<font color=red>2.29%</font>|<font color=red>4.8%</font>|-1.4|9.82|
|2021-05-07|2.974|<font color=green>-2.97%</font>|0.67|0|3|<font color=red>2.17%</font>|<font color=red>2.3%</font>|<font color=red>1.89%</font>|8.89|6.39|
|2021-05-06|3.065|<font color=green>-1.1%</font>|0.75|0|2|<font color=red>3.3%</font>|<font color=red>2.18%</font>|<font color=red>0.8%</font>|31.93|5.28|
|2021-04-30|3.099|<font color=green>-0.13%</font>|0.86|0|1|<font color=red>3.43%</font>|<font color=red>2.0%</font>|<font color=red>0.67%</font>|39.62|5.24|
|2021-04-29|3.103|<font color=green>-0.67%</font>|1.0|5|0|<font color=red>4.13%</font>|<font color=red>1.65%</font>|<font color=red>0%</font>|0|3.47|
|2021-04-28|3.124|<font color=red>0.61%</font>|1.0|4|0|<font color=red>3.5%</font>|<font color=red>1.27%</font>|<font color=red>0%</font>|0|3.68|
|2021-04-27|3.105|<font color=red>0.78%</font>|1.0|3|0|<font color=red>2.7%</font>|<font color=red>0.92%</font>|<font color=red>0%</font>|0|4.07|
|2021-04-26|3.081|<font color=red>0.72%</font>|1.0|2|0|<font color=red>1.97%</font>|<font color=red>0.57%</font>|<font color=red>0%</font>|0|4.56|
|2021-04-23|3.059|<font color=red>0.26%</font>|1.0|1|0|<font color=red>1.7%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|2.4|
|2021-04-22|3.051|<font color=red>1.7%</font>|1.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-04-21|3.0|<font color=red>1.08%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
