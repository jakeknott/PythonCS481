import Course
from PyQt4 import QtCore, QtGui, uic
import os
import sys
import json


class PySchedule(QtGui.QMainWindow):
    """
    Main class of the application.
    """

    def __init__(self, parent=None):
        """
        Initializes a PySchedule window and binds all the button events to the correct method.
        """

        super().__init__(parent)
        self.Courses = []
        uic.loadUi('PySchedule.ui', self)
        self.AddCourseButton.clicked.connect(self.addCourse)
        self.AddAssignmentButton.clicked.connect(self.addAssignment)
        self.NotificationList.doubleClicked.connect(self.expandNotification)

        self.MondayCourses.doubleClicked.connect(self.promptDeleteCourseMonday)
        self.TuesdayCourses.doubleClicked.connect(self.promptDeleteCourseTuesday)
        self.WednesdayCourses.doubleClicked.connect(self.promptDeleteCourseWednesday)
        self.ThursdayCourses.doubleClicked.connect(self.promptDeleteCourseThursday)
        self.FridayCourses.doubleClicked.connect(self.promptDeleteCourseFriday)

        self.CourseTimeStart.setTime(QtCore.QTime.currentTime())
        self.CourseTimeEnd.setTime(QtCore.QTime.currentTime().addSecs(60 * 60))
        self.CourseDateTimeEdit.setDate(QtCore.QDate.currentDate())
        self.CourseDateTimeEdit.setTime(QtCore.QTime.currentTime())

    def promptDeleteCourseMonday(self):
        """
        Prompts the user via promptDeleteCourse to delete the currently selected item in the Monday Lists.
        """

        selectedItem = self.MondayCourses.currentItem().text()
        self.promptDeleteCourse(selectedItem)

    def promptDeleteCourseTuesday(self):
        """
        Prompts the user via promptDeleteCourse to delete the currently selected item in the Tuesday Lists.
        """

        selectedItem = self.TuesdayCourses.currentItem().text()
        self.promptDeleteCourse(selectedItem)

    def promptDeleteCourseWednesday(self):
        """
        Prompts the user via promptDeleteCourse to delete the currently selected item in the Wednesday Lists.
        """

        selectedItem = self.WednesdayCourses.currentItem().text()
        self.promptDeleteCourse(selectedItem)

    def promptDeleteCourseThursday(self):
        """
        Prompts the user via promptDeleteCourse to delete the currently selected item in the Thursday Lists.
        """

        selectedItem = self.ThursdayCourses.currentItem().text()
        self.promptDeleteCourse(selectedItem)

    def promptDeleteCourseFriday(self):
        """
        Prompts the user via promptDeleteCourse to delete the currently selected item in the Friday Lists.
        """

        selectedItem = self.FridayCourses.currentItem().text()
        self.promptDeleteCourse(selectedItem)

    def promptDeleteCourse(self, selectedItem):
        """
        Prompts the user via a pop up window to remove the selected item. (course)
        :param selectedItem: The item that we want to remove (given the user chooses 'yes' in the popup)
        :return: None
        """
        courseTitle = selectedItem.split("\n")[0]

        msg = QtGui.QMessageBox()
        msg.setWindowTitle("Remove Course")
        msg.setText("Are you sure you want to delete this course and all it's assignments?")
        msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        result = msg.exec_()

        if result == QtGui.QMessageBox.Yes:
            # Find the asignment to edit
            for c in self.Courses:
                if c.getTitle() == courseTitle:
                    self.Courses.remove(c)
                    break
            self.updateScheduleView()
            self.updateNotificationView()

    def expandNotification(self):
        """
        Expands the selected notification and displays a window with the title, the course, duedate and percent complete.
        You can also edit the percent complete in this window and set a new percent complete for the seleted
        assignment.
        :return: None
        """

        assignmnet = self.NotificationList.currentItem().text()
        assignmentDetails = assignmnet.split('\n')

        msg = QtGui.QMessageBox()

        msg.setText("Assignment Title: {}\nCourse Title: {}\nAssignment DueDate: {}\n\nPersent Complete:\t      % comp".
                    format(assignmentDetails[0], assignmentDetails[1], assignmentDetails[2]))
        msg.setWindowTitle("Assignment Details")

        spinBox = QtGui.QSpinBox(msg)

        percentComp = assignmentDetails[3].split('%')[0]
        spinBox.setValue(int(percentComp))
        spinBox.setMaximum(100)
        spinBox.setMinimum(0)
        spinBox.setFixedHeight(25)
        spinBox.setFixedWidth(55)
        spinBox.move(160, 65)

        msg.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
        result = msg.exec_()

        while assignmentDetails[0][0] == ' ':
            assignmentDetails[0] = assignmentDetails[0][1:]

        while assignmentDetails[1][0] == ' ':
            assignmentDetails[1] = assignmentDetails[1][1:]

        if result == QtGui.QMessageBox.Save:
            # Find the asignment to edit
            for c in self.Courses:
                if c.getTitle() == assignmentDetails[1]:
                    # now we have the course, find the assignment and update the percent complete
                    for a in c.getHW():
                        if a.getTitle() == assignmentDetails[0]:
                            if spinBox.value() == 100:
                                msg = QtGui.QMessageBox()
                                msg.setIcon(QtGui.QMessageBox.Warning)
                                msg.setWindowTitle("Remove Assignment")
                                msg.setText("By setting percent to 100%, this will permanently remove this assignment "
                                            "from your notifications. Continue?")
                                msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                                result = msg.exec_()

                                if result == QtGui.QMessageBox.Yes:
                                    a.setPercentComp(100)
                                    c.getHW().remove(a)
                            else:
                                a.setPercentComp(spinBox.value())

                            self.updateNotificationView()
                            break

    def addAssignmnetLogic(self, title, courseToAddTo, dueDateTime, percentComplete):
        """
        The add assignment logic, without touching the actual gui.
        :param title: Title of assignment to add.
        :param courseToAddTo: The title of the course we want to add this assignment to.
        :param dueDateTime: The due date of this assignment.
        :param percentComplete: Percentage of the assignment that is already completed.
        :return: None
        """

        for i in self.Courses:
            if i.getTitle() == courseToAddTo:
                i.addHomework(title, dueDateTime, percentComplete)

    def addAssignment(self):
        """
        This functions will add an assignment to a course. Using the combo box, it finds the course
        and adds the assignment to that course. This will use the gui's inputs to set the assignment's
        title, and due date.
        :return: None
        """

        if self.AssignmentTitle.text() is "" or self.CoursesComboBox.count() == 0:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)

            msg.setText("To add an assignment you need a title and a course!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
            return

        self.addAssignmnetLogic(self.AssignmentTitle.text(), self.CoursesComboBox.currentText(),
                                self.CourseDateTimeEdit.dateTime(), self.AssignmentPercentComplete.value())
        self.updateNotificationView()

    def updateNotificationView(self):
        """
        Updates the notifications list. This will get all the assignments,
        order them based on due date, and print the information to the
        notifications list view.
        :return: None
        """

        self.NotificationList.clear()

        allHW = []

        for i in self.Courses:
            allHW += i.getHW()

        orderedHW = self.__orderOnDateTime(allHW)
        for a in orderedHW:
            self.NotificationList.addItem("{}\n   {}\n   {}\n   {}% comp\n"
                                          .format(a.getTitle(), a.getCourse(),
                                                  a.getDueDate().toString("ddd MMMM d h:m a"), a.getPercentComp()))

    def addCourseLogic(self, title, location, isMWF, isTTH, startTime, endTime):
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

        c = Course.Course(title, startTime, endTime, location, isMWF, isTTH)
        self.Courses.append(c)
        return 0

    def addCourse(self):
        """
        Adds a course then updates the view.
        If not all information is filled out an error message will appear and the course
        will not be added.
        :return: None
        """

        didAdd = self.addCourseLogic(self.CourseTitle.text(), self.CourseLocation.text(),
                                     self.CheckBoxMWF.checkState(), self.CheckBoxTTH.checkState(),
                                     self.CourseTimeStart.time(),
                                     self.CourseTimeEnd.time())

        if didAdd == 1:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)

            msg.setText("Unable to add course without all fields filled in!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
            return

        if didAdd == 2:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)

            msg.setText("Unable to add course, course already exists! "
                        "Please double click course and delete before adding again.")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
            return

        self.updateScheduleView()

    def updateScheduleView(self):
        """
        Updates the gui of the schedule. This will get all the
        courses and order them based on start time and print
        them in the view that they belong, i.e. if a course
        occurs on Mondays then that course will be added to the Monday view.

        This method will also update the combo box in the 'Add Assignment' tab
        to only represent current course options.
        :return: None
        """

        # Clear the lists
        self.MondayCourses.clear()
        self.TuesdayCourses.clear()
        self.WednesdayCourses.clear()
        self.ThursdayCourses.clear()
        self.FridayCourses.clear()

        MWFCourses = []
        TTHCourses = []

        for i in self.Courses:
            if i.getIsMWF():
                MWFCourses.append(i)
            if i.getIsTTH():
                TTHCourses.append(i)

        MWFCourses = self.__orderOnTime(MWFCourses)
        TTHCourses = self.__orderOnTime(TTHCourses)

        for i in MWFCourses:
            starTimeString = i.getStartTime().toString("h:mm a")
            endTimeString = i.getEndTime().toString("h:mm a")

            self.MondayCourses.addItem(
                "{}\n   {}\n   {}\n   {}\n".format(i.getTitle(), i.getLocation(), starTimeString, endTimeString))
            self.WednesdayCourses.addItem(
                "{}\n   {}\n   {}\n   {}\n".format(i.getTitle(), i.getLocation(), starTimeString, endTimeString))
            self.FridayCourses.addItem(
                "{}\n   {}\n   {}\n   {}\n".format(i.getTitle(), i.getLocation(), starTimeString, endTimeString))

        for i in TTHCourses:
            starTimeString = i.getStartTime().toString("h:mm a")
            endTimeString = i.getEndTime().toString("h:mm a")

            self.TuesdayCourses.addItem(
                "{}\n   {}\n   {}\n   {}\n".format(i.getTitle(), i.getLocation(), starTimeString, endTimeString))
            self.ThursdayCourses.addItem(
                "{}\n   {}\n   {}\n   {}\n".format(i.getTitle(), i.getLocation(), starTimeString, endTimeString))

        AllItems = [self.CoursesComboBox.itemText(i) for i in range(self.CoursesComboBox.count())]

        for c in self.Courses:
            if not AllItems.__contains__(c.getTitle()):
                self.CoursesComboBox.addItem(c.getTitle())

        for i in range(len(AllItems)):
            isInCourse = False
            for c in self.Courses:
                if c.getTitle() == AllItems[i]:
                    isInCourse = True
            if not isInCourse:
                self.CoursesComboBox.removeItem(i)
                i -= i

    def __orderOnTime(self, myList):
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

    def __orderOnDateTime(self, myList):
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

