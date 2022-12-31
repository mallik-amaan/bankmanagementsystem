from tkinter import *
def newaccount():
    import newaccount
ac_sc=Toplevel()

ac_sc.maxsize(500,720)
ac_sc.minsize(500,720)

bgimage1=PhotoImage(file="bg4.png")
Label(ac_sc,image=bgimage1).place(x=0,y=0)

mgimage=PhotoImage(file="accountant.png")
Label(ac_sc,image=mgimage,bg="#181D31").place(x=20,y=20)

Label(ac_sc,text="Accountant",font=("Tw Cen MT",35,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=30)

b1=Button(ac_sc,text="Cash Deposit",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",padx=30,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE)
b1.place(x=130,y=230)

b2=Button(ac_sc,text=" Show Accounts ",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",padx=10,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE)
b2.place(x=130,y=320)

b3=Button(ac_sc,text="Create an Account",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE,command=newaccount)
b3.place(x=130,y=410)



ac_sc.mainloop()