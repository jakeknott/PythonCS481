# import unittest
# from schedulerUI import *
#
#
# class TestFaroShuffle(unittest.TestCase):
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