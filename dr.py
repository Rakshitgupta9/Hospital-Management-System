from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win = Tk()
win.state('zoomed')
win.config(bg='black')
#Botton Function
def pd():
    if e1.get()=="":
        messagebox.showerror('ERROR','Please Enter the Name of Doctor')
    elif e2.get()=="":
        messagebox.showerror('ERROR','Please Enter Doctor ID')    
    elif e3.get()=="":
        messagebox.showerror('ERROR','Please Enter Gender')
    elif e4.get()=="":
        messagebox.showerror('ERROR','Please Enter E-mail')
    elif e5.get()=="":
        messagebox.showerror('ERROR','Please Enter Phone')
    elif e6.get()=="":
        messagebox.showerror('ERROR','Please Enter Specialist in')
    elif e7.get()=="":
        messagebox.showerror('ERROR','Please Enter DOB')
    elif e8.get()=="":
        messagebox.showerror('ERROR','Please Enter Blood Group')
    elif e9.get()=="":
        messagebox.showerror('ERROR','Please Enter Age')
    elif e10.get()=="":
        messagebox.showerror('ERROR','Please Enter Appointment Date')
    elif e11.get()=="":
        messagebox.showerror('ERROR','Please Enter Block')
    elif e12.get()=="":
        messagebox.showerror('ERROR','Please Enter Address')
    else:
        con = mysql.connector.connect(host='localhost',username='root',password='gupta@123',database='project')
        my_cursor=con.cursor()
        my_cursor.execute('insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            nod.get(),
            di.get(),
            gen.get(),
            mail.get(),
            phn.get(),
            sp.get(),
            dob.get(),
            bg.get(),
            age.get(),
            ad.get(),
            bop.get(),
            add.get(),
            ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo('Success','Record has been inserted')
def fetch_data():
        con = mysql.connector.connect(host='localhost',username='root',password='gupta@123',database='project')
        my_cursor=con.cursor()
        my_cursor.execute('select * from doctor')
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            table.delete(* table.get_children())
            for items in rows:
                table.insert('',END,values=items)
            con.commit()
        con.close()
def get_data(event=''):
    cursor_row=table.focus()
    data = table.item(cursor_row)
    row=data['values']
    nod.set(row[0]),
    di.set(row[1]),
    gen.set(row[2]),
    mail.set(row[3]),
    phn.set(row[4]),
    sp.set(row[5]),
    dob.set(row[6]),
    bg.set(row[7]),
    age.set(row[8]),
    ad.set(row[9]),
    bop.set(row[10]),
    add.set(row[11]),

def pre():
    txt_frm.insert(END,'Name of doctor:\t\t\t'+nod.get()+'\n')
    txt_frm.insert(END,'Doctor ID:\t\t\t'+di.get()+'\n')
    txt_frm.insert(END,'Gender:\t\t\t'+gen.get()+'\n')
    txt_frm.insert(END,'E-mail:\t\t\t'+mail.get()+'\n')
    txt_frm.insert(END,'Phone:\t\t\t'+phn.get()+'\n')
    txt_frm.insert(END,'Specialist:\t\t\t'+sp.get()+'\n')
    txt_frm.insert(END,'DOB:\t\t\t'+dob.get()+'\n')
    txt_frm.insert(END,'Blood Group:\t\t\t'+bg.get()+'\n')
    txt_frm.insert(END,'Age:\t\t\t'+age.get()+'\n')
    txt_frm.insert(END,'Appointment Date:\t\t\t'+ad.get()+'\n')
    txt_frm.insert(END,'Block:\t\t\t'+bop.get()+'\n')
    txt_frm.insert(END,'Address:\t\t\t'+add.get()+'\n')

#Delete Botton
def delete():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to Delete')
    if confirm>0:
        con = mysql.connector.connect(host='localhost',username='root',password='gupta@123',database='project')
        my_cursor=con.cursor()
        querry=('delete from doctor where Reference=%s')
        value=(di.get(),)
        my_cursor.execute(querry,value)
        con.commit()
        con.close()
        fetch_data()
        messagebox.showinfo('Deleted','Doctor Data has been deleted')

#Clear Botton
def clear():
    nod.set('')
    di.set('')
    gen.set('')
    mail.set('')
    phn.set('')
    sp.set('')
    dob.set('')
    bg.set('')
    age.set('')
    ad.set('')
    bop.set('')
    add.set('')
    txt_frm.delete(1.0,END)
#Exit Button
def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        import menu
#Heading
Label (win, text='+ Doctor Management System  +', font ='inpack 31 bold',bg='silver',fg='red').pack()

#frame1
frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=50,width=1920,height=500)
#Label Frame - Patient Info
lf1=LabelFrame(frame1,text='Doctor Information',font='ariel 10 bold',bd=10,bg='grey')
lf1.place(x=10,y=10,width=1200,height=460)

