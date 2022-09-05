globals()['var_'] = '?'

def input_(text):
    globals()['var_'] = input(text)

def print_(text):
    print(text, end='')

def vprint_(text):
    print(var_, end='')

def new_line(text):
    print('')
