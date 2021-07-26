---
title: 产品详情
date: 2021-07-26 21:36:58
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
- 近一个月涨跌幅：-10.28%
- 近三个月涨跌幅: -10.16%
- 近六个月涨跌幅: -2.43%

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
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-26|2.768|<font color=green>-3.22%</font>|0.47|0|2|<font color=green>-8.45%</font>|<font color=green>-0.94%</font>|<font color=red>13.44%</font>|-4.87|10.22|
|2021-07-23|2.86|<font color=green>-2.95%</font>|0.48|0|1|<font color=green>-5.67%</font>|<font color=green>-0.86%</font>|<font color=red>10.81%</font>|-4.06|9.89|
|2021-07-22|2.947|<font color=green>-2.03%</font>|0.49|2|0|<font color=green>-3.71%</font>|<font color=green>-0.8%</font>|<font color=red>10.74%</font>|-2.67|9.77|
|2021-07-21|3.008|<font color=red>0.17%</font>|0.48|1|0|<font color=green>-3.87%</font>|<font color=green>-0.75%</font>|<font color=red>10.74%</font>|-2.79|9.86|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.47|0|3|<font color=green>-4.29%</font>|<font color=green>-0.69%</font>|<font color=red>10.74%</font>|-3.09|9.93|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.48|0|2|<font color=green>-4.16%</font>|<font color=green>-0.62%</font>|<font color=red>10.74%</font>|-3.0|10.02|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.49|0|1|<font color=green>-3.01%</font>|<font color=green>-0.58%</font>|<font color=red>10.74%</font>|-2.17|10.04|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.5|4|0|<font color=green>-1.06%</font>|<font color=green>-0.57%</font>|<font color=red>10.74%</font>|-0.76|9.92|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.49|3|0|<font color=green>-1.09%</font>|<font color=green>-0.56%</font>|<font color=red>10.74%</font>|-0.79|10.02|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.48|2|0|<font color=green>-2.21%</font>|<font color=green>-0.52%</font>|<font color=red>10.74%</font>|-1.59|10.04|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.47|1|0|<font color=green>-2.98%</font>|<font color=green>-0.47%</font>|<font color=red>10.74%</font>|-2.15|10.1|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.46|0|1|<font color=green>-3.39%</font>|<font color=green>-0.41%</font>|<font color=red>10.74%</font>|-2.44|10.19|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.47|1|0|<font color=green>-2.14%</font>|<font color=green>-0.38%</font>|<font color=red>10.74%</font>|-1.54|10.2|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.46|0|3|<font color=green>-3.17%</font>|<font color=green>-0.32%</font>|<font color=red>10.74%</font>|-2.28|10.24|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.47|0|2|<font color=green>-1.31%</font>|<font color=green>-0.29%</font>|<font color=red>10.74%</font>|-0.94|10.13|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.48|0|1|<font color=green>-0.8%</font>|<font color=green>-0.28%</font>|<font color=red>10.74%</font>|-0.58|10.22|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.49|1|0|<font color=red>0.67%</font>|<font color=green>-0.3%</font>|<font color=red>10.74%</font>|0.48|10.19|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.48|0|2|<font color=red>0.54%</font>|<font color=green>-0.32%</font>|<font color=red>10.74%</font>|0.39|10.31|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.49|0|1|<font color=red>1.09%</font>|<font color=green>-0.36%</font>|<font color=red>10.74%</font>|0.79|10.41|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.5|2|0|<font color=red>2.14%</font>|<font color=green>-0.42%</font>|<font color=red>10.74%</font>|1.54|10.46|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.49|1|0|<font color=green>-1.25%</font>|<font color=green>-0.4%</font>|<font color=red>10.74%</font>|-0.9|9.71|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.47|0|1|<font color=green>-1.47%</font>|<font color=green>-0.37%</font>|<font color=red>10.74%</font>|-1.06|9.83|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.49|4|0|<font color=green>-1.25%</font>|<font color=green>-0.35%</font>|<font color=red>10.74%</font>|-0.9|9.96|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.47|3|0|<font color=green>-1.95%</font>|<font color=green>-0.3%</font>|<font color=red>10.74%</font>|-1.41|10.06|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.46|2|0|<font color=green>-2.56%</font>|<font color=green>-0.24%</font>|<font color=red>10.74%</font>|-1.84|10.16|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.44|1|0|<font color=green>-4.83%</font>|<font color=green>-0.1%</font>|<font color=red>10.74%</font>|-3.48|9.77|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.42|0|7|<font color=green>-5.6%</font>|<font color=red>0.06%</font>|<font color=red>10.74%</font>|-4.04|9.84|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.44|0|6|<font color=green>-5.54%</font>|<font color=red>0.24%</font>|<font color=red>10.68%</font>|-4.01|9.99|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.45|0|5|<font color=green>-3.55%</font>|<font color=red>0.36%</font>|<font color=red>8.81%</font>|-3.12|9.78|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.47|0|4|<font color=green>-1.95%</font>|<font color=red>0.44%</font>|<font color=red>7.29%</font>|-2.07|9.7|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.48|0|3|<font color=green>-0.51%</font>|<font color=red>0.47%</font>|<font color=red>5.93%</font>|-0.67|9.64|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.5|0|2|<font color=green>-0.13%</font>|<font color=red>0.49%</font>|<font color=red>5.57%</font>|-0.18|9.8|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.52|0|1|<font color=red>0.67%</font>|<font color=red>0.48%</font>|<font color=red>4.81%</font>|1.08|9.9|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.54|1|0|<font color=red>1.82%</font>|<font color=red>0.43%</font>|<font color=red>4.8%</font>|2.93|9.92|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.52|0|3|<font color=red>1.09%</font>|<font color=red>0.41%</font>|<font color=red>4.8%</font>|1.76|10.07|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.54|0|2|<font color=red>1.12%</font>|<font color=red>0.38%</font>|<font color=red>4.8%</font>|1.81|10.27|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.57|0|1|<font color=red>2.85%</font>|<font color=red>0.27%</font>|<font color=red>4.8%</font>|4.6|10.09|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.59|2|0|<font color=red>5.76%</font>|<font color=red>0.02%</font>|<font color=red>4.8%</font>|9.29|9.07|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.57|1|0|<font color=red>4.35%</font>|<font color=green>-0.19%</font>|<font color=red>4.8%</font>|7.01|9.1|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.55|0|1|<font color=red>2.62%</font>|<font color=green>-0.33%</font>|<font color=red>4.8%</font>|4.22|8.97|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.58|4|0|<font color=red>3.94%</font>|<font color=green>-0.55%</font>|<font color=red>4.8%</font>|6.35|8.83|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.56|3|0|<font color=red>1.95%</font>|<font color=green>-0.69%</font>|<font color=red>4.8%</font>|3.14|8.49|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.53|2|0|<font color=red>1.44%</font>|<font color=green>-0.82%</font>|<font color=red>4.8%</font>|2.32|8.71|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.5|1|0|<font color=red>0.35%</font>|<font color=green>-0.89%</font>|<font color=red>4.8%</font>|0.56|8.77|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.47|0|1|<font color=red>0.26%</font>|<font color=green>-0.96%</font>|<font color=red>4.8%</font>|0.42|9.06|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0.5|1|0|<font color=red>0.64%</font>|<font color=green>-1.08%</font>|<font color=red>4.8%</font>|1.03|9.33|
|2021-05-20|3.144|<font color=red>0.51%</font>|0.46|0|3|<font color=red>0.13%</font>|<font color=green>-1.17%</font>|<font color=red>4.8%</font>|0.21|9.63|
|2021-05-19|3.128|<font color=green>-0.6%</font>|0.5|0|2|<font color=red>0.74%</font>|<font color=green>-1.33%</font>|<font color=red>4.8%</font>|1.19|9.91|
|2021-05-18|3.147|<font color=green>-0.38%</font>|0.55|0|1|<font color=red>1.12%</font>|<font color=green>-1.55%</font>|<font color=red>4.8%</font>|1.81|10.28|
|2021-05-17|3.159|<font color=green>-0.03%</font>|0.6|5|0|<font color=red>1.15%</font>|<font color=green>-1.82%</font>|<font color=red>4.8%</font>|1.85|10.77|
|2021-05-14|3.16|<font color=red>1.94%</font>|0.56|4|0|<font color=green>-0.77%</font>|<font color=green>-1.94%</font>|<font color=red>4.8%</font>|-1.24|10.3|
|2021-05-13|3.1|<font color=red>0.94%</font>|0.5|3|0|<font color=green>-1.7%</font>|<font color=green>-1.97%</font>|<font color=red>4.8%</font>|-2.74|10.57|
|2021-05-12|3.071|<font color=red>1.55%</font>|0.43|2|0|<font color=green>-3.2%</font>|<font color=green>-1.8%</font>|<font color=red>4.8%</font>|-5.16|10.0|
|2021-05-11|3.024|<font color=red>1.27%</font>|0.33|1|0|<font color=green>-4.42%</font>|<font color=green>-1.36%</font>|<font color=red>4.8%</font>|-7.13|9.24|
|2021-05-10|2.986|<font color=red>0.4%</font>|0.2|0|4|<font color=green>-4.8%</font>|<font color=green>-0.67%</font>|<font color=red>4.8%</font>|-7.74|9.31|
|2021-05-07|2.974|<font color=green>-2.97%</font>|0.25|0|3|<font color=green>-1.89%</font>|<font color=green>-0.37%</font>|<font color=red>1.89%</font>|-7.74|4.94|
|2021-05-06|3.065|<font color=green>-1.1%</font>|0.33|0|2|<font color=green>-0.8%</font>|<font color=green>-0.22%</font>|<font color=red>0.8%</font>|-7.74|4.06|
|2021-04-30|3.099|<font color=green>-0.13%</font>|0.5|0|1|<font color=green>-0.67%</font>|<font color=red>0.0%</font>|<font color=red>0.67%</font>|-7.74|4.95|
|2021-04-29|3.103|<font color=green>-0.67%</font>|1.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-04-28|3.124|<font color=red>0.61%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
