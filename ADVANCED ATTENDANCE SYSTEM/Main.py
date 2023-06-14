from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from Student import Student
from Train import Train
from Face_Recognition import Face_Recognition
from Attendance import Attendance
from Developer import Developer
from Help import Help


class Advanced_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        # firstimage
        img = Image.open(
            r"Project_Images\Main1.png")
        img = img.resize((506, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=506, height=130)

        # secondimage
        img1 = Image.open(
            r"Project_Images\Main2.png")
        img1 = img1.resize((507, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=506, y=0, width=507, height=130)

        # thirdimage
        img2 = Image.open(
            r"Project_Images\Main3.png")
        img2 = img2.resize((507, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1013, y=0, width=507, height=130)

        # backgroundimage
        img3 = Image.open(r"Project_Images\MainBg.png")
        img3 = img3.resize((1520, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1520, height=710)

        title_lbl = Label(bg_img, text="WELCOME TO ADVANCED ATTENDANCE SYSTEM", font=(
            "times new roman", 35, "bold"), bg="DarkBlue", fg="White")
        title_lbl.place(x=-2, y=-2, width=1520, height=45)

        # =========================time========================

        def time():
            string = strftime('%x \n%A')
            lbl.config(text=string)
            # lbl.after(1000, time)

            # string1=strftime('%H:%M:%S %p')
            string1 = strftime('%I:%M:%S %p')
            lbl1.config(text=string1)
            lbl1.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 15, 'bold'),
                    background='DarkBlue', foreground='White')
        lbl.place(x=0, y=(-4), width=110, height=50)

        lbl1 = Label(title_lbl, font=('times new roman', 14, 'bold'),
                     background='DarkBlue', foreground='White')
        lbl1.place(x=1400, y=(-10), width=110, height=50)

        time()

        # studentbutton
        img4 = Image.open(
            r"Project_Images\MainStudent.png")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Registeration", command=self.student_details,
                      cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


        
        # Photos_button
        img9 = Image.open(
            r"Project_Images\MainPhotos.png")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Photo Samples", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)


        # Train_face_button
        img8 = Image.open(
            r"Project_Images\MainTrain.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # detect_face_button
        img5 = Image.open(
            r"Project_Images\MainFace.png")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Attendance_button
        img6 = Image.open(
            r"Project_Images\MainAttendance.png")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2", command=self.attendance_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance Record", cursor="hand2", command=self.attendance_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)



        
        # Developer_button
        img10 = Image.open(
            r"Project_Images\MainDeveloper.png")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.developer_data)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)


        # Help_button
        img7 = Image.open(
            r"Project_Images\MainHelp.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2", command=self.helper_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.helper_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        

        # Exit_face_button
        img11 = Image.open(
            r"Project_Images\MainExit.png")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,
                    cursor="hand2", command=self.IExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.IExit, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("Data")

    def IExit(self):
        self.IExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure to Exit this project ??", parent=self.root)
        if self.IExit > 0:
            self.root.destroy()
        else:
            return

# ====================================Functions Buttons=============================================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helper_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Advanced_Attendance_System(root)
    root.mainloop()
