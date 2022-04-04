from tkinter import *


win = Tk()
win.geometry("550x550")
win.resizable(1,1)
win.title("Magic The Gathering Life Counter")


canvas = Canvas(win, width=287, height=30, bg="grey")

canvas.create_text(287, 30, text="Magic The Gathering Life Counter", fill="black", font="Arial")
canvas.pack()



def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)



input_text = StringVar()


input_frame = Frame(win, width=575, height=550, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 13, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(win, width=575, height=550, bg="grey")
btns_frame.pack()




#run app
win.mainloop()