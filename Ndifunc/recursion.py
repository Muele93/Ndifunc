def sum_array(array):
    """funtion returns the sum of all items in array"""
    x= len(array)

    if x == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:],)


def fibonacci(n):
    """"Returns the nth term in a fibonacci sequence when n==0 and n==1"""
    if n==0 or n==1:
        return n
    else:
        #When n>1, the nth term of a fibonacci sequence is returned by adding the 2 previous terms
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    """Returns the factorial of n when it is greater than 0"""
    if n==0:
        return 1
    #The factorial of 0 is always 1
    else:
        return n* factorial(n-1)


def reverse(word):
    """The function returns a string in reverse"""
    reversed_string = ''
    index = len(word)
    while index:
        index =index- 1
        reversed_string = reversed_string + word[index]
    return reversed_string
