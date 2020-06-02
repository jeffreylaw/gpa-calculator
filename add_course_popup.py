import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from course import Course


class AddCoursePopup(tk.Frame):
    """ Popup Frame to add a Course """

    def __init__(self, parent, close_callback, calc):
        """ Initialize popup window"""
        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.calc = calc
        self.grid(rowspan=2, columnspan=2)

        ttk.Label(self, text="Course Code:").grid(row=0, column=0)
        self._course_code = ttk.Entry(self)
        self._course_code.grid(row=0, column=1)

        ttk.Label(self, text="Name:").grid(row=1, column=0)
        self._course_name = ttk.Entry(self)
        self._course_name.grid(row=1, column=1)

        ttk.Label(self, text="Credits:").grid(row=2, column=0)
        self._credits = ttk.Entry(self)
        self._credits.grid(row=2, column=1)

        ttk.Label(self, text="Mark:").grid(row=3, column=0)
        self._mark = ttk.Entry(self)
        self._mark.grid(row=3, column=1)

        ttk.Button(self, text="Submit", command=self._submit_cb).grid(row=4, column=0)
        ttk.Button(self, text="Close", command=self._close_cb).grid(row=4, column=1)

    def _submit_cb(self):
        """ Submit callback """
        try:
            course = Course(self._course_code.get(), self._course_name.get(), float(self._credits.get()), int(self._mark.get()))
            self.calc.add_course(course)
            self._close_cb()
        except ValueError as e:
            tk.messagebox.showerror(title="Error", message=e)

