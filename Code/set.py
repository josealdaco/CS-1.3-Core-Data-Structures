
from linkedlist import *


class Set(object):

    def __init__(self, elements=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = LinkedList()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)

    def add(self, element):
        """ No duplicates on set"""
        if element not in self.list.items():
            self.list.append(element)
            self.size += 1
        else:
            return None

    def display_Items(self):
        return self.list.items()

    def contains(self, element):
        if element in self.list.items():
            return True
        else:
            return False

    def remove(self, item):
        try:
            self.list.delete(item)
            self.size -= 1
        except Exception:
            return None

    def union(self, other_set):
        """  New set from both"""
        for item in other_set.list.items():
            self.add(item)
        return Set(self.list.items())

    def intersection(self, other_set):
        data = []
        for item in other_set.list.items():
            if self.contains(item) is True:
                data.append(item)
        return Set(data)

    def diferrence(self, other_set):
        data = []
        for item in other_set.list.items():
            if self.contains(item) is False:
                data.append(item)
        return Set(data)

    def is_subset(self, other_set):
        for item in other_set.list.items():
            if self.contains(item) is not True:
                return False
        return True


def test_SetClass():
    obj1 = Set([1, 2, 3, 4, 5, 6, 7, 8])
    print("Object one", obj1.display_Items())
    obj1.add(1)
    print(obj1.display_Items())
    obj1.remove(2)
    print(obj1.display_Items())
    print(obj1.contains(1))
    obj2 = Set([10, 11, 12, 13, 14, 15, 16, 17])
    obj3 = obj1.union(obj2)
    print(obj3.display_Items())


if __name__ == '__main__':
    test_SetClass()
