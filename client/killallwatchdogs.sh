filename="client.py"
for line in $(ps aux | grep $filename | awk -F " " '{print $2}');do 
	kill -9 $line 2>/dev/null && echo "Killed watchdog : $line " 
done
