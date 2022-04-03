from cProfile import label
from  tkinter import Tk, Label

window = Tk()
window.title("Clock")
window.geometry("600x300")
window.configure(bg="steelblue")

label = Label(window, font=("Arial Black",30,"bold"), bg="blue", fg="yellow")
label.pack(pady=100)

window.mainloop()
