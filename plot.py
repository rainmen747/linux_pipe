import  tkinter 
import time
import subprocess



proc = subprocess.Popen(['./rain_fx3'],stdout=subprocess.PIPE)

window=tkinter.Tk()

window.title("Rainmen")
window.geometry("1000x400+100+100")
window.resizable(True,True)
myCanvas = tkinter.Canvas(window, bg="white", height=300, width=1000)
myCanvas.pack()

x=0

while True:
    output_str = proc.stdout.readline()
    s=output_str.decode("utf-8")
    mylist = s.split(" ")
    for ix in range(1,900,1):
        myCanvas.create_line(ix,int(mylist[ix]),ix+1,int(mylist[ix+1]),fill="Blue")
    myCanvas.update()
    time.sleep(0.001)
    myCanvas.delete("all")
    
    
    
    
    
window.mainloop()
