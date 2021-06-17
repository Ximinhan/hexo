min=100
max=0
http http://fund.eastmoney.com/pingzhongdata/$2.js|sed 's/;/\n/g'|grep Data_netWorthTrend|grep -Po '(?<=\[).*(?=\])'|sed 's/}\,{/\n/g'|sed "s/[A-Za-z\"\:]*//g"|cut -d ',' -f 1,2,3|sed 's/,/|/g'|sed 's/^/|&/g'|sed 's/$/&|/g'|tac|head -n 60 > ./testn
while read line;
do 
    s1=`echo $line|cut -d "|" -f 2`
    s2=`echo $line|cut -d "|" -f 3`
    s3=`echo $line|cut -d "|" -f 4`
    s1=`date -d @${s1:0:10} +'%Y-%m-%d'`
    if [ ${s3:0:1} == "-" ];then
        s3="<font color=green>$s3%</font>"
    else
        s3="<font color=red>$s3%</font>"
    fi
    
    [ $max -lt ${s2%.*} ] && max=${s2%.*}
    
    [ $min -gt ${s2%.*} ] && min=${s2%.*}
    #echo "|$s1|$s2|$s3|";

    #s1=`date -d @${s1:0:10} +'%Y/%m/%d'`;
    #echo "[\"$s1\",$s2],";
done < ./testn
if [ $1 == "max" ]
then
    echo $[max+1]
else
    echo $[min]
fi
rm ./testn
