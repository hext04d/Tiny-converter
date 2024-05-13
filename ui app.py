import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Tiny Converter')
        self.geometry('400x500')
        self.grid_columnconfigure((0,1), weight=1)

class NavBar(tk.Frame):
    def __init__(self, master=None, segments=[], command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.segments = segments
        self.command = command
        self.selected_index = None
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i, segment in enumerate(self.segments):
            button = ctk.CTkButton(
        self,
        text=segment,
        command=lambda idx=i: self.select_segment(idx)
            )
            button.grid(row=0, column=i, sticky='ew')
            self.buttons.append(button)
    
    def select_segment(self, index):
        if index != self.selected_index:
            if self.selected_index is not None:
               # self.buttons[self.selected_index].configure(relief=tk.RAISED)
                self.selected_index = index
            self.buttons[index].configure(relief=tk.SUNKEN)
            if self.command:
                self.command(index)
    
def segment_selected(index): 
    print(f'Segment {index} selected')

segments = ['Temperature', 'Weight', 'Length']
app = App()
segmented_menu = NavBar(app, segments=segments, command=segment_selected)
segmented_menu.pack(padx=10, pady=10)
app.mainloop()
