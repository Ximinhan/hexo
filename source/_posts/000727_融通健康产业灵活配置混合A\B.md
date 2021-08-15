---
title: 产品详情
date: 2021-08-15 15:53:31
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
- 近一个月涨跌幅：-5.95%
- 近三个月涨跌幅: -6.26%
- 近六个月涨跌幅: -4.56%

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
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-08-13|2.906|<font color=red>0.87%</font>|0.46|0|2|<font color=green>-8.01%</font>|<font color=green>-3.3%</font>|<font color=red>18.89%</font>|-3.28|12.24|
|2021-08-12|2.881|<font color=green>-0.93%</font>|0.47|0|1|<font color=green>-7.15%</font>|<font color=green>-3.23%</font>|<font color=red>18.89%</font>|-2.93|12.32|
|2021-08-11|2.908|<font color=green>-1.05%</font>|0.47|2|0|<font color=green>-6.16%</font>|<font color=green>-3.18%</font>|<font color=red>18.89%</font>|-2.52|12.39|
|2021-08-10|2.939|<font color=red>2.12%</font>|0.46|1|0|<font color=green>-8.11%</font>|<font color=green>-3.09%</font>|<font color=red>18.89%</font>|-3.32|12.28|
|2021-08-09|2.878|<font color=red>3.23%</font>|0.45|0|3|<font color=green>-10.98%</font>|<font color=green>-2.95%</font>|<font color=red>18.89%</font>|-4.5|11.87|
|2021-08-06|2.788|<font color=green>-2.35%</font>|0.46|0|2|<font color=green>-8.84%</font>|<font color=green>-2.84%</font>|<font color=red>18.89%</font>|-3.62|11.76|
|2021-08-05|2.855|<font color=green>-0.73%</font>|0.47|0|1|<font color=green>-8.17%</font>|<font color=green>-2.74%</font>|<font color=red>18.89%</font>|-3.35|11.86|
|2021-08-04|2.876|<font color=green>-0.9%</font>|0.48|4|0|<font color=green>-7.34%</font>|<font color=green>-2.65%</font>|<font color=red>18.89%</font>|-3.01|11.95|
|2021-08-03|2.902|<font color=red>4.16%</font>|0.47|3|0|<font color=green>-11.05%</font>|<font color=green>-2.49%</font>|<font color=red>18.89%</font>|-4.53|11.11|
|2021-08-02|2.786|<font color=red>1.46%</font>|0.46|2|0|<font color=green>-12.32%</font>|<font color=green>-2.29%</font>|<font color=red>18.89%</font>|-5.05|11.06|
|2021-07-30|2.746|<font color=red>1.63%</font>|0.45|1|0|<font color=green>-13.73%</font>|<font color=green>-2.06%</font>|<font color=red>18.89%</font>|-5.63|10.97|
|2021-07-29|2.702|<font color=red>0.82%</font>|0.44|0|5|<font color=green>-14.43%</font>|<font color=green>-1.8%</font>|<font color=red>18.89%</font>|-5.91|11.01|
|2021-07-28|2.68|<font color=green>-0.3%</font>|0.45|0|4|<font color=green>-14.18%</font>|<font color=green>-1.54%</font>|<font color=red>18.64%</font>|-5.89|11.13|
|2021-07-27|2.688|<font color=green>-2.89%</font>|0.46|0|3|<font color=green>-11.62%</font>|<font color=green>-1.32%</font>|<font color=red>16.22%</font>|-5.54|10.85|
|2021-07-26|2.768|<font color=green>-3.22%</font>|0.47|0|2|<font color=green>-8.68%</font>|<font color=green>-1.15%</font>|<font color=red>13.44%</font>|-5.0|10.42|
|2021-07-23|2.86|<font color=green>-2.95%</font>|0.48|0|1|<font color=green>-5.91%</font>|<font color=green>-1.05%</font>|<font color=red>10.81%</font>|-4.23|10.02|
|2021-07-22|2.947|<font color=green>-2.03%</font>|0.49|2|0|<font color=green>-3.96%</font>|<font color=green>-0.98%</font>|<font color=red>10.74%</font>|-2.85|9.88|
|2021-07-21|3.008|<font color=red>0.17%</font>|0.48|1|0|<font color=green>-4.12%</font>|<font color=green>-0.9%</font>|<font color=red>10.74%</font>|-2.97|10.0|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.46|0|3|<font color=green>-4.53%</font>|<font color=green>-0.81%</font>|<font color=red>10.74%</font>|-3.26|10.1|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.47|0|2|<font color=green>-4.41%</font>|<font color=green>-0.72%</font>|<font color=red>10.74%</font>|-3.18|10.22|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.49|0|1|<font color=green>-3.26%</font>|<font color=green>-0.66%</font>|<font color=red>10.74%</font>|-2.35|10.26|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.5|4|0|<font color=green>-1.31%</font>|<font color=green>-0.64%</font>|<font color=red>10.74%</font>|-0.94|10.12|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.49|3|0|<font color=green>-1.34%</font>|<font color=green>-0.62%</font>|<font color=red>10.74%</font>|-0.97|10.25|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.47|2|0|<font color=green>-2.46%</font>|<font color=green>-0.57%</font>|<font color=red>10.74%</font>|-1.77|10.28|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.46|1|0|<font color=green>-3.22%</font>|<font color=green>-0.5%</font>|<font color=red>10.74%</font>|-2.32|10.36|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.44|0|1|<font color=green>-3.64%</font>|<font color=green>-0.4%</font>|<font color=red>10.74%</font>|-2.62|10.49|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.45|1|0|<font color=green>-2.39%</font>|<font color=green>-0.34%</font>|<font color=red>10.74%</font>|-1.72|10.53|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.44|0|3|<font color=green>-3.42%</font>|<font color=green>-0.25%</font>|<font color=red>10.74%</font>|-2.46|10.57|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.45|0|2|<font color=green>-1.56%</font>|<font color=green>-0.21%</font>|<font color=red>10.74%</font>|-1.12|10.45|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.47|0|1|<font color=green>-1.05%</font>|<font color=green>-0.18%</font>|<font color=red>10.74%</font>|-0.76|10.6|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.48|1|0|<font color=red>0.42%</font>|<font color=green>-0.2%</font>|<font color=red>10.74%</font>|0.3|10.58|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.46|0|2|<font color=red>0.29%</font>|<font color=green>-0.22%</font>|<font color=red>10.74%</font>|0.21|10.76|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.48|0|1|<font color=red>0.83%</font>|<font color=green>-0.25%</font>|<font color=red>10.74%</font>|0.6|10.93|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.5|2|0|<font color=red>1.88%</font>|<font color=green>-0.34%</font>|<font color=red>10.74%</font>|1.35|11.02|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.48|1|0|<font color=green>-1.5%</font>|<font color=green>-0.29%</font>|<font color=red>10.74%</font>|-1.08|9.89|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.46|0|1|<font color=green>-1.72%</font>|<font color=green>-0.23%</font>|<font color=red>10.74%</font>|-1.24|10.09|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.48|4|0|<font color=green>-1.5%</font>|<font color=green>-0.17%</font>|<font color=red>10.74%</font>|-1.08|10.3|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.45|3|0|<font color=green>-2.2%</font>|<font color=green>-0.08%</font>|<font color=red>10.74%</font>|-1.59|10.45|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.43|2|0|<font color=green>-2.81%</font>|<font color=red>0.05%</font>|<font color=red>10.74%</font>|-2.03|10.62|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.4|1|0|<font color=green>-5.08%</font>|<font color=red>0.3%</font>|<font color=red>10.74%</font>|-3.66|9.91|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.37|0|7|<font color=green>-5.84%</font>|<font color=red>0.63%</font>|<font color=red>10.74%</font>|-4.21|9.97|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.39|0|6|<font color=green>-5.78%</font>|<font color=red>0.98%</font>|<font color=red>10.68%</font>|-4.19|10.23|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.41|0|5|<font color=green>-3.8%</font>|<font color=red>1.26%</font>|<font color=red>8.81%</font>|-3.34|9.99|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.44|0|4|<font color=green>-2.2%</font>|<font color=red>1.48%</font>|<font color=red>7.29%</font>|-2.34|9.92|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.47|0|3|<font color=green>-0.77%</font>|<font color=red>1.63%</font>|<font color=red>5.93%</font>|-1.01|9.89|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.5|0|2|<font color=green>-0.38%</font>|<font color=red>1.77%</font>|<font color=red>5.57%</font>|-0.53|10.22|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.54|0|1|<font color=red>0.42%</font>|<font color=red>1.88%</font>|<font color=red>4.81%</font>|0.68|10.47|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.58|1|0|<font color=red>1.56%</font>|<font color=red>1.9%</font>|<font color=red>4.42%</font>|2.73|10.57|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.55|0|3|<font color=red>0.83%</font>|<font color=red>2.0%</font>|<font color=red>4.42%</font>|1.45|10.94|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.6|0|2|<font color=red>0.86%</font>|<font color=red>2.12%</font>|<font color=red>4.39%</font>|1.52|11.47|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.67|0|1|<font color=red>2.59%</font>|<font color=red>2.06%</font>|<font color=red>2.75%</font>|7.29|11.13|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.75|2|0|<font color=red>5.49%</font>|<font color=red>1.64%</font>|<font color=red>1.26%</font>|33.72|7.96|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.71|1|0|<font color=red>4.09%</font>|<font color=red>1.29%</font>|<font color=red>1.26%</font>|25.12|8.2|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.67|0|1|<font color=red>2.36%</font>|<font color=red>1.11%</font>|<font color=red>1.26%</font>|14.5|7.93|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.8|4|0|<font color=red>3.67%</font>|<font color=red>0.59%</font>|<font color=red>0%</font>|0|6.25|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.75|3|0|<font color=red>1.69%</font>|<font color=red>0.32%</font>|<font color=red>0%</font>|0|4.15|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.67|2|0|<font color=red>1.18%</font>|<font color=red>0.03%</font>|<font color=red>0%</font>|0|4.7|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.5|1|0|<font color=red>0.1%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|1.86|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
