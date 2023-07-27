# prints number and list of arguments

if __name__ == "__main__":

    import sys
    args = sys.argv
    Num_of_args = len(args) - 1

    if Num_of_args == 0:
        print("0 arguments.")
    elif Num_of_args == 1:
        print("1 argument:")
    else:
        print(f"{Num_of_args} arguments:")

    for i, arg in enumerate(args[1:], start=1):
        print(f"{i}: {arg}")
