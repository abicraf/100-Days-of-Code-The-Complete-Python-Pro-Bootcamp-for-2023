import tkinter

windows = tkinter.Tk()  # initial a window
windows.geometry("500x500")
windows.title("Howdy!")

# initial a label component.
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# show the label in the window.
my_label.pack(side="left")
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

add(3,5,6,8,10)


def calculate(**kwargs):
    print(type(kwargs))  # the type is 'dictionary'.

calculate()



windows.mainloop()  # keep the window GUI appeared on the screen.

