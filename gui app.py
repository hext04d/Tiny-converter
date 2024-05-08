import tkinter as tk
from tkinter import messagebox
from tempconv import ftin_to_mcm  # Import function
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


# Create the main window
root = tk.Tk()
root.title("Tiny converter")

root.config(
    bg='#CCCCFF'
)

# Create labels and entry widgets
label_feet = tk.Label(root, text="Feet:")
label_feet.grid(row=0, column=0)
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


# Create convert button
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