#Labels - Patient info
Label(lf1,text='Name of Doctor',bg='grey',font='ariel 15').place(x=5,y=10)
Label(lf1,text='Doctor ID',bg='grey',font='ariel 15').place(x=5,y=50)
Label(lf1,text='Gender',bg='grey',font='ariel 15').place(x=5,y=90)
Label(lf1,text='E-mail',bg='grey',font='ariel 15').place(x=5,y=130)
Label(lf1,text='Phone',bg='grey',font='ariel 15').place(x=5,y=170)
Label(lf1,text='Specialist',bg='grey',font='ariel 15').place(x=5,y=210)
Label(lf1,text='DOB',bg='grey',font='ariel 15').place(x=5,y=250)
Label(lf1,text='Blood Group',bg='grey',font='ariel 15').place(x=5,y=290)
Label(lf1,text='Age',bg='grey',font='ariel 15').place(x=5,y=330)
Label(lf1,text='Appointment Date',bg='grey',font='ariel 15').place(x=5,y=370)
Label(lf1,text='Block',bg='grey',font='ariel 15').place(x=570,y=10)
Label(lf1,text='Address',bg='grey',font='ariel 15').place(x=570,y=50)


#Textvariable
nod=StringVar()
di=StringVar()
gen=StringVar()
mail=StringVar()
phn=StringVar()
sp=StringVar()
dob=StringVar()
bg=StringVar()
age=StringVar()
ad=StringVar()
bop=StringVar()
add=StringVar()

#Entry Field
e1=Entry(lf1,bd=4,textvariable=nod)
e1.place(x=200,y=10,width=300)
e2=Entry(lf1,bd=4,textvariable=di)
e2.place(x=200,y=50,width=300)
e3=Entry(lf1,bd=4,textvariable=gen)
e3.place(x=200,y=90,width=300)
e4=Entry(lf1,bd=4,textvariable=mail)
e4.place(x=200,y=130,width=300)
e5=Entry(lf1,bd=4,textvariable=phn)
e5.place(x=200,y=170,width=300)
e6=Entry(lf1,bd=4,textvariable=sp)
e6.place(x=200,y=210,width=300)
e7=Entry(lf1,bd=4,textvariable=dob)
e7.place(x=200,y=250,width=300)
e8=Entry(lf1,bd=4,textvariable=bg)
e8.place(x=200,y=290,width=300)
e9=Entry(lf1,bd=4,textvariable=age)
e9.place(x=200,y=330,width=300)
e10=Entry(lf1,bd=4,textvariable=ad)
e10.place(x=200,y=370,width=300)
e11=Entry(lf1,bd=4,textvariable=bop)
e11.place(x=800,y=10,width=300)
e12=Entry(lf1,bd=4,textvariable=add)
e12.place(x=800,y=50,width=300)

#Label Frame - Prescription
lf2=LabelFrame(frame1,text='Prescription',font='ariel 12 bold',bg='blue',bd=10)
lf2.place(x=1220,y=10,width=670,height=460)
#Textbox
txt_frm=Text(lf2,font='ariel 12 bold',width=40,height=40,bg='cyan')
txt_frm.pack(fill=BOTH)
#frmae2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=560,width=1920,height=400)


#Botton
#Delete botton
del_btn=Button(win,text='Delete',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=delete)
del_btn.place(x=0,y=970,width=350)
#prescription botton
pre_btn=Button(win,text='Details',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=pre)
pre_btn.place(x=350,y=970,width=420)
#save prescription data botton
pd_btn=Button(win,text='Save Detail',font='ariel 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command=pd)
pd_btn.place(x=770,y=970,width=450)
#clear botton
clr_btn=Button(win,text='Clear',font='ariel 15 bold',bg='green',fg='white',bd=6,cursor='hand2',command=clear)
clr_btn.place(x=1220,y=970,width=350)
#Exit botton
exit_btn=Button(win,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=exit)
exit_btn.place(x=1570,y=970,width=350)


#Scroll Bar
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill=X)
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill=Y)
table = ttk.Treeview(frame2,columns=('nod','di','gen','mail','phn','sp','dob','bg','age','ad','bop','add'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)


#Heading - Table
table.heading('nod',text='Name of doctor')
table.heading('di',text='Doctor ID')
table.heading('gen',text='Gender')
table.heading('mail',text='E-mail')
table.heading('phn',text='Phone')
table.heading('sp',text='Specialist')
table.heading('dob',text='DOB')
table.heading('bg',text='Blood Group')
table.heading('age',text='Age')
table.heading('ad',text='Appointment Date')
table.heading('bop',text='Block')
table.heading('add',text='Address')
table['show']='headings'
table.pack(fill=BOTH,expand=1)
table.column('nod',width=100)
table.column('di',width=100)
table.column('gen',width=100)
table.column('mail',width=100)
table.column('phn',width=100)
table.column('sp',width=100)
table.column('dob',width=100)
table.column('bg',width=100)
table.column('age',width=100)
table.column('ad',width=100)
table.column('bop',width=100)
table.column('add',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()

