from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

from Main import Advanced_Attendance_System


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("LOGIN")

        self.var_txtuser = StringVar()
        self.var_txtpass = StringVar()

        # self.bg = ImageTk.PhotoImage(
        #     file=r"Project_Images\3.png")
        # lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ====================Title=====================
        title_lbl = Label(self.root, text="ADVANCED ATTENDANCE SOFTWARE", font=(
            "times new roman", 30, "bold"), bg="DarkBlue", fg="White")
        title_lbl.place(x=0, y=0, width=1520, height=40)

        # ===================Background Image===========================
        img_top = Image.open(r"Project_Images\RegisterBG.jpg")
        img_top = img_top.resize((1520, 750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1520, height=750)

        frame = Frame(self.root, bg="White")
        frame.place(x=535, y=120, width=450, height=580)

        img1 = Image.open(
            r"Project_Images\LoginIcon.jpg")
        img1 = img1.resize((130, 130), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=700, y=125, width=130, height=130)

        get_str = Label(frame, text="Get Started!!", font=(
            "times new roman", 20, "bold"), fg="DarkBlue", bg="White")
        get_str.place(x=160, y=130)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 18, "bold"), fg="DarkBlue", bg="White")
        username.place(x=70, y=195)

        self.txtuser = ttk.Entry(
            frame, textvariable=self.var_txtuser, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=225, width=300)

        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 18, "bold"), fg="DarkBlue", bg="White")
        password.place(x=70, y=271)

        self.txtpass = ttk.Entry(
            frame, textvariable=self.var_txtpass, background="white", foreground="Black", show='*', font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=300, width=300)

    # ===========================Icon Images========================

        img2 = Image.open(
            r"Project_Images\LoginIcon2.jpg")
        img2 = img2.resize((30, 30), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimage2,
                        bg="White", borderwidth=0)
        lblimg2.place(x=40, y=195, width=30, height=30)

        img3 = Image.open(
            r"Project_Images\PasswordIcon.jpg")
        img3 = img3.resize((30, 30), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimage3,
                        bg="white", borderwidth=0)
        lblimg3.place(x=40, y=271, width=30, height=30)

        # login_button

        img0 = Image.open(
            r"Project_Images\LoginButton1.jpg")
        img0 = img0.resize((200, 65), Image.Resampling.LANCZOS)
        self.photoimage0 = ImageTk.PhotoImage(img0)
        login_button = Button(frame, image=self.photoimage0, command=self.login,
                              borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        # bd=3, relief=RIDGE, , bg="DarkBlue", activeforeground="white", activebackground="red")
        login_button.place(x=120, y=390, width=200)

        # register_button

        img4 = Image.open(
            r"Project_Images\RegisterButton1.png")
        img4 = img4.resize((200, 60), Image.Resampling.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        register_button = Button(frame, image=self.photoimage4, bg="white", command=lambda: [self.register_window(), self.reset_data()], borderwidth=0, cursor="hand2", activebackground="White", font=(
            "times new roman", 15, "bold"))
        register_button.place(x=20, y=510, width=200)

        # forget_button
        forget_button = Button(frame, text="Forget Password", command=lambda: [self.forget_password_window(), self.reset_one()], font=(
            "times new roman", 15, "bold"), borderwidth=0, fg="Red", bg="White", activebackground="White")
        forget_button.place(x=20, y=470, width=200)

        check_button = Checkbutton(frame, text="Show Password", command=self.show_password, font=(
            "times new roman", 15, "bold"), borderwidth=0, fg="DarkBlue", bg="White", activebackground="White")
        check_button.place(x=20, y=340, width=200)

    def show(self):
        self.txtpass.config(show='')

    def hide(self):
        self.txtpass.config(show='*')

    def show_password(self):
        if self.txtpass.cget('show') == '*':
            self.txtpass.config(show='')
        else:
            self.txtpass.config(show='*')

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_window(self.new_window)

    def reset_data(self):

        self.var_txtuser.set("")
        self.var_txtpass.set("")

    def reset_one(self):
        self.var_txtpass.set("")

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields are Required !!")

        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s ", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                # print(row)
                messagebox.showerror("Invalid", "Invalid Credentials !!")
            else:
                open_main = messagebox.askyesno("YesNo", "Access Only Admin")

                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Advanced_Attendance_System(self.new_window)
                    messagebox.showinfo(
                        "Success", "LOGIN SUCCESSFUL !!", parent=self.new_window)
                    messagebox.showinfo(
                        "Success", "Welcome to ADVANCED ATTENDANCE SOFTWARE !!", parent=self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
           # self.clear()
            conn.close()
    # =====================================Reset Password========================================

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror(
                "Error", "Select Security Question", parent=self.root2)
        elif self.txt_securityA.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the Answer", parent=self.root2)
        elif self.txt_new_password.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the New Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
            my_cursor = conn.cursor()
            qury = (
                "select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
            valu = (self.txtuser.get(), self.combo_security_Q.get(),
                    self.txt_securityA.get(),)
            my_cursor.execute(qury, valu)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Please Enter Correct Answer", parent=self.root2)
            else:
                query = ("update register set Password =%s where Email=%s")
                value = (self.txt_new_password.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Your Password has been Reset, Please Login with New Password", parent=self.root2)
                self.root2.destroy()

    # ======================================Forget Password=======================================

    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the Email Address to Reset the Password ")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
            my_cursor = conn.cursor()
            query = ("select * from register where Email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror(
                    "My Error", "Please Enter the Valid User Name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("452x552+533+150")
                self.root2.resizable(0, 0)

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 20, "bold"), fg="White", bg="DarkBlue")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=(
                    "times new roman", 15, "bold"), bg="white", fg="Darkblue")
                security_Q.place(x=110, y=100)

                self.combo_security_Q = ttk.Combobox(self.root2, font=(
                    "times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                    "Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_security_Q.place(x=110, y=140, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=(
                    "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
                security_A.place(x=110, y=215)

                self.txt_securityA = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_securityA.place(x=110, y=250, width=250)

                new_password = Label(self.root2, text="New Password", font=(
                    "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
                new_password.place(x=110, y=315)

                self.txt_new_password = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_new_password.place(x=110, y=350, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=(
                    "times new roman", 15, "bold"), fg="white", bg="DarkBlue")
                btn.place(x=100, y=400, width=270)


class Register_window:
    def __init__(self, root,):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("REGISTER")

    # ===========================variables======================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

    # ==================BG image=========================
        self.bg = ImageTk.PhotoImage(
            file=r"Project_Images\RegisterBg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

    # ==================left image=========================
        self.bg1 = ImageTk.PhotoImage(
            file=r"Project_Images\Register1.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

    # ===============main Frame===============================

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

    # ======================Label and entry=========================

    # =======================row1========================

        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        fname.place(x=50, y=90)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=120, width=250)
        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        l_name.place(x=370, y=90)
        self.txt_lname = ttk.Entry(

            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=120, width=250)

    # ============================row2======================

        contact = Label(frame, text="Contact Number", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)
    # =====================row3================================

        security_Q = Label(frame, text="Select Security Questions", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

    # ===========================row4=========================

        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue")
        confirm_pswd.place(x=370, y=310)

        self.confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.confirm_pswd.place(x=370, y=340, width=250)

    # =========================checkButton==========================
        self.var_check = IntVar()
        Checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=(
            "times new roman", 15, "bold"), onvalue=1, offvalue=0, fg="DarkBlue", bg="White")
        Checkbtn.place(x=50, y=390)
    # ==========================buttons==============================

        img = Image.open(
            r"Project_Images\RegisterButton2.jpg")
        img = img.resize((200, 70), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data,
                    borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=50, y=450, width=200)

        img1 = Image.open(
            r"Project_Images\LoginButton2.png")
        img1 = img1.resize((200, 60), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, command=self.return_login,
                    borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=380, y=460, width=200)

    # ===============================Function Declaration=========================================

    def register_data(self):

        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Password  & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and conditions", parent=self.root)
        elif (len(self.var_contact.get()) != 10):
            messagebox.showerror(
                "Error", " Wrong Mobile Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
            my_cursor = conn.cursor()
            query = ("select * from register where Email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User Already Exist,Please Try With Another Email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Success", "Registered Successfully !!", parent=self.root)
                self.var_check.set(0)
                self.var_fname.set("")
                self.var_lname.set("")
                self.var_email.set("")
                self.var_contact.set("")
                self.var_securityA.set("")
                self.var_securityQ.set("Select")
                self.var_confpass.set("")
                self.var_pass.set("")

    def return_login(self):
        self.root.destroy()
    # def erase_data(self):
    #         self.var_check.set(0)
    #         self.var_fname.set("")
    #         self.var_lname.set("")
    #         self.var_email.set("")
    #         self.var_contact.set("")
    #         self.var_securityA.set("")
    #         self.var_securityQ.set("Select")
    #         self.var_confpass.set("")
    #         self.var_pass.set("")


if __name__ == "__main__":
    main()
