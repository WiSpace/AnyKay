import argparse

parser = argparse.ArgumentParser(description='AnyKey language.')
parser.add_argument('path', type=str, help='Input file')
parser.add_argument('-e', default="utf-8", type=str, help='Input file encoding')
# parser.add_argument('-o', type=str, help='Output dir')

init = parser.parse_args
