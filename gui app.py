import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tempconv import ftin_to_mcm
from tempconv import lbs_to_kg
from tempconv import f_to_c_conv

def convert_ftinch():
    try:
        ft = float(entry_feet.get())
        inch = float(entry_inches.get())
        meters, centimeters = ftin_to_mcm(ft, inch)
        messagebox.showinfo("Conversion Result", f"Meters: {meters}\nCentimeters: {centimeters:.1f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for feet and inches.")

def convert_lbskg():
    try:
        lbs = float(entry_lbs.get())
        kg = lbs_to_kg(lbs)
        messagebox.showinfo('Conversion Result', f'Killograms: {kg}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical value for LBS/pounds.")

def convert_ftoc():
    try:
        f = float(entry_f.get())
        celsius = f_to_c_conv(f)
        messagebox.showinfo('Conversion Result', f'Celsius: {celsius}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numerical value for Fahrenheit.')

def clear_entries():
    # Clear entry widgets
    entry_feet.delete(0, tk.END)
    entry_inches.delete(0, tk.END)
    entry_lbs.delete(0, tk.END)
    entry_f.delete(0, tk.END)   

def on_select(event):
    index=sideb.curselection()

    if index: 
        selected = sideb.get(index)
        if selected == 'Temperature':
            clear_entries()
            label_f.config(text='Fahrenheit')
            btn_conv_ftoc.config(command=convert_ftoc)
        elif selected== 'Weight':
            clear_entries()
            label_lbs.config(text='LBS/Pounds:')
            btn_conv_lbs.config(command=convert_lbskg)
        elif selected == "Height":
            # Show height conversion options
            clear_entries()
            label_feet.config(text="Feet:")
            label_inches.config(text="Inches:")
            btn_conv_ftinch.config(command="")
            btn_conv_ftoc.config(command=convert_ftoc)



root = tk.Tk()
root.title("Tiny converter")

root.config(
    bg='#CCCCFF'
)

sideb = Listbox(root)

sideb.insert(1, 'Temperature'),
sideb.insert(2, 'Weight')
sideb.insert(3, 'Height')
sideb.grid(
    row=0,
    column=0,
    rowspan=4,
    padx=10,
    pady=10
)



label_feet = tk.Label(root, text="Feet:")
label_feet.grid(row=0, column=1)
entry_feet = tk.Entry(root)
entry_feet.grid(row=0, column=1)

label_inches = tk.Label(root, text="Inches:")
label_inches.grid(row=1, column=0)
entry_inches = tk.Entry(root)
entry_inches.grid(row=1, column=1)

label_lbs = tk.Label(root, text="Pounds:")
label_lbs.grid(row=2, column=0)
entry_lbs = tk.Entry(root)
entry_lbs.grid(row=2, column=1)

label_f = tk.Label(root, text='Fahrenheit:')
label_f.grid(row=3, column=0)
entry_f = tk.Entry(root)
entry_f.grid(row=3, column=1)



btn_conv_ftinch = tk.Button(
    root,
    text="Convert",
    command=convert_ftinch)
btn_conv_ftinch.grid(row=1, column=2, columnspan=1)

btn_conv_lbs = tk.Button(
    root,
    text='Convert',
    command=convert_lbskg
)
btn_conv_lbs.grid(row=2, column=2,columnspan=3)

btn_conv_ftoc = tk.Button(
    root,
    text = 'Convert',
    command=convert_ftoc

)
btn_conv_ftoc.grid(row=3, column=2, columnspan=1)

root.mainloop()
