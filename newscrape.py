import socks
import socket
import requests
import time
import subprocess
import os
import pandas as pd
from time import sleep
import requests
from bs4 import BeautifulSoup
counter = 0

def change_ip():
	socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
	socket.socket = socks.socksocket
	print(requests.get("http://icanhazip.com").text)
	os.system("killall tor")
	time.sleep(5)
	os.system("tor &")
	time.sleep(10)
		

print(requests.get("http://icanhazip.com").text)
alltitles = []
df = pd.read_csv('myurls.csv', names=["title"])
for article in df["title"]:
	sleep(0.3)
	html = requests.get(article, verify=False)
	if html.status_code != 200:
		change_ip()
	page = html.text
	soup = BeautifulSoup(page, 'html.parser')
	sleep(0.3)
	alltitles.append(soup)
	print("success!")
	sleep(0.1)
	counter = counter+1
	if counter == 20:
		change_ip()
		counter = 0

newdf = pd.DataFrame(alltitles)
newdf.to_csv("thisismygannettdata", sep=' ', index=False, header=False)
