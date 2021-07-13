---
title: 产品详情
date: 2021-07-13 20:40:42
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
- 近一个月涨跌幅：0.88%
- 近三个月涨跌幅: 7.52%
- 近六个月涨跌幅: 13.9%

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
["2021/04/20",2.968],
["2021/04/19",2.953],
["2021/04/16",2.892],
["2021/04/15",2.891],
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-13|3.09|<font color=red>1.15%</font>|0.56|2|0|<font color=red>5.67%</font>|<font color=red>6.79%</font>|<font color=red>10.74%</font>|4.09|9.75|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.55|1|0|<font color=red>4.84%</font>|<font color=red>6.82%</font>|<font color=red>10.74%</font>|3.49|9.81|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.54|0|1|<font color=red>4.39%</font>|<font color=red>6.87%</font>|<font color=red>10.74%</font>|3.16|9.89|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.55|1|0|<font color=red>5.74%</font>|<font color=red>6.89%</font>|<font color=red>10.74%</font>|4.14|9.87|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.55|0|3|<font color=red>4.64%</font>|<font color=red>6.93%</font>|<font color=red>10.74%</font>|3.34|9.91|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.56|0|2|<font color=red>6.64%</font>|<font color=red>6.93%</font>|<font color=red>10.74%</font>|4.79|9.78|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.57|0|1|<font color=red>7.19%</font>|<font color=red>6.93%</font>|<font color=red>10.74%</font>|5.18|9.85|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.58|1|0|<font color=red>8.79%</font>|<font color=red>6.89%</font>|<font color=red>10.74%</font>|6.33|9.79|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.57|0|2|<font color=red>8.65%</font>|<font color=red>6.86%</font>|<font color=red>10.74%</font>|6.23|9.88|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.58|0|1|<font color=red>9.24%</font>|<font color=red>6.81%</font>|<font color=red>10.74%</font>|6.66|9.95|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.59|2|0|<font color=red>10.38%</font>|<font color=red>6.74%</font>|<font color=red>10.74%</font>|7.48|9.95|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.58|1|0|<font color=red>6.71%</font>|<font color=red>6.74%</font>|<font color=red>10.74%</font>|4.84|9.38|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.57|0|1|<font color=red>6.47%</font>|<font color=red>6.74%</font>|<font color=red>10.74%</font>|4.66|9.48|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.59|4|0|<font color=red>6.71%</font>|<font color=red>6.74%</font>|<font color=red>10.74%</font>|4.84|9.57|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.58|3|0|<font color=red>5.95%</font>|<font color=red>6.76%</font>|<font color=red>10.74%</font>|4.29|9.65|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.57|2|0|<font color=red>5.29%</font>|<font color=red>6.79%</font>|<font color=red>10.74%</font>|3.81|9.75|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.56|1|0|<font color=red>2.84%</font>|<font color=red>6.89%</font>|<font color=red>10.74%</font>|2.05|9.48|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.55|0|7|<font color=red>2.01%</font>|<font color=red>7.0%</font>|<font color=red>10.74%</font>|1.45|9.56|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.56|0|6|<font color=red>2.08%</font>|<font color=red>7.12%</font>|<font color=red>10.68%</font>|1.51|9.67|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.57|0|5|<font color=red>4.22%</font>|<font color=red>7.19%</font>|<font color=red>8.81%</font>|3.71|9.43|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.59|0|4|<font color=red>5.95%</font>|<font color=red>7.23%</font>|<font color=red>7.29%</font>|6.32|9.29|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.61|0|3|<font color=red>7.51%</font>|<font color=red>7.22%</font>|<font color=red>5.93%</font>|9.8|9.19|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.62|0|2|<font color=red>7.92%</font>|<font color=red>7.2%</font>|<font color=red>5.57%</font>|11.01|9.28|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.64|0|1|<font color=red>8.79%</font>|<font color=red>7.16%</font>|<font color=red>4.81%</font>|14.14|9.31|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.66|1|0|<font color=red>10.03%</font>|<font color=red>7.07%</font>|<font color=red>4.8%</font>|16.17|9.26|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.65|0|3|<font color=red>9.24%</font>|<font color=red>7.01%</font>|<font color=red>4.8%</font>|14.9|9.38|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.67|0|2|<font color=red>9.27%</font>|<font color=red>6.94%</font>|<font color=red>4.8%</font>|14.95|9.51|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.69|0|1|<font color=red>11.14%</font>|<font color=red>6.81%</font>|<font color=red>4.8%</font>|17.96|9.26|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.71|2|0|<font color=red>14.29%</font>|<font color=red>6.57%</font>|<font color=red>4.8%</font>|23.04|8.33|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.7|1|0|<font color=red>12.76%</font>|<font color=red>6.36%</font>|<font color=red>4.8%</font>|20.58|8.37|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.69|0|1|<font color=red>10.9%</font>|<font color=red>6.21%</font>|<font color=red>4.8%</font>|17.58|8.31|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.71|4|0|<font color=red>12.31%</font>|<font color=red>5.99%</font>|<font color=red>4.8%</font>|19.85|8.1|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.7|3|0|<font color=red>10.17%</font>|<font color=red>5.83%</font>|<font color=red>4.8%</font>|16.4|7.92|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.69|2|0|<font color=red>9.62%</font>|<font color=red>5.69%</font>|<font color=red>4.8%</font>|15.51|8.07|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.68|1|0|<font color=red>8.44%</font>|<font color=red>5.58%</font>|<font color=red>4.8%</font>|13.61|8.15|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.67|0|1|<font color=red>8.34%</font>|<font color=red>5.46%</font>|<font color=red>4.8%</font>|13.45|8.31|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0.7|1|0|<font color=red>8.75%</font>|<font color=red>5.32%</font>|<font color=red>4.8%</font>|14.11|8.4|
|2021-05-20|3.144|<font color=red>0.51%</font>|0.68|0|3|<font color=red>8.2%</font>|<font color=red>5.19%</font>|<font color=red>4.8%</font>|13.22|8.59|
|2021-05-19|3.128|<font color=green>-0.6%</font>|0.71|0|2|<font color=red>8.86%</font>|<font color=red>5.01%</font>|<font color=red>4.8%</font>|14.29|8.63|
|2021-05-18|3.147|<font color=green>-0.38%</font>|0.75|0|1|<font color=red>9.27%</font>|<font color=red>4.8%</font>|<font color=red>4.8%</font>|14.95|8.72|
|2021-05-17|3.159|<font color=green>-0.03%</font>|0.79|5|0|<font color=red>9.3%</font>|<font color=red>4.56%</font>|<font color=red>4.8%</font>|15.0|8.9|
|2021-05-14|3.16|<font color=red>1.94%</font>|0.78|4|0|<font color=red>7.23%</font>|<font color=red>4.42%</font>|<font color=red>4.8%</font>|11.66|8.74|
|2021-05-13|3.1|<font color=red>0.94%</font>|0.76|3|0|<font color=red>6.23%</font>|<font color=red>4.31%</font>|<font color=red>4.8%</font>|10.05|8.93|
|2021-05-12|3.071|<font color=red>1.55%</font>|0.75|2|0|<font color=red>4.6%</font>|<font color=red>4.29%</font>|<font color=red>4.8%</font>|7.42|8.91|
|2021-05-11|3.024|<font color=red>1.27%</font>|0.73|1|0|<font color=red>3.29%</font>|<font color=red>4.36%</font>|<font color=red>4.8%</font>|5.31|8.99|
|2021-05-10|2.986|<font color=red>0.4%</font>|0.71|0|4|<font color=red>2.87%</font>|<font color=red>4.46%</font>|<font color=red>4.8%</font>|4.63|9.3|
|2021-05-07|2.974|<font color=green>-2.97%</font>|0.77|0|3|<font color=red>6.02%</font>|<font color=red>4.35%</font>|<font color=red>1.89%</font>|24.65|6.48|
|2021-05-06|3.065|<font color=green>-1.1%</font>|0.83|0|2|<font color=red>7.19%</font>|<font color=red>4.11%</font>|<font color=red>0.8%</font>|69.56|5.64|
|2021-04-30|3.099|<font color=green>-0.13%</font>|0.91|0|1|<font color=red>7.33%</font>|<font color=red>3.82%</font>|<font color=red>0.67%</font>|84.68|5.6|
|2021-04-29|3.103|<font color=green>-0.67%</font>|1.0|9|0|<font color=red>8.06%</font>|<font color=red>3.39%</font>|<font color=red>0%</font>|0|4.73|
|2021-04-28|3.124|<font color=red>0.61%</font>|1.0|8|0|<font color=red>7.4%</font>|<font color=red>2.95%</font>|<font color=red>0%</font>|0|4.95|
|2021-04-27|3.105|<font color=red>0.78%</font>|1.0|7|0|<font color=red>6.57%</font>|<font color=red>2.49%</font>|<font color=red>0%</font>|0|5.25|
|2021-04-26|3.081|<font color=red>0.72%</font>|1.0|6|0|<font color=red>5.81%</font>|<font color=red>2.02%</font>|<font color=red>0%</font>|0|5.59|
|2021-04-23|3.059|<font color=red>0.26%</font>|1.0|5|0|<font color=red>5.53%</font>|<font color=red>1.43%</font>|<font color=red>0%</font>|0|5.66|
|2021-04-22|3.051|<font color=red>1.7%</font>|1.0|4|0|<font color=red>3.77%</font>|<font color=red>0.97%</font>|<font color=red>0%</font>|0|5.57|
|2021-04-21|3.0|<font color=red>1.08%</font>|1.0|3|0|<font color=red>2.66%</font>|<font color=red>0.54%</font>|<font color=red>0%</font>|0|6.14|
|2021-04-20|2.968|<font color=red>0.51%</font>|1.0|2|0|<font color=red>2.14%</font>|<font color=red>0.01%</font>|<font color=red>0%</font>|0|6.95|
|2021-04-19|2.953|<font color=red>2.11%</font>|1.0|1|0|<font color=red>0.03%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|1.63|
|2021-04-16|2.892|<font color=red>0.03%</font>|1.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-04-15|2.891|<font color=red>0.45%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
