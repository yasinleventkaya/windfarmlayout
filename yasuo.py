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


def print_list(print_gen):
    print("========")
    for i in print_gen:
        print(i)
    print("========")


def create_one_layout():
    raw_array = np.hstack((np.ones((turbine_num,), int), np.zeros((cell_num - turbine_num,), int)))
    np.random.shuffle(raw_array)

    layout = {
        "rawArray": raw_array
    }

    update_layout(layout)
    return layout


def update_layout(layout):
    add_matrix_form(layout)
    add_total_power_to_layout(layout)


def add_matrix_form(layout):
    raw_array = layout["rawArray"]

    sub_array = []
    matrix_array = []
    for cellIndex in range(len(raw_array)):
        sub_array.append(raw_array[cellIndex])
        if cellIndex % row_num == row_num - 1:
            matrix_array.append(sub_array)
            sub_array = []
    layout["matrixArray"] = matrix_array


def add_total_power_to_layout(layout):
    total_power = 0
    matrix_array = layout["matrixArray"]

    for column in matrix_array:
        counter = 0
        for cellIndex in range(len(column)):
            if column[cellIndex] == 1:
                if cellIndex > 0 and column[cellIndex - 1] == 1:
                    counter += 1
                else:
                    counter = 0
                total_power = total_power + turbine_power * (loss ** counter)
    layout["total_power"] = round(total_power, 4)


def get_next_generation(prev_generation):
    next_generation = []
    for i in range(int(population_size * er)):
        next_generation.append(prev_generation[i])
    crossover_temp = []
    for i in range(int(population_size * cr)):
        crossover_temp.append(prev_generation[i])
    make_crossover(crossover_temp)
    for i in range(int(population_size * (1 - er))):
        next_generation.append(create_one_layout())
    next_generation = sorted(next_generation, key=lambda k: k['total_power'], reverse=True)
    return next_generation


def make_crossover(generation_piece):
    temp = []
    sub_array = []
    for i in generation_piece:
        sub_array.append(i)
        if len(sub_array) == 2:
            temp.append(sub_array)
            sub_array = []
    print_list(temp)


def get_generation(prev_generation):
    next_generation = []
    if len(prev_generation) == 0:
        pass
    else:
        pass
    add_props_to_generation(next_generation)
    return next_generation


def add_props_to_generation(generation):
    pass


def start_evolution():
    current_generation = []
    for i in range(generation_num):
        current_generation = get_generation(current_generation)
        winner_layout = current_generation[0]



if __name__ == '__main__':
    start_evolution()


################################################


current_generation = []
for i in range(population_size):
    current_generation.append(create_one_layout())
    current_generation = sorted(current_generation, key=lambda k: k['total_power'], reverse=True)

for i in range(generation_num - 1):
    if current_generation[0].get("total_power") > cut_power_coefficient*turbine_num*turbine_power:
        break
    current_generation = get_next_generation(current_generation)


print_list(current_generation)
king = current_generation[0]
# print(king.get("total_power"))



