from tkinter import * 
win = Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "2 entry")
lb.insert(END, "3 entry")
lb.insert(END, "4 entry")

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
