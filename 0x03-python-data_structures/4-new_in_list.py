#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx <0:
        return(my_list)

    len1 = len(my_list)
    if idx > len1 - 1:
        return(my_list)

    else:
        new_list[idx] = element

    return(new_list)
