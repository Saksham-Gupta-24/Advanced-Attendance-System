from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        # ====================Label=====================

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "times new roman", 35, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=0, width=1520, height=40)

        # ==============First Image=======================
        img_top = Image.open(r"Project_Images\Train1.png")
        img_top = img_top.resize((1520, 300), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1520, height=300)
        # =============Button===========================
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier,
                      cursor="hand2", font=("times new roman", 20, "bold"), bg="Orchid", fg="Indigo")
        b1_1.place(x=460, y=340, width=600, height=60)
        # ==============Second Image===========================
        img_bottom = Image.open(r"Project_Images\Train2.jpg")
        img_bottom = img_bottom.resize((760, 370), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width=760, height=370)
        # ==============Third Image============================
        img_bottom1 = Image.open(r"Project_Images\Train2.jpg")
        img_bottom1 = img_bottom1.resize((760, 370), Image.Resampling.LANCZOS)
        self.photoimg_bottom1 = ImageTk.PhotoImage(img_bottom1)

        f_lbl1 = Label(self.root, image=self.photoimg_bottom1)
        f_lbl1.place(x=760, y=400, width=760, height=370)

    def train_classifier(self):

        data_dir = ("Data")
        path = [os.path.join(data_dir, file)for file in os.listdir(data_dir)]

        faces = []
        ids = []
        try:
            for image in path:
                img = Image.open(image).convert('L')  # Gray scale image
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1) == 13

            ids = np.array(ids)

    # ==================================Train the classifier And Save ========================================

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, np.array(ids))
            clf.write("Classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo(
                "Result", "Training Datasets Completed !!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", "No Photos Found", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
