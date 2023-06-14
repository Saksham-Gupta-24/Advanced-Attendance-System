from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import re


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x775+0+5")
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        # ======================================Variables=======================================

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_usn = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()
        self.var_searchcombo = StringVar()

        def click(event):
            dob_entry.config(state=NORMAL)
            dob_entry.delete(0, END)

         # firstimage
        img = Image.open(
            r"Project_Images\Student1.png")
        img = img.resize((506, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=506, height=120)

        # secondimage
        img1 = Image.open(
            r"Project_Images\Student2.png")
        img1 = img1.resize((507, 120), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=506, y=0, width=507, height=120)

        # thirdimage
        img2 = Image.open(
            r"Project_Images\Student3.png")
        img2 = img2.resize((507, 120), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1013, y=0, width=507, height=120)

        # backgroundimage
        img3 = Image.open(r"Project_Images\StudentBg.jpg")
        img3 = img3.resize((1520, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=120, width=1520, height=710)

        # Main Frame
        title_lbl = Label(bg_img, text="STUDENT REGISTERATION", font=(
            "times new roman", 35, "bold"), bg="DarkBlue", fg="White")
        title_lbl.place(x=-2, y=-2, width=1520, height=40)

        main_frame = Frame(bg_img, bd=2, bg="DarkBlue")
        main_frame.place(x=0, y=40, width=1514, height=612)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=5, y=5, width=770, height=600)

        img_left = Image.open(
            r"Project_Images\Student4.png")
        img_left = img_left.resize((765, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=765, height=130)

        # Current_course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=1, y=135, width=765, height=115)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 13, "bold"), state="readonly", width=25)
        dep_combo["values"] = ("Select Department", "Aerospace Engineering", "Artificial Intelligence And Machine Learning", "Automobile Engineering", "Computer Science And Engineering", "Computer Engineering", "Civil Engineering",
                               "Chemical Engineering", "Electronics And Communication Engineering", "Electrical AND Electronics Engineering", "Industrial Engineering", "Information Science And Engineering", "Mechanical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course

        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=20, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), state="readonly", width=25)
        course_combo["values"] = (
            "Select Course", "B.E.", "M.tech", "B.BA", "M.BA", "B.com")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year

        year_label = Label(current_course_frame, text="Batch-Year",
                           font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="readonly", width=25)
        year_combo["values"] = ("Select Year", "2019-20",
                                "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester

        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=20, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 13, "bold"), state="readonly", width=25)
        semester_combo["values"] = (
            "Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class_Student_Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=1, y=250, width=765, height=325)

        # Student_ID
        student_Id_label = Label(class_student_frame, text="Student ID", font=(
            "times new roman", 13, "bold"), bg="white")
        student_Id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_Id_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_id, width=20, font=("times new roman", 13, "bold"))
        student_Id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student_Name
        studentName_label = Label(class_student_frame, text="Student Name", font=(
            "times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=45, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class_Division
        class_div_label = Label(class_student_frame, text="Class Division", font=(
            "times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        div_combo["values"] = ("Select Division ", "A", "B", "C", "D", "E")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # USN
        usn_label = Label(class_student_frame, text="USN", font=(
            "times new roman", 13, "bold"), bg="white")
        usn_label.grid(row=1, column=2, padx=45, pady=5, sticky=W)

        usn_entry = ttk.Entry(class_student_frame, textvariable=self.var_usn, width=20, font=(
            "times new roman", 13, "bold"))
        usn_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=(
            "times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="D.O.B", font=(
            "times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=45, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 13, "bold"))
        dob_entry.insert(0, "DD/MM/YYYY")
        dob_entry.config(state=DISABLED)
        dob_entry.bind("<Button-1>", click)
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=(
            "times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone_No
        phone_label = Label(class_student_frame, text="Phone No.", font=(
            "times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=45, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=(
            "times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher_Name
        teacherName_label = Label(class_student_frame, text="Teacher Name", font=(
            "times new roman", 13, "bold"), bg="white")
        teacherName_label.grid(row=4, column=2, padx=45, pady=5, sticky=W)

        teacherName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio_buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # 1st Buttons_Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=215, width=763, height=40)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=18, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        reset_btn.grid(row=0, column=3)

        # 2nd Buttons_Frame
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=258, width=763, height=40)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=37, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Update Photo Sample", width=37, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=785, y=5, width=725, height=600)

        img_right = Image.open(
            r"Project_Images\Student5.png")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=1, y=0, width=720, height=130)

        # ====================================================SEARCHING SYSTEM=======================================================

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=1, y=135, width=720, height=80)

        search_label = Label(search_frame, text="Search Student By:", font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchcombo, font=(
            "times new roman", 13, "bold"), state="readonly", width=10)
        search_combo["values"] = ("Select", "Usn", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, textvariable=self.var_search, font=(
            "times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, width=10, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        search_btn.grid(row=0, column=3, padx=1)

        showAll_btn = Button(search_frame, text="Show All", command=self.fetch_data, width=10, font=(
            "times new roman", 13, "bold"), bg="DarkBlue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=1)

        # ===============================================TABLE FRAME ======================================================
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=1, y=215, width=720, height=360)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "usn", "gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Batch-Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("usn", text="USN")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No.")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table.column("dep", width=200)
        self.student_table.column("course", width=150)
        self.student_table.column("year", width=150)
        self.student_table.column("sem", width=150)
        self.student_table.column("id", width=150)
        self.student_table.column("name", width=200)
        self.student_table.column("div", width=150)
        self.student_table.column("usn", width=160)
        self.student_table.column("gender", width=150)
        self.student_table.column("dob", width=150)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=150)
        self.student_table.column("address", width=200)
        self.student_table.column("teacher", width=200)
        self.student_table.column("photo", width=150)

        self.student_table["show"] = "headings"
        # style=ttk.Style()
        # style.theme_use("default")

        # style.configure("Treeview",background="#707070")

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ===========================================Function Declaration================================================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_address.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_course == "" or self.var_div == "Select Division" or self.var_dob == "" or self.var_email == "" or self.var_gender == "Select Gender" or self.var_usn == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        elif (len(self.var_phone.get()) != 10):
            messagebox.showerror(
                "Error", " Wrong Mobile Number", parent=self.root)

        # elif(self.var_email.get()!='^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'):
        #        messagebox.showerror("Error"," Wrong Mailll Number",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_usn.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "success", "Student details has been added successfully !!", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # =======================================fetch data=============================================

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===================================================get cursor=================================================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_usn.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_address.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_course == "" or self.var_div == "" or self.var_dob == "" or self.var_email == "" or self.var_gender == "" or self.var_usn == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update this Student Details ??", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Usn=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where ID =%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_usn.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student Details Updated Successfully!!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due TO:{str(es)}", parent=self.root)

    # Delete Function

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to Delete this Student Details ??", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Student Details Deleted Successfully !!", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due TO:{str(es)}", parent=self.root)

    # Reset Button
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_usn.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("DD/MM/YYYY")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # search

    def search_data(self):
        if self.var_searchcombo.get() == "Select":
            messagebox.showerror(
                "Error", "Select Combo Option", parent=self.root)
        elif self.var_search.get() == "":
            messagebox.showerror(
                "Error", "Fill the Search Field", parent=self.root)

        else:

            try:

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where " + str(
                    self.var_searchcombo.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()

                else:
                    messagebox.showerror(
                        "Error", "Data Not Found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)


# ==================================================Generate data set or Take photo samples===================================================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select year" or self.var_sem.get() == "Select semester" or self.var_address.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_course == "" or self.var_div == "" or self.var_dob == "" or self.var_email == "" or self.var_gender == "" or self.var_usn == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="yourpassword", database="advanced_attendance_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Usn=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where ID =%s", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_usn.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

    # ===============================================Load predefined data on face frontals from opencv========================================

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor =1.3
                    # Minimum Neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(
                            my_frame), (450, 450), fx=0.5, fy=0.5)
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating Data Sets completed !!!", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due TO:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
