from translator import get_lexeme

line = ("repeat myvar:=-123 until func(id);")

tokens = get_lexeme(line)

