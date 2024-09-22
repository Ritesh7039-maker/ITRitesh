#hotel booking window
import tkinter
from tkinter import *
# Creating the Main Window
window = tkinter.Tk()
window.title("Hotel Booking System")  # Set the window title
window.geometry('800x900')
# window.minsize(width=800, height=600)         # Set the window size

canvas = Canvas(height=300, width=800)
logo_img = PhotoImage(file="E:/internship python-programming/hotel_booking_system/logo1.png")
canvas.create_image(150, 50, image=logo_img)
canvas.grid(row=0, column=1)

# declaring string variable
# for storing name and password
email_var = StringVar()
passw_var = StringVar()

 
# defining a function that will
# get the name and password and 
# print them on the screen
def submit():

    email=email_var.get()
    password=passw_var.get()
    
    print("The name is : " + email)
    print("The password is : " + password)
    
    email_var.set("")
    passw_var.set("")
    
    
# creating a label for name using widget Label
email_label = Label(window, text = 'Email', font=('calibre',10, 'bold'))
 
# creating a entry for input name using widget Entry
email_entry = Entry(window,textvariable = email_var, font=('calibre',10,'normal'))
 
# creating a label for password
passw_label = Label(window, text = 'Password', font = ('calibre',10,'bold'))
 
# creating a entry for password
passw_entry = Entry(window, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
 
# creating a button using the widget Button that will call the submit function 
sub_btn = Button(window,text = 'Submit', command = submit)
 
# placing the label and entry in the required position using grid method
email_label.grid(row=1,column=0)
email_entry.grid(row=1,column=2)
passw_label.grid(row=2,column=0)
passw_entry.grid(row=2,column=2)
sub_btn.grid(row=3,column=2)

# Adding a Label                https://www.geeksforgeeks.org/python-tkinter-label/
label = Label(window, text="Welcome to PARADICE Hotel !", bg='yellow')
label.grid(row=0,column=1)                    # Doc: https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# Adding a Button
def button_click():
    label.config(text=entry.get())

button = Button(window, text="purpose:Click Me", command=button_click)
button.grid(row=4,column=1)

# Adding an Entry (Text Box)    Doc: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
entry = Entry(window, width=60)
entry.grid(row=4,column=0)
# user_input = entry.get() 

# Running the Application
window.mainloop()