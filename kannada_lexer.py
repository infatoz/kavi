import re
import ply.lex as lex

# Kannada reserved keywords
reserved = {
    'ಮುದ್ರಿಸು': 'PRINT',
    'ನಿದರ್ಶನ': 'IF',
    'ಇಲ್ಲವೇ': 'ELSE',
    'ಮರುಕಳನೆ': 'LOOP',
    'ಸತ್ಯ': 'TRUE',
    'ಸುಳ್ಳು': 'FALSE',
}

# List of token names
tokens = (
    'NUMBER', 'STRING', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'EQUAL', 'GREATER', 'LESS', 'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE', 'SEMICOLON', 'IDENTIFIER', 'NEWLINE', 'EXCLAMATION'
) + tuple(reserved.values())

# Token rules
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_GREATER = r'>'
t_LESS = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_EXCLAMATION = r'!'  # Token for '!'
t_ignore = ' \t'  # Ignore spaces and tabs

# Comment rule
def t_COMMENT(t):
    r'\#.*'  # Match a hash and everything after it on the line
    pass  # Ignore comments

# Token for identifiers (allowing Kannada characters)
def t_IDENTIFIER(t):
    r'[\u0C80-\u0CFF][\w\u0C80-\u0CFF_]*'  # Match Kannada letters
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# Token for numbers
def t_NUMBER(t):
    r'\d+'  # Match one or more digits
    t.value = int(t.value)  # Convert to integer
    return t

# Token for strings
def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Handle newlines to track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(reflags=re.UNICODE)

# Example test function to demonstrate lexer
def test_lexer(code):
    lexer.input(code)
    for token in lexer:
        print(token)

# Example code
if __name__ == "__main__":
    code = '''
    ಹಲೋ ಪ್ರಪಂಚ!  # This line has an exclamation mark
    ಯ = 10;
    ಸಂಖ್ಯೆ 5 ಕ್ಕಿಂತ ದೊಡ್ಡದು;
    ಸಂಖ್ಯೆ 5 ಕ್ಕಿಂತ ಕಡಿಮೆ;
    ಮರುಕಳನೆ ( 5 ) {
        ಮುದ್ರಿಸು ("ಲೂಪ್ ರನ್ ಆಗುತ್ತಿದೆ");
    };
    '''
    test_lexer(code)
