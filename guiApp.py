# Importing Tkinter Library
from tkinter import *
import customtkinter
import tkinter

#Setting up theme of your app
customtkinter.set_appearance_mode("dark")

# Setting up theme of your components
customtkinter.set_default_color_theme('green')

# Creating Window of our App
# root = Tk()
root = customtkinter.CTk()

# Setting Window width and Height
root.geometry('300x400')

# Creating  a button widget
#mybutton = Button(root, text='Hello World', font=("Inter", 14))
button = customtkinter.CTkButton(master=root, text='Hello Word')

# Showing at the center of the screen
# mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

def slider_event(value):
    print(value)
    
slider = customtkinter.CTkSlider(master=root, from_=8, to=20, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tkinter.BOTTOM)


# Running the app
root.mainloop()