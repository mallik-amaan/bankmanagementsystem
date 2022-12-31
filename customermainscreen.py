from tkinter import *
from tkinter import messagebox
def withdrawl_click():
    window=Tk()
    window.title("WITHDRAWL")
    window.geometry('400x200')
    window.configure(bg="#181D31")
    withdraw=Label(window,text="ENTER AMOUNT TO WITHDRAW:",font=("Tw Cen MT",12,"bold"),fg="#F0E9D2",bg="#181D31").place(x=100,y=20)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=87,y=40)
    amount=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold")).place(x=177,y=80)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=87,y=100)
    but_withdraw=Button(window,text="WITHDRAW",bg="lightgrey",command=window.destroy).place(x=168,y=150)
    window.mainloop()
def current_click():
    window=Tk()
    window.title("CURRENT BALANCE")
    window.geometry('400x200')
    window.configure(bg="#181D31")
    l1=Label(window,text="YOUR CURRENT BALANCE IS:",font="20",bg="#181D31",fg="#F0E9D2").place(x=10,y=10)
    Frame(window,width=300,height=2,bg="#F0E9D2").place(x=10,y=35)
    b1=Button(window,text="      CLOSE    ",bg="lightgrey",activebackground="green",activeforeground="white",command=window.destroy).place(x=168,y=150)
    window.mainloop()
def fund_click():
    window=Tk()
    window.configure(bg="#181D31")
    window.title("FUND TRANSFER")
    window.geometry('400x200')
    account=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Ariel",12)).place(x=165,y=20)
    accountno=Label(window,text="Acc no:",fg="#F0E9D2",bg="#181D31",font=("Ariel",12)).place(x=100,y=20)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=40)
    moneytext=Label(window,text="Amount:",fg="#F0E9D2",bg="#181D31",font=("Arial",12)).place(x=100,y=60)
    money=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Ariel",12)).place(x=165,y=60)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=80)
    
    but_transfer=Button(window,text="SEND MONEY",bg="#F0E9D2",activebackground="green",activeforeground="white",command=window.destroy).place(x=150,y=120)
    
    if money:
        print(money)
    window.mainloop()
def trans_click():
     window=Tk()
     window.configure(bg="lightblue")
     window.title("FUND TRANSFER")
     window.geometry('400x200')
     


main=Toplevel() 
main.title("CLIENT ACCOUNT")
main.maxsize(500,720)
main.minsize(500,720)
background_img=PhotoImage(file="bg4.png")
background=Label(main,image=background_img).place(x=0,y=0)
main.configure(bg="white")
main.resizable(False,False)
img=PhotoImage(file="customer.png")
label = Label(main,image=img,bg="#181D31").place(x=20,y=20)
Label(main,text="Client 1",font=("Tw Cen MT",35,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=30)
fund=PhotoImage(file="transfer.png")
fundpic=Label(main,image=fund,bg="#F0E9D2").place(x=120,y=409)
trans=PhotoImage(file="transaction.png")
transpic=Label(main,image=trans,bg="#F0E9D2").place(x=120,y=347)
currbal=PhotoImage(file="currentbalance.png")
curbalpic=Label(main,image=currbal,bg="#F0E9D2").place(x=120,y=278)
button_currentbalance=Button(main,text=" CURRENT BALANCE",bg="#181D31",fg="#F0E9D2",font=("Tw Cen MT",15,"bold"),activebackground="green",activeforeground="white",command=current_click).place(x=180,y=300)
button_fundtransfer=Button(main,text="  FUNDS TRANSFER ",bg="#181D31",fg="#F0E9D2",font=("Tw Cen MT",15,"bold"),activebackground="green",activeforeground="white",command=fund_click).place(x=180,y=430)
button_transaction=Button(main,text=   "       WITHDRAWL      ",bg="#181D31",fg="#F0E9D2",font=("Tw Cen MT",15,"bold"),activebackground="green",activeforeground="white",command=withdrawl_click).place(x=180,y=365)

main.mainloop()