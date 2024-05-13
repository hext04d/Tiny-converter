<<<<<<< HEAD
from tkinter import *
def gantihal(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='goto frame 2', command=lambda:gantihal(f2)).pack()
Label(f1, text='this is in frame 1').pack()

Label(f2, text='this is in frame two').pack()
Button(f2, text='goto frame 3', command=lambda:gantihal(f3)).pack()

Label(f3, text='this is in frame 3').pack(side='left')
Button(f3, text='next frame :)', command=lambda:gantihal(f4)).pack(side='left')

Label(f4, text='fourth frame').pack()
Button(f4, text='goto 1st frame', command=lambda:gantihal(f1)).pack()

gantihal(f1)
root.mainloop()
=======
import customtkinter as ctk
import tkinter as tk

class NavBar(tk.Frame):  # Inherits from tk.Frame
    def __init__(self, master=None, segments=[], command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.segments = segments
        self.command = command
        self.selected_index = None
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i, segment in enumerate(self.segments):
            button = ctk.CTkButton(self, text=segment, command=lambda idx=i: self.select_segment(idx))
            button.grid(row=0, column=i, sticky="ew")
            self.buttons.append(button)

    def select_segment(self, index):
        if index != self.selected_index:
            if self.selected_index is not None:
                self.buttons[self.selected_index].config(relief=tk.RAISED)
            self.selected_index = index
            self.buttons[index].config(relief=tk.SUNKEN)
            if self.command:
                self.command(index)

# Example usage
def segment_selected(index):
    print(f"Segment {index} selected")

root = tk.Tk()
root.title('Tiny Converter')
root.geometry('400x500')

segments = ["Segment 1", "Segment 2", "Segment 3"]
segmented_menu = NavBar(root, segments=segments, command=segment_selected)
segmented_menu.pack(padx=10, pady=10)

root.mainloop()
>>>>>>> 234ed0f4390f5dd2a6e9c92ee4db2b6c0cb9e87f
