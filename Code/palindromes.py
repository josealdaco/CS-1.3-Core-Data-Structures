#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):   # tacocat
    # TODO: implement the is_palindrome function iteratively here

    # Space Complexity is O(n)
    local_Word = text.translate({ord(i): None for i in "' '!@#$%^&*()?,.-_"})
    start = 0
    end = len(local_Word) - 1
    if not local_Word:
        """  In case the string is empty"""
        return True
    while True:
        if local_Word[start].lower() == local_Word[end].lower() and start != len(local_Word)-1 and end != 0:
            start += 1
            end -= 1
        elif local_Word[start].lower() == local_Word[end].lower() and start == len(local_Word)-1 and end == 0:
            return True
        else:
            return False
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, start=0, end=None):
    # TODO: implement the is_palindrome function recursively here
    # Space Complexity is O(n)
    if not text:
        """  In case the string is empty"""
        return True
    if end is None:
        text = text.translate({ord(i): None for i in "' '!@#$%^&*()?,.-_"})
        end = len(text) - 1
    if text[start].lower() == text[end].lower():
        if start < len(text)-1 and end > 0:
            start += 1
            end -= 1
            return is_palindrome_recursive(text, start, end)
        elif start == len(text)-1 and end == 0:
            return True
    else:
        return False
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
