import tkinter 
import time
#import subprocess
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x32e9, idProduct=0xfff1)
if dev is None:
    raise ValueError('Device is not found')
# device is found :-)
#print(dev)

#dev.set_configuration()

usb.util.claim_interface(dev, 0)



window=tkinter.Tk()

window.title("Rainmen")
window.geometry("1000x480+100+100")
window.resizable(True,True)
myCanvas = tkinter.Canvas(window, bg="white", height=400, width=1020)
myCanvas.pack() 

x=0
 
while True:
    data= dev.read(0x81,1024*16,10)
    for ix in range(1,500,1):
        myCanvas.create_line(ix*2,20+(data[ix+2000]),ix*2+2,20+(data[ix+1+2000]),fill="Blue")
    myCanvas.update()
    time.sleep(0.001)
    myCanvas.delete("all")
    
    
    
    
    
window.mainloop()


    
