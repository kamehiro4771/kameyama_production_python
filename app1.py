import tkinter
import random

def dispLabel():
    kuji = ['大吉','中吉','小吉','凶']
    lbl.configure(text=random.choice(kuji))

root = tkinter.Tk()
root.geometry("200x100")

lbl = tkinter.Label(text="LABEL")
btn = tkinter.Button(text="PUSH",command = dispLabel)

lbl.pack()
btn.pack()
tkinter.mainloop()
