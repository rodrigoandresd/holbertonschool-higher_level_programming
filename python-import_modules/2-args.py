#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_arg = len(sys.argv) - 1
    if no_arg == 0:
        print("0 arguments.")
    elif no_arg == 1:
        print("1 argument:")
        print("1: ", sys.argv[1])
    elif no_arg > 1:
        print("{} arguments:".format(no_arg))
        for i in range(1, no_arg + 1):
            print("{}:".format(i), sys.argv[i])
