import numpy
import random
import time

def calc_as_function(line, colun):
    result = 0
    for i in range(len(line)):
        result = result + line[i] * colun[i]
    return result

def create_matrix(lines, coluns):

    A = []

    for i in range(lines):

		line = []

		for j in range(coluns):

			line  = line + [random.randint(1, 1000)]

		A = A + [line]

    return A

def populate_matrix(lines, coluns, array):

    A = []
    CONT = 0

    for i in range(lines):

        line = []

        for j in range(coluns):

            line = line + [array[CONT]]
            CONT = CONT + 1

        A = A + [line]

    return A
