import Course
from PyQt4 import QtCore, QtGui, uic
import copy
import sys
from PyQt4.QtGui import QApplication, QDialog


class Scheduler(QtGui.QMainWindow):
    """
    Main class of the application.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.Courses = []
        uic.loadUi('school_Scheduler.ui', self)
        self.AddCourseButton.clicked.connect(self.addCourse)
        self.AddAssignmentButton.clicked.connect(self.addAssignment)
        self.NotificationList.doubleClicked.connect(self.expandNotification)

    def expandNotification(self):
        print("expanding")

        assignmnet = self.NotificationList.currentItem().text()
        assignmentDetails = assignmnet.split('\n')

        msg = QtGui.QMessageBox()

        msg.setText("Assignment Title: {}\nCourse Title: {}\nAssignment DueDate: {}\nPersent Complete: {}".format(assignmentDetails[0], assignmentDetails[1], assignmentDetails[2], assignmentDetails[3]))
        msg.setWindowTitle("Assignment Details")

        spinBox = QtGui.QSpinBox(msg)

        percentComp = assignmentDetails[3].split('%')[0]
        spinBox.setValue(int(percentComp))
        spinBox.setMaximum(100)
        spinBox.setMinimum(0)
        spinBox.setFixedHeight(25)
        spinBox.move(70, 80)




        msg.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
        result = msg.exec_()

        print("after button click, result = ", result)

    def addAssignment(self):
        """
        This functions will add an assignemnt to the correct course. Finding the course
        from the combo box and adding the assignment with the imputs as the title
        and due date.
        """

        if self.AssignmentTitle.text() is "" or self.CoursesComboBox.count() == 0:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)

            msg.setText("To add an assignment you need a title and a course!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
            return

        courseToAddTo = self.CoursesComboBox.currentText()

        for i in self.Courses:
            if i.getTitle() == courseToAddTo:
                i.addHomework(self.AssignmentTitle.text(), self.CourseDateTimeEdit.dateTime(), self.AssignmentPercentComplete.value())

        self.updateNotificationView()

    def updateNotificationView(self):
        self.NotificationList.clear()

        for i in self.Courses:
            hw = list(i.getHW())
            orderedHW = self.__orderOnDateTime(hw)
            for a in orderedHW:
                self.NotificationList.addItem("{}\n   {}\n   {}\n   {}% comp\n".format(a.getTitle(), i.getTitle(), a.getDueDate().toString("ddd MMMM d h:m a"), a.getPercentComp()))


    def addCourse(self):
        """
        Adds a course then updates the view.
        If not all information is filled out an error message will appear and the course
        will not be added.
        """

        if (self.CourseTitle.text() is ""
            or self.CourseLocation.text() is ""
            or (not self.CheckBoxMWF.checkState() and not self.CheckBoxTTH.checkState())):
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Critical)

            msg.setText("Unable to add course without all fields filled in!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
            return

        for course in self.Courses:
            if course.getTitle() == self.CourseTitle.text():
                course.__title = self.CourseTitle.text()
                course.__startTime = self.CourseTimeStart.time()
                course.__endTime = self.CourseTimeEnd.time()
                course.__location = self.CourseLocation.text()
                course.__isMWF = self.CheckBoxMWF.checkState()
                course.__isTTH = self.CheckBoxTTH.checkState()
                self.Courses.remove(course)

        c = Course.Course(self.CourseTitle.text(), self.CourseTimeStart.time(), self.CourseTimeEnd.time(),
                          self.CourseLocation.text(), self.CheckBoxMWF.checkState(), self.CheckBoxTTH.checkState())
        self.Courses.append(c)
        self.updateScheduleView()

    def updateScheduleView(self):
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

        if not AllItems.__contains__(self.CourseTitle.text()):
            self.CoursesComboBox.addItem(self.CourseTitle.text())

    def __orderOnTime(self, list):
        orderList = []

        for i in range(len(list)):
            currentEarlyTime = self.__findEarliestTime(list)
            orderList.append(currentEarlyTime)
            list.remove(currentEarlyTime)
            i -= i

        return orderList

    def __findEarliestTime(self, list):
        earliest = list[0]

        for i in list:
            if i.getStartTime() < earliest.getStartTime():
                earliest = i

        return earliest

    def __orderOnDateTime(self, list):
        orderList = []

        for i in range(len(list)):
            currentEarlyDateTime = self.__findEarliestDateTime(list)
            orderList.append(currentEarlyDateTime)
            list.remove(currentEarlyDateTime)
            i -= i

        return orderList

    def __findEarliestDateTime(self, list):
        earliest = list[0]

        for i in list:
            if i.getDueDate() < earliest.getDueDate():
                earliest = i

        return earliest


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainapplication = Scheduler()
    mainapplication.show()
    app.exec_()
