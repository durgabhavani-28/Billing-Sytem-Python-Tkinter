from tkinter import *
import random
import os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1580x810+0+0")
        self.root.title("GENERAL STORE")
        bg_color = "#a0a0a0"

        # Title Label
        title = Label(self.root, text="GENERAL STORE", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#1e81b0", fg="BLACK", relief=GROOVE)
        title.pack(fill=X)

        # Variables
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.bandages = IntVar()
        self.thermometer = IntVar()
        self.rice = IntVar()
        self.edible_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.salt = IntVar()
        self.green_dal = IntVar()
        self.sprite = IntVar()
        self.fizz = IntVar()
        self.maaza = IntVar()
        self.coke = IntVar()
        self.sting = IntVar()
        self.mountain_dew = IntVar()

        # Total product price
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        # Customer
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Tax
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # Customer retail details
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#a0a0a0")
        F1.place(x=0, y=80, relwidth=1)

        # cname
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        # cphone
        cphn_lbl = Label(F1, text="Customer Phone:", bg="#a0a0a0", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        # cbill
        c_bill_lbl = Label(F1, text="Bill Number:", bg="#a0a0a0", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        # billbutton
        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # Medical
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#bebebe")
        F2.place(x=5, y=180, width=325, height=380)

        # sanitizer
        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        # mask
        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        # handgloves
        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        # syrup
        syrup_lbl = Label(F2, text="Syrup", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        syrup_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        syrup_txt = Entry(F2, width=10, textvariable=self.syrup, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        syrup_txt.grid(row=3, column=1, padx=10, pady=10)

        # bandages
        bandages_lbl = Label(F2, text="Bandages", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        bandages_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        bandages_txt = Entry(F2, width=10, textvariable=self.bandages, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        bandages_txt.grid(row=4, column=1, padx=10, pady=10)

        # thermometer
        thermometer_lbl = Label(F2, text="Thermometer", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        thermometer_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermometer_txt = Entry(F2, width=10, textvariable=self.thermometer, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thermometer_txt.grid(row=5, column=1, padx=10, pady=10)

        # Grocery Items
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#bebebe")
        F3.place(x=340, y=180, width=325, height=380)

        # rice
        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        # edibleoil
        edible_oil_lbl = Label(F3, text="Edible Oil", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        edible_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        edible_oil_txt = Entry(F3, width=10, textvariable=self.edible_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        edible_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        # wheat
        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        # sugar
        sugar_lbl = Label(F3, text="Sugar", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        sugar_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        sugar_txt = Entry(F3, width=10, textvariable=self.sugar, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sugar_txt.grid(row=3, column=1, padx=10, pady=10)

        # salt
        salt_lbl = Label(F3, text="Salt", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        salt_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        salt_txt = Entry(F3, width=10, textvariable=self.salt, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        salt_txt.grid(row=4, column=1, padx=10, pady=10)

        # green dal
        green_dal_lbl = Label(F3, text="Green Dal", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        green_dal_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        green_dal_txt = Entry(F3, width=10, textvariable=self.green_dal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        green_dal_txt.grid(row=5, column=1, padx=10, pady=10)

        # COLD DRINKS
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#bebebe")
        F4.place(x=670, y=180, width=325, height=380)

        # Sprite
        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        # fizz
        fizz_lbl = Label(F4, text="Fizz", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        fizz_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        fizz_txt = Entry(F4, width=10, textvariable=self.fizz, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fizz_txt.grid(row=1, column=1, padx=10, pady=10)

        # maaza
        maaza_lbl = Label(F4, text="Maaza", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        maaza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        maaza_txt = Entry(F4, width=10, textvariable=self.maaza, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maaza_txt.grid(row=2, column=1, padx=10, pady=10)

        # Coke
        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        # Sting
        sting_lbl = Label(F4, text="Sting", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        sting_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        sting_txt = Entry(F4, width=10, textvariable=self.sting, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sting_txt.grid(row=4, column=1, padx=10, pady=10)

        # mountain_dew
        mountain_dew_lbl = Label(F4, text="Mountain Dew", font=('times new roman', 16, 'bold'), bg="#bebebe", fg="black")
        mountain_dew_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_dew_txt = Entry(F4, width=10, textvariable=self.mountain_dew, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_dew_txt.grid(row=5, column=1, padx=10, pady=10)

        # Bill Area
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=550, height=380)
        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Button Frame
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#bebebe")
        F6.place(x=0, y=560, relwidth=1, height=140)

        # button frame for medical price
        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), bg="#bebebe", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        # button frame for grocery price
        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#bebebe", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        # button frame for cold drink price
        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#bebebe", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        # medical tax
        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), bg="#bebebe", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        # Grocery tax
        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#bebebe", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        # Cold Drink Tax
        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#bebebe", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

        # Buttons
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)
        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)
        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bg="#535C68", bd=2, fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()

    def total(self):
        self.m_h_g_p = self.hand_gloves.get() * 12
        self.m_f_p = self.sanitizer.get() * 20
        self.m_m_p = self.mask.get() * 10
        self.m_s_p = self.syrup.get() * 30
        self.m_b_p = self.bandages.get() * 5
        self.m_t_g_p = self.thermometer.get() * 80
        self.total_medical_price = float(self.m_h_g_p + self.m_f_p + self.m_m_p + self.m_s_p + self.m_b_p + self.m_t_g_p)
        self.medical_price.set("Rs. " + str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 100
        self.g_e_o_p = self.edible_oil.get() * 150
        self.g_w_p = self.wheat.get() * 40
        self.g_f_p = self.sugar.get() * 30
        self.g_s_p = self.salt.get() * 30
        self.g_g_p = self.green_dal.get() * 50
        self.total_grocery_price = float(self.g_r_p + self.g_e_o_p + self.g_w_p + self.g_f_p + self.g_s_p + self.g_g_p)
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_v_p = self.sprite.get() * 20
        self.c_d_f_p = self.fizz.get() * 12
        self.c_d_m_p = self.maaza.get() * 20
        self.c_d_c_p = self.coke.get() * 20
        self.c_d_s_p = self.sting.get() * 20
        self.c_m_d_p = self.mountain_dew.get() * 20
        self.total_cold_drinks_price = float(self.c_d_v_p + self.c_d_f_p + self.c_d_m_p + self.c_d_c_p + self.c_d_s_p + self.c_m_d_p)
        self.cold_drinks_price.set("Rs. " + str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. " + str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price + self.total_grocery_price + self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t     Welcome SDB Grocery Retail\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n========================================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\t\tPrice")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # medical
            if self.sanitizer.get() != 0:
                self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_f_p}")
            if self.mask.get() != 0:
                self.txtarea.insert(END, f"\n Mask\t\t\t{self.mask.get()}\t\t{self.m_m_p}")
            if self.hand_gloves.get() != 0:
                self.txtarea.insert(END, f"\n Hand Gloves\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
            if self.syrup.get() != 0:
                self.txtarea.insert(END, f"\n Syrup\t\t{self.syrup.get()}\t\t{self.m_s_p}")
            if self.bandages.get() != 0:
                self.txtarea.insert(END, f"\n Bandages\t\t{self.bandages.get()}\t\t{self.m_b_p}")
            if self.thermometer.get() != 0:
                self.txtarea.insert(END, f"\n Thermometer\t{self.thermometer.get()}\t\t{self.m_t_g_p}")

            # Grocery
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.edible_oil.get() != 0:
                self.txtarea.insert(END, f"\n Edible Oil\t\t{self.edible_oil.get()}\t\t{self.g_e_o_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_f_p}")
            if self.salt.get() != 0:
                self.txtarea.insert(END, f"\n Salt \t\t{self.salt.get()}\t\t{self.g_s_p}")
            if self.green_dal.get() != 0:
                self.txtarea.insert(END, f"\n Green Dal \t\t{self.green_dal.get()}\t\t{self.g_g_p}")

            # cold drinks
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite \t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
            if self.fizz.get() != 0:
                self.txtarea.insert(END, f"\n Fizz \t\t{self.fizz.get()}\t\t{self.c_d_f_p}")
            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\n Maaza \t\t{self.maaza.get()}\t\t{self.c_d_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke \t\t{self.coke.get()}\t\t{self.c_d_c_p}")
            if self.sting.get() != 0:
                self.txtarea.insert(END, f"\n Sting \t\t{self.sting.get()}\t\t{self.c_d_s_p}")
            if self.mountain_dew.get() != 0:
                self.txtarea.insert(END, f"\n Mountain Dew \t\t{self.mountain_dew.get()}\t\t{self.c_m_d_p}")

            self.txtarea.insert(END, "\n--------------------------")
            # taxes
            if self.medical_tax.get() != '0.0':
                self.txtarea.insert(END, f"\n Medical Tax \t\t{self.medical_tax.get()}")
            if self.grocery_tax.get() != '0.0':
                self.txtarea.insert(END, f"\n Grocery Tax \t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get() != '0.0':
                self.txtarea.insert(END, f"\n Cold Drinks Tax \t\t{self.cold_drinks_tax.get()}")
            self.txtarea.insert(END, f"\n Total Bill :\t\t Rs.{self.total_bill}")
            self.txtarea.insert(END, "\n----------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.bandages.set(0)
            self.thermometer.set(0)
            self.rice.set(0)
            self.edible_oil.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.salt.set(0)
            self.green_dal.set(0)
            self.sprite.set(0)
            self.fizz.set(0)
            self.maaza.set(0)
            self.coke.set(0)
            self.sting.set(0)
            self.mountain_dew.set(0)
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()