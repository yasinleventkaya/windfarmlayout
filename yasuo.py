# -*- coding: utf-8 -*-

import numpy as np

population_size = 10
generation_num = 3
er = 0.2
cr = 0.4
mr = 0.5

row_num = 3
column_num = 4
turbine_num = 8
cell_num = row_num * column_num
loss = 0.83
turbine_power = 5
cut_power_coefficient = 0.98


def print_generation(print_gen):
    print("========")
    for i in print_gen:
        print(i)
    print("========")

def create_one_layout():
    array_form_of_layout = np.hstack((np.ones((turbine_num,), int), np.zeros((cell_num - turbine_num,), int)))
    np.random.shuffle(array_form_of_layout)

    sub_array = []
    matrix_array = []
    total_power = 0
    for cellIndex in range(len(array_form_of_layout)):
        sub_array.append(array_form_of_layout[cellIndex])
        if cellIndex % row_num == row_num - 1:
            matrix_array.append(sub_array)
            sub_array = []
    for column in matrix_array:
        for cellIndex in range(len(column)):
            if column[cellIndex] == 1:
                if cellIndex == 0:
                    total_power = total_power + turbine_power
                else:
                    if column[cellIndex - 1] == 1:
                        total_power = total_power + turbine_power*loss
                    else:
                        total_power = total_power + turbine_power

    retDict = {
        "rawArray": array_form_of_layout,
        "matrixArray": matrix_array,
        "total_power": total_power
    }
    return retDict


def get_next_generation(prev_generation):
    next_generation = []
    for i in range(int(population_size * er)):
        next_generation.append(prev_generation[i])
    for i in range(int(population_size * (1 - er))):
        next_generation.append(create_one_layout())
    next_generation = sorted(next_generation, key=lambda k: k['total_power'], reverse=True)
    return next_generation

################################################

current_generation = []
for i in range(population_size):
    current_generation.append(create_one_layout())
    current_generation = sorted(current_generation, key=lambda k: k['total_power'], reverse=True)

print_generation(current_generation)

for i in range(generation_num - 1):
    if current_generation[0].get("total_power") > cut_power_coefficient*turbine_num*turbine_power:
        break
    current_generation = get_next_generation(current_generation)
    print_generation(current_generation)


king = current_generation[0]



