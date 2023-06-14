from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register_window:
    def __init__(self, root):
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
            file=r"C:\Users\saksh\Desktop\PROJECT\college_images\u.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

    # ==================left image=========================
        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\saksh\Desktop\PROJECT\college_images\thought-good-morning-messages-LoveSove.jpg")
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
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=80)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=120, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

    # ============================row2======================

        contact = Label(frame, text="Contact Number", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)
    # =====================row3================================

        security_Q = Label(frame, text="Select Security Questions", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=360, y=270, width=250)

    # ===========================row4=========================

        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.confirm_pswd.place(x=370, y=340, width=250)

    # =========================checkButton==========================
        self.var_check = IntVar()
        Checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=(
            "times new roman", 15, "bold"), onvalue=1, offvalue=0)
        Checkbtn.place(x=50, y=380)
    # ==========================buttons==============================

        img = Image.open(
            r"C:\Users\saksh\Desktop\PROJECT\college_images\register-now-button1.jpg")
        img = img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data,
                    borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=50, y=450, width=200)

        img1 = Image.open(
            r"C:\Users\saksh\Desktop\PROJECT\college_images\loginpng.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0,
                    cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=380, y=450, width=200)

    # ===============================Function Declaration=========================================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields Are Required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Passweord  & Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User Already Exist,Please Try With Another Email")
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
            messagebox.showinfo("Success", "Register Successfully")


if __name__ == "__main__":
    root = Tk()
    obj = Register_window(root)
    root.mainloop()
