import tkinter

windows = tkinter.Tk()  # initial a window
windows.geometry("600x600")
windows.title("Howdy!")
windows.config(padx=100, pady=200)

# initial a label component.
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "Hello"

# show the label in the window.
#my_label.pack(side="left")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)
# Entry
input = tkinter.Entry(width = 10)
#input.pack()
input.grid(row=2, column=3)
# You can't mix up grid() and pack() in the same program.

# create the button
def botton_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

def new_botton_clicked():
    print("New Button got clicked")



botton = tkinter.Button(text = "Click Me", command = botton_clicked)
#botton.pack()
# You can't mix up grid() and pack() in the same program.
#botton.place(x = 1, y = 1)
botton.grid(row=1, column=1)


new_botton = tkinter.Button(text = "New Button", command = new_botton_clicked)
new_botton.grid(row=0, column=2)



#
# writing the main code inside
#

# define an unlimited args in function.
def add(*args):
    print(type(args))  # the type is 'tuple'
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(3, 5, 6, 8, 10)


def calculate(n, **kwargs):
    print(type(kwargs))  # the type is 'dictionary'.
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    print(kwargs)

calculate(2, add=3, multiply=5)

class Car():
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")  # .get("xxx") - to avoid building error
        self.model = kw.get("model")

#my_car = Car(make = "Tesla", model = "Model Y")
my_car = Car(make = "Tesla")
print(my_car.model)  # print "None" as there is no default value of "model"


def all_aboard(**kw):
    print(kw)

all_aboard(x=10, y=64)

windows.mainloop()  # keep the window GUI appeared on the screen.
