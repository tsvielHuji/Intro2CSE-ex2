#################################################################
# FILE : quadratic_equation.py
# WRITER : Tsviel Zaikman , tsviel , 208241133
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: Help the Muggle solve a Quadratic Equation with some magic
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one
# WEB PAGES I USED: https://www.w3schools.com/
# NOTES:
#################################################################

import math
USERS_MESSAGE = "Insert coefficients a, b, and c: "
A_IS_ZERO_ERROR = "The parameter 'a' may not equal 0"
TWO_SOLUTIONS_MESSAGE = "The equation has 2 solutions: %s and %s"
ONE_SOLUTIONS_MESSAGE = "The equation has 1 solution: %s"
NO_SOLUTION = "The equation has no solutions"


def quadratic_equation(coefficient_a, coefficient_b, coefficient_c):
    """The function solves Quadratic Equations"""
    delta = (coefficient_b ** 2) - (4 * coefficient_a * coefficient_c)
    sol_1, sol_2 = None, None
    if delta > 0:
        sol_1 = (-coefficient_b) + math.sqrt(delta)
        sol_1 = sol_1 / 2 * coefficient_a
        sol_2 = (-coefficient_b) - math.sqrt(delta)
        sol_2 = sol_2 / 2 * coefficient_a

    elif delta == 0:
        return (-coefficient_b ) / 2 * coefficient_a, None
    return sol_1, sol_2


def quadratic_equation_user_input():
    """The function solves Quadratic Equations by Users input"""
    users_input = input(USERS_MESSAGE).split()
    answers = quadratic_equation(float(users_input[0]),
                                 float(users_input[1]),
                                 float(users_input[2]))
    if answers[0] == 0:
        print(A_IS_ZERO_ERROR)
        return
    if answers == (None, None):
        print(NO_SOLUTION)
        return
    if None not in answers:
        print(TWO_SOLUTIONS_MESSAGE % (answers[0], answers[1]))
        return
    if answers[0] is None and answers[1] is not None:
        print(ONE_SOLUTIONS_MESSAGE % answers[1])
        return
    if answers[1] is None and answers[0] is not None:
        print(ONE_SOLUTIONS_MESSAGE % answers[0])
        return


if __name__ == '__main__':
    quadratic_equation_user_input()