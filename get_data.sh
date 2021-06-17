if [ $1 == "name" ]
then
    curl -s http://fund.eastmoney.com/pingzhongdata/$2.js|sed 's/;/\n/g'| grep fS_name |grep -Po '(?<=\").*(?=\")'
elif [ $1 == "1m" ]
then
    curl -s http://fund.eastmoney.com/pingzhongdata/$2.js|sed 's/;/\n/g'| grep syl_1y |grep -Po '(?<=\").*(?=\")'
elif [ $1 == "3m" ]
then
    curl -s http://fund.eastmoney.com/pingzhongdata/$2.js|sed 's/;/\n/g'| grep syl_3y |grep -Po '(?<=\").*(?=\")'
elif [ $1 == "6m" ]
then
    curl -s http://fund.eastmoney.com/pingzhongdata/$2.js|sed 's/;/\n/g'| grep syl_6y |grep -Po '(?<=\").*(?=\")'
elif [ $1 == "stocklist" ]
then
    curl -s http://fund.eastmoney.com/pingzhongdata/$2.js|sed 's/;/\n/g'|grep stockCodesNew|grep -Po '(?<=\[).*(?=\])'|sed 's/,/\n/g'|cut -d '.' -f 2|sed 's/"//g'
elif [ $1 == "getstock" ]
then
    cat stock_list.txt | grep $2
else    
    echo ""
fi
