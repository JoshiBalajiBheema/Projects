from tkinter import *

basic_root = Tk()

basic_root.geometry("733x430")
basic_root.minsize(300,100)
basic_root.maxsize(1200,900)

text_lab0 = Label(text="Pycharm Community Edition")
text_lab0.pack()

text_lab1 = Label(text="Version 2017.2")
text_lab1.pack()

text_lab2 = Label(text="Create New Project")
text_lab2.pack()

basic_root.mainloop()
