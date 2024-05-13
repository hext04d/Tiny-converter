import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
from tkinter import *
from tempconv import Conversion



def convert_ftinch():
    try:
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
        messagebox.showinfo('Conversion Result', f'Killograms: {kg}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical value for LBS/pounds.")

def convert_ftoc():
    try:
        f = float(entry_f.get())
        conv = Conversion(f, None, None, None)  # Create a Conversion instance
        celsius = conv.f_to_celsius()  # Call the method on the instance
        messagebox.showinfo('Conversion Result', f'Celsius: {celsius}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numerical value for Fahrenheit.')

# GUI code starts here

def clear_entries():
    entry_feet.delete(0, ttk.END)
    entry_inches.delete(0, ttk.END)
    entry_lbs.delete(0, ttk.END)
    entry_f.delete(0, ttk.END)   

def on_select(event):
    index = sideb.curselection()
    print("Selection event triggered")
    print("Index:", index)

    if index:
        selected = sideb.get(index[0]) 
        print("Selected item:", selected)

        if selected == 'Temperature':
            # Update labels and commands for temperature conversion
            label_f.config(text='Fahrenheit:')
            label_feet.config(text='')
            label_inches.config(text='')
            btn_conv_ftinch.config(command='')
            btn_conv_lbs.config(command='')
            btn_conv_ftoc.config(command=convert_ftoc)
        elif selected == 'Weight':
            # Update labels and commands for weight conversion
            label_lbs.config(text='Pounds:')
            label_f.config(text='')
            label_feet.config(text='')
            label_inches.config(text='')
            btn_conv_ftinch.config(command='')
            btn_conv_ftoc.config(command='')
            btn_conv_lbs.config(command=convert_lbskg)
        elif selected == 'Height':
            # Update labels and commands for height conversion
            label_feet.config(text='Feet:')
            label_inches.config(text='Inches:')
            label_f.config(text='')
            label_lbs.config(text='')
            btn_conv_ftoc.config(command='')
            btn_conv_lbs.config(command='')
            btn_conv_ftinch.config(command=convert_ftinch)
    else:
        print("No item selected")


root = tk.Tk()
root.title("Tiny converter")

sv_ttk.set_theme("dark")

root.config(
    #bg='#CCCCFF'
)

sideb = Listbox(root)

sideb.insert(1, 'Temperature')
sideb.insert(2, 'Weight')
sideb.insert(3, 'Height')
sideb.bind('<<ListboxSelect>>', on_select)
sideb.grid(
    row=0,
    column=0,
    rowspan=4,
    padx=10,
    pady=10,
    sticky='ns'
)

label_feet = ttk.Label(root, text="Feet:")
label_feet.grid(row=0, column=1)
entry_feet = ttk.Entry(root)
entry_feet.grid(row=1, column=2)

label_inches = ttk.Label(root, text="Inches:")
label_inches.grid(row=1, column=0)
entry_inches = ttk.Entry(root)
entry_inches.grid(row=1, column=2)

label_lbs = ttk.Label(root, text="Pounds:")
label_lbs.grid(row=2, column=0)
entry_lbs = ttk.Entry(root)
entry_lbs.grid(row=2, column=2)

label_f = ttk.Label(root, text='Fahrenheit:')
label_f.grid(row=3, column=0)
entry_f = ttk.Entry(root)
entry_f.grid(row=3, column=2)

btn_conv_ftinch = ttk.Button(
    root,
    text="Convert",
    command=convert_ftinch)
btn_conv_ftinch.grid(row=1, column=2, columnspan=1)

btn_conv_lbs = ttk.Button(
    root,
    text='Convert',
    command=convert_lbskg
)
btn_conv_lbs.grid(row=2, column=2,columnspan=3)

btn_conv_ftoc = ttk.Button(
    root,
    text = 'Convert',
    command=convert_ftoc

)
btn_conv_ftoc.grid(row=3, column=2, columnspan=1)


root.mainloop()
