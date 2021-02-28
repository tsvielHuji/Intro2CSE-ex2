#################################################################
# FILE : shapes.py
# WRITER : Tsviel Zaikman , tsviel , 208241133
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: Help the Muggle solve a Quadratic Equation with some magic
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one
# WEB PAGES I USED: https://www.w3schools.com/
# NOTES:
#################################################################

import math

CHOOSE_SHAPE_MESSAGE = "Choose shape (1=circle, 2=rectangle, 3=triangle): "
CIRCLE = "1"
RECTANGLE = "2"
TRIANGLE = "3"

PI = math.pi


def circle_area():
    """Calculate a circle's area by user's input"""
    radius = float(input())
    return PI * (radius ** 2)


def rectangle_area():
    """Calculate a rectangles's area by user's input"""
    edge_a = float(input())
    edge_b = float(input())
    return edge_a * edge_b


def triangle_area():
    """Calculate a triangle's area by user's input"""
    edge = float(input())
    return (math.sqrt(3) / 4) * (edge ** 2)


def shape_area():
    """Calculate a shapes's area by user's choice"""
    user_choice = input(CHOOSE_SHAPE_MESSAGE)
    if user_choice == CIRCLE:
        return circle_area()

    elif user_choice == RECTANGLE:
        return rectangle_area()

    elif user_choice == TRIANGLE:
        return triangle_area()

    else:
        return None
