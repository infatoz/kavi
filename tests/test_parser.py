from kannada_parser import parser

with open('example.kannada', 'r', encoding='utf-8') as f:
    code = f.read()

# Parse the Kannada code
parser.parse(code)
