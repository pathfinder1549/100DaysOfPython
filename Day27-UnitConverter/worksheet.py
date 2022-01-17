import tkinter

wndw = tkinter.Tk()
wndw.title("Test Window")
wndw.minsize(width=500, height=300)

lbl = tkinter.Label(text="Label Here", font=("Ariel", 24, "bold"))
lbl.pack()



# main loop at end
wndw.mainloop()

