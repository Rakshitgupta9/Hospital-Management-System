from tkinter import *
from tkinter import ttk
from tkinter import messagebox

menu = Tk()
menu.geometry("900x900")
menu.config(bg='black')

#Functions
def pr():
    menu.destroy()
    import HMS

def dt():
    menu.destroy()
    import dr
    
def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        menu.destroy()
        return
#Heading
Label (menu, text='MENU', font ='inpack 31 bold',bg='red',fg='white').pack()

#precription Botton
pr_btn=Button(menu,text='Precription managment',font='ariel 15 bold',bg='white',fg='red',bd=6,cursor='hand2',command=pr)
pr_btn.place(x=250,y=200,width=450)

#precription Botton
pr_btn=Button(menu,text='Doctor managment',font='ariel 15 bold',bg='white',fg='red',bd=6,cursor='hand2',command=dt)
pr_btn.place(x=250,y=300,width=450)


#Exit botton
exit_btn=Button(menu,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=exit)
exit_btn.place(x=250,y=400,width=450)


mainloop()
