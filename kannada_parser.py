import ply.yacc as yacc
from kannada_lexer import tokens

# Grammar rules

def p_program(p):
    '''program : statement
               | statement program'''
    pass

def p_statement_print(p):
    'statement : PRINT LPAREN STRING RPAREN SEMICOLON'
    print(p[3])

def p_statement_assign(p):
    'statement : IDENTIFIER EQUAL expression SEMICOLON'
    print(f"{p[1]} = {p[3]}")

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LBRACE program RBRACE ELSE LBRACE program RBRACE'''
    if p[3]:  # p[3] is the evaluated expression from if condition
        print("Executing IF block")
    else:
        print("Executing ELSE block")

def p_statement_loop(p):
    '''statement : LOOP LPAREN NUMBER RPAREN LBRACE program RBRACE'''
    for _ in range(p[3]):
        print("Executing loop")

def p_expression_arithmetic(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:  # Means p[2] is PLUS or MINUS
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]  # Only term

def p_expression_boolean(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = True if p[1] == 'TRUE' else False

def p_expression_comparison(p):
    '''expression : expression GREATER expression
                  | expression LESS expression'''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]

def p_term_multiplication(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:  # Means p[2] is MULTIPLY or DIVIDE
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]  # Only factor

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_identifier(p):
    'factor : IDENTIFIER'
    p[0] = 0  # Placeholder for variable values

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Example test function to demonstrate parser
def test_parser(code):
    parser.parse(code)

# Example usage
if __name__ == "__main__":
    code = '''
    ಹಲೋ ಪ್ರಪಂಚ!  # This line has an exclamation mark
    ಯ = 10;
    ಸಂಖ್ಯೆ = 5;
    ನಿದರ್ಶನ (ಸಂಖ್ಯೆ > 5) {
        ಮುದ್ರಿಸು ("ಸಂಖ್ಯೆ 5 ಕ್ಕಿಂತ ದೊಡ್ಡದು");
    } ಇನ್ನೇನಾದರೂ {
        ಮುದ್ರಿಸು ("ಸಂಖ್ಯೆ 5 ಕ್ಕಿಂತ ಕಡಿಮೆ");
    };
    ಮರುಕಳನೆ (5) {
        ಮುದ್ರಿಸು ("ಲೂಪ್ ರನ್ ಆಗುತ್ತಿದೆ");
    };
    '''
    test_parser(code)
