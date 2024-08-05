import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tempconv import Conversion
import sv_ttk
class TinyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tiny Converter")

        sv_ttk.set_theme("dark")
        self.root.config()

        self.setup_frames()
        self.setup_widgets()
        self.clear_entries()

    def setup_frames(self):
        self.f1 = Frame(self.root)  # Home
        self.f2 = Frame(self.root)  # Temp
        self.f3 = Frame(self.root)  # Weight
        self.f4 = Frame(self.root)  # Height

        for frame in (self.f1, self.f2, self.f3, self.f4):
            frame.grid(row=0, column=2, sticky='nsew')  # Stack frames on top of each other

    def setup_widgets(self):
        self.sideb = Listbox(self.root)
        self.sideb.insert(1, 'Temperature')
        self.sideb.insert(2, 'Weight')
        self.sideb.insert(3, 'Height')
        self.sideb.bind('<<ListboxSelect>>', self.on_select)
        self.sideb.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky='ns')

        self.label_feet = ttk.Label(self.f4, text="Feet:")
        self.label_feet.grid(row=0, column=0)
        self.entry_feet = ttk.Entry(self.f4)
        self.entry_feet.grid(row=1, column=1)

        self.label_inches = ttk.Label(self.f4, text="Inches: ")
        self.label_inches.grid(row=2, column=0)
        self.entry_inches = ttk.Entry(self.f4)
        self.entry_inches.grid(row=3, column=1)

        self.label_lbs = ttk.Label(self.f3, text="Pounds: ")
        self.label_lbs.grid(row=1, column=1)
        self.entry_lbs = ttk.Entry(self.f3)
        self.entry_lbs.grid(row=2, column=2)

        self.label_f = ttk.Label(self.f2, text='Fahrenheit: ')
        self.label_f.grid(row=1, column=0)
        self.entry_f = ttk.Entry(self.f2)
        self.entry_f.grid(row=2, column=1)

        self.btn_conv_ftinch = ttk.Button(
            self.f4,
            text="Convert",
            command=self.convert_ftinch
        )
        self.btn_conv_ftinch.grid(row=4, column=1, columnspan=1)

        self.btn_conv_lbs = ttk.Button(
            self.f3,
            text='Convert',
            command=self.convert_lbskg
        )
        self.btn_conv_lbs.grid(row=4, column=2, columnspan=3)

        self.btn_conv_ftoc = ttk.Button(
            self.f2,
            text='Convert',
            command=self.convert_ftoc
        )
        self.btn_conv_ftoc.grid(row=3, column=1, columnspan=3)

    def on_select(self, event):
        index = self.sideb.curselection()
        if index:
            selected = self.sideb.get(index[0])
            if selected == 'Temperature':
                self.SceneSwitch(self.f2)
            elif selected == 'Weight':
                self.SceneSwitch(self.f3)
            elif selected == 'Height':
                self.SceneSwitch(self.f4)
            else:
                self.SceneSwitch(self.f1)

    def SceneSwitch(self, frame):
        frame.tkraise()

    def convert_ftinch(self):
        try:
            feet = float(self.entry_feet.get())
            inches = float(self.entry_inches.get())
            conv = Conversion(None, None, feet, inches)  # Create a Conversion instance
            meters, centimeters = conv.ftin_to_mcm()
            messagebox.showinfo("Conversion Result", f"Meters: {meters}\nCentimeters: {centimeters:.1f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for feet and inches.")

    def convert_lbskg(self):
        try:
            lbs = float(self.entry_lbs.get())
            conv = Conversion(None, lbs, None, None)  # Create a Conversion instance
            kg = conv.lbs_to_kg()  # Call the method on the instance
            messagebox.showinfo('Conversion Result', f'Kilograms: {kg}')
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical value for LBS/pounds.")

    def convert_ftoc(self):
        try:
            f = float(self.entry_f.get())
            conv = Conversion(f, None, None, None)  # Create a Conversion instance
            celsius = conv.f_to_celsius()  # Call the method on the instance
            messagebox.showinfo('Conversion Result', f'Celsius: {celsius}')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numerical value for Fahrenheit.')

    def clear_entries(self):
        self.entry_feet.delete(0, tk.END)
        self.entry_inches.delete(0, tk.END)
        self.entry_lbs.delete(0, tk.END)
        self.entry_f.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TinyConverterApp(root)
    root.mainloop()
