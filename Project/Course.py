class Homework:
    """
    All information needed for a homework assignment.
    """

    def __init__(self, title, dueDate, percentComp, course):
        """
        Makes a new homework assignment.
        :param title:
        :param dueDate:
        :param percentComp:
        :param course:
        """
        self.__title = title
        self.__dueDate = dueDate
        self.__percentComp = percentComp
        self.__course = course

    def getDueDate(self):
        """
        Gets the due date.
        :return: dueDate.
        """
        return self.__dueDate

    def getTitle(self):
        """
        Gets the title.
        :return: title.
        """
        return self.__title

    def getPercentComp(self):
        """
        Gets the percentage completed.
        :return: percent complete
        """
        return self.__percentComp

    def setPercentComp(self, percentage):
        """
        Sets the percentage completed
        :param percentage: percent to set the assignment to.
        :return: None.
        """
        self.__percentComp = percentage

    def getCourse(self):
        """
        Gets the course that this assignment is under.
        :return: course title.
        """
        return self.__course


class Course:
    """
    All the information needed to keep track of a course.
    """

    def __init__(self, title, startTime, endTime, location, isMWF, isTTH):
        """
        Creates a new course.
        :param title: Title of the course.
        :param startTime: Start time of the course.
        :param endTime: End time of the course.
        :param location: Location of the course.
        :param isMWF: Bool, is MWF
        :param isTTH: Bool, is TTH
        """
        self.__title = title
        self.__startTime = startTime
        self.__endTime = endTime
        self.__location = location
        self.__isMWF = isMWF
        self.__isTTH = isTTH
        self.__homework = []

    def getTitle(self):
        """
        Gets the title.
        :return: Title
        """
        return self.__title

    def getStartTime(self):
        """
        Gets the start time
        :return: Start Time
        """
        return self.__startTime

    def getEndTime(self):
        """
        Gets the end time.
        :return: End Time
        """
        return self.__endTime

    def getLocation(self):
        """
        Gets the location.
        :return: Location.
        """
        return self.__location

    def getIsMWF(self):
        """
        Gets is MWF.
        :return: Bool, isMWF.
        """
        return self.__isMWF

    def getIsTTH(self):
        """
        Gets is TTH.
        :return: Bool, isTTH.
        """
        return self.__isTTH

    def getHW(self):
        """
        Gets the homework assignments that belong to this course.
        :return: A list of the assignments this course has.
        """
        return self.__homework

    def addHomework(self, title, dueDate, percentComp):
        """
        Adds a homework assignment to this course.
        :param title: Title of the assignment.
        :param dueDate: Due date of the assignment.
        :param percentComp: Percentage completed of the assignment.
        :return: None.
        """
        assignment = Homework(title, dueDate, percentComp, self.getTitle())
        self.__homework.append(assignment)