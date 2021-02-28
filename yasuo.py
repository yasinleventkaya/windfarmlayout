# -*- coding: utf-8 -*-

import random
import numpy as np
import math


row_num = 3
column_num = 4
turbine_num = 8
cell_num = row_num * column_num
loss = 0.83
turbine_power = 5

#lelele


def create_one_layout():
    array_form_of_layout = np.hstack((np.ones((turbine_num,), int), np.zeros((cell_num - turbine_num,), int)))
    np.random.shuffle(array_form_of_layout)
    print(array_form_of_layout)

    sub_array = []
    output_array = []
    for cellIndex in range(len(array_form_of_layout)):
        sub_array.append(array_form_of_layout[cellIndex])
        if cellIndex % row_num == row_num - 1:
            output_array.append(sub_array)
            sub_array = []
    print(output_array)

create_one_layout()
