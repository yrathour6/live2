from tkinter import *
from tkinter.ttk import *
window=Tk()
window.geometry('350x200')
window.title("weicome")
#chk_state.set=BooleanVar()

#chk_state.set(True)
chk=Checkbutton(window,text="choose")
chk.grid(column=0,row=0)
window.mainloop()
