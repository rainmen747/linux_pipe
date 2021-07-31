import subprocess
#import matplotlib.pyplot as plt

proc = subprocess.Popen(['./test_stdout'],stdout=subprocess.PIPE)
while True:
    output_str = proc.stdout.readline()
    s=output_str.decode("utf-8")
    mylist = s.split(" ")
    print(mylist[10])
    