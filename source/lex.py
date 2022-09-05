import tokens

lexems_type = list[tokens.Token]

def Lexer(code):
    lexems: lexems_type = []

    for i in code:
        match i:
            case 'a':
                if len(lexems)==0 or lexems[-1].token==tokens.Tokens.end:
                    lexems.append(tokens.Token(tokens.Tokens.fun, tokens.Functions.print_))
                elif lexems[-1].token==tokens.Tokens.fun:
                    lexems.append(tokens.Token(tokens.Tokens.start))
                elif lexems[-1].token==tokens.Tokens.start:
                    lexems.append(tokens.Token(tokens.Tokens.val, i))
                    lexems.append(tokens.Token(tokens.Tokens.end))
            case 'b':
                if len(lexems)==0 or lexems[-1].token==tokens.Tokens.end:
                    lexems.append(tokens.Token(tokens.Tokens.fun, tokens.Functions.input_))
                elif lexems[-1].token==tokens.Tokens.fun:
                    lexems.append(tokens.Token(tokens.Tokens.start))
                elif lexems[-1].token==tokens.Tokens.start:
                    lexems.append(tokens.Token(tokens.Tokens.val, i))
                    lexems.append(tokens.Token(tokens.Tokens.end))
            case 'c':
                if len(lexems)==0 or lexems[-1].token==tokens.Tokens.end:
                    lexems.append(tokens.Token(tokens.Tokens.fun, tokens.Functions.vprint))
                elif lexems[-1].token==tokens.Tokens.fun:
                    lexems.append(tokens.Token(tokens.Tokens.start))
                elif lexems[-1].token==tokens.Tokens.start:
                    lexems.append(tokens.Token(tokens.Tokens.val, i))
                    lexems.append(tokens.Token(tokens.Tokens.end))
            case 'd':
                if len(lexems)==0 or lexems[-1].token==tokens.Tokens.end:
                    lexems.append(tokens.Token(tokens.Tokens.fun, tokens.Functions.nl))
                elif lexems[-1].token==tokens.Tokens.fun:
                    lexems.append(tokens.Token(tokens.Tokens.start))
                elif lexems[-1].token==tokens.Tokens.start:
                    lexems.append(tokens.Token(tokens.Tokens.val, i))
                    lexems.append(tokens.Token(tokens.Tokens.end))
            case _:
                if len(lexems)==0 or lexems[-1].token==tokens.Tokens.end:
                    lexems.append(tokens.Token(tokens.Tokens.fun, tokens.Functions.print_))
                elif lexems[-1].token==tokens.Tokens.fun:
                    lexems.append(tokens.Token(tokens.Tokens.start))
                elif lexems[-1].token==tokens.Tokens.start:
                    lexems.append(tokens.Token(tokens.Tokens.val, i))
                    lexems.append(tokens.Token(tokens.Tokens.end))


    return lexems
