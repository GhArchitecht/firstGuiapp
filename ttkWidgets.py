import tkinter as tk
from tkinter import ttk
import string 
import secrets

root = tk.Tk()


def secretsPasswordGeneratorIII(length):
     #Specifica

     characters = string.ascii_letters + string.digits + string.punctuation

     while True:
        psswd = ''.join(secrets.choice(characters) for i in range(length))
        if (sum(c.islower() for c in psswd) <=2 and
            sum(c.isupper() for c in psswd) <=2 and
            sum(c in string.punctuation for c in psswd) ==1 and
            any(c.isdigit() for c in psswd) ):
            break
     return print(psswd)


ttk.Button(root, text='Rock', command=lambda: secretsPasswordGeneratorIII(10)).pack()
ttk.Button(root, text='Paper',command=lambda: secretsPasswordGeneratorIII(10)).pack()
ttk.Button(root, text='Scissors', command=lambda: secretsPasswordGeneratorIII(10)).pack()

root.mainloop()