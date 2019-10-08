# function with annotation
def seeknum(phrase: str) -> set:
    """ Return all numbers as set, from keyboard  input word"""
    numbers = set('1234567890')
    return numbers.intersection(set(phrase))

def seekletter(phrase: str, letters: str) -> set:
    """ Return from 'letters', found in 'phrase' """
    return set(letters).intersection(set(phrase))
