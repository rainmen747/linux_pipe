import os,sys
import time
print("Client ..\n")

fifo='/tmp/rain_pipe'
#os.remove(fifo)
pipe=os.open(fifo,os.O_WRONLY | os.O_NONBLOCK)

print("mkfifo_",fifo)

i=0
with open(fifo,"w") as w:
    print("Writing\n")
    while i<1001:
        mystr="Welcome Im rainmen {0}\n".format(i)
        os.write(pipe,mystr.encode())
        i+=1

os.close(pipe)

        
