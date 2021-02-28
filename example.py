# -*- coding: utf-8 -*-

var1 = [1,2,3,4,5]
print(var1)

def create_list():
    dummy_list = [1,2,3,4,5]
    return dummy_list

var2 = create_list()
print(var2)

def print_list(printed_list):
    print(printed_list)


print_list(var1)

###################




def create_one_random_layout():
    listo = [1,2,3,4,5,6,8,9]
    return listo

def make_crossover_for_two_layot(lay1, lay2):
    # 2. elemanları değiştirsim

    swapVar1 = lay1[1]
    swapVar2 = lay2[1]
    lay1[1] = swapVar2
    lay2[1] = swapVar1

    retDict = {
        "lay1": lay1,
        "lay2": lay2
    }
    return retDict


layout1 = [1,2,3,4]
layout2 = [5,6,7,8]


aa = make_crossover_for_two_layot(layout1, layout2)

layout1 = aa["lay1"]
layout2 = aa["lay2"]

print(layout1)
print(layout2)

def mutate_one_layout(lay):
    # 2. ve 3. elemanı yer değiştir
    cacheVar = lay[1]
    lay[1] = lay[2]
    lay[2] = cacheVar
    return lay

layout_m = [1,2,3,4,5,7]
print(layout_m)
layout_m = mutate_one_layout(layout_m)
print(layout_m)

