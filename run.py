import sys


def main():
    # The operation we want to perform will be passed
    # as a string in the positional command line args
    # Example: python run.py '1 + 2'
    args = sys.argv[1].strip().split()
    x, op, y = args[0], args[1], args[2]
    print(x, op, y)


if __name__ == '__main__':
    main()
    
    
