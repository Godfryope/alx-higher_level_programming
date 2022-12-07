#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(None)

    len1 = len(my_list)

    elif idx > len1:
        return(None)

    return(my_list[idx])
