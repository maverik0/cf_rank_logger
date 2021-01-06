import requests 
import threading
import sys
import re
import time

handle = str(input("please enter the cf handle : "))
roundID = int(input("please enter the contestID : "))

url = "https://codeforces.com/api/contest.standings?contestId={0}&handles={1}&showUnofficial=true".format(roundID, handle)

file = open("cf_logger.txt", "w")

def fn():
	while 1:
		t = time.time()
		with requests.get(url) as r:
			match = re.search(r"\"rank\":(\d),", r.text)
			s = str(int((t-t_start)/60)) + "  :  "
			if match:
				file.write(s + str(match.group(1)))
				file.write('\n')
		time.sleep(8)
			

x = threading.Thread(target = fn, daemon = True)
t_start = time.time()
x.start()

while str(input("press \"y\" to end the process : ")) != "y":     
	pass

file.close()

sys.exit(0)