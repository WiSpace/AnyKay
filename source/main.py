import args as a

from lex import Lexer
from parser import Pars

args = a.init()

with open(args.path, encoding=args.e) as f:
    code = Lexer(f.read())

    Pars(code)
