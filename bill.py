from tkinter import*

from numpy.ma import column_stack
import math,random,os
from tkinter import messagebox


class Bill_App:
    def __init__(self,root):
        self.root=root
        root.geometry("1350x700+0+0")
        root.title("Billing software")
        bgcolor="#2E4053"
        title=Label(root,text="Billing Software",bd=12,relief=GROOVE,bg=bgcolor,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        #=================variable=====================

        #cosmetic+++++
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        #=======grocery========
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #=====cold drink ========
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #====total product price and tax====
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #customer=========
        self.c_name =StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        #============variable=========================
        # customer detail frame
        f1=LabelFrame(root,text="customer Detail",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        f1.place(x=0,y=80,relwidth=1)

        cnamelbl=Label(f1,text="customer Name",bg=bgcolor,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cnametxt=Entry(f1,width=18,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        #phone
        cphonelbl = Label(f1, text="phone No.", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphonetxt = Entry(f1, width=18, font="arial 15",textvariable=self.c_phone, bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)
        #bill
        cbilllbl = Label(f1, text="Bill number", bg=bgcolor, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbilltxt = Entry(f1, width=18, font="arial 15",textvariable=self.search_bill, bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)
        #search button
        billbtn=Button(f1,text="search",width=10,command=self.findbill,bg="#2E4053",bd=7,font="arial 12 bold").grid(row=0,column=6)

        #+++++Cosmetic detail++++++=====
        f2=LabelFrame(root,bd=10,relief=GROOVE,text="Cosmetic",font=("times new roman",15,"bold"),fg="gold",bg=bgcolor)
        f2.place(x=5,y=170,width=325,height=380)

        bathsoaplbl=Label(f2,text="Bath Soap",font=("times new roman",15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bathsoaptxt=Entry(f2,width=10,font=("times new roman",16,"bold"),textvariable=self.soap,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        bathfacelbl = Label(f2, text="face cream",font=("times new roman", 15,"bold"),bg=bgcolor,fg="lightgreen").grid(row=1, column=0,padx=10, pady=10, sticky="w")
        bathfacetxt = Entry(f2, width=10, font=("times new roman", 16, "bold"),textvariable=self.face_wash, bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        bathwashlbl = Label(f2, text="face Wash", font=("times new roman", 15, "bold"),bg=bgcolor, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        bathwashtxt = Entry(f2, width=10, font=("times new roman", 16, "bold"),textvariable=self.face_cream,bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)
        bathspraylbl = Label(f2, text="Hair Spray", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        bathspraytxt = Entry(f2, width=10, font=("times new roman", 16, "bold"),textvariable=self.spray, bd=5, relief=SUNKEN).grid(row=3, column=1,padx=1, pady=10)
        bathgellbl = Label(f2, text="Hair Gel", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        bathgeltxt = Entry(f2, width=10, font=("times new roman", 16, "bold"),textvariable=self.gell, bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)
        bathloshanlbl = Label(f2, text="Body Loshan", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        bathloshantxt = Entry(f2, width=10, font=("times new roman", 16, "bold"),textvariable=self.loshan,bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # +++++Grocery detail++++++=====
        f3 = LabelFrame(root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"), fg="gold",bg=bgcolor)
        f3.place(x=340, y=170, width=325, height=380)

        ricelbl = Label(f3, text="Rice", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        ricetxt = Entry(f3, width=10, font=("times new roman", 16, "bold"),textvariable=self.rice,bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                      padx=10, pady=10)

        foodlbl = Label(f3, text="food oil", font=("times new roman", 15, "bold"),bg=bgcolor, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        foodtxt = Entry(f3, width=10, font=("times new roman", 16, "bold"),textvariable=self.food_oil, bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                      padx=10, pady=10)

        daallbl = Label(f3, text="Daal", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        daaltxt = Entry(f3, width=10, font=("times new roman", 16, "bold"),textvariable=self.daal, bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                      padx=10, pady=10)
        wheatlbl = Label(f3, text="Wheat", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        whaettxt = Entry(f3, width=10, font=("times new roman", 16, "bold"),textvariable=self.wheat, bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                      padx=1, pady=10)
        sugarlbl = Label(f3, text="sugar", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        sugartxt = Entry(f3, width=10, font=("times new roman", 16, "bold"),textvariable=self.sugar, bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                      padx=10, pady=10)
        tealbl = Label(f3, text="Tea", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        teatxt = Entry(f3, width=10, font=("times new roman", 16, "bold"),textvariable=self.tea, bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                      padx=10, pady=10)

        #=====cold drink++++++=====
        f4 = LabelFrame(root, bd=10, relief=GROOVE, text="Cold Drink", font=("times new roman", 15, "bold"), fg="gold",
                        bg=bgcolor)
        f4.place(x=670, y=170, width=325, height=380)

        mazalbl = Label(f4, text="Maza", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        mazatxt = Entry(f4, width=10, font=("times new roman", 16, "bold"),textvariable=self.maza, bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                      padx=10, pady=10)

        cooklbl = Label(f4, text="Cock", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        cooktxt = Entry(f4, width=10, font=("times new roman", 16, "bold"),textvariable=self.cock, bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                      padx=10, pady=10)

        frootilbl = Label(f4, text="Frooti", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        frootitxt = Entry(f4, width=10, font=("times new roman", 16, "bold"),textvariable=self.frooti, bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                      padx=10, pady=10)
        thumbslbl = Label(f4, text="Thumbs Up", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        thumbstxt = Entry(f4, width=10, font=("times new roman", 16, "bold"),textvariable=self.thumsup, bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=1, pady=10)
        limicalbl = Label(f4, text="Limica", font=("times new roman", 15, "bold"),bg=bgcolor, fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        limicatxt = Entry(f4, width=10, font=("times new roman", 16, "bold"),textvariable=self.limca, bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)
        spritelbl = Label(f4, text="sprite", font=("times new roman", 15, "bold"), bg=bgcolor, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        spritetxt = Entry(f4, width=10, font=("times new roman", 16, "bold"),textvariable=self.sprite, bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)

        #=====Bill Area======
        f5 = LabelFrame(root, bd=10, relief=GROOVE)
        f5.place(x=1010, y=180, width=325, height=380)
        bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #====Bill Button frame
        f6 = LabelFrame(root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold",bg=bgcolor)
        f6.place(x=0, y=560,relwidth=1, height=140)
        mllbl=Label(f6,text="total cosmetic price",fg="white",bg=bgcolor,font=("times new roman", 15, "bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        mltxt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.cosmetic_price,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        gplbl = Label(f6, text="total Grocery price", fg="white", bg=bgcolor,
                      font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        gptxt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.grocery_price, bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        dplbl = Label(f6, text="total cold drink price", fg="white", bg=bgcolor,
                      font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        dptxt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.cold_drink_price, bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        #next tax
        ctlbl = Label(f6, text=" cosmetic Tax", fg="white", bg=bgcolor,
                      font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        cttxt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.cosmetic_tax, bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        gtlbl = Label(f6, text="Grocery Tax", fg="white", bg=bgcolor,
                      font=("times new roman", 15, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        gttxt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.grocery_tax, bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        cdtlbl = Label(f6, text="cold drink tax", fg="white", bg=bgcolor,
                      font=("times new roman", 15, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        cdttxt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)


        btnframe=Frame(f6,bd=7,relief=GROOVE)
        btnframe.place(x=750,width=580,height=105)
        total_btn=Button(btnframe,command=self.total,text="Total",bg="#2E4053",fg="white",bd=5,width=10,pady=15,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        generatebill_btn = Button(btnframe, text="Generate Bill",command=self.Bill_area, bg="#2E4053", fg="white", bd=5,width=10, pady=15,
                           font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btnframe, text="clear",command=self.cleardata, bg="#2E4053", fg="white",width=10, bd=5, pady=15,
                           font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btnframe, text="exit",command=self.exitfunction,bg="#2E4053",width=10, fg="white", bd=5, pady=15,
                                  font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
    def total(self):
        self.cspa = self.soap.get()*40
        self.cfcp=self.face_cream.get()*40
        self.cfwp=self.face_wash.get()*40
        self.chsp=self.spray.get()*40
        self.chgp = self.gell.get() * 40
        self.cblp = self.loshan.get() * 40
        self.total_cosmetic_price=float(
                (self.soap.get()*40)+
                (self.face_cream.get() * 40) +
                (self.face_wash.get() * 40) +
                (self.spray.get() * 40) +(self.gell.get() * 40) +
                (self.loshan.get() * 40)
            )
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax=self.total_cosmetic_price*0.05
        self.cosmetic_tax.set(self.c_tax)

        self.grp = self.rice.get() * 40
        self.gfp = self.food_oil.get() * 40
        self.gdp = self.daal.get() * 40
        self.gwp = self.wheat.get() * 40
        self.gsp = self.sugar.get() * 40
        self.gtp = self.tea.get() * 40

        self.total_glocery_price = float(

            (self.rice.get() * 40) +
            (self.food_oil.get() * 40) +
            (self.daal.get() * 40) +
            (self.wheat.get() * 40) +
            (self.sugar.get() * 40) +
            (self.tea.get() * 40)
        )
        self.grocery_price.set(str(self.total_glocery_price))
        self.g_tax = self.total_glocery_price * 0.05
        self.grocery_tax.set(self.g_tax)

        self.cmp = self.maza.get() * 40
        self.ccp = self.cock.get() * 40
        self.cfp = self.frooti.get() * 40
        self.ctp = self.thumsup.get() * 40
        self.clp = self.limca.get() * 40
        self.csp = self.sprite.get() * 40

        self.total_cold_drink = float(

            (self.maza.get() * 40) +
            (self.cock.get() * 40) +
            (self.frooti.get() * 40) +
            (self.thumsup.get() * 40) +
            (self.limca.get() * 40) +
            (self.sprite.get() * 40)
        )
        self.cold_drink_price.set(str(self.total_cold_drink))
        self.d_tax = self.total_cold_drink* 0.05
        self.cold_drink_tax.set(self.d_tax)

        self.total_billall=float(self.total_cosmetic_price+self.total_glocery_price+self.total_cold_drink+self.c_tax+self.g_tax+self.d_tax)




    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\twelcome Retailer shop")
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n customer Name::{self.c_name.get()}")
        self.txtarea.insert(END,f"\n phone number:{self.c_phone.get()}")
        self.txtarea.insert(END,f"\n===================================")
        self.txtarea.insert(END,f"\n products    \t QTY   \t price")
        self.txtarea.insert(END,f"\n===================================")

    def Bill_area(self):
        if(self.c_name.get()=="" or self.c_phone==""):
            messagebox.showerror("Error","customer detail are must")
        elif(self.total_billall==0):
            messagebox.showerror("error","Item not selected")

        else:

            self.welcome_bill()
            # cosmetic
            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\n Bath soap \t\t{self.soap.get()}\t{self.cspa}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END, f"\n face cream \t\t{self.face_cream.get()}\t{self.cfcp}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\n face wash\t\t{self.face_wash.get()}\t{self.cfwp}")
            if self.spray.get()!=0:
                self.txtarea.insert(END, f"\n hair spray \t\t{self.spray.get()}\t{self.chsp}")
            if self.gell.get()!=0:
                self.txtarea.insert(END, f"\n hair gel\t\t{self.gell.get()}\t{self.chgp}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END, f"\n body Loshan \t\t{self.loshan.get()}\t{self.cblp}")
                # grocery
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice \t\t{self.rice.get()}\t{self.grp}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n food oil \t\t{self.food_oil.get()}\t{self.gfp}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n daal\t\t{self.daal.get()}\t{self.gdp}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n wheat \t\t{self.wheat.get()}\t{self.gwp}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n sugar\t\t{self.sugar.get()}\t{self.gsp}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea \t\t{self.tea.get()}\t{self.gtp}")

             # cold drink
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza \t\t{self.maza.get()}\t{self.cmp}")
            if self.cock.get() != 0:
                self.txtarea.insert(END, f"\n cock \t\t{self.cock.get()}\t{self.ccp}")
            if self.frooti.get() != 0:
                 self.txtarea.insert(END, f"\n fruiti \t\t{self.frooti.get()}\t{self.cfp}")
            if self.thumsup.get() != 0:
                self.txtarea.insert(END, f"\n thumps up \t\t{self.thumsup.get()}\t{self.ctp}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n limica \t\t{self.limca.get()}\t{self.clp}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n sprite \t\t{self.sprite.get()}\t{self.csp}")

            self.txtarea.insert(END, f"\n-----------------------------------")
            if(self.cosmetic_tax.get()!="0.0"):
               self.txtarea.insert(END, f"\n cosmetic Tax   \t\t {self.cosmetic_tax.get()}")
            if (self.grocery_tax.get() != "0.0"):
             self.txtarea.insert(END, f"\n Growsery Tax   \t\t {self.grocery_tax.get()}")
            if (self.cold_drink_tax.get() != "0.0"):
                 self.txtarea.insert(END, f"\n cold drink Tax  \t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END, f"\n Total Bill  \t\t{self.total_billall}")
            self.txtarea.insert(END, f"\n-----------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save Bill","do you want to save the Bill?")
        if op>0:
            self.bill_date=self.txtarea.get('1.0',END)
            f1=open("billsave/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_date)
            f1.close()
            messagebox.showinfo("saved","saved successfully!")
        else:
            return

    def findbill(self):
        present="no"
        for i in os.listdir("billsave/"):
            print(i)
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"billsave/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if(present=="no"):
            messagebox.showerror("erroe","invalid bill number")

    def cleardata(self):
        # cosmetic+++++
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        # =======grocery========
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        # =====cold drink ========
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        # ====total product price and tax====
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")
        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        # customer=========
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def exitfunction(self):
        op=messagebox.askyesno("exit","do you really want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()