def LoadData():
    """
    This will open the '~/PySchedule/data.json' file (if it exists)
    and read in all the items and add them to the instance of Scheduler
    then update the views.

    :return: None
    """

    savedFile = "{}/{}".format(os.environ['HOME'], "PySchedule/data.json")
    if not os.path.exists(savedFile):
        return

    with open('{}'.format(savedFile)) as data_file:
        data = json.load(data_file)
        # If we are here then we know that we have somthing in the file
        # and expect it to be a course first
        for c in data['courses']:
            time = c['startTime'].split(":")
            startTime = QtCore.QTime(int(time[0]), int(time[1]))

            time = c['endTime'].split(":")
            endTime = QtCore.QTime(int(time[0]), int(time[1]))

            mainapplication.addCourseLogic(c['title'], c['location'], c['isMWF'], c['isTTH'], startTime, endTime)

            # int y, int m, int d, int h, int m,

            if 'homeWork' in c:
                for hw in c['homeWork']:
                    dueDate = hw['dueDate'].split(" ")
                    dueTime = dueDate[3].split(":")

                    dueDateTime = QtCore.QDateTime(int(dueDate[2]), int(dueDate[0]), int(dueDate[1]), int(dueTime[0]),
                                                   int(dueTime[1]))

                    mainapplication.addAssignmnetLogic(hw['title'], c['title'], dueDateTime, hw['percentCmp'])

    mainapplication.updateScheduleView()
    mainapplication.updateNotificationView()


