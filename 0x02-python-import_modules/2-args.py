#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
        i = 0
        for arg1 in sys.argv:
            if i == 1:
                print("{}: {}".format(i, arg1))
            i += 1
        
    elif i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
    else:
        print("{} argument.".format(i))
