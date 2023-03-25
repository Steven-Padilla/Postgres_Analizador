import ply.lex as lex

tokens = (
    'CREATE_DATABASE',
    'CREATE_TABLE',
    'INSERT',
    'DELETE',
    'UPDATE',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'VALUES',
    'SET',
    'WHERE',
    'INTEGER',
    'STRING',
    'SEMICOLON',
    'EQUAL',
    # 'INTO',
    # 'FROM',
    # 'COLUMN_NAME',
    'DATA_TYPE',
    'IDENTIFIER',

)


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_CREATE_DATABASE(t):
    r'(?i)CREATE\s+DATABASE\s+'
    return t


def t_CREATE_TABLE(t):
    r'(?i)CREATE\s+TABLE\s+'
    return t


def t_INSERT(t):
    r'(?i)INSERT\s+INTO\s+'
    return t


def t_DELETE(t):
    r'(?i)DELETE\s+FROM\s+'
    return t


def t_UPDATE(t):
    r'(?i)UPDATE'
    return t
def t_DATA_TYPE(t):
    r'(int|smallint|bigint|real|double precision|numeric|text|char|varchar|date|time|timestamp|boolean)'
    return t
def t_VALUES(t):
    r'(?i)VALUES'
    return t
def t_WHERE(t):
    r'(?i)WHERE'
    return t
def t_SET(t):
    r'(?i)SET'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
# t_VALUES = r'(?i)VALUES'
# t_SET = r'SET'
# t_WHERE = r'(?i)WHERE'
t_INTEGER = r'\d+'
t_STRING = r'\'[^\']*\''
t_SEMICOLON = r';'
t_EQUAL = r'='
# t_INTO = r'(?i)INTO'
# t_FROM = r'(?i)FROM'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

# def t_COLUMN_NAME(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     return t
#
# def t_DATA_TYPE(t):
#     r'(int|smallint|bigint|real|double precision|numeric|text|char|varchar|date|time|timestamp|boolean)'
#     return t

t_ignore = ' \t'


# Manejador de errores para caracteres no reconocidos
def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# Ejemplo de uso
# data = '''CREATE DATABASE mydatabase;
# CREATE TABLE mytable (id INT, name CHAR);
# INSERT INTO mytable (id, name) VALUES (1, 'John');
# DELETE FROM mytable WHERE id = 1;
# UPDATE mytable SET name = 'Jane' WHERE id = 1;'''
# lexer.input("UPDATE mytable SET name = 'Jane' WHERE id = 1;")
# Recorremos los tokens reconocidos por el analizador léxico
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No hay más tokens
#     print(f"lexico: {tok.type, tok.value}")
