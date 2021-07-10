---
title: 产品详情
date: 2021-07-10 15:22:04
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
- 近一个月涨跌幅：-2.85%
- 近三个月涨跌幅: 1.99%
- 近六个月涨跌幅: 13.14%

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
        min: 100,
        max: 1,
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
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-08|3.031|<font color=red>0.43%</font>|0.54|0|1|<font color=red>5.01%</font>|<font color=red>7.24%</font>|<font color=red>10.74%</font>|3.61|9.73|
|2021-07-07|3.018|<font color=green>-1.28%</font>|0.55|1|0|<font color=red>6.37%</font>|<font color=red>7.25%</font>|<font color=red>10.74%</font>|4.59|9.71|
|2021-07-06|3.057|<font color=red>1.06%</font>|0.54|0|3|<font color=red>5.25%</font>|<font color=red>7.29%</font>|<font color=red>10.74%</font>|3.78|9.74|
|2021-07-05|3.025|<font color=green>-1.88%</font>|0.55|0|2|<font color=red>7.27%</font>|<font color=red>7.29%</font>|<font color=red>10.74%</font>|5.24|9.61|
|2021-07-04|3.083|<font color=green>-0.52%</font>|0.56|0|1|<font color=red>7.83%</font>|<font color=red>7.28%</font>|<font color=red>10.74%</font>|5.64|9.68|
|2021-07-01|3.099|<font color=green>-1.46%</font>|0.57|1|0|<font color=red>9.43%</font>|<font color=red>7.24%</font>|<font color=red>10.74%</font>|6.8|9.62|
|2021-06-30|3.145|<font color=red>0.13%</font>|0.57|0|2|<font color=red>9.29%</font>|<font color=red>7.2%</font>|<font color=red>10.74%</font>|6.7|9.71|
|2021-06-29|3.141|<font color=green>-0.54%</font>|0.58|0|1|<font color=red>9.88%</font>|<font color=red>7.15%</font>|<font color=red>10.74%</font>|7.12|9.77|
|2021-06-28|3.158|<font color=green>-1.03%</font>|0.59|2|0|<font color=red>11.03%</font>|<font color=red>7.07%</font>|<font color=red>10.74%</font>|7.95|9.77|
|2021-06-27|3.191|<font color=red>3.44%</font>|0.58|1|0|<font color=red>7.34%</font>|<font color=red>7.06%</font>|<font color=red>10.74%</font>|5.29|9.2|
|2021-06-24|3.085|<font color=red>0.23%</font>|0.57|0|1|<font color=red>7.1%</font>|<font color=red>7.06%</font>|<font color=red>10.74%</font>|5.12|9.3|
|2021-06-23|3.078|<font color=green>-0.23%</font>|0.58|4|0|<font color=red>7.34%</font>|<font color=red>7.06%</font>|<font color=red>10.74%</font>|5.29|9.38|
|2021-06-22|3.085|<font color=red>0.72%</font>|0.57|3|0|<font color=red>6.58%</font>|<font color=red>7.07%</font>|<font color=red>10.74%</font>|4.74|9.46|
|2021-06-21|3.063|<font color=red>0.62%</font>|0.57|2|0|<font color=red>5.92%</font>|<font color=red>7.09%</font>|<font color=red>10.74%</font>|4.27|9.54|
|2021-06-20|3.044|<font color=red>2.39%</font>|0.56|1|0|<font color=red>3.44%</font>|<font color=red>7.17%</font>|<font color=red>10.74%</font>|2.48|9.28|
|2021-06-17|2.973|<font color=red>0.81%</font>|0.55|0|7|<font color=red>2.61%</font>|<font color=red>7.28%</font>|<font color=red>10.74%</font>|1.88|9.35|
|2021-06-16|2.949|<font color=green>-0.07%</font>|0.56|0|6|<font color=red>2.68%</font>|<font color=red>7.38%</font>|<font color=red>10.68%</font>|1.94|9.45|
|2021-06-15|2.951|<font color=green>-2.06%</font>|0.57|0|5|<font color=red>4.84%</font>|<font color=red>7.45%</font>|<font color=red>8.81%</font>|4.25|9.22|
|2021-06-14|3.013|<font color=green>-1.63%</font>|0.59|0|4|<font color=red>6.58%</font>|<font color=red>7.47%</font>|<font color=red>7.29%</font>|6.99|9.08|
|2021-06-10|3.063|<font color=green>-1.45%</font>|0.6|0|3|<font color=red>8.14%</font>|<font color=red>7.45%</font>|<font color=red>5.93%</font>|10.62|8.98|
|2021-06-09|3.108|<font color=green>-0.38%</font>|0.62|0|2|<font color=red>8.56%</font>|<font color=red>7.42%</font>|<font color=red>5.57%</font>|11.89|9.06|
|2021-06-08|3.12|<font color=green>-0.79%</font>|0.63|0|1|<font color=red>9.43%</font>|<font color=red>7.37%</font>|<font color=red>4.81%</font>|15.17|9.09|
|2021-06-07|3.145|<font color=green>-1.13%</font>|0.65|1|0|<font color=red>10.68%</font>|<font color=red>7.28%</font>|<font color=red>4.8%</font>|17.22|9.04|
|2021-06-06|3.181|<font color=red>0.73%</font>|0.64|0|3|<font color=red>9.88%</font>|<font color=red>7.21%</font>|<font color=red>4.8%</font>|15.93|9.15|
|2021-06-03|3.158|<font color=green>-0.03%</font>|0.66|0|2|<font color=red>9.92%</font>|<font color=red>7.13%</font>|<font color=red>4.8%</font>|16.0|9.27|
|2021-06-02|3.159|<font color=green>-1.68%</font>|0.68|0|1|<font color=red>11.8%</font>|<font color=red>6.99%</font>|<font color=red>4.8%</font>|19.03|9.03|
|2021-06-01|3.213|<font color=green>-2.75%</font>|0.7|2|0|<font color=red>14.96%</font>|<font color=red>6.75%</font>|<font color=red>4.8%</font>|24.12|8.15|
|2021-05-31|3.304|<font color=red>1.35%</font>|0.69|1|0|<font color=red>13.43%</font>|<font color=red>6.54%</font>|<font color=red>4.8%</font>|21.66|8.17|
|2021-05-30|3.26|<font color=red>1.68%</font>|0.68|0|1|<font color=red>11.55%</font>|<font color=red>6.38%</font>|<font color=red>4.8%</font>|18.62|8.1|
|2021-05-27|3.206|<font color=green>-1.26%</font>|0.7|4|0|<font color=red>12.98%</font>|<font color=red>6.16%</font>|<font color=red>4.8%</font>|20.93|7.9|
|2021-05-26|3.247|<font color=red>1.95%</font>|0.69|3|0|<font color=red>10.82%</font>|<font color=red>6.0%</font>|<font color=red>4.8%</font>|17.45|7.71|
|2021-05-25|3.185|<font color=red>0.5%</font>|0.68|2|0|<font color=red>10.26%</font>|<font color=red>5.85%</font>|<font color=red>4.8%</font>|16.54|7.84|
|2021-05-24|3.169|<font color=red>1.08%</font>|0.67|1|0|<font color=red>9.08%</font>|<font color=red>5.73%</font>|<font color=red>4.8%</font>|14.64|7.91|
|2021-05-23|3.135|<font color=red>0.1%</font>|0.65|0|1|<font color=red>8.98%</font>|<font color=red>5.6%</font>|<font color=red>4.8%</font>|14.48|8.05|
|2021-05-20|3.132|<font color=green>-0.38%</font>|0.68|1|0|<font color=red>9.39%</font>|<font color=red>5.45%</font>|<font color=red>4.8%</font>|15.14|8.14|
|2021-05-19|3.144|<font color=red>0.51%</font>|0.67|0|3|<font color=red>8.84%</font>|<font color=red>5.31%</font>|<font color=red>4.8%</font>|14.25|8.3|
|2021-05-18|3.128|<font color=green>-0.6%</font>|0.7|0|2|<font color=red>9.5%</font>|<font color=red>5.13%</font>|<font color=red>4.8%</font>|15.32|8.34|
|2021-05-17|3.147|<font color=green>-0.38%</font>|0.73|0|1|<font color=red>9.92%</font>|<font color=red>4.91%</font>|<font color=red>4.8%</font>|16.0|8.42|
|2021-05-16|3.159|<font color=green>-0.03%</font>|0.76|5|0|<font color=red>9.95%</font>|<font color=red>4.67%</font>|<font color=red>4.8%</font>|16.04|8.59|
|2021-05-13|3.16|<font color=red>1.94%</font>|0.75|4|0|<font color=red>7.86%</font>|<font color=red>4.51%</font>|<font color=red>4.8%</font>|12.67|8.39|
|2021-05-12|3.1|<font color=red>0.94%</font>|0.74|3|0|<font color=red>6.85%</font>|<font color=red>4.39%</font>|<font color=red>4.8%</font>|11.05|8.54|
|2021-05-11|3.071|<font color=red>1.55%</font>|0.72|2|0|<font color=red>5.22%</font>|<font color=red>4.34%</font>|<font color=red>4.8%</font>|8.42|8.48|
|2021-05-10|3.024|<font color=red>1.27%</font>|0.71|1|0|<font color=red>3.9%</font>|<font color=red>4.37%</font>|<font color=red>4.8%</font>|6.29|8.51|
|2021-05-09|2.986|<font color=red>0.4%</font>|0.69|0|4|<font color=red>3.48%</font>|<font color=red>4.42%</font>|<font color=red>4.8%</font>|5.61|8.76|
|2021-05-06|2.974|<font color=green>-2.97%</font>|0.73|0|3|<font color=red>6.65%</font>|<font color=red>4.27%</font>|<font color=red>1.89%</font>|27.23|6.25|
|2021-05-05|3.065|<font color=green>-1.1%</font>|0.79|0|2|<font color=red>7.83%</font>|<font color=red>4.02%</font>|<font color=red>0.8%</font>|75.76|5.6|
|2021-04-29|3.099|<font color=green>-0.13%</font>|0.85|0|1|<font color=red>7.97%</font>|<font color=red>3.72%</font>|<font color=red>0.67%</font>|92.07|5.63|
|2021-04-28|3.103|<font color=green>-0.67%</font>|0.92|11|0|<font color=red>8.7%</font>|<font color=red>3.3%</font>|<font color=red>0%</font>|0|5.1|
|2021-04-27|3.124|<font color=red>0.61%</font>|0.91|10|0|<font color=red>8.04%</font>|<font color=red>2.87%</font>|<font color=red>0%</font>|0|5.33|
|2021-04-26|3.105|<font color=red>0.78%</font>|0.9|9|0|<font color=red>7.2%</font>|<font color=red>2.44%</font>|<font color=red>0%</font>|0|5.58|
|2021-04-25|3.081|<font color=red>0.72%</font>|0.89|8|0|<font color=red>6.44%</font>|<font color=red>1.99%</font>|<font color=red>0%</font>|0|5.88|
|2021-04-22|3.059|<font color=red>0.26%</font>|0.88|7|0|<font color=red>6.16%</font>|<font color=red>1.47%</font>|<font color=red>0%</font>|0|6.13|
|2021-04-21|3.051|<font color=red>1.7%</font>|0.86|6|0|<font color=red>4.38%</font>|<font color=red>1.05%</font>|<font color=red>0%</font>|0|5.78|
|2021-04-20|3.0|<font color=red>1.08%</font>|0.83|5|0|<font color=red>3.27%</font>|<font color=red>0.68%</font>|<font color=red>0%</font>|0|6.0|
|2021-04-19|2.968|<font color=red>0.51%</font>|0.8|4|0|<font color=red>2.75%</font>|<font color=red>0.27%</font>|<font color=red>0%</font>|0|6.57|
|2021-04-18|2.953|<font color=red>2.11%</font>|0.75|3|0|<font color=red>0.63%</font>|<font color=red>0.18%</font>|<font color=red>0%</font>|0|2.1|
|2021-04-15|2.892|<font color=red>0.03%</font>|0.67|2|0|<font color=red>0.59%</font>|<font color=red>0.05%</font>|<font color=red>0%</font>|0|2.42|
|2021-04-14|2.891|<font color=red>0.45%</font>|0.5|1|0|<font color=red>0.14%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|1.74|
|2021-04-13|2.878|<font color=red>0.14%</font>|0.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-04-12|2.874|<font color=green>-0.31%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
