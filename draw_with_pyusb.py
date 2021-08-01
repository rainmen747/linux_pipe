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

scrollbar=tkinter.Scrollbar(window)
scrollbar=tkinter.Scrollbar(orient=tkinter.HORIZONTAL)

scrollbar.pack(side="bottom", fill="x")
scrollbar.config(command=myCanvas.xview)
myCanvas.pack() 

 
ret=dev.ctrl_transfer(0x81,usb.util.CTRL_OUT, 0x21, 0x20, 2);
while True:
    data= dev.read(0x81,1024*16,10)
    dev.control
    line_array = [(n, 20+data[n+1000]) for n in range(1,1000)]
    myCanvas.create_line(line_array,fill="Blue")

    #for ix in range(1,500,1):
    #    myCanvas.create_line(ix*2,20+(data[ix+200]),ix*2+2,20+(data[ix+1+200]),fill="Blue")
    myCanvas.update()
    time.sleep(0.001)
    myCanvas.delete("all")
    
    
    
    
    
window.mainloop()


    
