import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tempconv import Conversion
import sv_ttk

def convert_ftinch():
    try:
        feet = float(entry_feet.get())
        inches = float(entry_inches.get())
        conv = Conversion(None, None, feet, inches)  # Create a Conversion instance
        meters, centimeters = conv.ftin_to_mcm()  # Call the method on the instance
        feet = float(entry_feet.get())
        inches = float(entry_inches.get())
        conv = Conversion(None, None, feet, inches)  # Create a Conversion instance
        meters, centimeters = conv.ftin_to_mcm()  # Call the method on the instance
        messagebox.showinfo("Conversion Result", f"Meters: {meters}\nCentimeters: {centimeters:.1f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for feet and inches.")

def convert_lbskg():
    try:
        lbs = float(entry_lbs.get())
        conv = Conversion(None, lbs, None, None)  # Create a Conversion instance
        kg = conv.lbs_to_kg()  # Call the method on the instance
        conv = Conversion(None, lbs, None, None)  # Create a Conversion instance
        kg = conv.lbs_to_kg()  # Call the method on the instance
        messagebox.showinfo('Conversion Result', f'Killograms: {kg}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical value for LBS/pounds.")

def convert_ftoc():
    try:
        f = float(entry_f.get())
        conv = Conversion(f, None, None, None)  # Create a Conversion instance
        celsius = conv.f_to_celsius()  # Call the method on the instance
        conv = Conversion(f, None, None, None)  # Create a Conversion instance
        celsius = conv.f_to_celsius()  # Call the method on the instance
        messagebox.showinfo('Conversion Result', f'Celsius: {celsius}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numerical value for Fahrenheit.')

# GUI code starts here

# GUI code starts here

def clear_entries():
    entry_feet.delete(0, ttk.END)
    entry_inches.delete(0, ttk.END)
    entry_lbs.delete(0, ttk.END)
    entry_f.delete(0, ttk.END)   
    entry_feet.delete(0, ttk.END)
    entry_inches.delete(0, ttk.END)
    entry_lbs.delete(0, ttk.END)
    entry_f.delete(0, ttk.END)   

def SceneSwitch(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Tiny converter")

sv_ttk.set_theme("dark")

sv_ttk.set_theme("dark")

root.config(
    #bg='#CCCCFF'
    #bg='#CCCCFF'
)

f1 = Frame(root)  # Home
f2 = Frame(root)  # Temp
f3 = Frame(root)  # Weight
f4 = Frame(root)  # Height

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=2, sticky='nsew')  # Stack frames on top of each other

def on_select(event):
    index = sideb.curselection()

    if index:
        selected = sideb.get(index[0])
        if selected == 'Temperature':
            SceneSwitch(f2)
            print('selected f2')
        elif selected == 'Weight':
            SceneSwitch(f3)
            print('selected f3')
        elif selected == 'Height':
            SceneSwitch(f4)
            print('selected f4')
        else:
            SceneSwitch(f1)

sideb = Listbox(root)

sideb.insert(1, 'Temperature')
sideb.insert(1, 'Temperature')
sideb.insert(2, 'Weight')
sideb.insert(3, 'Height')
sideb.bind('<<ListboxSelect>>', on_select)
sideb.bind('<<ListboxSelect>>', on_select)
sideb.grid(
    row=0,
    column=0,
    rowspan=4,
    padx=10,
    pady=10,
    sticky='ns'
    pady=10,
    sticky='ns'
)

label_feet = ttk.Label(f4, text="Feet:")
label_feet.grid(row=0, column=0)
entry_feet = ttk.Entry(f4)
entry_feet.grid(row=1, column=1)

label_inches = ttk.Label(f4, text="Inches: ")
label_inches.grid(row=2, column=0)
entry_inches = ttk.Entry(f4)
entry_inches.grid(row=3, column=1)

label_lbs = ttk.Label(f3, text="Pounds: ")
label_lbs.grid(row=1, column=1)
entry_lbs = ttk.Entry(f3)
entry_lbs.grid(row=2, column=2)

label_f = ttk.Label(f2, text='Fahrenheit: ')
label_f.grid(row=1, column=0)
entry_f = ttk.Entry(f2)
entry_f.grid(row=2, column=1)

btn_conv_ftinch = ttk.Button(
    f4,
    text="Convert",
    command=convert_ftinch)
btn_conv_ftinch.grid(row=4, column=1, columnspan=1)

btn_conv_lbs = ttk.Button(
    f3,
    text='Convert',
    command=convert_lbskg
)
btn_conv_lbs.grid(row=4, column=2, columnspan=3)

btn_conv_ftoc = ttk.Button(
    f2,
    text='Convert',
    command=convert_ftoc
)
btn_conv_ftoc.grid(row=3, column=1, columnspan=3)

root.mainloop()