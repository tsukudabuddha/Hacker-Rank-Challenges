"""CamelCase Hackerrank."""


def num_of_words(s):
    """Take in camel case word and return word count."""
    wc = 1
    for letter in s:
        if letter.isupper():
            wc += 1
    return wc
