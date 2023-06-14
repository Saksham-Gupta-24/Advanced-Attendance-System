from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("CREATER")
        # ====================Title=====================
        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="DarkBlue")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # ===================Background Image===========================
        img_top = Image.open(r"Project_Images\DeveloperBg.png")
        img_top = img_top.resize((1520, 750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1520, height=750)

        # #frame
        # main_frame=Frame(f_lbl,bd=2,bg="white")
        # main_frame.place(x=958,y=-1,width=560,height=600)
        # # ==========================First Image==========================
        img_top1 = Image.open(
            r"Project_Images\Developer.jpg")
        img_top1 = img_top1.resize((250, 250), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=30, y=400, width=250, height=250)

        # Developer info
        dep_label = Label(self.root, text="HELLO, MY NAME IS SAKSHAM GUPTA", font=(
            "times new roman", 17, "bold"), bg="DarkBlue", fg="White")
        dep_label.place(x=30, y=641)

        dep_label = Label(self.root, text="I AM A DEVELOPER OF THIS SOFTWARE ", font=(
            "times new roman", 17, "bold"), fg="white", bg="DarkBlue")
        dep_label.place(x=30, y=673)

        # #thirdimage
        # img2=Image.open(r"C:\Users\saksh\Desktop\PROJECT\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        # img2=img2.resize((560,390),Image.Resampling.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(main_frame,image=self.photoimg2)
        # f_lbl.place(x=-2,y=210,width=560,height=390)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
