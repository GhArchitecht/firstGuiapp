from tkinter import *

root = Tk()

#Creating a label widget 
myLabel = Label(root, text='Hello World')
myLabel2 = Label(root, text='Hello World')
myLabel = Label(root, text='Hello World')

# Shoving the label widget onto the screen
myLabel.pack()
myLabel2.pack()

root.mainloop()