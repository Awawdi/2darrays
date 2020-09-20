#!/bin/python3

import math
import os
import random
import re
import sys


def get_sum(array, row_number, col_number):
    hour_glass_sum = 0

    hour_glass_sum += array[row_number][col_number]

    hour_glass_sum += array[row_number - 1][col_number - 1]
    hour_glass_sum += array[row_number - 1][col_number]
    hour_glass_sum += array[row_number - 1][col_number + 1]

    hour_glass_sum += array[row_number + 1][col_number - 1]
    hour_glass_sum += array[row_number + 1][col_number]
    hour_glass_sum += array[row_number + 1][col_number + 1]

    return hour_glass_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum_of_hourGlasses = 7 * -9

    for i in range(1, 5):
        # loops rows
        for j in range(1, 5):
            # loop columns
            sum_of_current_hourGlass = get_sum(arr, i, j)
            if sum_of_current_hourGlass > max_sum_of_hourGlasses:
                max_sum_of_hourGlasses = sum_of_current_hourGlass

    print("maximum sum of hour glasses is: %s" % sum_of_current_hourGlass)
