#!/usr/bin/env python3
import re
import subprocess
inp = input("type the website: ")
found = []
words = []
c=0
f = open("Report.txt","w")
with open("subdomains-top1mil-5000.txt","r") as file:
	words = file.readlines()
#words = ["www."]
for x in words:
	x = x[:-1]
	#print("{}.youtube.com".format(x))
	c=c+1
	y = subprocess.run(["host","-t","A","{}.{}".format(x,inp)], capture_output=True)
	res = y.stdout
	print(res)
	regex = re.findall(r"has address (\d*.\d*.\d*.\d*)",str(res))
	if len(regex)>0:
		for ip in regex:
			print("YES {}".format(ip))
			found.append(ip)
			f.write(str(ip)+"\t"+"{}.{}".format(x,inp)+"\n")
	print(c)
print(found)
f.close()


