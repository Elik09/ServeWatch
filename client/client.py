#! /usr/bin/python3
# import time module, Observer, FileSystemEventHandler
import time
import datetime
import platform
import sys
import os
import nmap
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Used for temporary purposes and will be removed
import hashlib
starttime=time.time()
nmapresults=""
# echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
session=requests.Session()
try:
	folder_to_track=sys.argv[1]
except:
	folder_to_track="/tmp"

TIMEOUT=10
send_json=True # Decides whether to send the Post request as json or not
user=os.getenv('USER')
os=platform.uname()[0]
arch=platform.uname()[-1]
machine=platform.uname()[1]
hmac=f"{user}{machine}{os}{arch}"
hmac=hashlib.md5(hmac.encode()).hexdigest()
url=f"http://localhost:5000/submit/logs"

if user != "root":
	logfile=f"/home/{user}/logfile.log"
else:
	logfile=f"/tmp/logfile.swp"

def logtofile(content):
	try:
		with open(logfile,'a') as w:
			w.write(f"{content}\n")
			w.close()
	except:
		print(f"Could not add content to logfile '{logfile}'")




def nmap_scan():
	target_hosts = "10.10.5.167"
	# target_hosts = "localhost"
	# target_hosts = "192.168.10.1/24" # for range
	# Searching common ports to make the scan faster
	# nmap_arguments = "-p80 -Pn -T4 --max-retries 1"
	nmap_arguments = "-p21,22,23,25,53,80,135,139,143,443,445,993,995,1723,3306,3389,5000,5900,8080 -Pn -T4 --max-retries 1"

	# initialise the port scanner
	print(f"[+] Scanning range {target_hosts}")
	nm = nmap.PortScanner()

	res=nm.scan(hosts=target_hosts, arguments=nmap_arguments)
	to_scan=(res['nmap']['scaninfo']['tcp']['services']) # Showing the ports to scan
	print(f"[+] scanning ports {to_scan}")
	# print(f"[+] Printing results\n\n")

	# print(res)
	results=[]
	for host in nm.all_hosts():
		final=""
		try:
			state = res['scan'][host]['status']['state'] # Checking which machines are up
			name = res['scan'][host]['hostnames'][0]['name']# Checking which machines are up
			host=nm[host]['addresses']['ipv4']
			res = res['scan'][host]['tcp']
		except:
			state = nm[host]['status']['state'] # Checking which machines are up
			name = nm[host]['hostnames'][0]['name']# Checking which machines are up
			host=nm[host]['addresses']['ipv4']
			res=nm[host]['tcp']
		# print(res)
		for (port,value) in res.items():
			portstate=value['state']
			if(portstate.strip().lower() == "open"):
				if len(final) < 2:
					final+=(f"{host} ({name}).Ports : ")
				final+=f"{port},"

		if len(final):
			results.append(final[:-1])

	print(results)
	print(f"[+] Scan complete")
	return '  ::  '.join(results)


def send_to_db(date_time,message,path):
	global user,arch,machine,os,hmac,url,TIMEOUT,starttime,nmapresults
	# Perform an nmap scan every hour
	nmapdelay=3600 # After how long it should wait before scanning again.Time in seconds.
	timedifference=(time.time() - starttime)

	if int(timedifference) > nmapdelay:
		print("Rescanning with nmap")
		nmapresults=nmap_scan()
		starttime=time.time()
		print(f"starttime is now {starttime}")
	else:
		print(f"Time difference is {timedifference}")

	payload={
		"id":f"{hmac}", # This is a test hash , should be uniq for every machine
		"machine":f"{machine}", # Depending on the machine
		"user":f"{user}", # Temp value for now, It should be the user of the client machine
		"action":f"{message}",
		"file":f"{path}",
		"nmapresults":f"{nmapresults}",
		"timestamp":f"{date_time}",
		}

	# print(payload)
	customheaders={
					  # Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
		"User-Agent":f"ServeWatch/1.0 ({os}; {arch}; {machine}; {user}; rv:50) Watchdog/89.0"
	}
	try:
		if (send_json):
			response=requests.post(url,headers=customheaders,json=payload,timeout=TIMEOUT)
		else:
			response=requests.post(url,headers=customheaders,data=payload,timeout=TIMEOUT)

		if '"Message": "Ok"'.lower() not in response.text.lower():
			print(f"	[-] Unable to upload to database - Missing  ok in response")
			return
		else:
			print(f"	[+] Uploaded to database")
			return
	except Exception as e:
		fail=end=""
		print(f"{fail}  [-] Unable to upload to database - GET Query failed or took too long.Error {e}{end}")
		return


class OnMyWatch:
	# Set the directory on watch
	global folder_to_track
	watchDirectory = folder_to_track

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
		self.observer.start()
		try:
			while True:
				 time.sleep(5)
		except KeyboardInterrupt:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()



class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		# Setting the extensions to ignore
		blacklisted_extensions=['swp','save']
		blacklisted_files=[f'{logfile.lower()}','serverwatch.txt','sh-thd']
		blacklisted_folders=['/root']

		# Getting the extension of the modified or added file
		extension=event.src_path.split('.')[-1]
		filename=event.src_path.split('/')
		folder=event.src_path
		#print(f"Extension : {extension}")

		for blacklisted_file in blacklisted_files:
			for file_path in filename:
				if blacklisted_file.lower() in file_path.lower():
					print(f"	[*] Ignored file in blacklist > {blacklisted_file}")
					return None
				else:
					pass

		if folder.lower().strip() in blacklisted_folders:
			# print(f"Ignoring file '{event.src_path}'")
			return None
		elif extension.lower().strip() in blacklisted_extensions:
			# print(f"Ignoring extension '{extension}'")
			return None
			# return None
		elif event.is_directory:
			return None
		elif event.event_type == 'created':
			message="File_Created"
		elif event.event_type == 'modified':
			message="File_Modified"
		elif event.event_type == 'deleted':
			message="File_Deleted"
		elif event.event_type == 'closed':
			message="File_Closed"
		elif event.event_type == 'moved':
			message="File_Moved"
		else:
			message="Unknown_event"

		try:
			#print(f"Logging extension '{extension}'")
			date=datetime.datetime.now().strftime('%y%m%d%H%M%S')
			content=(f"{date} - {message} => {event.src_path}")
			logtofile(content)
			print(content)
			send_to_db(date,message,event.src_path)
			# Log the message to a file
			# Upload the log to a remote server
			# Add the log to a database
		except:
			print(f"Logging Failed")

if __name__ == '__main__':
	#folders_to_track="/tmp,./,/home/kali/".split(',')
	#for folder_to_track in folders_to_track:
	print(f"OS : {os}")
	print(f"User : {user}")
	print(f"ARCH : {arch}")
	print(f"MACHINE_ID : {hmac}")
	print(f"MACHINE : {machine}")
	print(f"REMOTE LOG : {url}")
	print(f"LOCAL LOG :  {logfile}\n")
	print(f"Watchdog started tracking - {folder_to_track}\n\n")

	print("To increase the limit on the number of files to watch, run the following command")
	print("run 'echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p'\n\n")


	try:
		watch = OnMyWatch()
		nmapresults=nmap_scan()
		watch.run()
	except OSError:
		print("The directory contains files/folders not owned by the current user. Run the program as root/sudo")
	except KeyboardInterrupt:
		print(" \n\n\nObserver Stopped")
