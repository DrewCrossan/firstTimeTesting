def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def divide(first_number, second_number):
    return first_number / second_number


def multiply(first_number, second_number):
    return first_number * second_number

def exponent2(number):
    # return number * number
    return number ** 2

def exponent3(number):
    # return exponent2(number) * number
    return number ** 3

def exponent4(number):
    # return exponent3(number) * number #<-- Before i knew about ** = "to the power of"
    return number ** 4

def square_root(number):
    return number ** 0.5 #<-- after i found out about the ** operator

def volume(length, width, height):
    return (length * width * height)

def is_circle_round(circumference, radius):
    return divide(circumference, radius)