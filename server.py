import os,sys
import time
print("Server ..\n")

fifo='/tmp/rain_pipe'

if os.path.exists(fifo)==False:
    os.mkfifo(fifo)
    
#os.remove(fifo)
#time.sleep(1)

print("mkfifo_",fifo)

#data=bytes(range(256))
data=bytearray(2000)
count=0

with open(fifo,"r") as r:
	print("Reading\n")
	while True:
		#time.sleep(0.1)
		data=r.read()
		count=count+1
		print(count)
	r.close()
    
