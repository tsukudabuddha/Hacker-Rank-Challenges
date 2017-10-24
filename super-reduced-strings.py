"""Super reduced string python."""


def should_continue(s):
    """Return true if there are no more duplicates."""
    for index in range(len(s)):
        if index == 0:
            previous_letter = s[index]
        else:
            if s[index] == previous_letter:
                return True
            previous_letter = s[index]
    return False


def super_reduced_string(s):
    """Reduce string duplicates."""
    previous_letter = ""
    while should_continue(s):
        for index in range(len(s)):
            temp = s
            if index == 0:
                previous_letter = s[index]
            else:
                if s[index] == previous_letter:
                    s = temp[:index-1] + temp[index + 1:]
                    break
                else:
                    previous_letter = s[index]
    if len(s) == 0:
        s = "Empty String"
    print(s)


super_reduced_string("aaaabbccddddeeff")