def SaveData():
    """
    Opens/creates '~/PySchedule/data.json' and writes to it
    all the data that is currently in the instance of Scheduler.

    :return: None
    """

    saveDir = "{}/{}".format(os.environ['HOME'], "PySchedule")
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    if __name__ == '__main__':
        with open('{}/{}'.format(saveDir, 'data.json'), 'w') as outfile:
            if len(mainapplication.Courses) > 0:
                outfile.write('{"courses":[')

            numCourses = 0
            for c in mainapplication.Courses:
                if numCourses > 0:
                    outfile.write(',')
                outfile.write('{')
                outfile.write('"{}": "{}",'.format('title', c.getTitle()))
                outfile.write('"{}": "{}",'.format('startTime', c.getStartTime().toString("H:mm")))
                outfile.write('"{}": "{}",'.format('endTime', c.getEndTime().toString("H:mm")))
                outfile.write('"{}": "{}",'.format('location', c.getLocation()))
                outfile.write('"{}": {},'.format('isMWF', c.getIsMWF()))
                outfile.write('"{}": {}'.format('isTTH', c.getIsTTH()))

                if len(c.getHW()) > 0:
                    outfile.write(',"homeWork":[')
                numHW = 0
                for hw in c.getHW():
                    if numHW > 0:
                        outfile.write(',')
                    outfile.write('{')
                    outfile.write('"{}": "{}",'.format('title', hw.getTitle()))
                    outfile.write('"{}": "{}",'.format('dueDate', hw.getDueDate().toString("M d yyyy H:mm")))
                    outfile.write('"{}": "{}"'.format('percentCmp', hw.getPercentComp()))
                    outfile.write('}')
                    numHW += 1

                if len(c.getHW()) > 0:
                    outfile.write(']')

                outfile.write('}')
                numCourses += 1

            if len(mainapplication.Courses) > 0:
                outfile.write(']}')
            else:
                # if there are no courses then there is nothing to save
                # we do not want an empty file, so just delete the one that is thre
                os.remove(saveDir + "/data.json")


app = QtGui.QApplication(sys.argv)
mainapplication = PySchedule()
LoadData()
mainapplication.show()
app.exec_()
SaveData()
