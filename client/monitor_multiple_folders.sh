#! /bin/bash
folders_to_track="/tmp /var/www/html"
echo "Monitoring directories : $folders_to_track"
sleep 1 
for folder_to_track in $folders_to_track;do
	#Check if dir exists
	#Monitor the folder
	#echo $folder_to_track &
	python3 client.py $folder_to_track > /dev/null  &

	echo "$folder_to_track is now being monitored"
	sleep 1
done
echo "Sending the processes to background"
sleep 3
disown -a

