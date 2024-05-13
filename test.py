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