#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    elif index == len(array) - 1:
        return None
    else:
        index += 1
        return linear_search_recursive(array, item, index)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    """ Assuming array is already Sorted"""
    start = 0
    end = len(array) - 1
    target = (len(array) - 1)//2
    while True:
        if target == len(array) or target < 0:
            return None
        temp_list = [array[target], item]
        temp_list.sort()
        if array[start] == item:
            return start
        elif array[end] == item:
            return end
        if array[target] == item:
            return target
        elif temp_list[0] == array[target]:
            # Going Right
            start = target
            target = (target + end)//2
            end -= 1
        elif temp_list[0] == item:
            # Going Left
            end = target
            target = abs((target - start)//2)
            start += 1
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, start=0, endmark=0, target=0, trig=True):
    # TODO: implement binary search recursively here
    if trig is True:
        trig = False
        endmark = len(array) - 1
        target = (len(array) - 1)//2
    if target == len(array) or target < 0:
        return None
    temp_list = [array[target], item]
    temp_list.sort()
    if array[start] == item:
        return start
    elif array[endmark] == item:
        return endmark
    if array[target] == item:
        return target
    elif temp_list[0] == array[target]:
        # Going Right
        start = target
        target = (target + endmark)//2
        endmark -= 1
        return binary_search_recursive(array, item, start, endmark, target, trig)
    elif temp_list[0] == item:
        # Going Left
        endmark = target
        target = abs((target - start) //2)
        start += 1
        return binary_search_recursive(array, item, start, endmark, target, trig)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
