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
        messagebox.showerror('ERROR','Please Enter the Name of Tablet')
    elif e2.get()=="":
        messagebox.showerror('ERROR','Please Enter Reference No.')    
    elif e3.get()=="":
        messagebox.showerror('ERROR','Please Enter Dose')
    elif e4.get()=="":
        messagebox.showerror('ERROR','Please Enter Number of tablets')
    elif e5.get()=="":
        messagebox.showerror('ERROR','Please Enter issue Date')
    elif e6.get()=="":
        messagebox.showerror('ERROR','Please Enter Expiry Date')
    elif e7.get()=="":
        messagebox.showerror('ERROR','Please Enter Daily Dose')
    elif e8.get()=="":
        messagebox.showerror('ERROR','Please Enter Side Effect')
    elif e9.get()=="":
        messagebox.showerror('ERROR','Please Enter Blood Groop')
    elif e10.get()=="":
        messagebox.showerror('ERROR','Please Enter the age')
    elif e11.get()=="":
        messagebox.showerror('ERROR','Please Enter The gender')
    elif e12.get()=="":
        messagebox.showerror('ERROR','Please Enter The Patient ID')
    elif e13.get()=="":
        messagebox.showerror('ERROR','Please Enter Name Of patient')
    elif e14.get()=="":
        messagebox.showerror('ERROR','Please Enter DOB')
    elif e15.get()=="":
        messagebox.showerror('ERROR','Please Enter Patient address')
    else:
        con = mysql.connector.connect(host='localhost',username='root',password='gupta@123',database='project')
        my_cursor=con.cursor()
        my_cursor.execute('insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            bp.get(),
            age.get(),
            gender.get(),
            patientid.get(),
            nameofpatient.get(),
            dob.get(),
            patientaddress.get(),
            ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo('Success','Record has been inserted')
def fetch_data():
        con = mysql.connector.connect(host='localhost',username='root',password='gupta@123',database='project')
        my_cursor=con.cursor()
        my_cursor.execute('select * from hospital')
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
    nameoftablets.set(row[0])
    ref.set(row[1]),
    dose.set(row[2]),
    nooftablets.set(row[3]),
    issuedate.set(row[4]),
    expdate.set(row[5]),
    dailydose.set(row[6]),
    sideeffect.set(row[7]),
    bp.set(row[8]),
    age.set(row[9]),
    gender.set(row[10]),
    patientid.set(row[11]),
    nameofpatient.set(row[12]),
    dob.set(row[13]),
    patientaddress.set(row[14]),

def pre():
    txt_frm.insert(END,'Name of Tablet:\t\t\t'+nameoftablets.get()+'\n')
    txt_frm.insert(END,'Refernce No:\t\t\t'+ref.get()+'\n')
    txt_frm.insert(END,'Dose:\t\t\t'+dose.get()+'\n')
    txt_frm.insert(END,'No. of Tablet:\t\t\t'+nooftablets.get()+'\n')
    txt_frm.insert(END,'Issue Date:\t\t\t'+issuedate.get()+'\n')
    txt_frm.insert(END,'Expiry Date:\t\t\t'+expdate.get()+'\n')
    txt_frm.insert(END,'Daily Dose:\t\t\t'+dailydose.get()+'\n')
    txt_frm.insert(END,'Side Effect:\t\t\t'+sideeffect.get()+'\n')
    txt_frm.insert(END,'Blood Group:\t\t\t'+bp.get()+'\n')
    txt_frm.insert(END,'Age:\t\t\t'+age.get()+'\n')
    txt_frm.insert(END,'Gender:\t\t\t'+gender.get()+'\n')
    txt_frm.insert(END,'Patient ID:\t\t\t'+patientid.get()+'\n')
    txt_frm.insert(END,'Name of Patient:\t\t\t'+nameofpatient.get()+'\n')
    txt_frm.insert(END,'DOB:\t\t\t'+dob.get()+'\n')
    txt_frm.insert(END,'Patient Address:\t\t\t'+patientaddress.get()+'\n')

#Delete Botton
def delete():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to Delete')
    if confirm>0:
        con = mysql.connector.connect(host='localhost',username='root',password='gupta@123',database='project')
        my_cursor=con.cursor()
        querry=('delete from hospital where Reference=%s')
        value=(ref.get(),)
        my_cursor.execute(querry,value)
        con.commit()
        con.close()
        fetch_data()
        messagebox.showinfo('Deleted','Patient Data has been deleted')

#Clear Botton
def clear():
    nameoftablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    sideeffect.set('')
    bp.set('')
    age.set('')
    gender.set('')
    patientid.set('')
    nameofpatient.set('')
    dob.set('')
    patientaddress.set('')
    txt_frm.delete(1.0,END)
#Exit Button
def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        import menu
#Heading
Label (win, text='+ Hospital Management System  +', font ='inpack 31 bold',bg='blue',fg='red').pack()

#frame1
frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=50,width=1920,height=500)
#Label Frame - Patient Info
lf1=LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10,bg='orange')
lf1.place(x=10,y=10,width=1200,height=460)

