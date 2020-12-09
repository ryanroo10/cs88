"""Homework 2."""

# Question 1

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    answer = 1
    counter = 0
    while counter < k:
        answer = answer * n
        counter += 1
        n -= 1
    return answer


# Question 2

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    steps = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
            print(int(n))
            steps +=1
        else:
            n = 3 * n +1
            print(int(n))
            steps += 1
    return steps


# Question 3

def odd_even(x):
    """Classify a number as odd or even.

    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    return list(map(odd_even, s))


# Question 4

def deep_list(seq):
    """Returns a new list containing elements of the original list that are lists.

    >>> seq = [49, 8, 2, 1, 102]
    >>> deep_list(seq)
    []
    >>> seq = [[500], [30, 25, 24], 8, [0]]
    >>> deep_list(seq)
    [[500], [30, 25, 24], [0]]
    >>> seq = ["hello", [12, [25], 24], 8, [0]]
    >>> deep_list(seq)
    [[12, [25], 24], [0]]
    """
    def is_list(x):
        return type(x) == list
    return list(filter(is_list, seq))



# Question 5

def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(999, 1231, 34)
    [999, 1033, 1067, 1101, 1135, 1169, 1203]

    """
    arange_list = []
    while start < end:
        arange_list = arange_list + [start]
        start += step
    return arange_list





# Question 6

def count_cond(condition, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    j, count = 1, 0
    while j <= n:
        if condition(n, j):
            count += 1
        j += 1
    return count




# Question 7

def match_and_apply(pairs, function):
    """
    >>> pairs = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
    >>> def square(num):
    ...     return num**2
    >>> func = match_and_apply(pairs, square)
    >>> result = func(3)
    >>> result
    16
    >>> result = func(1)
    >>> result
    4
    >>> result = func(7)
    >>> result
    64
    >>> result = func(15)
    >>> print(result)
    None

    """
    def apply(n):
        for pair in pairs:
            if pair[0] == n:
                return function(pair[1])
        return None
    return apply
