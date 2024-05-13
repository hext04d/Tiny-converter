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
