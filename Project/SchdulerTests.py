import unittest
from PySchedule import *
import Course

class TestPyScheduleLogic(unittest.TestCase):
    def test_addAssignmnetLogic(self):
        """
        add asignment test
        :return: None
        """
        mySchedule = PyScheduleLogic()

        # Should fail since there is no course with the name 'fakeCourse'
        self.assertFalse(mySchedule.addAssignmnet('testing', 'fakeCourse', 'duedate', 0))

        mySchedule.addCourse('fakeCourse', 'fakeLocation', True, False, 'start', 'end')

        # Should be true after adding the course
        # Check that if we added 500 assignments to a course that the getHW() returns a
        # list of the correct amount of assignments and that they were added correctly.
        for i in range(1, 500):
            self.assertTrue(mySchedule.addAssignmnet('testing', 'fakeCourse', 'duedate', 0))
            self.assertEqual('testing', mySchedule.Courses[0].getHW()[i - 1].getTitle())
            self.assertEqual('fakeCourse', mySchedule.Courses[0].getHW()[i - 1].getCourse())
            self.assertEqual('duedate', mySchedule.Courses[0].getHW()[i - 1].getDueDate())
            self.assertEqual(0, mySchedule.Courses[0].getHW()[i - 1].getPercentComp())
            self.assertEqual(len(mySchedule.Courses[0].getHW()), i)

        self.assertFalse(mySchedule.addAssignmnet("", "Fake", "dueDate", 0))
        self.assertFalse(mySchedule.addAssignmnet("title", "Fake", "", 0))
        self.assertFalse(mySchedule.addAssignmnet("title", "Fake", None, 0))
        self.assertFalse(mySchedule.addAssignmnet("title", "Fake", "dueDate", -5))
        self.assertFalse(mySchedule.addAssignmnet("title", "Fake", "dueDate", 110))



    def test_addCourseLogic(self):
        mySchedule = PyScheduleLogic()

        # Cannot add without a title
        self.assertEqual(1, mySchedule.addCourse("", "location", True, False, "startitme", "endTime"))
        self.assertEqual(1, mySchedule.addCourse("title", "", True, False, "startitme", "endTime"))
        self.assertEqual(1, mySchedule.addCourse("title", "location", False, False, "startitme", "endTime"))


        for i in range(1, 500):
            self.assertEqual(0, mySchedule.addCourse('title({})'.format(i), 'location', False, True, 'startTime', 'endTime'))
            self.assertEqual('title({})'.format(i), mySchedule.Courses[i-1].getTitle())
            self.assertEqual('location', mySchedule.Courses[i-1].getLocation())
            self.assertEqual(False, mySchedule.Courses[i-1].getIsMWF())
            self.assertEqual(True, mySchedule.Courses[i-1].getIsTTH())
            self.assertEqual('startTime', mySchedule.Courses[i-1].getStartTime())
            self.assertEqual('endTime', mySchedule.Courses[i-1].getEndTime())

            self.assertEqual(len(mySchedule.Courses), i)

        # 2 Means the course already exists
        self.assertEqual(2, mySchedule.addCourse('title({})'.format(1), 'location', True, False, 'start', 'end'))


    def test_appendCourse(self):
        mySchedule = PyScheduleLogic()

        for i in range(1, 500):
            myCourse = Course.Course('title({})'.format(i), 'start', 'end', 'location', False, True)
            mySchedule.appendCourse(myCourse)
            self.assertEqual('title({})'.format(i), mySchedule.Courses[i - 1].getTitle())
            self.assertEqual('location', mySchedule.Courses[i - 1].getLocation())
            self.assertEqual(False, mySchedule.Courses[i - 1].getIsMWF())
            self.assertEqual(True, mySchedule.Courses[i - 1].getIsTTH())
            self.assertEqual('start', mySchedule.Courses[i - 1].getStartTime())
            self.assertEqual('end', mySchedule.Courses[i - 1].getEndTime())

            self.assertEqual(len(mySchedule.Courses), i)

    def test_removeCourse(self):
        mySchedule = PyScheduleLogic()

        myCourse = Course.Course('course1', 'location1', True, False, 'start', 'end')
        mySchedule.appendCourse(myCourse)

        self.assertEqual(len(mySchedule.Courses), 1)

        mySchedule.removeCourse(myCourse)

        self.assertEqual(len(mySchedule.Courses), 0)

        mySchedule.appendCourse(myCourse)

        # add 500 differnet courses
        for i in range(1, 500):
            self.assertEqual(0, mySchedule.addCourse('title({})'.format(i), 'location', False, True, 'startTime', 'endTime'))

        mySchedule.removeCourse(myCourse)

        # Ensure course is gone
        for c in mySchedule.Courses:
            self.assertNotEqual(c.getTitle(), myCourse.getTitle())

        # delete all
        for c in mySchedule.Courses:
            mySchedule.removeCourse(c)

            # Ensure course is gone
            for c2 in mySchedule.Courses:
                self.assertNotEqual(c.getTitle(), c2.getTitle())

    def test_deleteCourse(self):
        mySchedule = PyScheduleLogic()

        # add 500 differnet courses
        for i in range(1, 500):
            self.assertEqual(0, mySchedule.addCourse('title({})'.format(i), 'location', False, True, 'startTime', 'endTime'))

        for c in mySchedule.Courses:
            mySchedule.deleteCourse(c.getTitle())

            # Ensure course is gone
            for c2 in mySchedule.Courses:
                self.assertNotEqual(c2.getTitle(), c.getTitle())


#     def test_twoCards(self):
#         """
#         two card shuffle test
#         """
#         self.assertEqual(faroShuffle([0, 1]), [0, 1])
#
#     def test_fourCards(self):
#         self.assertEqual(faroShuffle([0, 1, 2, 3]), [0, 2, 1, 3])
#
#     def test_tenCards(self):
#         self.assertEqual(faroShuffle(range(10)),
#                          [0, 5, 1, 6, 2, 7, 3, 8, 4, 9])
#
#     def test_shuffleAnything(self):
#         self.assertEqual(faroShuffle(['queen', 'jack', 'ace', 7]),
#                          ['queen', 'ace', 'jack', 7])
#
#     def test_threeCards(self):
#         self.assertRaises(ValueError, faroShuffle, [0, 1, 2])
#
#     def test_nonsequence(self):
#         self.assertRaises(TypeError, faroShuffle, 1)
#
#     def test_emptyList(self):
#         self.assertEqual(faroShuffle([]), [])
#
#     def test_noArgument(self):
#         self.assertRaises(TypeError, faroShuffle)
#
#
# class TestCountShuffles(unittest.TestCase):
#     def test_twoCards(self):
#         self.assertEqual(countShuffles(2), 1)
#
#     def test_fiftyTwoCards(self):
#         self.assertEqual(countShuffles(52), 8)
#
#     def test_oneThousandCards(self):
#         self.assertEqual(countShuffles(1024), 10)
#
#
# if __name__ == '__main__':
#     unittest.main()