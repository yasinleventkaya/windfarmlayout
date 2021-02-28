# -*- coding: utf-8 -*-

import random
import numpy as np
import math

# Contrary to the usual, array_form_of_layout is a matrix formed by sequencing the columns one after the other.

row_num = 5                     # number of rows on the layout
column_num = 4                  # number of columns on the layout
turbine_num = 12                # number o turbines in the wind farm
cell_num = row_num * column_num
loss = 0.83
windSpeed = 10                  # average wind speed in m/s
cut_in_windSpeed = 6            # cut-in wind speed of the turbine in m/s
population_size = 100            # number of layouts in a population
er = 0.1                        # elitism rate
cr = 0.4                        # crossover rate
mr = 0.5                        # mutation rate
generation_number = 10          # number of generations

layouts = []

for i in range(population_size):
    array_form_of_layout = np.hstack((np.ones((turbine_num,), int), np.zeros((cell_num - turbine_num,), int)))
    np.random.shuffle(array_form_of_layout)
    #print(array_form_of_layout)

    sub_array = []
    output_array = []
    for cellIndex in range(len(array_form_of_layout)):
        sub_array.append(array_form_of_layout[cellIndex])
        if cellIndex % row_num == row_num - 1:
            output_array.append(sub_array)
            sub_array = []
    #print(output_array)

    for sub_array in output_array:
        for cellIndex in range(len(sub_array) - 1):
            if sub_array[cellIndex] != 0:
                sub_array[cellIndex + 1] = sub_array[cellIndex] * sub_array[cellIndex + 1] * loss
    #print(output_array)

    for sub_array in output_array:
        for cellIndex in range(len(sub_array)):
            if sub_array[cellIndex] * windSpeed <= cut_in_windSpeed:
                sub_array[cellIndex] = 0
    #print(output_array)

    total_power = 0
    for sub_array in output_array:
        for cell in sub_array:
            total_power += cell
    #print(total_power)

    layout_with_power = {
        "layout_matrix": array_form_of_layout,
        "layout_power": total_power
    }
    layout_with_power_copy = layout_with_power.copy()
    layouts.append(layout_with_power_copy)

#print(layouts)
sorted_layouts = sorted(layouts, key=lambda k: k['layout_power'], reverse=True)
#print(sorted_layouts)
for i in sorted_layouts:
    print(i)
