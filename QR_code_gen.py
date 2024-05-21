from tkinter import*
import qrcode
from PIL import Image, ImageTk

class QR_generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1270x750+200+50")
        self.root.title(" QR generator | Developed By GRP-1 (P3)")
        self.root.resizable(False, False)

        title = Label(self.root, text="        𝘼 𝙎𝙞𝙢𝙥𝙡𝙚 𝙌𝙍 𝘾𝙤𝙙𝙚 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧                                                                                                                                                                                                                                                  𝘽𝙮 ~Yash ", font=('arial', 11), bg='black', fg='white', anchor='w').place(x=0, y=0, relwidth = 1)



# =====================Variables ================
        self.var_st_code = StringVar()
        self.var_url_code = StringVar()
        self.var_ct1_code = StringVar()
        self.var_ct2_code = StringVar()
        self.var_add1_code = StringVar()
        self.var_add2_code = StringVar()
        self.var_add3_code = StringVar()
        self.var_add4_code = StringVar()
        self.var_add5_code = StringVar()
        self.var_add6_code = StringVar()
        self.var_add7_code = StringVar()
        self.var_add8_code = StringVar()

#  1 ============== Simple Text detail window ==============

        def myclick():
            photo1 = PhotoImage(file="backround.png")
            window_backround_st = Label(self.root, bd=0, image=photo1).place(x=0, y=20, width=1270, height=750)
            st_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            st_Frame.place(x=30, y=60, width=650, height=663)
            st_bg = PhotoImage(file="full 111.png")
            st_bg_lable = Label(st_Frame, bd=0, image=st_bg).place(x=0, y=0, width=650, height=663)
            lbl_st_code = Label(st_Frame, text="Enter here  ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=65, y=122)
            txt_st_code = Entry(st_Frame, font=("dubai medium", 15), textvariable=self.var_st_code, bg='white', fg='black').place(x=260, y=120, relwidth=0.4335)
            btn_generator = Button(self.root, text="G e n e r a t e", command=self.generate1, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=120, y=590)
            btn_clear = Button(self.root, text="C l e a r", command=self.clear, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=440, y=590)
            self.msg = ""
            self.lbl_msg = Label(st_Frame, text=self.msg, font=('times new roman', 20), bg='black', fg='green')
            self.lbl_msg.place(x=75, y=600, relwidth=0.7899)



# =============== QR CODE window ===========

            qr_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            qr_Frame.place(x=740, y=60, width=500, height=663)
            qr_bg = PhotoImage(file="Qr window bg.png")
            qr_bg_lable = Label(qr_Frame, bd=0, image=qr_bg).place(x=0, y=0, width=500, height=663)
            self.qr_code = Label(qr_Frame, text='After pressing \nGenerate , QR code \nwill appear here ', font=('times new roman', 15), bg='white', fg='black')
            self.qr_code.place(x=75, y=250, width=350, height=350)

            pic = PhotoImage(file="down2.png")
            save_btn = Button(qr_Frame, image=(pic), bg='black', cursor='bottom_side', bd=0, command=self.save1).place(x=165, y=55, width=173, height=50)
            self.message = Label(qr_Frame, text='NOTE 1 : MINIMIZE WINDOW after pressed download\nNOTE 2 : After downloading please change the file name\n     if u wanna download another QR-Code ', font=('times new roman', 13), bg='black', fg='red').place(x=64, y=120)
            qr_Frame.mainloop()


        def myclick1():
            photo1 = PhotoImage(file="backround.png")
            window_backround_st = Label(self.root, bd=0, image=photo1).place(x=0, y=20, width=1270, height=750)
            url_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            url_Frame.place(x=30, y=60, width=650, height=663)
            url_bg = PhotoImage(file="full 222.png")
            url_bg_lable = Label(url_Frame, bd=1, image=url_bg).place(x=0, y=0, width=650, height=663)
            lbl_url_code = Label(url_Frame, text="Enter URL here ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=70, y=120)
            txt_url_code = Entry(url_Frame, font=("dubai medium", 15), textvariable=self.var_url_code, bg='white', fg='black').place(x=290, y=120, relwidth=0.4335)
            btn_generator = Button(self.root, text="G e n e r a t e", command=self.generate2, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=120, y=590)
            btn_clear = Button(self.root, text="C l e a r", command=self.clear, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=440, y=590)
            self.msg = ""
            self.lbl_msg = Label(url_Frame, text=self.msg, font=('times new roman', 20), bg='black', fg='green')
            self.lbl_msg.place(x=75, y=600, relwidth=0.7899)

# ============== QR window details ========================

            qr_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            qr_Frame.place(x=740, y=60, width=500, height=663)
            qr_bg = PhotoImage(file="Qr window bg.png")
            qr_bg_lable = Label(qr_Frame, bd=0, image=qr_bg).place(x=0, y=0, width=500, height=663)
            self.qr_code = Label(qr_Frame, text='After pressing \nGenerate , QR code \nwill appear here ', font=('times new roman', 13), bg='white', fg='black')
            self.qr_code.place(x=75, y=250, width=350, height=350)

            pic = PhotoImage(file="down2.png")
            save_btn = Button(qr_Frame, image=(pic), bg='black', cursor='bottom_side', bd=0, command=self.save2).place(x=165, y=55, width=173, height=50)
            self.message = Label(qr_Frame, text='NOTE 1 : MINIMIZE WINDOW after pressed download\nNOTE 2 : After downloading please change the file name\n     if u wanna download another QR-Code ', font=('times new roman', 13), bg='black', fg='red').place(x=64, y=120)
            qr_Frame.mainloop()

        def myclick2():
            photo1 = PhotoImage(file="backround.png")
            window_backround_st = Label(self.root, bd=0, image=photo1).place(x=0, y=20, width=1270, height=750)
            ct_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            ct_Frame.place(x=10, y=77, width=650, height=663)
            ct_bg = PhotoImage(file="full 333.png")
            ct_bg_lable = Label(ct_Frame, bd=0, image=ct_bg).place(x=0, y=0, width=650, height=663)
            lbl_ct_code = Label(ct_Frame, text="Enter Name here    ➤", font=("dubai medium", 15, 'bold'), bg='black',fg='white').place(x=70, y=120)
            lbl_ct_code = Label(ct_Frame, text="Enter Contact here ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=70, y=180)
            txt1_ct_code = Entry(ct_Frame, font=("dubai medium", 15), textvariable=self.var_ct1_code, bg='white',fg='black').place(x=290, y=120, relwidth=0.4335)
            txt2_ct_code = Entry(ct_Frame, font=("dubai medium", 15), textvariable=self.var_ct2_code, bg='white',fg='black').place(x=290, y=180, relwidth=0.4335)
            btn_generator = Button(self.root, text="G e n e r a t e", command=self.generate3,font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=120, y=590)
            btn_clear = Button(self.root, text="C l e a r", command=self.clear, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=440, y=590)
            self.msg = ""
            self.lbl_msg = Label(ct_Frame, text=self.msg, font=('times new roman', 20), bg='black', fg='green')
            self.lbl_msg.place(x=75, y=600, relwidth=0.7899)

# =============== QR CODE window ===========

            qr_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            qr_Frame.place(x=760, y=77, width=500, height=663)
            qr_bg = PhotoImage(file="Qr window bg.png")
            qr_bg_lable = Label(qr_Frame, bd=0, image=qr_bg).place(x=0, y=0, width=500, height=663)
            self.qr_code = Label(qr_Frame, text='After pressing \nGenerate , QR code \nwill appear here ', font=('times new roman', 15), bg='white', fg='black')
            self.qr_code.place(x=75, y=250, width=350, height=350)

            pic = PhotoImage(file="down2.png")
            save_btn = Button(qr_Frame, image=(pic), bg='black', cursor='bottom_side', bd=0, command=self.save3).place(x=165, y=55, width=173, height=50)
            self.message = Label(qr_Frame, text='NOTE 1 : MINIMIZE WINDOW after pressed download\nNOTE 2 : After downloading please change the file name\n     if u wanna download another QR-Code ', font=('times new roman', 13), bg='black', fg='red').place(x=64, y=120)
            qr_Frame.mainloop()

        def myclick3():
            photo1 = PhotoImage(file="backround.png")
            window_backround_st = Label(self.root, bd=0, image=photo1).place(x=0, y=20, width=1270, height=750)
            add_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            add_Frame.place(x=10, y=77, width=650, height=663)
            add_bg = PhotoImage(file="full 444.png")
            add_bg_lable = Label(add_Frame, bd=0, image=add_bg).place(x=0, y=0, width=650, height=663)
            lbl_add1_code = Label(add_Frame, text="Name *full      ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=90)
            lbl_add2_code = Label(add_Frame, text="Email              ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=144)
            lbl_add3_code = Label(add_Frame, text="Phone             ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=198)
            lbl_add4_code = Label(add_Frame, text="Street             ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=252)
            lbl_add5_code = Label(add_Frame, text="City                 ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=306)
            lbl_add6_code = Label(add_Frame, text="State/region   ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=360)
            lbl_add7_code = Label(add_Frame, text="Post Code       ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=414)
            lbl_add8_code = Label(add_Frame, text="Country          ➤", font=("dubai medium", 15, 'bold'), bg='black', fg='white').place(x=68, y=468)

            txt_add1_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add1_code, bg='white', fg='black').place(x=290, y=90, relwidth=0.4335)
            txt_add2_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add2_code, bg='white', fg='black').place(x=290, y=145, relwidth=0.4335)
            txt_add3_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add3_code, bg='white', fg='black').place(x=290, y=200, relwidth=0.4335)
            txt_add4_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add4_code, bg='white', fg='black').place(x=290, y=255, relwidth=0.4335)
            txt_add5_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add5_code, bg='white', fg='black').place(x=290, y=307, relwidth=0.4335)
            txt_add6_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add6_code, bg='white', fg='black').place(x=290, y=360, relwidth=0.4335)
            txt_add7_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add7_code, bg='white', fg='black').place(x=290, y=416, relwidth=0.4335)
            txt_add8_code = Entry(add_Frame, font=("dubai medium", 15), textvariable=self.var_add8_code, bg='white', fg='black').place(x=290, y=470, relwidth=0.4335)

            btn_generator = Button(self.root, text="G e n e r a t e", command=self.generate4, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=120, y=600)
            btn_clear = Button(self.root, text="C l e a r", command=self.clear, font=("times new roman", 25, 'bold'), bg='#008000', fg='white').place(x=420, y=600)
            self.msg = ""
            self.lbl_msg = Label(add_Frame, text=self.msg, font=('times new roman', 20), bg='black', fg='green')
            self.lbl_msg.place(x=75, y=600, relwidth=0.7899)

# =============== QR CODE window ===========
            qr_Frame = Frame(self.root, bd=0, relief=RIDGE, bg='black')
            qr_Frame.place(x=760, y=77, width=500, height=663)
            qr_bg = PhotoImage(file="Qr window bg.png")
            qr_bg_lable = Label(qr_Frame, bd=0, image=qr_bg).place(x=0, y=0, width=500, height=663)
            self.qr_code = Label(qr_Frame, text='After pressing \nGenerate , QR code \nwill appear here ', font=('times new roman', 15), bg='white', fg='black')
            self.qr_code.place(x=75, y=250, width=350, height=350)

            pic = PhotoImage(file="down2.png")
            save_btn = Button(qr_Frame, image=(pic), bg='black', cursor='bottom_side', bd=0, command=self.save4).place(x=165, y=55, width=173, height=50)
            self.message = Label(qr_Frame, text='NOTE 1 : MINIMIZE WINDOW after pressed download\nNOTE 2 : After downloading please change the file name\n     if u wanna download another QR-Code ', font=('times new roman', 13), bg='black', fg='red').place(x=64, y=120)
            qr_Frame.mainloop()

        photo = PhotoImage(file="final11.png")
        window_backround = Label(self.root, bd=0, image=photo).place(x=0, y=20, width=1270, height=750)
        st_button = Button(self.root, text="( ST Click Me )", bd=1,  command=myclick, font=("times new roman", 20), bg='#000000', fg='white').place(x=160, y=350, width=250, height=50)
        url_button = Button(self.root, text="( URL Click Me )", bd=1, command=myclick1, font=("consolas", 20), bg='#000000', fg='white').place(x=800, y=350, width=250, height=50)
        ct_button = Button(self.root, text="( CT Click Me )", bd=1, command=myclick2, font=("consolas", 20), bg='#000000', fg='white').place(x=160, y=560, width=250, height=50)
        add_button = Button(self.root, text="( Add Click Me )", bd=1, command=myclick3, font=("consolas", 20), bg='#000000', fg='white').place(x=800, y=560, width=250, height=50)
        root.mainloop()
    def clear(self):
        self.var_st_code.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

        self.var_url_code.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

        self.var_ct1_code.set('')
        self.var_ct2_code.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

        self.var_add1_code.set('')
        self.var_add2_code.set('')
        self.var_add3_code.set('')
        self.var_add4_code.set('')
        self.var_add5_code.set('')
        self.var_add6_code.set('')
        self.var_add7_code.set('')
        self.var_add8_code.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')



    def generate1(self):
        if self.var_st_code.get() == "":
            self.msg='All fields are required'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=5
            )

            qr.add_data(self.var_st_code.get())
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            print(img)

    # ================ QR code image update =============
            self.im = ImageTk.PhotoImage(img)
            self.qr_code.config(image=self.im)
            # ========= updating ============
            self.msg = "QR Code Generated Sucessfully !!!"
            self.lbl_msg.config(text=self.msg, fg='green')

    def save1(self):

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)

        qr.add_data(self.var_st_code.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("QRcode  (your File Name).png")
        pass


    def generate2(self):
        if self.var_url_code.get() == "":
            self.msg = 'All fields are required'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )

            qr.add_data(self.var_url_code.get())
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            print(img)

    # ================ QR code image update =============
            self.im = ImageTk.PhotoImage(img)
            self.qr_code.config(image=self.im)
            # ========= updating ============
            self.msg = "QR Code Generated Sucessfully !!!"
            self.lbl_msg.config(text=self.msg, fg='green')

    def save2(self):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

        qr.add_data(self.var_url_code.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("URL QRcode .png")
        pass

    def generate3(self):
        if self.var_ct1_code.get() == "" or self.var_ct2_code.get() == "":
            self.msg='All fields are required'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=5
            )

            qr.add_data(f"Contact Name : {self.var_ct1_code.get()}\nContact Number : {self.var_ct2_code.get()} ")
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            print(img)

    # ================ QR code image update =============
            self.im = ImageTk.PhotoImage(img)
            self.qr_code.config(image=self.im)
            # ========= updating ============
            self.msg = "QR Code Generated Sucessfully !!!"
            self.lbl_msg.config(text=self.msg, fg='green')


    def save3(self):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)

        qr.add_data(f"Contact Name : {self.var_ct1_code.get()}\nContact Number : {self.var_ct2_code.get()} ")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("Contact QRcode .png")
        pass

    def generate4(self):
        if self.var_add1_code.get() == "" or self.var_add2_code.get() == "" or self.var_add3_code.get() == "" or self.var_add4_code.get() == "" or self.var_add5_code.get() == "" or self.var_add6_code.get() == "" or self.var_add7_code.get() == "" or self.var_add8_code.get() == "":
            self.msg='All fields are required'
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=6,
                border=5
            )

            qr.add_data(f"Name : {self.var_add1_code.get()}\nEmail : {self.var_add2_code.get()}\nPhone : {self.var_add3_code.get()}\nStreet : {self.var_add4_code.get()}\nCity : {self.var_add5_code.get()}\nState : {self.var_add6_code.get()}\nPost Code : {self.var_add7_code.get()}\nCountry : {self.var_add8_code.get()}")
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            print(img)

    # ================ QR code image update =============
            self.im = ImageTk.PhotoImage(img)
            self.qr_code.config(image=self.im)
            # ========= updating ============
            self.msg = "QR Code Generated Sucessfully !!!"
            self.lbl_msg.config(text=self.msg, fg='green')

    def save4(self):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=6, border=5)

        qr.add_data(f"Name : {self.var_add1_code.get()}\nEmail : {self.var_add2_code.get()}\nPhone : {self.var_add3_code.get()}\nStreet : {self.var_add4_code.get()}\nCity : {self.var_add5_code.get()}\nState : {self.var_add6_code.get()}\nPost Code : {self.var_add7_code.get()}\nCountry : {self.var_add8_code.get()}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("Address QRcode .png")
        pass

        root.mainloop()

root = Tk()
obj = QR_generator(root)
root.mainloop()