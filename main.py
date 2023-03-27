from tkinter import StringVar, Tk,ttk
from tkinter import  messagebox
from functools import partial
from ttkthemes import ThemedTk as tt
from semantic import evaluate_expression
import psycopg2


#inicializar el root del tkinter
root = tt(theme="breeze")
style=ttk.Style(root)
style.configure('TButton', font=('Lexend', 12), padding=10)
try:
    conn=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='postgres',
        database='prueba'
    )
    print('Conexión exitosa')
except Exception as e:
    print(e)
#crear StringVar de los parametros
operacion = StringVar()

def create_gui():
    #ventana principal
    root.title("Postgres 7")
    ancho_ventana = 860
    alto_ventana = 520

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)

    root.resizable(1,1)
    
    # #etiquetas    
    # label_operacion = ttk.Label(root, text="Ingrese su sentencia SQL: ", font=("Lexend", 12))
    # label_operacion.pack(ipady=20)

    # #cuadros de texto    
    # operacion.set("")
    # valor_operacion = ttk.Entry(root,textvariable=operacion)
    # valor_operacion.pack()
    
    # #botones
    # ejecutar = ttk.Button(root, text="Ejecutar", command=partial(run),style='TButton')
    # ejecutar.pack(side='right',ipadx=20, padx=30)
    
    # clear_button = ttk.Button(root, text="Limpiar campo", command=partial(clear_all), style='TButton')
    # clear_button.pack(ipadx=20, padx=30)
    
    # Crear los 4 espacios de texto
    text1_label = ttk.Label(root, text="Codigo:")
    text1_label.grid(row=0, column=0)
    # text1_label.pack()
    text1_box = ttk.Entry(root, width=50)
    text1_box.grid(row=1, column=0)
    
    # text1_box.pack(pady=5)
    button1 = ttk.Button(root, text="Insert")
    button1.grid(row=1, column=1)
    # button1.pack(pady=5)

    button2 = ttk.Button(root, text="Select")
    # button2.pack(pady=5)
    button2.grid(row=1, column=2)

    button3 = ttk.Button(root, text="Update")
    # button3.pack(pady=5)
    button3.grid(row=1, column=3)

    button4 = ttk.Button(root, text="Update")
    # button4.pack(pady=5)
    button4.grid(row=1, column=4)

    text2_label = ttk.Label(root, text="Analizador Sintáctico:")
    # text2_label.pack()
    text2_label.grid(row=2, column=0)
    text2_box = ttk.Entry(root, width=50,state='disabled')
    # text2_box.pack(pady=5)
    text2_box.grid(row=3, column=0)

    text3_label = ttk.Label(root, text="Analizador Léxico:")
    # text3_label.pack()
    text3_label.grid(row=4, column=0)
    text3_box = ttk.Entry(root, width=50,state='disabled')
    # text3_box.pack(pady=5)
    text3_box.grid(row=5, column=0)
    button5 = ttk.Button(root, text="Ejecutar código")
    button5.grid(row=7, column=1)
    # button5.pack(pady=5)
    text4_label = ttk.Label(root, text="Salida")
    # text4_label.pack()
    text4_label.grid(row=6, column=0)
    text4_box = ttk.Entry(root, width=50,state='disabled')
    text4_box.grid(row=7, column=0)
    # text4_box.pack(pady=5)

    # Crear los 7 botones
    

   

    button6 = ttk.Button(root, text="Analizar")
    # button6.pack(pady=5)
    button6.grid(row=8, column=1)

    button7 = ttk.Button(root, text="Limpiar")
    # button7.pack(pady=5)
    button7.grid(row=8, column=2)

    # Crear la tabla
    table = ttk.Treeview(root, columns=('Col1','Col2','Col3','Col4','Col5','Col6','Col7'), show='headings')
    table.column('Col1', width=50, anchor='center')
    table.column('Col2', width=50, anchor='center')
    table.column('Col3', width=50, anchor='center')
    table.column('Col4', width=50, anchor='center')
    table.column('Col5', width=50, anchor='center')
    table.column('Col6', width=50, anchor='center')
    table.column('Col7', width=50, anchor='center')

    table.heading('Col1', text='Linea')
    table.heading('Col2', text='Token')
    table.heading('Col3', text='Pr')
    table.heading('Col4', text='Identificador')
    table.heading('Col5', text='Datos')
    table.heading('Col6', text='Numero')
    table.heading('Col7', text='Simbolo')
    table.insert('', 'end', values=('Valor 1', 'Valor 2'))
    table.insert('', 'end', values=('Valor 3', 'Valor 4'))
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

