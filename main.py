from translator import get_lexeme
from lexer import get_words
line = ("repeat myvar:=-123 until func(id);")

tokens = get_lexeme(line)
print(tokens)
tokens2 = get_words(tokens)
print(tokens2)

