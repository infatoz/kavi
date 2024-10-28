from kannada_lexer import lexer

# Open the .kannada file
with open('example.kannada', 'r', encoding='utf-8') as f:
    code = f.read()

lexer.input(code)

# Tokenize the input
for token in lexer:
    print(token)
