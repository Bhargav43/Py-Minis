import sys

def print_builtins():
    #Prints the list of built-in module name, 1 per line. No Args, no return value.
    [print(builtin) for builtin in sorted([name for name in sys.modules.keys()])]

def return_builtins():
    #Returns the sorted list of built-in module names.
    return sorted([name for name in sys.modules.keys()])

def check_builtins(key):
    #Looks for a single built-in module name is present in Python. Returns True or False.
    return True if str(key) in sys.modules.keys() else False

def search_builtins(string):
    #Searches for the list of modules, sent as string, in Python Built-in modules and prints Yes or No. Returns True if function runs successfully.
    [print(f'{key}: Yes') if check_builtins(key) else print(f'{key}: No') for key in string.replace(' ', '').split(',')]
    return True

def main():
    print_builtins()
    builtins = return_builtins()
    exist = check_builtins('sys')
    search_builtins('sys, os, has')

if __name__ == '__main__':
    main()