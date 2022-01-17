import tkinter

# *args allows unknown num of params
# creates tuple of args
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(0,3))
print(add(1,3,5))
print(add(1,3,5,6,7,8))

# **kwargs does same with keyword args
# creates dict of args
def calc(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mult"]
    return n

print(calc(2, add=2, mult=1))
print(calc(2, add=2, mult=2))

# will crash if all args not listed
# use .get() instead of [] to return None instead

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(model="Evo")
print(my_car.make, my_car.model)




# tkinter testing

def change_text():
    lbl.config(text=inpt.get())

wndw = tkinter.Tk()
wndw.title("Test Window")
wndw.minsize(width=500, height=300)
wndw.config(padx=20, pady=20)

lbl = tkinter.Label(text="Label Here", font=("Ariel", 24, "bold"))
# lbl.pack()
# lbl.place(x=45,y=20)
lbl.grid(column=0, row=0)
lbl.config(padx=30, pady=30)

btn = tkinter.Button(text="click me",command=change_text)
btn.grid(column=1, row=1)

btn2 = tkinter.Button(text="new btn")
btn2.grid(column=2,row=0)

inpt = tkinter.Entry(width=10)
inpt.grid(column=3, row=2)

# main loop at end
wndw.mainloop()

