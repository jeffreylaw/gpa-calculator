class Course:
    """ Course class """

    def __init__(self, code: str, name: str, _credits: float, mark: float):
        """ Initializes the course variables """
        self._validate_parameters(code, name, _credits, mark)
        self._code = code
        self._credits = _credits
        self._mark = mark
        self._name = name

    @property
    def code(self):
        """ Get course code """
        return self._code
    
    @property
    def name(self):
        """ Get course name """
        return self._name

    @property
    def credits(self):
        """ Get course credits """
        return self._credits

    @property
    def mark(self):
        """ Get course mark """
        return self._mark        

    def edit_course(self, code: str, name: str, _credits: float, mark: int):
        """ Set course variables """
        self._code = code
        self._name = name
        self._credits = _credits
        self._mark = mark

    def to_dict(self):
        """ Return dictionary representation """
        data = {
            "code": self._code,
            "name": self._name,
            "credits": self._credits,
            "mark": self._mark
        }
        return data

    def __str__(self):
        """ Return string representation """
        return f"<Course> Code: {self._code}, Name: {self._name}, Credits: {self._credits}, Mark: {self._mark}"

    def _validate_parameters(self, code, name, _credits, mark):
        """ Validate course parameters """
        if not isinstance(code, str) or code == "":
            raise ValueError("The course code must be a string and cannot be empty.")
        if not isinstance(name, str):
            raise ValueError("The course name must be a string.")
        if not isinstance(float(_credits), float) or _credits < 0:
            raise ValueError("Credits must be a float and greater than 0.")
        if not isinstance(mark, int) or mark < 0 or mark > 100:
            raise ValueError("A mark must be an integer and between 0 and 100.")