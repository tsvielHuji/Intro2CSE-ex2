#################################################################
# FILE : temperature.py
# WRITER : Tsviel Zaikman , tsviel , 208241133
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: Help Hugrid prepare for summer
# STUDENTS I DISCUSSED THE EXERCISE WITH: No one
# WEB PAGES I USED: None
# NOTES:
#################################################################

HEAT_DAYS_AMOUNT = 2


def is_it_summer_yet(limit_temp, temp_1, temp_2, temp_3):
    """Helps Hugrid to determine if its already summer in London"""
    temp_lst = [temp_1, temp_2, temp_3]
    if sum([limit_temp < i for i in temp_lst]) >= HEAT_DAYS_AMOUNT:
        return True
    return False
