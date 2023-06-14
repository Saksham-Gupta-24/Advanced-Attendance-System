from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        title_lbl = Label(self.root, text="HELP DESK ", font=(
            "times new roman", 35, "bold"), bg="white", fg="SlateBlue")
        title_lbl.place(x=0, y=0, width=1520, height=40)

        img_top = Image.open(r"Project_Images\Help.jpg")
        img_top = img_top.resize((1520, 750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1520, height=750)

        # Developer info
        dep_label = Label(self.root, text="MAIL ID: officialsaksham23@gmail.com",
                          font=("times new roman", 18, "bold"), bg="white")
        dep_label.place(x=1010, y=700)

        new = 1
        url = "https://www.linkedin.com/in/saksham-gupta-99ba8022b/"
        url1 = "https://github.com/Saksham-Gupta-24"

        def openweb():
            webbrowser.open(url, new=new)

        def openweb1():
            webbrowser.open(url1, new=new)
        Btn = Button(root, text="LinkedIn", command=openweb, font=(
            "times new roman", 15, "bold"), bg="coral", fg="Black")
        Btn.place(x=1010, y=657, width=130)

        Btn1 = Button(root, text="GitHub", command=openweb1, font=(
            "times new roman", 15, "bold"), bg="coral", fg="Black")
        Btn1.place(x=1305, y=657, width=130)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
