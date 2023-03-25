from tkinter import StringVar, Tk,ttk
from tkinter import  messagebox
from functools import partial
from semantic import evaluate_expression
import psycopg2


#inicializar el root del tkinter
root = Tk()
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
    ancho_ventana = 900
    alto_ventana = 300

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)

    root.resizable(1,1)
    
    #etiquetas    
    label_operacion = ttk.Label(root, text="Ingrese su sentencia SQL: ", font=("Lexend", 12))
    label_operacion.pack(ipady=30)

    #cuadros de texto    
    operacion.set("")
    valor_operacion = ttk.Entry(root,textvariable=operacion)
    valor_operacion.pack()
    
    # #botones
    ejecutar = ttk.Button(root, text="Ejecutar", command=partial(run))
    ejecutar.pack(side='right',ipadx=20, padx=30)
    
    clear_button = ttk.Button(root, text="Limpiar campo", command=partial(clear_all))
    clear_button.pack(side='left',ipadx=20, padx=30)

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

