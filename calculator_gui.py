import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from add_course_popup import AddCoursePopup
from gpa_calculator import GPACalculator
from course import Course
import csv


class MainAppController(tk.Frame):

    def __init__(self, parent):
        """ Initialize the GUI """
        tk.Frame.__init__(self, parent)

        left_frame = tk.Frame(master=self)
        left_frame.grid(row=0, column=0, columnspan=2)

        right_frame = tk.Frame(master=self)
        right_frame.grid(row=0, column=2)

        courses_label = tk.Label(left_frame, text="Courses:")
        courses_label.grid(row=0, column=0)

        self.courses_list = tk.Listbox(left_frame)
        self.courses_list.grid(row=1, column=0, columnspan=2)
        self.courses_list.bind("<<ListboxSelect>>", self._update_info_box)

        ttk.Button(left_frame, text="Add Course", command=self._add_course).grid(row=2, column=0)
        ttk.Button(left_frame, text="Delete Course", command=self._delete_course).grid(row=2, column=1)
        ttk.Button(left_frame, text="Upload csv", command=self._open_file).grid(row=4, column=0)
        ttk.Button(left_frame, text="Save csv", command=self._save_file).grid(row=4, column=1)

        courses_label = tk.Label(right_frame, state='normal', text="Course info:")
        courses_label.grid(row=0, column=0)

        self.course_info = tk.Text(right_frame, height=8, width=50)
        self.course_info.grid(row=1, column=0)

        self.credits_label = tk.Label(right_frame, text="Total credits: ")
        self.credits_label.grid(row=2, column=0)

        self.grade_points_label = tk.Label(right_frame, text="Grade points: ")
        self.grade_points_label.grid(row=3, column=0)

        self.gpa_label = tk.Label(right_frame, text="GPA: ")
        self.gpa_label.grid(row=4, column=0)

        self.calc = GPACalculator()
        self.get_all_courses()

    def _update_info_box(self, evt):
        """ Update the course info box """
        selected_course = self.courses_list.curselection()
        if selected_course:
            selected_index = selected_course[0]
            course_code = self.courses_list.get(selected_index)
            self.course_info.configure(state='normal')
            self.course_info.delete(1.0, tk.END)
            course = self.calc.get_course(course_code)
            for k, v in course.to_dict().items():
                self.course_info.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
                self.course_info.insert(tk.END, f"{v}\n")
            self.course_info.configure(state='disabled')

    def get_all_courses(self):
        """ Get all courses and update the display """
        self.courses_list.delete(0, tk.END)
        self.course_info.delete(1.0, tk.END)
        courses = self.calc.get_courses()
        for course in courses:
            self.courses_list.insert(tk.END, course.code)
        self.update_summary()

    def update_summary(self):
        """ Update summary of grades """
        self.credits_label['text'] = f"Total credits: {self.calc.calculate_credits()}"
        self.grade_points_label['text'] = f"Total grade points: {self.calc.calculate_grade_points()}"
        self.gpa_label['text'] = f"GPA: {self.calc.calculate_gpa()}"

    def _add_course(self):
        """ Add Course popup """
        self._popup_win = tk.Toplevel()
        self._popup_win.title('Add course')
        screen_height = root.winfo_screenheight()
        screen_width = root.winfo_screenwidth()
        popup_height = 109
        popup_width = 202
        x_cordinate = int((screen_width / 2) - (popup_width / 2))
        y_cordinate = int((screen_height / 2) - (popup_height / 2))
        self._popup_win.geometry("{}x{}+{}+{}".format(popup_width, popup_height, x_cordinate, y_cordinate))
        self._popup = AddCoursePopup(self._popup_win, self._close_cb, self.calc)

    def _delete_course(self):
        """ Delete Course from courses list """
        selected_values = self.courses_list.curselection()
        if selected_values:
            selected_index = selected_values[0]
            course_code = self.courses_list.get(selected_index)
            self.calc.delete_course(course_code)
            self.get_all_courses()

    def _close_cb(self):
        """ Close callback """
        self._popup_win.destroy()
        self.get_all_courses()

    def _quit_callback(self):
        """ Quit callback """
        self.quit()

    def _open_file(self):
        """ Open file, generate Courses, and add to GPACalculator """
        filename = filedialog.askopenfile()
        if filename:
            try:
                self.calc.reset_courses()
                csv_reader = csv.reader(filename, delimiter=',')
                for row in csv_reader:
                    course = Course(row[0], row[1], float(row[2]), int(row[3]))
                    self.calc.add_course(course)
                self.get_all_courses()
            except ValueError as e:
                print(e)

    def _save_file(self):
        """ Save the current courses into a CSV file """
        filename = filedialog.asksaveasfilename(title="Save File", filetypes=[("csv files", "*.csv")],
                                                confirmoverwrite=True, defaultextension='.csv')
        if filename:
            with open(filename, newline='', mode='w') as f:
                csv_writer = csv.writer(f, delimiter=',')
                for course in self.calc.get_courses():
                    csv_writer.writerow([course.code, course.name, course.credits, course.mark])


if __name__ == '__main__':
    root = tk.Tk()
    root.title('GPA Calculator')
    root.resizable(False, False)
    window_width = 600
    window_height = 250

    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    # root.geometry("600x250")
    MainAppController(root).pack()
    root.mainloop()
