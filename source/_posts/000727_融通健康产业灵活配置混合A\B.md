---
title: 产品详情
date: 2021-07-08 16:40:15
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
- 近一个月涨跌幅：-3.9%
- 近三个月涨跌幅: 3.52%
- 近六个月涨跌幅: 14.8%

# 重仓股票
- 300149 创业 睿智医药
- 300406 创业 九强生物
- 300601 创业 康泰生物
- 002727 深证 一心堂
- 603883 上证 老百姓
- 002399 深证 海普瑞
- 300639 创业 凯普生物
- 
- 603658 上证 安图生物
- 002044 深证 美年健康
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
["2021/04/20",2.968],
["2021/04/19",2.953],
["2021/04/16",2.892],
["2021/04/15",2.891],
["2021/04/14",2.878],
["2021/04/13",2.874],
["2021/04/12",2.883],
["2021/04/09",2.972],
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-07|3.057|<font color=red>1.06%</font>|0.53|0|3|<font color=red>1.78%</font>|<font color=red>3.63%</font>|<font color=red>10.74%</font>|1.28|10.09|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.53|0|2|<font color=red>3.73%</font>|<font color=red>3.62%</font>|<font color=red>10.74%</font>|2.69|9.98|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.54|0|1|<font color=red>4.27%</font>|<font color=red>3.61%</font>|<font color=red>10.74%</font>|3.08|10.05|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.55|1|0|<font color=red>5.82%</font>|<font color=red>3.57%</font>|<font color=red>10.74%</font>|4.19|10.01|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.55|0|2|<font color=red>5.69%</font>|<font color=red>3.53%</font>|<font color=red>10.74%</font>|4.1|10.11|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.56|0|1|<font color=red>6.26%</font>|<font color=red>3.48%</font>|<font color=red>10.74%</font>|4.51|10.18|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.57|2|0|<font color=red>7.37%</font>|<font color=red>3.41%</font>|<font color=red>10.74%</font>|5.31|10.2|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.56|1|0|<font color=red>3.8%</font>|<font color=red>3.4%</font>|<font color=red>10.74%</font>|2.74|9.65|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.55|0|1|<font color=red>3.57%</font>|<font color=red>3.4%</font>|<font color=red>10.74%</font>|2.57|9.74|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.56|4|0|<font color=red>3.8%</font>|<font color=red>3.39%</font>|<font color=red>10.74%</font>|2.74|9.84|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.55|3|0|<font color=red>3.06%</font>|<font color=red>3.4%</font>|<font color=red>10.74%</font>|2.21|9.91|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.54|2|0|<font color=red>2.42%</font>|<font color=red>3.42%</font>|<font color=red>10.74%</font>|1.74|9.99|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.53|1|0|<font color=red>0.03%</font>|<font color=red>3.49%</font>|<font color=red>10.74%</font>|0.02|9.74|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.52|0|7|<font color=green>-0.77%</font>|<font color=red>3.58%</font>|<font color=red>10.74%</font>|-0.55|9.8|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.53|0|6|<font color=green>-0.71%</font>|<font color=red>3.68%</font>|<font color=red>10.68%</font>|-0.51|9.9|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.55|0|5|<font color=red>1.38%</font>|<font color=red>3.73%</font>|<font color=red>8.81%</font>|1.21|9.72|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.56|0|4|<font color=red>3.06%</font>|<font color=red>3.75%</font>|<font color=red>7.29%</font>|3.25|9.63|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.57|0|3|<font color=red>4.58%</font>|<font color=red>3.73%</font>|<font color=red>5.93%</font>|5.98|9.58|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.59|0|2|<font color=red>4.98%</font>|<font color=red>3.7%</font>|<font color=red>5.57%</font>|6.92|9.67|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.6|0|1|<font color=red>5.82%</font>|<font color=red>3.64%</font>|<font color=red>4.81%</font>|9.37|9.73|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.62|1|0|<font color=red>7.03%</font>|<font color=red>3.56%</font>|<font color=red>4.8%</font>|11.34|9.73|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.61|0|3|<font color=red>6.26%</font>|<font color=red>3.49%</font>|<font color=red>4.8%</font>|10.09|9.83|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.62|0|2|<font color=red>6.29%</font>|<font color=red>3.41%</font>|<font color=red>4.8%</font>|10.14|9.96|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.64|0|1|<font color=red>8.11%</font>|<font color=red>3.28%</font>|<font color=red>4.8%</font>|13.08|9.8|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.66|2|0|<font color=red>11.17%</font>|<font color=red>3.05%</font>|<font color=red>4.8%</font>|18.01|9.14|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.65|1|0|<font color=red>9.69%</font>|<font color=red>2.86%</font>|<font color=red>4.8%</font>|15.63|9.16|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.64|0|1|<font color=red>7.87%</font>|<font color=red>2.71%</font>|<font color=red>4.8%</font>|12.69|9.09|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.66|4|0|<font color=red>9.25%</font>|<font color=red>2.5%</font>|<font color=red>4.8%</font>|14.92|9.0|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.65|3|0|<font color=red>7.17%</font>|<font color=red>2.35%</font>|<font color=red>4.8%</font>|11.56|8.83|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.63|2|0|<font color=red>6.63%</font>|<font color=red>2.21%</font>|<font color=red>4.8%</font>|10.69|8.97|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.62|1|0|<font color=red>5.48%</font>|<font color=red>2.1%</font>|<font color=red>4.8%</font>|8.84|9.03|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.61|0|1|<font color=red>5.38%</font>|<font color=red>1.98%</font>|<font color=red>4.8%</font>|8.68|9.19|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0.63|1|0|<font color=red>5.79%</font>|<font color=red>1.84%</font>|<font color=red>4.8%</font>|9.34|9.32|
|2021-05-20|3.144|<font color=red>0.51%</font>|0.62|0|3|<font color=red>5.25%</font>|<font color=red>1.71%</font>|<font color=red>4.8%</font>|8.47|9.48|
|2021-05-19|3.128|<font color=green>-0.6%</font>|0.64|0|2|<font color=red>5.89%</font>|<font color=red>1.54%</font>|<font color=red>4.8%</font>|9.5|9.59|
|2021-05-18|3.147|<font color=green>-0.38%</font>|0.67|0|1|<font color=red>6.29%</font>|<font color=red>1.34%</font>|<font color=red>4.8%</font>|10.14|9.75|
|2021-05-17|3.159|<font color=green>-0.03%</font>|0.7|5|0|<font color=red>6.33%</font>|<font color=red>1.13%</font>|<font color=red>4.8%</font>|10.21|9.95|
|2021-05-14|3.16|<font color=red>1.94%</font>|0.68|4|0|<font color=red>4.31%</font>|<font color=red>0.98%</font>|<font color=red>4.8%</font>|6.95|9.76|
|2021-05-13|3.1|<font color=red>0.94%</font>|0.67|3|0|<font color=red>3.33%</font>|<font color=red>0.87%</font>|<font color=red>4.8%</font>|5.37|9.9|
|2021-05-12|3.071|<font color=red>1.55%</font>|0.65|2|0|<font color=red>1.75%</font>|<font color=red>0.82%</font>|<font color=red>4.8%</font>|2.82|9.83|
|2021-05-11|3.024|<font color=red>1.27%</font>|0.63|1|0|<font color=red>0.47%</font>|<font color=red>0.84%</font>|<font color=red>4.8%</font>|0.76|9.84|
|2021-05-10|2.986|<font color=red>0.4%</font>|0.61|0|4|<font color=red>0.07%</font>|<font color=red>0.89%</font>|<font color=red>4.8%</font>|0.11|10.08|
|2021-05-07|2.974|<font color=green>-2.97%</font>|0.65|0|3|<font color=red>3.13%</font>|<font color=red>0.75%</font>|<font color=red>3.3%</font>|7.34|8.67|
|2021-05-06|3.065|<font color=green>-1.1%</font>|0.69|0|2|<font color=red>4.27%</font>|<font color=red>0.53%</font>|<font color=red>3.3%</font>|10.02|8.59|
|2021-04-30|3.099|<font color=green>-0.13%</font>|0.73|0|1|<font color=red>4.41%</font>|<font color=red>0.28%</font>|<font color=red>3.3%</font>|10.34|8.84|
|2021-04-29|3.103|<font color=green>-0.67%</font>|0.79|11|0|<font color=red>5.11%</font>|<font color=green>-0.07%</font>|<font color=red>3.3%</font>|11.99|8.93|
|2021-04-28|3.124|<font color=red>0.61%</font>|0.77|10|0|<font color=red>4.48%</font>|<font color=green>-0.42%</font>|<font color=red>3.3%</font>|10.51|9.25|
|2021-04-27|3.105|<font color=red>0.78%</font>|0.75|9|0|<font color=red>3.67%</font>|<font color=green>-0.76%</font>|<font color=red>3.3%</font>|8.61|9.56|
|2021-04-26|3.081|<font color=red>0.72%</font>|0.73|8|0|<font color=red>2.93%</font>|<font color=green>-1.09%</font>|<font color=red>3.3%</font>|6.87|9.92|
|2021-04-23|3.059|<font color=red>0.26%</font>|0.7|7|0|<font color=red>2.66%</font>|<font color=green>-1.47%</font>|<font color=red>3.3%</font>|6.24|10.4|
|2021-04-22|3.051|<font color=red>1.7%</font>|0.67|6|0|<font color=red>0.94%</font>|<font color=green>-1.74%</font>|<font color=red>3.3%</font>|2.2|10.18|
|2021-04-21|3.0|<font color=red>1.08%</font>|0.62|5|0|<font color=green>-0.13%</font>|<font color=green>-1.94%</font>|<font color=red>3.3%</font>|-0.3|10.37|
|2021-04-20|2.968|<font color=red>0.51%</font>|0.57|4|0|<font color=green>-0.64%</font>|<font color=green>-2.12%</font>|<font color=red>3.3%</font>|-1.5|10.92|
|2021-04-19|2.953|<font color=red>2.11%</font>|0.5|3|0|<font color=green>-2.69%</font>|<font color=green>-2.03%</font>|<font color=red>3.3%</font>|-6.31|8.85|
|2021-04-16|2.892|<font color=red>0.03%</font>|0.4|2|0|<font color=green>-2.73%</font>|<font color=green>-1.89%</font>|<font color=red>3.3%</font>|-6.4|9.43|
|2021-04-15|2.891|<font color=red>0.45%</font>|0.25|1|0|<font color=green>-3.16%</font>|<font color=green>-1.57%</font>|<font color=red>3.3%</font>|-7.41|9.35|
|2021-04-14|2.878|<font color=red>0.14%</font>|0.0|0|2|<font color=green>-3.3%</font>|<font color=green>-1.0%</font>|<font color=red>3.3%</font>|-7.74|9.19|
|2021-04-13|2.874|<font color=green>-0.31%</font>|0.0|0|1|<font color=green>-2.99%</font>|<font color=red>0.0%</font>|<font color=red>2.99%</font>|-7.74|8.98|
|2021-04-12|2.883|<font color=green>-2.99%</font>|0.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-04-09|2.972|<font color=green>-0.67%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
