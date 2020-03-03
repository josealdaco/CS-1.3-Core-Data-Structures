import unittest
from set import Set
import random


class SearchTest(unittest.TestCase):

    def test_add(self):
        set1 = Set()
        set1.add(1)
        for _ in range(20):
            set1.add(random.randint(0,100))
        assert set1.contains(1) is True
        assert set1.size >= 1
        assert set1.add(1) is None
        if set1.add(10) is None:
            set1.remove(10)
            set1.add(10)
        assert set1.contains(10) is True

    def test_contains(self):
        set1 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert set1.contains(1) is True
        assert set1.contains(2) is True
        assert set1.contains(3) is True
        assert set1.contains(100) is False

    def test_remove(self):
        set1 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        set1.remove(1)
        assert set1.contains(1) is False
        set1.remove(2)
        assert set1.contains(2) is False
        set1.remove(3)
        assert set1.contains(3) is False
        set1.remove(100) is None

    def test_union(self):
        set1 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        set2 = Set([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])
        set3 = set1.union(set2)
        assert set3.size == 20
        assert set3.contains(1) is True
        assert set3.contains(11) is True
        assert set3.contains(100) is False

    def test_intersection(self):
        set1 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        set2 = Set([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])
        set3 = set1.intersection(set2)
        assert set3.size == 1
        assert set3.contains(1) is True
        assert set3.contains(15) is False
        assert set3.contains(100) is False

    def test_difference(self):
        set1 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        set2 = Set([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])
        set3 = set1.diferrence(set2)
        assert set3.size == 10
        assert set3.contains(11) is True
        assert set3.contains(15) is True
        assert set3.contains(100) is False

    def test_is_subset(self):
        set1 = Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        set2 = Set([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])
        assert set1.is_subset(set2) is False
        set3 = Set([8, 9])
        assert set1.is_subset(set3) is True
        set4 = Set([9])
        assert set3.is_subset(set4) is True
        assert set3.is_subset(set1) is False
