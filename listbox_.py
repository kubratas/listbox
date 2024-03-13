from tkinter import *
from tkinter import messagebox 


def add():
    text = entrance.get()
    liste.insert(END,text)
    entrance.delete(0,END)

window =Tk()
window.geometry("400x300")
window.title("MESSAGE BOX")

liste=Listbox(window,width =20,height=10)
liste.pack(pady=10)

entrance=Entry()
entrance.pack(pady = 10)

button1= Button (text ="add",command= add)
button1.pack(pady=10)

button2=Button (text = "exit", command = window.destroy)
button2.pack(pady=10)

mainloop()