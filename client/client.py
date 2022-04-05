#! /usr/bin/python3
# import time module, Observer, FileSystemEventHandler
import time
import datetime
import platform
import sys
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Used for temporary purposes and will be removed
import hashlib

# echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
session=requests.Session()
try:
	folder_to_track=sys.argv[1]
except:
	folder_to_track="/tmp"


send_json=True # Decides whether to send the Post request as json or not
user=os.getenv('USER')
os=platform.uname()[0]
arch=platform.uname()[-1]
machine=platform.uname()[1]
hmac=f"{user}{machine}{os}{arch}"
hmac=hashlib.md5(hmac.encode()).hexdigest()
# url=f"http://10.10.10.1:5000/submit/logs"
url=f"http://localhost:5000/submit/logs"
# print(f"User : {user}")

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


def send_to_db(date_time,message,path):
	global user,arch,machine,os,hmac,url

	TIMEOUT=3
	payload={
		"id":f"{hmac}", # This is a test hash , should be uniq for every machine
		"machine":f"{machine}", # Depending on the machine
		"user":f"{user}", # Temp value for now, It should be the user of the client machine
		"action":f"{message}",
		"file":f"{path}",
		"timestamp":f"{date_time}",
		}

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
		else:
			print(f"	[+] Uploaded to database")
	except:
		fail=end=""
		print(f"{fail}  [-] Unable to upload to database - GET Query failed or took too long{end}")
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

	print("Make sure to run 'echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p'\n\n")

	try:
		watch = OnMyWatch()
		watch.run()
	except OSError:
		print("The directory contains files/folders not owned by the current user. Run the program as sudo")
	except KeyboardInterrupt:
		print(" \n\n\nObserver Stopped")
