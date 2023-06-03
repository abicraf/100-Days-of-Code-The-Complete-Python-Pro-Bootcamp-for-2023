from tkinter import *

windows = Tk()
windows.geometry("400x300")
windows.title("Mile to KM Converter")
windows.config(padx=100, pady=100)

input = Entry(width=5)
input.grid(row=0,column=1)
#Add some text to begin with
input.insert(END, string="0")


mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def mile_to_km():
    # Gets text in entry
    mile = float(input.get())
    km = round(mile*1.609344)
    #print(km)
    km_result = Label()
    km_result.config(text=km)
    km_result.grid(row=1, column=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(row=2, column=1)



windows.mainloop()