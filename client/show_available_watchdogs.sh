filename="client.py"
for line in $(ps aux | grep $filename | awk -F " " '{print $2}');do 
	scripttype=`ps aux | grep $filename| grep $line | awk -F " " '{print $11}'`
	scriptname=`ps aux| grep $filename | grep $line | awk -F " " '{print $12}'`
	dir=`ps aux | grep $filename| grep $line | awk -F " " '{print $13}'` 
	# echo "Watchdog : $line is monitoring $dir"
	if [[ $scripttype != "" ]];then
		echo "Watchdog : $line is monitoring $dir"
	else
		true
	fi
done

