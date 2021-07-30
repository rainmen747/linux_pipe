import os,sys
import time
print("Server ..\n")

fifo='/tmp/rain_pipe'

if os.path.exists(fifo)==False:
    os.mkfifo(fifo)
    
#os.remove(fifo)
#time.sleep(1)

print("mkfifo_",fifo)

with open(fifo,"r") as r:
	print("Reading\n")
	while True:
		time.sleep(0.1)
		data=r.read()
		if (data!=""):
			print(data)
	r.close()
    
