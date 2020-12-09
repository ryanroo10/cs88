######################
# Required Questions #
######################

def map(f, s):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    if s == []:
        return s
    return [f(s[0])] + map(f, s[1:])


def filter(f, s):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    if s == []:
        return s
    return ([s[0]] if f(s[0]) else []) + filter(f, s[1:])



from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    if s == []:
        return base
    return reduce(reducer, s[1:], reducer(base, s[0]))




def lambda_curry2(func):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    return lambda x: lambda y: func(x, y)



def polynomial(degree, coeffs):
    """
    >>> fourth = polynomial(4, [3,6,2,1, 100])
    >>> fourth(3)   # 3*(3**4) + 6*(3**3) + 2*(3**2) + 1*(3**1) + 100
    526
    >>> third = polynomial(3, [2, 0, 0, 0])
    >>> third(4)   # 2*(4**3) + 0*(4**2) + 0*(4**1) + 0
    128
    """
    return lambda x: sum([coeffs[i] * x ** (degree - i) for i in range(len(coeffs))])



######################
# Optional Questions #
######################

def comparelambda(op):
	"""
	Write a function that returns a subtraction lambda function or addition lambda function depending on the operator passed into compare lambda.
	Both lambda functions take in two arguments.

	>>>adding = comparelambda("+")
	>>>adding(3,2)
	5
	>>>subtracting = comparelambda("-")
	>>>subtracting(6,2)
	4
	>>>operator_not_supported = comparelambda("*")
	>>>operator_not_supported(2,3)
	"Remember to only use + or -!"
	"""
	"*** YOUR CODE HERE ***"

def higher_order_lambdas():
    """
    Return a lambda function that takes in a multiplier and returns a lambda function that given an input will
    return the input multiplied by the multiplier
    >>>hol = higher_order_lambdas():
    >>>doubles = hol(2)
    >>>doubles(3)
    6
    >>>hol = higher_order_lambdas():
    >>>triples = hol(3)
    >>>triples(4)
    12
    """
    "*** YOUR CODE HERE ***"

def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    "*** YOUR CODE HERE ***"


def binary(n):
    """Return a list representing the representation of a number in base 2.

    >>> binary(55055)
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    >>> binary(-136)
    ['-', 1, 0, 0, 0, 1, 0, 0, 0]
    """
    "*** YOUR CODE HERE ***"
