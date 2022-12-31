from tkinter import *

def mainscreen():
    import accountantmainscreen

mg=Toplevel()
mg.maxsize(500,720)
mg.minsize(500,720)

bgimage1=PhotoImage(file="bg 2.png")
Label(mg,image=bgimage1).place(x=0,y=0)

mgimage=PhotoImage(file="accountant.png")
Label(mg,image=mgimage,bg="#181D31").place(x=200,y=170)

Label(mg,text="Log in as Accountant",font=("Tw Cen MT",25,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=90,y=270)

user=Entry(mg,width=25,fg="#F0E9D2",border=0,bg="#181D31",font=("Ariel",12))
user.place(x=130,y=350)
user.insert(0,"Username")
userimg=PhotoImage(file="username.png")
Label(mg,image=userimg,bg="#181D31").place(x=80,y=340)
Frame(mg,width=250,height=2,bg="#F0E9D2").place(x=130,y=370)

passw=Entry(mg,width=25,fg="#F0E9D2",border=0,bg="#181D31",font=("Ariel",12))
passw.place(x=130,y=420)
passw.insert(0,"Password")
passimg=PhotoImage(file="password.png")
Label(mg,image=passimg,bg="#181D31").place(x=80,y=410)
Frame(mg,width=250,height=2,bg="#F0E9D2").place(x=130,y=440)

sub_button=Button(mg,text="Submit",font=("Tw Cen MT",15,"bold"),fg="#F0E9D2",bg="#678983",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE,command=mainscreen)
sub_button.place(x=200,y=480)

Frame(mg,width=300,height=50,bg="#678983").place(x=220,y=640)
mg.mainloop()
