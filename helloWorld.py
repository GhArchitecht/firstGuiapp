import tkinter as tk
from tkinter import ttk

root  = tk.Tk()

root.title('Tkinter Window Demo')

root.geometry('600x400+50+50')

root.attributes('-alpha',0.9)

root.resizable(0, 0)
root.attributes('-topmost', 1)
root.iconbitmap('/Users/gharchitecht/Downloads/favicon.icns')



# place a label on the root window
message = tk.Label(root, text='Hello World label')
message.pack()

ttk.Label(root, text='Themed Label').pack()


# keep the window displaying
root.mainloop()