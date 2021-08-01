---
title: 产品详情
date: 2021-08-01 15:02:07
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
- 近一个月涨跌幅：-12.58%
- 近三个月涨跌幅: -11.39%
- 近六个月涨跌幅: -0.18%

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
]
        }
    ]
};
{% endecharts %}

# 历史净值

| 日期 | 净值 | 涨幅 | 上涨概率 | 连涨 | 连跌 | 区间净收益 | 区间累计收益 | 最大回撤 | 收益回撤比 | 波动率 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2021-07-30|2.746|<font color=red>1.63%</font>|0.47|1|0|<font color=green>-9.15%</font>|<font color=red>3.18%</font>|<font color=red>18.89%</font>|-3.75|10.98|
|2021-07-29|2.702|<font color=red>0.82%</font>|0.47|0|5|<font color=green>-9.89%</font>|<font color=red>3.4%</font>|<font color=red>18.89%</font>|-4.05|11.03|
|2021-07-28|2.68|<font color=green>-0.3%</font>|0.47|0|4|<font color=green>-9.62%</font>|<font color=red>3.63%</font>|<font color=red>18.64%</font>|-3.99|11.12|
|2021-07-27|2.688|<font color=green>-2.89%</font>|0.48|0|3|<font color=green>-6.93%</font>|<font color=red>3.82%</font>|<font color=red>16.22%</font>|-3.31|10.87|
|2021-07-26|2.768|<font color=green>-3.22%</font>|0.49|0|2|<font color=green>-3.83%</font>|<font color=red>3.96%</font>|<font color=red>13.44%</font>|-2.21|10.49|
|2021-07-23|2.86|<font color=green>-2.95%</font>|0.5|0|1|<font color=green>-0.91%</font>|<font color=red>4.05%</font>|<font color=red>10.81%</font>|-0.65|10.15|
|2021-07-22|2.947|<font color=green>-2.03%</font>|0.51|2|0|<font color=red>1.14%</font>|<font color=red>4.11%</font>|<font color=red>10.74%</font>|0.82|10.02|
|2021-07-21|3.008|<font color=red>0.17%</font>|0.5|1|0|<font color=red>0.98%</font>|<font color=red>4.17%</font>|<font color=red>10.74%</font>|0.71|10.12|
|2021-07-20|3.003|<font color=red>0.43%</font>|0.49|0|3|<font color=red>0.54%</font>|<font color=red>4.24%</font>|<font color=red>10.74%</font>|0.39|10.2|
|2021-07-19|2.99|<font color=green>-0.13%</font>|0.5|0|2|<font color=red>0.67%</font>|<font color=red>4.31%</font>|<font color=red>10.74%</font>|0.48|10.3|
|2021-07-16|2.994|<font color=green>-1.19%</font>|0.51|0|1|<font color=red>1.88%</font>|<font color=red>4.36%</font>|<font color=red>10.74%</font>|1.35|10.33|
|2021-07-15|3.03|<font color=green>-1.97%</font>|0.52|4|0|<font color=red>3.93%</font>|<font color=red>4.37%</font>|<font color=red>10.74%</font>|2.83|10.2|
|2021-07-14|3.091|<font color=red>0.03%</font>|0.51|3|0|<font color=red>3.9%</font>|<font color=red>4.38%</font>|<font color=red>10.74%</font>|2.81|10.31|
|2021-07-13|3.09|<font color=red>1.15%</font>|0.5|2|0|<font color=red>2.72%</font>|<font color=red>4.41%</font>|<font color=red>10.74%</font>|1.96|10.34|
|2021-07-12|3.055|<font color=red>0.79%</font>|0.49|1|0|<font color=red>1.92%</font>|<font color=red>4.47%</font>|<font color=red>10.74%</font>|1.38|10.41|
|2021-07-09|3.031|<font color=red>0.43%</font>|0.48|0|1|<font color=red>1.48%</font>|<font color=red>4.54%</font>|<font color=red>10.74%</font>|1.07|10.52|
|2021-07-08|3.018|<font color=green>-1.28%</font>|0.49|1|0|<font color=red>2.79%</font>|<font color=red>4.58%</font>|<font color=red>10.74%</font>|2.01|10.53|
|2021-07-07|3.057|<font color=red>1.06%</font>|0.48|0|3|<font color=red>1.71%</font>|<font color=red>4.65%</font>|<font color=red>10.74%</font>|1.23|10.58|
|2021-07-06|3.025|<font color=green>-1.88%</font>|0.49|0|2|<font color=red>3.67%</font>|<font color=red>4.67%</font>|<font color=red>10.74%</font>|2.64|10.46|
|2021-07-05|3.083|<font color=green>-0.52%</font>|0.5|0|1|<font color=red>4.2%</font>|<font color=red>4.68%</font>|<font color=red>10.74%</font>|3.03|10.57|
|2021-07-02|3.099|<font color=green>-1.46%</font>|0.51|1|0|<font color=red>5.75%</font>|<font color=red>4.65%</font>|<font color=red>10.74%</font>|4.14|10.54|
|2021-07-01|3.145|<font color=red>0.13%</font>|0.5|0|2|<font color=red>5.62%</font>|<font color=red>4.63%</font>|<font color=red>10.74%</font>|4.05|10.68|
|2021-06-30|3.141|<font color=green>-0.54%</font>|0.51|0|1|<font color=red>6.19%</font>|<font color=red>4.59%</font>|<font color=red>10.74%</font>|4.46|10.79|
|2021-06-29|3.158|<font color=green>-1.03%</font>|0.53|2|0|<font color=red>7.3%</font>|<font color=red>4.51%</font>|<font color=red>10.74%</font>|5.26|10.84|
|2021-06-28|3.191|<font color=red>3.44%</font>|0.51|1|0|<font color=red>3.73%</font>|<font color=red>4.53%</font>|<font color=red>10.74%</font>|2.69|10.08|
|2021-06-25|3.085|<font color=red>0.23%</font>|0.5|0|1|<font color=red>3.5%</font>|<font color=red>4.56%</font>|<font color=red>10.74%</font>|2.52|10.22|
|2021-06-24|3.078|<font color=green>-0.23%</font>|0.52|4|0|<font color=red>3.73%</font>|<font color=red>4.59%</font>|<font color=red>10.74%</font>|2.69|10.37|
|2021-06-23|3.085|<font color=red>0.72%</font>|0.5|3|0|<font color=red>2.99%</font>|<font color=red>4.64%</font>|<font color=red>10.74%</font>|2.15|10.49|
|2021-06-22|3.063|<font color=red>0.62%</font>|0.48|2|0|<font color=red>2.35%</font>|<font color=red>4.71%</font>|<font color=red>10.74%</font>|1.69|10.62|
|2021-06-21|3.044|<font color=red>2.39%</font>|0.47|1|0|<font color=green>-0.03%</font>|<font color=red>4.87%</font>|<font color=red>10.74%</font>|-0.02|10.23|
|2021-06-18|2.973|<font color=red>0.81%</font>|0.45|0|7|<font color=green>-0.84%</font>|<font color=red>5.07%</font>|<font color=red>10.74%</font>|-0.61|10.32|
|2021-06-17|2.949|<font color=green>-0.07%</font>|0.46|0|6|<font color=green>-0.77%</font>|<font color=red>5.28%</font>|<font color=red>10.68%</font>|-0.56|10.5|
|2021-06-16|2.951|<font color=green>-2.06%</font>|0.48|0|5|<font color=red>1.31%</font>|<font color=red>5.42%</font>|<font color=red>8.81%</font>|1.15|10.28|
|2021-06-15|3.013|<font color=green>-1.63%</font>|0.5|0|4|<font color=red>2.99%</font>|<font color=red>5.52%</font>|<font color=red>7.29%</font>|3.17|10.19|
|2021-06-11|3.063|<font color=green>-1.45%</font>|0.52|0|3|<font color=red>4.51%</font>|<font color=red>5.56%</font>|<font color=red>5.93%</font>|5.89|10.14|
|2021-06-10|3.108|<font color=green>-0.38%</font>|0.54|0|2|<font color=red>4.91%</font>|<font color=red>5.58%</font>|<font color=red>5.57%</font>|6.82|10.32|
|2021-06-09|3.12|<font color=green>-0.79%</font>|0.57|0|1|<font color=red>5.75%</font>|<font color=red>5.58%</font>|<font color=red>4.81%</font>|9.25|10.44|
|2021-06-08|3.145|<font color=green>-1.13%</font>|0.59|1|0|<font color=red>6.96%</font>|<font color=red>5.51%</font>|<font color=red>4.42%</font>|12.19|10.47|
|2021-06-07|3.181|<font color=red>0.73%</font>|0.57|0|3|<font color=red>6.19%</font>|<font color=red>5.48%</font>|<font color=red>4.42%</font>|10.84|10.67|
|2021-06-04|3.158|<font color=green>-0.03%</font>|0.6|0|2|<font color=red>6.22%</font>|<font color=red>5.44%</font>|<font color=red>4.39%</font>|10.97|10.93|
|2021-06-03|3.159|<font color=green>-1.68%</font>|0.63|0|1|<font color=red>8.04%</font>|<font color=red>5.31%</font>|<font color=red>2.75%</font>|22.63|10.7|
|2021-06-02|3.213|<font color=green>-2.75%</font>|0.67|2|0|<font color=red>11.1%</font>|<font color=red>4.99%</font>|<font color=red>1.26%</font>|68.19|9.44|
|2021-06-01|3.304|<font color=red>1.35%</font>|0.65|1|0|<font color=red>9.62%</font>|<font color=red>4.71%</font>|<font color=red>1.26%</font>|59.09|9.55|
|2021-05-31|3.26|<font color=red>1.68%</font>|0.62|0|1|<font color=red>7.8%</font>|<font color=red>4.52%</font>|<font color=red>1.26%</font>|47.91|9.49|
|2021-05-28|3.206|<font color=green>-1.26%</font>|0.67|4|0|<font color=red>9.18%</font>|<font color=red>4.21%</font>|<font color=red>1.01%</font>|70.35|9.26|
|2021-05-27|3.247|<font color=red>1.95%</font>|0.64|3|0|<font color=red>7.09%</font>|<font color=red>4.0%</font>|<font color=red>1.01%</font>|54.33|8.99|
|2021-05-26|3.185|<font color=red>0.5%</font>|0.62|2|0|<font color=red>6.56%</font>|<font color=red>3.81%</font>|<font color=red>1.01%</font>|50.27|9.31|
|2021-05-25|3.169|<font color=red>1.08%</font>|0.58|1|0|<font color=red>5.41%</font>|<font color=red>3.67%</font>|<font color=red>1.01%</font>|41.46|9.51|
|2021-05-24|3.135|<font color=red>0.1%</font>|0.55|0|1|<font color=red>5.31%</font>|<font color=red>3.52%</font>|<font color=red>1.01%</font>|40.69|9.93|
|2021-05-21|3.132|<font color=green>-0.38%</font>|0.6|1|0|<font color=red>5.72%</font>|<font color=red>3.3%</font>|<font color=red>1.01%</font>|43.83|10.3|
|2021-05-20|3.144|<font color=red>0.51%</font>|0.56|0|3|<font color=red>5.18%</font>|<font color=red>3.1%</font>|<font color=red>1.01%</font>|39.7|10.84|
|2021-05-19|3.128|<font color=green>-0.6%</font>|0.62|0|2|<font color=red>5.82%</font>|<font color=red>2.76%</font>|<font color=red>0.41%</font>|109.87|11.24|
|2021-05-18|3.147|<font color=green>-0.38%</font>|0.71|0|1|<font color=red>6.22%</font>|<font color=red>2.26%</font>|<font color=red>0.03%</font>|1604.76|11.8|
|2021-05-17|3.159|<font color=green>-0.03%</font>|0.83|5|0|<font color=red>6.25%</font>|<font color=red>1.6%</font>|<font color=red>0%</font>|0|12.64|
|2021-05-14|3.16|<font color=red>1.94%</font>|0.8|4|0|<font color=red>4.24%</font>|<font color=red>1.07%</font>|<font color=red>0%</font>|0|12.76|
|2021-05-13|3.1|<font color=red>0.94%</font>|0.75|3|0|<font color=red>3.26%</font>|<font color=red>0.52%</font>|<font color=red>0%</font>|0|13.94|
|2021-05-12|3.071|<font color=red>1.55%</font>|0.67|2|0|<font color=red>1.68%</font>|<font color=red>0.13%</font>|<font color=red>0%</font>|0|14.15|
|2021-05-11|3.024|<font color=red>1.27%</font>|0.5|1|0|<font color=red>0.4%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|13.04|
|2021-05-10|2.986|<font color=red>0.4%</font>|0.0|0|0|<font color=red>0.0%</font>|<font color=red>0.0%</font>|<font color=red>0%</font>|0|0.0|
|2021-05-07|2.974|<font color=green>-2.97%</font>|0|0|0|<font color=red>0%</font>|<font color=red>0%</font>|<font color=red>0%</font>|0|0|
