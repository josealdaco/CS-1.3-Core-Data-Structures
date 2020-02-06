#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if find_index(text, pattern) is not None:
        return True
    else:
        return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    # text = text.translate({ord(i): None for i in "' '!@#$%^&*()?,.-_"}).lower()
    # pattern = pattern.translate({ord(i): None for i in "' '!@#$%^&*()?,.-_"}).lower()
    for index, char in enumerate(text.lower()):
        """ Make sure all letters are lowered """ #  textcatNone
        if pattern == '':
            print("This is for the abs space test")
            return index
        elif len(pattern) > len(text):
            return None
        elif char == pattern[0]:  # If the letter matches the first letter in text  catabccat
            if pattern[len(pattern) - 1] == text[(index + len(pattern)-1)]:
                """ If first letter matches and last"""
                text_index = 0
                breaker = False
                for index2 in range(index, (index + len(pattern)-1)):
                    if text[index2] != pattern[text_index]:
                        breaker = True
                        break
                    text_index += 1
                if breaker is False:
                    return index
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    """ Just make the function above recursive """
    result = []
    start = 0
    index = 0
    while True:
        state = find_index(text[start:], pattern)
        if state is not None:
            if state in result:
                if not pattern:
                    result.append(result[index] + 1)
                    index += 1
                else:
                    result.append(start)
            elif state != 0:
                result.append(state+start)
            else:
                result.append(start)
        else:
            break
        if not pattern or pattern == text[len(pattern)-1:]:
            start += state + 1
        else:
            start += state + len(pattern)
        if start >= len(text):
            break
    return result


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
