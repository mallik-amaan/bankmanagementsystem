from tkinter import *
def newaccount():
    import newaccount
mg_sc=Toplevel()

mg_sc.maxsize(500,720)
mg_sc.minsize(500,720)

bgimage1=PhotoImage(file="bg4.png")
Label(mg_sc,image=bgimage1).place(x=0,y=0)

mgimage=PhotoImage(file="manager.png")
Label(mg_sc,image=mgimage,bg="#181D31").place(x=20,y=20)

Label(mg_sc,text="Bank Manager",font=("Tw Cen MT",35,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=30)

b1=Button(mg_sc,text="Block an Account",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",padx=15,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE)
b1.place(x=130,y=180)

b2=Button(mg_sc,text=" Accounts Detail ",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",padx=16,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE)
b2.place(x=130,y=270)

b3=Button(mg_sc,text="Create an Account",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",padx=10,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE,command=newaccount)
b3.place(x=130,y=360)

b4=Button(mg_sc,text="Remove an Account",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE)
b4.place(x=130,y=450)

mg_sc.mainloop()