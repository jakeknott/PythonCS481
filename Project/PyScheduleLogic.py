from Course import *

class PyScheduleLogic:

    def __init__(self):
        self.Courses = []

    def getCourses(self):
        return self.Courses

    def removeCourse(self, course):
        self.Courses.remove(course)

    def appendCourse(self, course):
        self.Courses.append(course)

    def deleteCourse(self, courseTitle):
        for c in self.Courses:
            if c.getTitle() == courseTitle:
                self.Courses.remove(c)
                return True

        return False

    def addAssignmnet(self, title, courseToAddTo, dueDateTime, percentComplete):
        """
        The add assignment logic, without touching the actual gui.
        :param title: Title of assignment to add.
        :param courseToAddTo: The title of the course we want to add this assignment to.
        :param dueDateTime: The due date of this assignment.
        :param percentComplete: Percentage of the assignment that is already completed.
        :return: Bool based on ability to add the assignment to the course
        """

        if title == "" or dueDateTime == None or percentComplete < 0 or percentComplete > 100:
            return False

        for i in self.Courses:
            if i.getTitle() == courseToAddTo:
                i.addHomework(title, dueDateTime, percentComplete)
                return True

        return False

    def addCourse(self, title, location, isMWF, isTTH, startTime, endTime):
        """
        This is the add course logic, this will add a course to the given assignment
        without touching the gui.

        :param title: Title of the Coure to add
        :param location: Location of the course to add
        :param isMWF: Bool, is course on MWF
        :param isTTH: Bool, is course on TTH
        :param startTime: QTime of start of course
        :param endTime: QTime of end of course
        :return: 0 represents the course is added,
                 1 represents not all fields are filled in,
                 2 represents course already exists.
        """

        if title is "" or location is "" or (not isMWF and not isTTH):
            return 1

        for course in self.Courses:
            if course.getTitle() == title:
                return 2

        c = Course(title, startTime, endTime, location, isMWF, isTTH)
        self.Courses.append(c)
        return 0

    def orderOnTime(self, myList):
        """
        Will take myList and order it based on it's time property.

        :param myList: The list to order.
        :return: MyList in order of time
        """

        orderList = []

        for i in range(len(myList)):
            currentEarlyTime = self.__findEarliestTime(myList)
            orderList.append(currentEarlyTime)
            myList.remove(currentEarlyTime)
            i -= i

        return orderList

    @staticmethod
    def __findEarliestTime(myList):
        """
        Searches through myList and finds the earliest item based on
        the start time property of the item.

        :param myList: List to find the earliest item.
        :return: myList item that is the earliest based on time.
        """

        earliest = myList[0]

        for i in myList:
            if i.getStartTime() < earliest.getStartTime():
                earliest = i

        return earliest

    def orderOnDateTime(self, myList):
        """
        Will take myList and order it based on it's date time property.

        :param myList: The list to order.
        :return: MyList in order of date time
        """

        orderList = []

        for i in range(len(myList)):
            currentEarlyDateTime = self.__findEarliestDateTime(myList)
            orderList.append(currentEarlyDateTime)
            myList.remove(currentEarlyDateTime)
            i -= i

        return orderList

    @staticmethod
    def __findEarliestDateTime(myList):
        """
        Searches through myList and finds the earliest item based on
        the due date property of the item.

        :param myList: List to find the earliest item.
        :return: myList item that is the earliest based on due date.
        """

        earliest = myList[0]

        for i in myList:
            if i.getDueDate() < earliest.getDueDate():
                earliest = i

        return earliest