import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.switch import switch_sort
import unittest

class TestSwichSort(unittest.TestCase):
    def test_case1(self):
        arr = [1, 2, 3, 4, 5]
        arr1 = [5,4,3,2,1]
        assert switch_sort(arr) == arr1

    def test_case2(self):
        arr = [1,2,3,4,5,1]
        arr2 = [5,4,3,2,1,1]
        assert switch_sort(arr) == arr2

    def test_case3(self):
        arr = [-1,2,3,4,5]
        arr3 = [5,4,3,2,-1]
        assert switch_sort(arr) == arr3

    def test_case4(self):
        arr = [1.2,3,4,5,6]
        arr4 = [6,5,4,3,1.2]
        assert switch_sort(arr) == arr4

if __name__ == '__main__':
    unittest.main()