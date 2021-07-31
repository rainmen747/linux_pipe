import subprocess
proc = subprocess.Popen(['./test_stdout'],stdout=subprocess.PIPE)
while True:
    output_str = proc.stdout.readline()
    print(output_str)
    
