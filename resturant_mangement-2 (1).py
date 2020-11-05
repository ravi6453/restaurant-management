from tkinter import *
from tkinter import ttk
import random,sys
from datetime import datetime
from tkinter import messagebox
from Connection import usernamedb,passworddb
import mysql.connector

ms=mysql.connector.Connect(host="sql12.freemysqlhosting.net", user=usernamedb
                           ,password=passworddb,database="sql12373333")
mc=ms.cursor()
def main():
    win=Tk()
    app=LoginPage(win)
    win.mainloop()
class LoginPage:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")
        
        self.title_label=Label(self.win,text="Restaurant Mangement system",font=('Arial',35,'bold'),bg="green",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        self.main_frame=Frame(self.win,bg="orange",bd=8,relief=GROOVE)
        self.main_frame.place(x=300,y=150,width=800,height=400)
        
        self.login_lbl=Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="red",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        
        self.entry_frame=LabelFrame(self.main_frame,text="Entry Details",bg="pink",bd=5,font=('sans_serief',17),relief=GROOVE)
        self.entry_frame.pack(fill=BOTH,expand=TRUE)
        
        self.entus_lbl=Label(self.entry_frame,text="Enter Username:",bg="#856ff8",font=('sans_serif',15))
        self.entus_lbl.grid(row=0,column=0)
        
        self.entus_lbll=Label(self.entry_frame,text="Enter Password :",bg="#856ff8",font=('sans-serif',15))
        self.entus_lbll.grid(row=1,column=0)
        
        #===========================variable==============================
        
        username =StringVar()
        password=StringVar()
        
        #==================================================================
        
        self.entus_ent=Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.entus_psd=Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password,show="*")
        self.entus_psd.grid(row=1,column=1,padx=3,pady=3)
        #=======================================Function=========================
        
        def check_login():
            '''this funcyion will check login '''
            mc.execute("select username,password from register")
            for i in mc:
                if i[0]==username.get().strip() and i[1]==password.get():
                    self.billing_btn.config(state="normal")
                    reset()
                    return
                else:
                    pass
                
        
        def reset():
            username.set("")
            password.set("")
        
        
        def billing_sec():
            self.newwindow=Toplevel(self.win)
            self.app=window2(self.newwindow)
            self.billing_btn.config(state="disabled")
            
        def newuser():
            self.newwindow=Toplevel(self.win)
            self.app=window3(self.newwindow)
            
        #======================================Button==============================
        
        self.button_frame=LabelFrame(self.entry_frame,text="option",font=('Arial',15),bg="orange",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=150)
        
        self.login_btn=Button(self.button_frame,text="Login",bg="yellow",font=('Arial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)
        
        self.billing_btn=Button(self.button_frame,text="Billing",bg="yellow",font=('Arial',15),bd=5,width=15,command=billing_sec)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")
        
        self.reset_btn=Button(self.button_frame,text="Reset",bg="yellow",font=('Arial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)
        
        self.forgot_btn=Button(self.button_frame,text="New User",bg="yellow",font=('Arial',15),bd=5,width=19,command=newuser)
        self.forgot_btn.grid(row=1,column=0,padx=20,pady=2)
#======================class2=========================================================
class window2:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")
        
        self.title_label=Label(self.win,text="Restaurant Mangement system",font=('Arial',35,'bold'),bg="green",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        #====================================variable=====================================
        bill_no=random.randint(100,9999)
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)
        cal_var=StringVar()
        
        cust_nm=StringVar()
        cust_con=StringVar()
        date_pr=StringVar()
        item_pur=StringVar()
        item_quantity=StringVar()
        con=StringVar()
        
        
        date_pr.set(datetime.now())
        total_list=[]
        self.grd_total=0
        self.gst_amount=0
        self.total_amount=0
        
        #==================================================================================
        
            
        #================================================================================================
        #                                       PRICE LIST
        def price_list():
            
            
            roo= Tk()
            roo.geometry("600x700+0+0")
            roo.title("Price List")

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
            lblinfo.grid(row=0, column=2)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
            lblinfo.grid(row=0, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="59", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Salad", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="49", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hamburger", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Litti-Chokha", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="39", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Salad", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Sandwhich", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="79", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Sandwhich", fg="steel blue", anchor=W)
            lblinfo.grid(row=7, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="steel blue", anchor=W)
            lblinfo.grid(row=7, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fish Sandwhich", fg="steel blue", anchor=W)
            lblinfo.grid(row=8, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="119", fg="steel blue", anchor=W)
            lblinfo.grid(row=8, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Brownie", fg="steel blue", anchor=W)
            lblinfo.grid(row=9, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="139", fg="steel blue", anchor=W)
            lblinfo.grid(row=9, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Gulab Jamun", fg="steel blue", anchor=W)
            lblinfo.grid(row=10, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="59", fg="steel blue", anchor=W)
            lblinfo.grid(row=10, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Paan", fg="steel blue", anchor=W)
            lblinfo.grid(row=11, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="39", fg="steel blue", anchor=W)
            lblinfo.grid(row=11, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Rasmalai", fg="steel blue", anchor=W)
            lblinfo.grid(row=12, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="59", fg="steel blue", anchor=W)
            lblinfo.grid(row=12, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Jalebi", fg="steel blue", anchor=W)
            lblinfo.grid(row=13, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="39", fg="steel blue", anchor=W)
            lblinfo.grid(row=13, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="steel blue", anchor=W)
            lblinfo.grid(row=14, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="49", fg="steel blue", anchor=W)
            lblinfo.grid(row=14, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="steel blue", anchor=W)
            lblinfo.grid(row=15, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="79", fg="steel blue", anchor=W)
            lblinfo.grid(row=15, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="steel blue", anchor=W)
            lblinfo.grid(row=16, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
            lblinfo.grid(row=16, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Orange Juice", fg="steel blue", anchor=W)
            lblinfo.grid(row=17, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
            lblinfo.grid(row=17, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mineral Water", fg="steel blue", anchor=W)
            lblinfo.grid(row=18, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
            lblinfo.grid(row=18, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Shake", fg="steel blue", anchor=W)
            lblinfo.grid(row=19, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
            lblinfo.grid(row=19, column=3)

            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Oreo Krusher", fg="steel blue", anchor=W)
            lblinfo.grid(row=20, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="105", fg="steel blue", anchor=W)
            lblinfo.grid(row=20, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vanilla Shake", fg="steel blue", anchor=W)
            lblinfo.grid(row=21, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
            lblinfo.grid(row=21, column=3)
            roo.mainloop()
          #===================================entry========================================
        self.entry_frame=LabelFrame(self.win,text="Entry details",background="lightgrey",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)
        
        self.bill_no_lbl=Label(self.entry_frame,text="Bill Number",font=('Arial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        self.bill_no_ent=Entry(self.entry_frame,bd=5,font=('Arial',15),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=1,pady=2)
        self.bill_no_ent.config(state="disabled")
        
        self.cust_nm_bill=Label(self.entry_frame,text="Coustmer Name",font=('Arial',15),bg="lightgrey")
        self.cust_nm_bill.grid(row=1,column=0,padx=2,pady=2)
        
        self.cust_nm_ent=Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)
        
        self.cust_contact_lbl=Label(self.entry_frame,text="Coustmer Contact",font=('Arial',15),bg="lightgrey")
        self.cust_contact_lbl.grid(row=2,column=0,padx=2,pady=2)
        
        self.cust_contact_ent=Entry(self.entry_frame,bd=5,textvariable=cust_con,font=('Arial',15))
        self.cust_contact_ent.grid(row=2,column=1,padx=2,pady=2)
        
        self.date_lbl=Label(self.entry_frame,text="Date",font=('Arial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.date_ent=Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        
        items=['SELECT','Fries','Salad','Hamburger','Litti-Chokha','Chicken Salad','Fish Sandwhich','Chocolate Brownie',
               'Gulab Jamun' ,'Paan','Rasmalai','Jalebi','Tea','Coffee','Cola','Orange Juice',
               'Mineral Water','Chocolate Shake','Oreo Krusher','Vanilla Shake']
        cost=[0,59,49,99,39,99,79,99,119,139,59,39,49,79,20,50,25,50,105,50]
        sel=StringVar()
        sel.set(items[0])
         
        self.item_pur_lbl=Label(self.entry_frame,text="Item Purchased",font=('Arial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
       
        self.item_pur_ent=OptionMenu(self.entry_frame, sel, *items)
        self.item_pur_ent.config(font=('Arial',15),bd=5)
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)
        
        self.item_qty_lbl=Label(self.entry_frame,text="Item Quantity",font=('Arial',15),bg="lightgrey")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_qty_ent=Entry(self.entry_frame,bd=5,textvariable=item_quantity,font=('Arial',15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)
       
        self.cost_one_lbl=Label(self.entry_frame,text="Cost of one",font=('Arial',15),bg="lightgrey")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        def setcost():
            con.set(cost[items.index(sel.get())])
            return
        
        con.set(cost[0])
        self.cost_one_ent=Button(self.entry_frame,bd=5,textvariable=con,font=('Arial',12),width=20,command=setcost)
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)
#========================================function===========================================
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\t  Mini Punjab")
            self.bill_txt.insert(END,"\n   Shop S15, Vaishali Nagar, behind MTS Towers, Jaipur, Rajasthan 302021")
            self.bill_txt.insert(END,"\n\t\t\t\tContact- +198457841238")
            self.bill_txt.insert(END,"\n===========================================================================")
            self.bill_txt.insert(END,f"\n Bill Number {bill_no_tk.get()}")
            
        def genbill():
            if cust_nm.get()=="" or (cust_con.get()=="" or len(cust_con.get())!=10):
                messagebox.show("Error","Please entre all the fields correctly.")
            else:
                
                self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\ncustomer Contact : {cust_con.get()}")
                self.bill_txt.insert(END,f"\n Date : {date_pr.get()}")
                self.bill_txt.insert(END,"\n==========================================================================")
                self.bill_txt.insert(END,"   \n Product Nmae\t\t         Quantity\t\t         Per Cost\t\t         Total")
                self.bill_txt.insert(END,"\n==========================================================================")
                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
            
        def clear_fun():
            cust_nm.set("")
            cust_con.set("")
            item_pur.set("")
            item_quantity.set("")
            con.set("")
            
        def reset_fun():
            total_list.clear()
            self.grd_total=0
            self.gst_amount=0
            
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()
            
        def add_fun():
            if sel.get()=="" or item_quantity.get()=="":
                messagebox.showinfo("Error","Please entre all the fields correctly.",parent=self.win)
            else:
                qty=int(item_quantity.get())
                cones=int(con.get())
                total=qty*cones
                total_list.append(total)
        
            self.bill_txt.insert(END,f"\n {           sel.get()}\t\t         \t{    item_quantity.get()}\t\t     RS.{  con.get()}\t\t       Rs.{  total}")
            
        def total_fun():
            for item in total_list:
                self.grd_total=self.grd_total+item
            
            self.bill_txt.insert(END,"\n==========================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t\t\t\t           Amount:Rs {self.grd_total}")
            
            self.gst_amount=round((18/100)*self.grd_total,2)
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGST 18% :Rs {self.gst_amount}")
            self.total_amount=self.grd_total+self.gst_amount
            self.bill_txt.insert(END,f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Grand total :Rs {self.total_amount}")
            self.bill_txt.insert(END,"\n==========================================================================")
            self.save_btn.config(state="normal")
        
        def save_fun():
            user_choice=messagebox.askyesno("Confirm?",f"Do you want to save the bill {bill_no_tk.get()}",parent=self.win)
            if user_choice >0:
                self.bill_content=self.bill_txt.get("1.0",END)
                try:
                    con=open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                    con.write(self.bill_content)
                    con.close()
                    messagebox.showinfo("Sucess!",f"Bill {bill_no_tk.get()} has been saved successfully!",parent=self.win)
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}")
            else:
                return
#============================================================================================
#=========================================Button===============================================
        self.button_frame=LabelFrame(self.entry_frame,bd=5,text="option",bg="lightgrey",font=('Arial',15))
        self.button_frame.place(x=20,y=280,width=395,height=300)
        
        
        self.add_btn=Button(self.button_frame,bd=4,text="Add",font=('Arial',12),width=12,height=3,command=add_fun)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        
        
        self.generate_btn=Button(self.button_frame,bd=4,text="Generate",font=('Arial',12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)
        
        
        self.clear_btn=Button(self.button_frame,bd=4,text="Clear",font=('Arial',12),width=12,height=3,command=clear_fun)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)
        
        self.total_btn=Button(self.button_frame,bd=4,text="Total",font=('Arial',12),width=12,height=3,command=total_fun)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)
        
        self.reset_btn=Button(self.button_frame,bd=4,text="Reset",font=('Arial',12),width=12,height=3,command=reset_fun)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)
        
        
        self.save_btn=Button(self.button_frame,bd=4,text="Save",font=('Arial',12),width=12,height=3,command=save_fun)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)
        
        self.menu_btn=Button(self.button_frame,bd=4,text="Menu",font=('Arial',13),width=12,height=3,command=price_list)
        self.menu_btn.grid(row=3,column=0,padx=5,pady=3)
        
        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")
               
#============================================================================================= 

#=================================Calculator Frame============================================

        self.calc_frame=Frame(self.win,bd=4,background="black",relief=GROOVE)
        self.calc_frame.place(x=585,y=90,width=700,height=295)
        
        self.num_ent=Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=cal_var,font=('Arial',15),width=50,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=11)
        
        def press_btn(event):
            text=event.widget.cget("text")
            if text=="=":
                if cal_var.get().isdigit():
                    value=int(cal_var.get())
                else:
                    try:
                    
                        value=eval(self.num_ent.get())
                    except:
                        print("Error")
                    
                cal_var.set(value)
                self.num_ent.update()
            elif text=="c":
                pass
            else:
                cal_var.set(cal_var.get()+text)
                self.num_ent.update()
                
        self.btn7=Button(self.calc_frame,bg="plum",text="7",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn7.grid(row=1,column=0,padx=2,pady=2)
        self.btn7.bind("<Button-1>",press_btn)
        
        self.btn8=Button(self.calc_frame,bg="plum",text="8",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn8.grid(row=1,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9=Button(self.calc_frame,bg="plum",text="9",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn9.grid(row=1,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>",press_btn)  
        
        
        self.btnadd=Button(self.calc_frame,bg="plum",text="+",bd=8,width=10,height=1,font=('Arial,15'))
        self.btnadd.grid(row=1,column=3,padx=2,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)  
        
        self.btn4=Button(self.calc_frame,bg="plum",text="4",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)  
        
        self.btn5=Button(self.calc_frame,bg="plum",text="5",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn5.grid(row=2,column=1,padx=2,pady=2)
        self.btn5.bind("<Button-1>",press_btn)  

        self.btn6=Button(self.calc_frame,bg="plum",text="6",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn6.grid(row=2,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>",press_btn)  
        
        def clr():
            cal_var.set('')
            
        self.btnclr=Button(self.calc_frame,bg="plum",text="C",bd=8,width=6,height=1,font=('Arial,15'),command=clr)
        self.btnclr.grid(row=2,column=4,padx=2,pady=2)
        
        self.btnsubtract=Button(self.calc_frame,bg="plum",text="-",bd=8,width=10,height=1,font=('Arial,15'))
        self.btnsubtract.grid(row=2,column=3,padx=2,pady=2)
        self.btnsubtract.bind("<Button-1>",press_btn)  
        
        self.btn1=Button(self.calc_frame,bg="plum",text="1",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn1.grid(row=3,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>",press_btn)  
        
        self.btn2=Button(self.calc_frame,bg="plum",text="2",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn2.grid(row=3,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>",press_btn)  
        
        self.btn3=Button(self.calc_frame,bg="plum",text="3",bd=8,width=10,height=1,font=('Arial,15'))
        self.btn3.grid(row=3,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>",press_btn)  
        
        self.btnmulti=Button(self.calc_frame,bg="plum",text="*",bd=8,width=10,height=1,font=('Arial,15'))
        self.btnmulti.grid(row=3,column=3,padx=2,pady=2)
        self.btnmulti.bind("<Button-1>",press_btn)  
        
        self.btnzero=Button(self.calc_frame,bg="plum",text="0",bd=8,width=10,height=1,font=('Arial,15'))
        self.btnzero.grid(row=4,column=0,padx=2,pady=2)
        self.btnzero.bind("<Button-1>",press_btn)  
        
        self.btnpoint=Button(self.calc_frame,bg="plum",text=".",bd=8,width=10,height=1,font=('Arial,15'))
        self.btnpoint.grid(row=4,column=1,padx=2,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)  
        
        self.btnclear=Button(self.calc_frame,bg="plum",text="=",bd=8,width=10,height=1,font=('Arial,15'))
        self.btnclear.grid(row=4,column=2,padx=2,pady=2)
        self.btnclear.bind ("<Button-1>",press_btn) 
        
        
        
        self.btndivide=Button(self.calc_frame,bg="plum",text="/",bd=8,width=10,height=1,font=('Arial,15'))
        self.btndivide.grid(row=4,column=3,padx=2,pady=2)
        self.btndivide.bind("<Button-1>",press_btn)  
#==============================bill FRAME ===============================================
        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=('Arial',18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=585,y=400,width=650,height=325)
        
        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=True)
        default_bill()

#=============================================================================================      

class window3:
     def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Register")
        self.title_label=Label(self.win,text="Welcome",font=('Arial',35,'bold'),bg="green",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.Register_lbl=Label(self.win,text="Register",bd=6,relief=GROOVE,anchor=CENTER,bg="red",font=('sans-serif',25,'bold'))
        self.Register_lbl.pack(side=TOP,fill=X)
        
        self.entus_lb1=Label(self.win,text="Enter Username:",bg="#856ff8",font=('sans_serif',15))
        self.entus_lb1.place(x=400,y=200)
        
        un=StringVar()
        self.entus_ent=Entry(self.win,font=('sans-serif',15),bd=6,textvariable=un)
        self.entus_ent.place(x=600,y=200)
        
        self.entus_lbl2=Label(self.win,text="Enter Password :",bg="#856ff8",font=('sans-serif',15))
        self.entus_lbl2.place(x=400,y=300)
        
        pas=StringVar()
        self.entus_ent1=Entry(self.win,font=('sans-serif',15),bd=6,textvariable=pas,show="*")
        self.entus_ent1.place(x=600,y=300)
        
        self.entus_lbl3=Label(self.win,text="Enter Confirm Password :",bg="#856ff8",font=('sans-serif',15))
        self.entus_lbl3.place(x=330,y=400)
        
        cnf=StringVar()
        self.entus_ent2=Entry(self.win,font=('sans-serif',15),bd=6,textvariable=cnf,show="*")
        self.entus_ent2.place(x=600,y=400)
        
        self.entus_lbl4=Label(self.win,text="Enter Mobile No. :",bg="#856ff8",font=('sans-serif',15))
        self.entus_lbl4.place(x=400,y=500)
        
        mn=StringVar()
        self.entus_ent3=Entry(self.win,font=('sans-serif',15),bd=6,textvariable=mn)
        self.entus_ent3.place(x=600,y=500)
        
        def cond():
            if un.get()=="" and len(pas.get())<8:
                return False
            if pas.get() != cnf.get():
                return False
            if len(mn.get())<10:
                return False
            return True
            
        def check_register():
            if cond():
                sql = "INSERT INTO register VALUES(%s, %s ,%s)"
                val = (un.get(), pas.get() ,mn.get())
                mc.execute(sql,val)
                ms.commit()
            else:
                messagebox.showinfo('Warning','Error!')
                
            
        self.Register_btn=Button(self.win,text="Register",bg="yellow",font=('Arial',15),bd=5,width=15,command=check_register)
        self.Register_btn.place(x=700,y=600)
        
        #==================================================================

       
if __name__=="__main__":
    main()