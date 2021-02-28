#################################################################
# FILE : largest_and_smallest.py
# WRITER : Tsviel Zaikman , tsviel , 208241133
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that will bring 10 points for Griffindor
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one
# WEB PAGES I USED: https://www.w3schools.com/
# NOTES: I had chose the cases for check_largest_and_smallest in order to
# check whether my function can check other numerical values that are not
# Integers and also I wanted to check if a case with all 3 arguments equals
# work correctly
#################################################################


def get_largest(num1, num2, num3):
    """ Function that receives 3 numbers, and returns the largest one """
    if num1 > num2:
        cache = num1
    else:
        cache = num2
    if cache > num3:
        return cache
    return num3


def get_smallest(num1, num2, num3):
    """ Function that receives 3 numbers, and returns the smallest one """
    if num1 > num2:
        cache = num2
    else:
        cache = num1
    if cache > num3:
        return num3
    return cache


def largest_and_smallest(num1, num2, num3):
    """
    :param num1, num2, num3: Numbers of Integers or Float types
    :return: The largest number and the smallest number
    """
    return get_largest(num1, num2, num3), get_smallest(num1, num2, num3)


def check_largest_and_smallest():
    """Checks the largest_and_smallest_function"""
    return largest_and_smallest(17, 1, 6) == (17, 1) and \
           largest_and_smallest(1, 17, 6) == (17, 1) and \
           largest_and_smallest(1, 1, 2) == (2, 1) and \
           largest_and_smallest(-8.6, 2, 0) == (2, -8.6) and \
           largest_and_smallest(8, 8, 8) == (8, 8)
