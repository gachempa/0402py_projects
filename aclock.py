from cProfile import label
from time import time
from  tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Clock")
window.geometry("600x300")
window.configure(bg="steelblue")

label = Label(window, font=("Arial Black",30,"bold"), bg="blue", fg="yellow")
label.pack(pady=100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)
    
clock()
window.mainloop()
