---
title: 产品详情
date: 2021-08-22 15:22:13
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
- 近一个月涨跌幅：-6.43%
- 近三个月涨跌幅: -10.62%
- 近六个月涨跌幅: -9.94%

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
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-08-20|2.81|<font color=green>-2.94%</font>|0.44|0|1|<font color=green>-9.7%</font>|<font color=green>-6.21%</font>|<font color=red>18.89%</font>|-3.97|12.43|
|2021-08-19|2.895|<font color=green>-0.69%</font>|0.45|1|0|<font color=green>-9.08%</font>|<font color=green>-6.16%</font>|<font color=red>18.89%</font>|-3.72|12.52|
|2021-08-18|2.915|<font color=red>1.6%</font>|0.44|0|1|<font color=green>-10.51%</font>|<font color=green>-6.09%</font>|<font color=red>18.89%</font>|-4.31|12.5|
|2021-08-17|2.869|<font color=green>-2.38%</font>|0.45|2|0|<font color=green>-8.33%</font>|<font color=green>-6.05%</font>|<font color=red>18.89%</font>|-3.41|12.4|
|2021-08-16|2.939|<font color=red>1.14%</font>|0.44|1|0|<font color=green>-9.36%</font>|<font color=green>-5.99%</font>|<font color=red>18.89%</font>|-3.84|12.44|
|2021-08-13|2.906|<font color=red>0.87%</font>|0.43|0|2|<font color=green>-10.14%</font>|<font color=green>-5.91%</font>|<font color=red>18.89%</font>|-4.15|12.51|
|2021-08-12|2.881|<font color=green>-0.93%</font>|0.43|0|1|<font color=green>-9.3%</font>|<font color=green>-5.84%</font>|<font color=red>18.89%</font>|-3.81|12.6|
|2021-08-11|2.908|<font color=green>-1.05%</font>|0.44|2|0|<font color=green>-8.33%</font>|<font color=green>-5.8%</font>|<font color=red>18.89%</font>|-3.41|12.69|
|2021-08-10|2.939|<font color=red>2.12%</font>|0.43|1|0|<font color=green>-10.23%</font>|<font color=green>-5.71%</font>|<font color=red>18.89%</font>|-4.19|12.56|
|2021-08-09|2.878|<font color=red>3.23%</font>|0.42|0|3|<font color=green>-13.04%</font>|<font color=green>-5.56%</font>|<font color=red>18.89%</font>|-5.34|12.1|
|2021-08-06|2.788|<font color=green>-2.35%</font>|0.43|0|2|<font color=green>-10.95%</font>|<font color=green>-5.45%</font>|<font color=red>18.89%</font>|-4.49|12.0|
|2021-08-05|2.855|<font color=green>-0.73%</font>|0.44|0|1|<font color=green>-10.29%</font>|<font color=green>-5.35%</font>|<font color=red>18.89%</font>|-4.22|12.11|
|2021-08-04|2.876|<font color=green>-0.9%</font>|0.45|4|0|<font color=green>-9.48%</font>|<font color=green>-5.26%</font>|<font color=red>18.89%</font>|-3.88|12.22|
|2021-08-03|2.902|<font color=red>4.16%</font>|0.43|3|0|<font color=green>-13.1%</font>|<font color=green>-5.09%</font>|<font color=red>18.89%</font>|-5.37|11.27|
|2021-08-02|2.786|<font color=red>1.46%</font>|0.42|2|0|<font color=green>-14.35%</font>|<font color=green>-4.89%</font>|<font color=red>18.89%</font>|-5.88|11.2|
|2021-07-30|2.746|<font color=red>1.63%</font>|0.41|1|0|<font color=green>-15.72%</font>|<font color=green>-4.64%</font>|<font color=red>18.89%</font>|-6.44|11.08|
|2021-07-29|2.702|<font color=red>0.82%</font>|0.4|0|5|<font color=green>-16.41%</font>|<font color=green>-4.37%</font>|<font color=red>18.89%</font>|-6.72|11.11|
|2021-07-28|2.68|<font color=green>-0.3%</font>|0.4|0|4|<font color=green>-16.16%</font>|<font color=green>-4.09%</font>|<font color=red>18.64%</font>|-6.71|11.24|
|2021-07-27|2.688|<font color=green>-2.89%</font>|0.41|0|3|<font color=green>-13.66%</font>|<font color=green>-3.85%</font>|<font color=red>16.22%</font>|-6.52|10.98|
|2021-07-26|2.768|<font color=green>-3.22%</font>|0.42|0|2|<font color=green>-10.79%</font>|<font color=green>-3.68%</font>|<font color=red>13.44%</font>|-6.21|10.54|
|2021-07-23|2.86|<font color=green>-2.95%</font>|0.44|0|1|<font color=green>-8.08%</font>|<font color=green>-3.57%</font>|<font color=red>10.81%</font>|-5.79|10.15|
|2021-07-22|2.947|<font color=green>-2.03%</font>|0.45|2|0|<font color=green>-6.18%</font>|<font color=green>-3.5%</font>|<font color=red>10.74%</font>|-4.45|10.02|
|2021-07-21|3.008|<font color=red>0.17%</font>|0.43|1|0|<font color=green>-6.33%</font>|<font color=green>-3.42%</font>|<font color=red>10.74%</font>|-4.56|10.15|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.42|0|3|<font color=green>-6.74%</font>|<font color=green>-3.33%</font>|<font color=red>10.74%</font>|-4.86|10.25|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.43|0|2|<font color=green>-6.61%</font>|<font color=green>-3.24%</font>|<font color=red>10.74%</font>|-4.76|10.4|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.44|0|1|<font color=green>-5.49%</font>|<font color=green>-3.17%</font>|<font color=red>10.74%</font>|-3.96|10.47|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.45|4|0|<font color=green>-3.59%</font>|<font color=green>-3.16%</font>|<font color=red>10.74%</font>|-2.59|10.35|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.44|3|0|<font color=green>-3.62%</font>|<font color=green>-3.14%</font>|<font color=red>10.74%</font>|-2.61|10.5|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.42|2|0|<font color=green>-4.71%</font>|<font color=green>-3.09%</font>|<font color=red>10.74%</font>|-3.39|10.51|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.4|1|0|<font color=green>-5.46%</font>|<font color=green>-3.01%</font>|<font color=red>10.74%</font>|-3.93|10.6|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.38|0|1|<font color=green>-5.86%</font>|<font color=green>-2.92%</font>|<font color=red>10.74%</font>|-4.22|10.74|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.39|1|0|<font color=green>-4.65%</font>|<font color=green>-2.85%</font>|<font color=red>10.74%</font>|-3.35|10.82|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.37|0|3|<font color=green>-5.65%</font>|<font color=green>-2.75%</font>|<font color=red>10.74%</font>|-4.07|10.85|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.38|0|2|<font color=green>-3.84%</font>|<font color=green>-2.71%</font>|<font color=red>10.74%</font>|-2.77|10.76|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.4|0|1|<font color=green>-3.34%</font>|<font color=green>-2.68%</font>|<font color=red>10.74%</font>|-2.41|10.96|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.42|1|0|<font color=green>-1.9%</font>|<font color=green>-2.72%</font>|<font color=red>10.74%</font>|-1.37|10.99|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.39|0|2|<font color=green>-2.03%</font>|<font color=green>-2.75%</font>|<font color=red>10.74%</font>|-1.46|11.22|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.41|0|1|<font color=green>-1.5%</font>|<font color=green>-2.8%</font>|<font color=red>10.74%</font>|-1.08|11.46|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.43|2|0|<font color=green>-0.47%</font>|<font color=green>-2.91%</font>|<font color=red>10.74%</font>|-0.34|11.62|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.4|1|0|<font color=green>-3.77%</font>|<font color=green>-2.87%</font>|<font color=red>10.74%</font>|-2.72|10.15|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.37|0|1|<font color=green>-3.99%</font>|<font color=green>-2.81%</font>|<font color=red>10.74%</font>|-2.88|10.37|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.39|4|0|<font color=green>-3.77%</font>|<font color=green>-2.76%</font>|<font color=red>10.74%</font>|-2.72|10.66|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.35|3|0|<font color=green>-4.46%</font>|<font color=green>-2.66%</font>|<font color=red>10.74%</font>|-3.21|10.8|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.31|2|0|<font color=green>-5.05%</font>|<font color=green>-2.51%</font>|<font color=red>10.74%</font>|-3.64|10.97|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.27|1|0|<font color=green>-7.27%</font>|<font color=green>-2.19%</font>|<font color=red>10.74%</font>|-5.24|9.76|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.21|0|7|<font color=green>-8.02%</font>|<font color=green>-1.78%</font>|<font color=red>10.74%</font>|-5.78|9.66|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.23|0|6|<font color=green>-7.95%</font>|<font color=green>-1.3%</font>|<font color=red>10.68%</font>|-5.76|9.93|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.25|0|5|<font color=green>-6.02%</font>|<font color=green>-0.91%</font>|<font color=red>8.81%</font>|-5.29|9.86|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.27|0|4|<font color=green>-4.46%</font>|<font color=green>-0.58%</font>|<font color=red>7.29%</font>|-4.74|9.99|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.3|0|3|<font color=green>-3.06%</font>|<font color=green>-0.34%</font>|<font color=red>5.93%</font>|-3.99|10.2|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.33|0|2|<font color=green>-2.68%</font>|<font color=green>-0.08%</font>|<font color=red>5.57%</font>|-3.72|10.76|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.38|0|1|<font color=green>-1.9%</font>|<font color=red>0.15%</font>|<font color=red>4.81%</font>|-3.06|11.36|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.43|1|0|<font color=green>-0.78%</font>|<font color=red>0.28%</font>|<font color=red>4.42%</font>|-1.37|11.92|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.33|0|3|<font color=green>-1.5%</font>|<font color=red>0.58%</font>|<font color=red>4.42%</font>|-2.63|12.41|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.4|0|2|<font color=green>-1.47%</font>|<font color=red>0.99%</font>|<font color=red>4.39%</font>|-2.59|13.5|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.5|0|1|<font color=red>0.22%</font>|<font color=red>1.19%</font>|<font color=red>2.75%</font>|0.62|14.25|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.67|2|0|<font color=red>3.06%</font>|<font color=red>0.56%</font>|<font color=red>0%</font>|0|10.18|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.5|1|0|<font color=red>1.68%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|11.38|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
