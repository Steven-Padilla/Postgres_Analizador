from sintactico import parser
from tkinter import  messagebox
from psycopg2 import extensions
def check_sql(sentense,conn):
    arr_sentense=sentense.split()
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level( autocommit )
    cursor = conn.cursor()
    try:
        cursor.execute(sentense)
    except Exception as e:
        return e
    cursor.close()

    


def evaluate_expression(valor,conn):
    try:
        parser.parse(valor)
        result =check_sql(valor,conn)

        if result != None:
            messagebox.showerror(
                title = 'Error',
                message = result
            )
            raise SyntaxError(result)
        else:
            messagebox.showinfo(
                title='Resultado',
                message='Sentencia sql ejecutada'
            )
    except ZeroDivisionError:
        messagebox.showerror(
            title = 'Error Semantico',
            message = f'Error: División por cero'
        )
