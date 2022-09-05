from dataclasses import dataclass
from enum import Enum
    

class Tokens(Enum):
    start = 1
    end = 2
    fun = 3
    val = 4

class Functions(Enum):
    print_ = 1
    input_ = 2
    vprint = 3
    nl = 3


@dataclass
class Token:
    token: Tokens
    val: str = ''
