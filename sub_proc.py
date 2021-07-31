#filters output
import subprocess
proc = subprocess.Popen(['./test_stdout'],stdout=subprocess.PIPE)
#data=bytearray[2000]
count=0
while True:
    for line in proc.stdout:
   #the real code does filtering here
       data=line.rstrip()
    count=count+1
    print(count,data)