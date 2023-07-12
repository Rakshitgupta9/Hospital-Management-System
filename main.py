from tkinter import *
from tkinter import ttk
from tkinter import messagebox
pas = Tk()
pas.geometry('200x200')
pas.config(bg='black')
def show():
    p = password.get() #get password from entry
    if (p=='admin'):
        pas.destroy()
        import menu

    elif (p==''):
        messagebox.showerror('Retry','Password cannot be empty')
    else:
        messagebox.showerror('Retry','Incorrect Password')
def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        pas.destroy()
        return
    
#Heading
Label (pas, text='Enter The password', font ='inpack 12 bold',bg='red',fg='white').pack()

password = StringVar() #Password variable
passEntry = Entry(pas, textvariable=password, show='*')
submit = Button(pas, text='Go to menu',cursor='hand2',command=show)

passEntry.place(x=40,y=70) 
submit.place(x=55,y=95,width = 100)

#Exit botton
exit_btn=Button(pas,text='Exit',bg='red',fg='white',cursor='hand2',command=exit)
exit_btn.place(x=55,y=125,width=100)

mainloop()
