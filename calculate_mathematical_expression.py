#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Tsviel Zaikman , tsviel , 208241133
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that will bring 10 points for Griffindor
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one
# WEB PAGES I USED: https://www.w3schools.com/
# NOTES:
#################################################################


def calculate_mathematical_expression(num1, num2, operator):
    """Function to help Ms. Granger to solve simple math expressions"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == ':':
        return num1 / num2
    else:
        return None


def calculate_from_string(pattern):
    """Function that extends the previous function as of the weasley's
    brothers request"""
    lst = pattern.split()
    return calculate_mathematical_expression(int(lst[0]), int(lst[2]), lst[1])
