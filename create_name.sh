curl -s http://fund.eastmoney.com/pingzhongdata/$1.js|sed 's/;/\n/g'| grep fS_name |grep -Po '(?<=\").*(?=\")'
