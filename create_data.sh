min=0
max=0
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
    echo "|$s1|$s2|$s3|";

    #s1=`date -d @${s1:0:10} +'%Y/%m/%d'`;
    #echo "[\"$s1\",$s2],";
done < ./test2

echo $[max+1]
echo $[min+1]
