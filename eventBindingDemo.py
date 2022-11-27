import tkinter as tk
from tkinter import ttk
import string
import secrets


# def return_pressed(event):
#     print('Return key pressed.')

def secretsPasswordGeneratorIII():
     #Specifica

     characters = string.ascii_letters + string.digits + string.punctuation

     while True:
        psswd = ''.join(secrets.choice(characters) for i in range(10))
        if (sum(c.islower() for c in psswd) <=2 and
            sum(c.isupper() for c in psswd) <=2 and
            sum(c in string.punctuation for c in psswd) ==1 and
            any(c.isdigit() for c in psswd) ):
            break
     return print(psswd)




root = tk.Tk()

btn = ttk.Button(root, text='Generate Password')
btn.bind('<Return>', secretsPasswordGeneratorIII)

btn.focus()
btn.pack(expand=True)

root.mainloop()