#Labels - Patient info
Label(lf1,text='Name of Tablets',bg='orange',font='ariel 15').place(x=5,y=10)
Label(lf1,text='Reference No.',bg='orange',font='ariel 15').place(x=5,y=50)
Label(lf1,text='Dose',bg='orange',font='ariel 15').place(x=5,y=90)
Label(lf1,text='No. of Tablets',bg='orange',font='ariel 15').place(x=5,y=130)
Label(lf1,text='Issue Date',bg='orange',font='ariel 15').place(x=5,y=170)
Label(lf1,text='Expire Date',bg='orange',font='ariel 15').place(x=5,y=210)
Label(lf1,text='Daily Dose',bg='orange',font='ariel 15').place(x=5,y=250)
Label(lf1,text='Side Effect',bg='orange',font='ariel 15').place(x=5,y=290)
Label(lf1,text='Blood Group',bg='orange',font='ariel 15').place(x=5,y=330)
Label(lf1,text='Age',bg='orange',font='ariel 15').place(x=5,y=370)
Label(lf1,text='Gender (M/F)',bg='orange',font='ariel 15').place(x=570,y=10)
Label(lf1,text='Patient ID',bg='orange',font='ariel 15').place(x=570,y=50)
Label(lf1,text='Name Of patient',bg='orange',font='ariel 15').place(x=570,y=90)
Label(lf1,text='DOB (YYYY-MM-DD)',bg='orange',font='ariel 15').place(x=570,y=130)
Label(lf1,text='Patient Address',bg='orange',font='ariel 15').place(x=570,y=170)


#Textvariable
nameoftablets = StringVar()
ref = StringVar()
dose = StringVar()
nooftablets=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
bp=StringVar()
age=StringVar()
gender=StringVar()
patientid=StringVar()
nameofpatient=StringVar()
dob=StringVar()
patientaddress=StringVar()

#Entry Field
e1=Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=200,y=10,width=300)
e2=Entry(lf1,bd=4,textvariable=ref)
e2.place(x=200,y=50,width=300)
e3=Entry(lf1,bd=4,textvariable=dose)
e3.place(x=200,y=90,width=300)
e4=Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=200,y=130,width=300)
e5=Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=200,y=170,width=300)
e6=Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=200,y=210,width=300)
e7=Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=200,y=250,width=300)
e8=Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=200,y=290,width=300)
e9=Entry(lf1,bd=4,textvariable=bp)
e9.place(x=200,y=330,width=300)
e10=Entry(lf1,bd=4,textvariable=age)
e10.place(x=200,y=370,width=300)
e11=Entry(lf1,bd=4,textvariable=gender)
e11.place(x=800,y=10,width=300)
e12=Entry(lf1,bd=4,textvariable=patientid)
e12.place(x=800,y=50,width=300)
e13=Entry(lf1,bd=4,textvariable=nameofpatient)
e13.place(x=800,y=90,width=300)
e14=Entry(lf1,bd=4,textvariable=dob)
e14.place(x=800,y=130,width=300)
e15=Entry(lf1,bd=4,textvariable=patientaddress)
e15.place(x=800,y=170,width=300)


#Label Frame - Prescription
lf2=LabelFrame(frame1,text='Prescription',font='ariel 12 bold',bg='grey',bd=10)
lf2.place(x=1220,y=10,width=670,height=460)
#Textbox
txt_frm=Text(lf2,font='ariel 12 bold',width=40,height=40,bg='yellow')
txt_frm.pack(fill=BOTH)
#frmae2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=560,width=1920,height=400)


#Botton
#prescription botton
del_btn=Button(win,text='Delete',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=delete)
del_btn.place(x=0,y=970,width=350)
#prescription botton
pre_btn=Button(win,text='Prescription',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=pre)
pre_btn.place(x=350,y=970,width=420)
#save prescription data botton
pd_btn=Button(win,text='Save Drescription Data',font='ariel 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command=pd)
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
table = ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','sd','bp','age','gen','pid','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)


#Heading - Table
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference No.')
table.heading('dose',text='Dose')
table.heading('nots',text='No. of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Expire Date')
table.heading('dd',text='Daily Dose')
table.heading('sd',text='Side Effects')
table.heading('bp',text='Blood Group')
table.heading('age',text='Age')
table.heading('gen',text='Gender')
table.heading('pid',text='Patient ID')
table.heading('pn',text='Patient Name')
table.heading('dob',text='DOB')
table.heading('pa',text='Patient Adress')
table['show']='headings'
table.pack(fill=BOTH,expand=1)
table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('bp',width=100)
table.column('age',width=100)
table.column('gen',width=100)
table.column('pid',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()

