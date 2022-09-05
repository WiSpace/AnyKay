import tokens
from lex import lexems_type
from functions import *

def Pars(Lexems: lexems_type):
    fun = ''
    now = ''

    for i in Lexems:
        match i.token:
            case tokens.Tokens.fun:
                match i.val:
                    case tokens.Functions.print_:
                        fun = print_
                    case tokens.Functions.vprint:
                        fun = vprint_
                    case tokens.Functions.input_:
                        fun = input_
                    case tokens.Functions.nl:
                        fun = new_line
            case tokens.Tokens.start:
                now = tokens.Tokens.start
            case tokens.Tokens.val:
                fun(i.val)
