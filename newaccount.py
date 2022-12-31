from tkinter import *

newac=Toplevel()

newac.maxsize(500,720)
newac.minsize(500,720)

bgimage3=PhotoImage(file="bg3.png")
Label(newac,image=bgimage3).place(x=0,y=0)

Label(newac,text="Welcome",font=("Tw Cen MT",30,"bold"),fg="#181D31",bg="#F0E9D2").place(x=170,y=170)

name=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
name.bind("<Button-1>",lambda e: name.delete(0,END))
name.place(x=130,y=250)
name.insert(0,"Enter Name")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=270)

user=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
user.bind("<Button-1>",lambda e: user.delete(0,END))
user.place(x=130,y=300)
user.insert(0,"Enter Username")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=320)

passw=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
passw.bind("<Button-1>",lambda e: passw.delete(0,END))
passw.place(x=130,y=350)
passw.insert(0,"Create a Password")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=370)

cnic=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
cnic.bind("<Button-1>",lambda e: cnic.delete(0,END))
cnic.place(x=130,y=400)
cnic.insert(0,"Enter CNIC")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=420)

phno=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
phno.bind("<Button-1>",lambda e: phno.delete(0,END))
phno.place(x=130,y=450)
phno.insert(0,"Enter Phone no")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=470)
menu=StringVar()
menu.set("ACCOUNT TYPE")
accounttype=OptionMenu(newac,menu,"SAVINGS","CURRENT","FIXED DEPOSITS","FORIEGN CURRENCY","BASIC").place(x=130,y=500)

sub_button=Button(newac,text="Submit",font=("Tw Cen MT",15,"bold"),fg="#F0E9D2",bg="#181D31",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE)
sub_button.place(x=200,y=550)

newac.mainloop()
