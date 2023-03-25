import ply.yacc as yacc
from lexer import tokens
from tkinter import  messagebox

# sintaxis
def p_query(p):
    '''
    query : create_database SEMICOLON
          | create_table SEMICOLON
          | insert SEMICOLON
          | delete SEMICOLON
          | update SEMICOLON
    '''

def p_create_database(p):
    '''
    create_database : CREATE_DATABASE IDENTIFIER
    '''

def p_create_table(p):
    '''
    create_table : CREATE_TABLE IDENTIFIER LPAREN columns RPAREN
    '''

def p_columns(p):
    '''
    columns : column_def COMMA columns
            | column_def
    '''

def p_column_def(p):
    '''
    column_def : IDENTIFIER DATA_TYPE
    '''

def p_insert(p):
    '''
    insert : INSERT IDENTIFIER LPAREN identifiers RPAREN VALUES LPAREN values RPAREN
    '''

def p_identifiers(p):
    '''
    identifiers : IDENTIFIER COMMA identifiers
                | IDENTIFIER
    '''

def p_values(p):
    '''
    values : value COMMA values
           | value
    '''

def p_value(p):
    '''
    value : INTEGER
          | STRING
    '''

def p_delete(p):
    '''
    delete : DELETE IDENTIFIER WHERE IDENTIFIER EQUAL value
    '''

def p_update(p):
    '''
    update : UPDATE IDENTIFIER SET IDENTIFIER EQUAL value WHERE IDENTIFIER EQUAL value
    '''

# Manejador de errores
def p_error(p):
    if p:
        messagebox.showerror(
            title = 'Error Sintactico',
            message = f'Token inesperado {p.value}'
        )
        console_err(f'Error de sintaxis en la entrada cerca de {p.value}')
    else:
        messagebox.showerror(
            title = 'Error Sintactico',
            message = "Fin de entrada inesperado"
        )
        console_err('Error de sintaxis al final de la entrada')

def console_err(value):
    raise SyntaxError(value)


parser = yacc.yacc()

# Ejemplo de uso
# data = '''CREATE DATABASE mydatabase;
# CREATE TABLE mytable (id INT, name CHAR);
# INSERT INTO mytable (id, name) VALUES (1, 'John');
# DELETE FROM mytable WHERE id = 1;
# UPDATE mytable SET name = 'Jane' WHERE id = 1;'''
# 
# 
# ejemplo="CREATE TABLE mytable (id INT, name CHAR)"
# parser.parse(ejemplo,tracking =True)

