from itertools import chain
from tkinter import StringVar, Tk,ttk
from tkinter import  messagebox
from functools import partial
from ttkthemes import ThemedTk as tt
from semantic import evaluate_expression
from lexer import execute
import psycopg2


#inicializar el root del tkinter
root = tt(theme="breeze")
style=ttk.Style(root)
style.configure('TButton', font=('Lexend', 12), padding=10)
try:
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1234',
        database='postgres'
    )
    print('Conexión exitosa')
except Exception as e:
    print(e)
#crear StringVar de los parametros
operacion = StringVar()
values=[]
values[0:14]=['','','','','','','','','','','','','','']

def create_gui():
    #ventana principal
    root.title("Postgres 7")
    ancho_ventana = 900
    alto_ventana = 520

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)

    root.resizable(1,1)
    def insert():
        operacion.set('INSERT INTO [TABLE]([COLUMNA1],[COLUMNA2]) VALUES ([VALOR1],[VALOR2]);')
        text1_box.insert(0,operacion.get())
        return operacion
    
    def select():
        operacion.set('SELECT * FROM [TABLE];')
        text1_box.insert(0,operacion.get())
        return operacion
    
    def update():
        operacion.set('UPDATE [TABLE] SET [COLUMNA]=[VALOR] WHERE [COLUMNA]=[VALOR];')
        text1_box.insert(0,operacion.get())
        return operacion
    
    def delete():
        operacion.set('DELETE FROM [TABLE] WHERE [COLUMNA]=[COLUMNA];')
        text1_box.insert(0,operacion.get())
        return operacion
    
    def getvalues():
        table.delete(*table.get_children())
        
        i=0
        values=execute(operacion.get())
        values=list(chain.from_iterable(values))
        print(values[0])
        while i<len(values):
            table.insert('', 'end', values=(values[i], values[i+1]))
            i=i+2



    text1_label = ttk.Label(root, text="Codigo:")
    text1_label.grid(row=0, column=0)
    
    # text1_label.pack()
    text1_box = ttk.Entry(root, width=50,textvariable=operacion)
    text1_box.grid(row=1, column=0)
    
    
    # text1_box.pack(pady=5)
    button1 = ttk.Button(root, text="Insert",command=insert)
    button1.grid(row=1, column=1)
    # button1.pack(pady=5)

    button2 = ttk.Button(root, text="Select",command=select)
    # button2.pack(pady=5)
    button2.grid(row=1, column=2)

    button3 = ttk.Button(root, text="Update",command=update)
    # button3.pack(pady=5)
    button3.grid(row=1, column=3)

    button4 = ttk.Button(root, text="Delete",command=delete)
    # button4.pack(pady=5)
    button4.grid(row=1, column=4)
    button5 = ttk.Button(root, text="Ejecutar código",command=lambda:[run(), getvalues()])
    button5.grid(row=7, column=0)
    # button5.pack(pady=5)

    # Crear los 7 botones
    

   

    button6 = ttk.Button(root, text="Analizar",command=getvalues)
    # button6.pack(pady=5)
    button6.grid(row=8, column=1)
    value=values[0]

    button7 = ttk.Button(root, text="Limpiar",command=partial(clear_all))
    # button7.pack(pady=5)
    button7.grid(row=8, column=2)

    # Crear la tabla
    table = ttk.Treeview(root, columns=('Col1','Col2'), show='headings')
    table.column('Col1', width=200, anchor='center')
    table.column('Col2', width=200, anchor='center')

    table.heading('Col1', text='Token')
    table.heading('Col2', text='Identificador')
    

    # table.pack(pady=20)
    table.grid(row=8, column=0)

    root.mainloop()

def clear_all():
    operacion.set("")  


def run():
    
    if (operacion.get() == ""):
        messagebox.showerror(
            title='Error al ejecutarse',
            message="No se pueden enviar valores con campos vacios"
        )
    else:
        ejecutar()

def ejecutar():
    evaluate_expression(operacion.get(),conn)
    
if __name__ == "__main__":
    create_gui()
    conn.close()
    print('Conexión cerrada')

