---
title: 产品详情
date: 2021-07-21 22:31:28
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
- 近一个月涨跌幅：-1.18%
- 近三个月涨跌幅: 0.27%
- 近六个月涨跌幅: 6.06%

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
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-21|3.008|<font color=red>0.17%</font>|0.51|1|0|<font color=green>-1.83%</font>|<font color=red>1.29%</font>|<font color=red>10.74%</font>|-1.32|9.67|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.5|0|3|<font color=green>-2.26%</font>|<font color=red>1.35%</font>|<font color=red>10.74%</font>|-1.63|9.74|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.51|0|2|<font color=green>-2.12%</font>|<font color=red>1.41%</font>|<font color=red>10.74%</font>|-1.53|9.83|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.52|0|1|<font color=green>-0.95%</font>|<font color=red>1.46%</font>|<font color=red>10.74%</font>|-0.68|9.84|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.53|4|0|<font color=red>1.05%</font>|<font color=red>1.46%</font>|<font color=red>10.74%</font>|0.76|9.71|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.52|3|0|<font color=red>1.01%</font>|<font color=red>1.47%</font>|<font color=red>10.74%</font>|0.73|9.8|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.51|2|0|<font color=green>-0.13%</font>|<font color=red>1.5%</font>|<font color=red>10.74%</font>|-0.09|9.82|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.5|1|0|<font color=green>-0.92%</font>|<font color=red>1.55%</font>|<font color=red>10.74%</font>|-0.66|9.88|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.49|0|1|<font color=green>-1.34%</font>|<font color=red>1.61%</font>|<font color=red>10.74%</font>|-0.97|9.96|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.5|1|0|<font color=green>-0.07%</font>|<font color=red>1.64%</font>|<font color=red>10.74%</font>|-0.05|9.96|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.49|0|3|<font color=green>-1.11%</font>|<font color=red>1.69%</font>|<font color=red>10.74%</font>|-0.8|10.0|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.5|0|2|<font color=red>0.78%</font>|<font color=red>1.71%</font>|<font color=red>10.74%</font>|0.56|9.88|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.51|0|1|<font color=red>1.31%</font>|<font color=red>1.72%</font>|<font color=red>10.74%</font>|0.94|9.96|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.52|1|0|<font color=red>2.81%</font>|<font color=red>1.7%</font>|<font color=red>10.74%</font>|2.03|9.92|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.51|0|2|<font color=red>2.68%</font>|<font color=red>1.68%</font>|<font color=red>10.74%</font>|1.93|10.03|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.52|0|1|<font color=red>3.24%</font>|<font color=red>1.64%</font>|<font color=red>10.74%</font>|2.33|10.12|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.53|2|0|<font color=red>4.32%</font>|<font color=red>1.58%</font>|<font color=red>10.74%</font>|3.11|10.15|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.52|1|0|<font color=red>0.85%</font>|<font color=red>1.6%</font>|<font color=red>10.74%</font>|0.61|9.45|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.51|0|1|<font color=red>0.62%</font>|<font color=red>1.62%</font>|<font color=red>10.74%</font>|0.45|9.56|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.53|4|0|<font color=red>0.85%</font>|<font color=red>1.64%</font>|<font color=red>10.74%</font>|0.61|9.67|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.51|3|0|<font color=red>0.13%</font>|<font color=red>1.68%</font>|<font color=red>10.74%</font>|0.09|9.76|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.5|2|0|<font color=green>-0.49%</font>|<font color=red>1.74%</font>|<font color=red>10.74%</font>|-0.35|9.85|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.49|1|0|<font color=green>-2.81%</font>|<font color=red>1.86%</font>|<font color=red>10.74%</font>|-2.03|9.5|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.47|0|7|<font color=green>-3.6%</font>|<font color=red>2.01%</font>|<font color=red>10.74%</font>|-2.59|9.56|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.49|0|6|<font color=green>-3.53%</font>|<font color=red>2.17%</font>|<font color=red>10.68%</font>|-2.56|9.7|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.5|0|5|<font color=green>-1.5%</font>|<font color=red>2.28%</font>|<font color=red>8.81%</font>|-1.32|9.48|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.52|0|4|<font color=red>0.13%</font>|<font color=red>2.34%</font>|<font color=red>7.29%</font>|0.14|9.37|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.53|0|3|<font color=red>1.6%</font>|<font color=red>2.36%</font>|<font color=red>5.93%</font>|2.09|9.29|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.55|0|2|<font color=red>1.99%</font>|<font color=red>2.38%</font>|<font color=red>5.57%</font>|2.77|9.42|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.57|0|1|<font color=red>2.81%</font>|<font color=red>2.36%</font>|<font color=red>4.81%</font>|4.52|9.49|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.59|1|0|<font color=red>3.99%</font>|<font color=red>2.31%</font>|<font color=red>4.8%</font>|6.43|9.48|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.57|0|3|<font color=red>3.24%</font>|<font color=red>2.27%</font>|<font color=red>4.8%</font>|5.22|9.61|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.59|0|2|<font color=red>3.27%</font>|<font color=red>2.24%</font>|<font color=red>4.8%</font>|5.27|9.78|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.62|0|1|<font color=red>5.03%</font>|<font color=red>2.13%</font>|<font color=red>4.8%</font>|8.11|9.57|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.64|2|0|<font color=red>8.01%</font>|<font color=red>1.89%</font>|<font color=red>4.8%</font>|12.92|8.57|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.62|1|0|<font color=red>6.57%</font>|<font color=red>1.7%</font>|<font color=red>4.8%</font>|10.59|8.58|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.61|0|1|<font color=red>4.81%</font>|<font color=red>1.56%</font>|<font color=red>4.8%</font>|7.76|8.46|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.64|4|0|<font color=red>6.15%</font>|<font color=red>1.35%</font>|<font color=red>4.8%</font>|9.92|8.28|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.62|3|0|<font color=red>4.12%</font>|<font color=red>1.22%</font>|<font color=red>4.8%</font>|6.64|7.98|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.6|2|0|<font color=red>3.6%</font>|<font color=red>1.1%</font>|<font color=red>4.8%</font>|5.81|8.16|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.58|1|0|<font color=red>2.48%</font>|<font color=red>1.03%</font>|<font color=red>4.8%</font>|4.0|8.21|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.56|0|1|<font color=red>2.39%</font>|<font color=red>0.96%</font>|<font color=red>4.8%</font>|3.85|8.44|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0.59|1|0|<font color=red>2.78%</font>|<font color=red>0.85%</font>|<font color=red>4.8%</font>|4.48|8.62|
|2021-05-20|3.144|<font color=red>0.51%</font>|0.56|0|3|<font color=red>2.26%</font>|<font color=red>0.76%</font>|<font color=red>4.8%</font>|3.64|8.86|
|2021-05-19|3.128|<font color=green>-0.6%</font>|0.6|0|2|<font color=red>2.88%</font>|<font color=red>0.62%</font>|<font color=red>4.8%</font>|4.64|9.02|
|2021-05-18|3.147|<font color=green>-0.38%</font>|0.64|0|1|<font color=red>3.27%</font>|<font color=red>0.43%</font>|<font color=red>4.8%</font>|5.27|9.25|
|2021-05-17|3.159|<font color=green>-0.03%</font>|0.69|5|0|<font color=red>3.3%</font>|<font color=red>0.21%</font>|<font color=red>4.8%</font>|5.32|9.57|
|2021-05-14|3.16|<font color=red>1.94%</font>|0.67|4|0|<font color=red>1.34%</font>|<font color=red>0.11%</font>|<font color=red>4.8%</font>|2.16|9.18|
|2021-05-13|3.1|<font color=red>0.94%</font>|0.64|3|0|<font color=red>0.39%</font>|<font color=red>0.09%</font>|<font color=red>4.8%</font>|0.63|9.39|
|2021-05-12|3.071|<font color=red>1.55%</font>|0.6|2|0|<font color=green>-1.14%</font>|<font color=red>0.21%</font>|<font color=red>4.8%</font>|-1.84|9.08|
|2021-05-11|3.024|<font color=red>1.27%</font>|0.56|1|0|<font color=green>-2.39%</font>|<font color=red>0.5%</font>|<font color=red>4.8%</font>|-3.85|8.84|
|2021-05-10|2.986|<font color=red>0.4%</font>|0.5|0|4|<font color=green>-2.78%</font>|<font color=red>0.91%</font>|<font color=red>4.8%</font>|-4.48|9.19|
|2021-05-07|2.974|<font color=green>-2.97%</font>|0.57|0|3|<font color=red>0.2%</font>|<font color=red>1.01%</font>|<font color=red>1.89%</font>|0.82|5.24|
|2021-05-06|3.065|<font color=green>-1.1%</font>|0.67|0|2|<font color=red>1.31%</font>|<font color=red>0.96%</font>|<font color=red>0.8%</font>|12.67|4.02|
|2021-04-30|3.099|<font color=green>-0.13%</font>|0.8|0|1|<font color=red>1.44%</font>|<font color=red>0.87%</font>|<font color=red>0.67%</font>|16.64|4.15|
|2021-04-29|3.103|<font color=green>-0.67%</font>|1.0|3|0|<font color=red>2.12%</font>|<font color=red>0.55%</font>|<font color=red>0%</font>|0|1.56|
|2021-04-28|3.124|<font color=red>0.61%</font>|1.0|2|0|<font color=red>1.5%</font>|<font color=red>0.24%</font>|<font color=red>0%</font>|0|1.8|
|2021-04-27|3.105|<font color=red>0.78%</font>|1.0|1|0|<font color=red>0.72%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|1.78|
|2021-04-26|3.081|<font color=red>0.72%</font>|1.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-04-23|3.059|<font color=red>0.26%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
