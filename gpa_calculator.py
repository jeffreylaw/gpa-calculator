from course import Course 


class GPACalculator:

    def __init__(self):
        """ Initializes the GPACalculator variables """
        self._courses = list()

    def add_course(self, course):
        """ Add course """
        self._validate_course(course)
        if not self.course_exists(course.code):
            self._courses.append(course)
        else:
            raise ValueError("Course already exists.")

    def delete_course(self, code):
        """ Delete course """
        if self.course_exists(code):
            self._courses.remove(self.get_course(code))
        else:
            raise ValueError("Course does not exist.")

    def get_course(self, code):
        """ Get course """
        for course in self._courses:
            if course.code == code:
                return course

    def get_courses(self):
        """ Return all courses """
        return self._courses

    def calculate_gpa(self):
        """ Calculate gpa """
        total_credits = 0
        total_grade_points = 0
        for course in self._courses:
            total_credits += course.credits
            total_grade_points += (course.credits * course.mark)
        if total_credits != 0:
            average = total_grade_points / total_credits
            return round(average)
        else:
            return 0

    def calculate_grade_points(self):
        """ Calculate total grade points """
        total_grade_points = 0
        for course in self._courses:
            total_grade_points += (course.credits * course.mark)
        return total_grade_points

    def calculate_credits(self):
        """ Calculate total credits """
        total_credits = 0
        for course in self._courses:
            total_credits += course.credits
        return total_credits

    def course_exists(self, code):
        """ Check if course exists """
        for course in self._courses:
            if course.code == code:
                return True
        return False

    def reset_courses(self):
        """ Reset courses """
        self._courses.clear()

    def _validate_course(self, course):
        """ Validate course """
        if not isinstance(course, Course):
            raise ValueError("add_course() takes in a Course object.")



    