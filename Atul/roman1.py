
class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


def to_roman(n):
    '''Input integer value
       Return equavalent Roman Numeral'''

    if n > 3999 or n < 1:
        raise OutOfRangeError('Number is out of range.')

    if not isinstance(n, int):
        raise NotIntegerError('Not an integer.')

    result = ''

    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer

    return result
