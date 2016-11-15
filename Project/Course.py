class Homework:
    """
    All information needed for a homework assignment.
    """

    def __init__(self, title, dueDate, percentComp):
        self.__title = title
        self.__dueDate = dueDate
        self.__percentComp = percentComp

    def getDueDate(self):
        return self.__dueDate

    def getTitle(self):
        return self.__title

    def getPercentComp(self):
        return self.__percentComp

class Course:
    """
    All the information needed to keep track of a course.
    """

    def __init__(self, title, startTime, endTime, location, isMWF, isTTH):
        self.__title = title
        self.__startTime = startTime
        self.__endTime = endTime
        self.__location = location
        self.__isMWF = isMWF
        self.__isTTH = isTTH
        self.__homework = []

    def getTitle(self):
        return self.__title

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def getLocation(self):
        return self.__location

    def getIsMWF(self):
        return self.__isMWF

    def getIsTTH(self):
        return self.__isTTH

    def getHW(self):
        return self.__homework

    def addHomework(self, title, dueDate, percentComp):
        assignemnt = Homework(title, dueDate, percentComp)
        self.__homework.append(assignemnt)

