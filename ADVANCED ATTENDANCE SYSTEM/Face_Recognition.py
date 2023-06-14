from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("FACE RECOGNITION SYSTEM")

        title_lbl = Label(self.root, text="FACE RECOGNITION ", font=(
            "times new roman", 35, "bold"), bg="white", fg="Darkgreen")
        title_lbl.place(x=0, y=0, width=1520, height=40)
        # first image
        img_top = Image.open(r"Project_Images\FaceRecognize.png")
        img_top = img_top.resize((1520, 740), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1520, height=740)

        # # 2nd image
        # img_bottom = Image.open(r"Project_Images\1.png")
        # img_bottom = img_bottom.resize((850, 740), Image.Resampling.LANCZOS)
        # self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # f_lbl = Label(self.root, image=self.photoimg_bottom)
        # f_lbl.place(x=750, y=40, width=850, height=740)

        # button
        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", command=self.face_recog, font=(
            "times new roman", 20, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=610, y=680, width=310, height=40)

# ===============================ATTENDANCE================================

    def mark_attendance(self, i, r, n, d):
        with open("Attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%I:%M:%S %p")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")


# ================================FACE RECOGNITION=============================#


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where ID = '{}'".format(str(id)))
                n = my_cursor.fetchone()
# n=str(n)
                n = "+".join(n)

                my_cursor.execute(
                    "select Usn from student where ID = '{}'".format(str(id)))
                r = my_cursor.fetchone()
               # r=str(r)
                r = "+".join(r)

                my_cursor.execute(
                    "select Department from student where ID = '{}'".format(str(id)))
                d = my_cursor.fetchone()
             #   d=str(d)
                d = "+".join(d)

                my_cursor.execute(
                    "select ID from student where ID = '{}'".format(str(id)))
                i = my_cursor.fetchone()
             #   d=str(d)
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Usn:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "UNKNOWN FACE", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION", img)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Attendance completed !!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

    #     # if cv2.waitKey(1) & 0xFF == 27:
    #     #     break

    # video_cap.release()
    # cv2.destroyAllWindows()
