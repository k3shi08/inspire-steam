import tkinter as tk
from tkinter import messagebox, ttk

class Student:
    def __init__(self, student_id, name, course, phone):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.phone = phone
        self.grade = None

class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")

        self.students = []

        # Input fields
        tk.Label(root, text="Student ID").grid(row=0, column=0)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)

        tk.Label(root, text="Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)

        tk.Label(root, text="Course").grid(row=2, column=0)
        self.course_entry = tk.Entry(root)
        self.course_entry.grid(row=2, column=1)

        tk.Label(root, text="Phone No").grid(row=3, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Register Student", command=self.register_student).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Display Students", command=self.display_students).grid(row=5, column=0, columnspan=2)

        # Treeview to display students
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Course", "Phone", "Grade"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Grade", text="Grade")
        self.tree.grid(row=6, column=0, columnspan=2)

        # Assign grade section
        tk.Label(root, text="Assign Grade").grid(row=7, column=0)
        self.grade_entry = tk.Entry(root)
        self.grade_entry.grid(row=7, column=1)

        tk.Button(root, text="Assign Grade", command=self.assign_grade).grid(row=8, column=0, columnspan=2)

    def register_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        course = self.course_entry.get()
        phone = self.phone_entry.get()

        if student_id and name and course and phone:
            student = Student(student_id, name, course, phone)
            self.students.append(student)
            messagebox.showinfo("Success", "Student Registered Successfully")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def display_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in self.students:
            self.tree.insert("", "end", values=(student.student_id, student.name, student.course, student.phone, student.grade))

    def assign_grade(self):
        selected_item = self.tree.selection()
        if selected_item:
            grade = self.grade_entry.get()
            if grade:
                item = selected_item[0]
                student_id = self.tree.item(item, "values")[0]
                for student in self.students:
                    if student.student_id == student_id:
                        student.grade = grade
                        messagebox.showinfo("Success", "Grade Assigned Successfully")
                        self.display_students()
                        self.grade_entry.delete(0, tk.END)
                        return
            else:
                messagebox.showwarning("Input Error", "Please enter a grade")
        else:
            messagebox.showwarning("Selection Error", "Please select a student")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()