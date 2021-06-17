min=0
max=0
http http://fund.eastmoney.com/pingzhongdata/$1.js|sed 's/;/\n/g'|grep Data_netWorthTrend|grep -Po '(?<=\[).*(?=\])'|sed 's/}\,{/\n/g'|sed "s/[A-Za-z\"\:]*//g"|cut -d ',' -f 1,2,3|sed 's/,/|/g'|sed 's/^/|&/g'|sed 's/$/&|/g'|tac|head -n 60 > ./testn
while read line;
do 
    s1=`echo $line|cut -d "|" -f 2`
    s2=`echo $line|cut -d "|" -f 3`

    s1=`date -d @${s1:0:10} +'%Y/%m/%d'`;
    echo "[\"$s1\",$s2],";
done < ./testn

#echo $[max+1]
#echo $[min+1]
#curl -s http://fund.eastmoney.com/pingzhongdata/001634.js|sed 's/;/\n/g'| grep fS_name |grep -Po '(?<=\").*(?=\")'
#万家瑞祥混合C
#
rm ./testn
