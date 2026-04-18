#Calculadora simple con interfaz gráfica usando Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = combo_operacion.get()
        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos")
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simple")
# Crear widgets
label_num1 = tk.Label(ventana, text="Número 1:")
entry_num1 = tk.Entry(ventana)
label_num2 = tk.Label(ventana, text="Número 2:")
entry_num2 = tk.Entry(ventana)
label_operacion = tk.Label(ventana, text="Operación:")
#combo_operacion = tk.ttk.Combobox(ventana, values=["Suma", "Resta", "Multiplicación", "División"])
combo_operacion = ttk.Combobox(ventana, values=["Suma", "Resta", "Multiplicación", "División"])
combo_operacion.current(0)
button_calcular = tk.Button(ventana, text="Calcular", command=calcular)
label_resultado = tk.Label(ventana, text="Resultado: ")
# Colocar widgets en la ventana
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1.grid(row=0, column=1, padx=10, pady=10)
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2.grid(row=1, column=1, padx=10, pady=10)
label_operacion.grid(row=2, column=0, padx=10, pady=10)
combo_operacion.grid(row=2, column=1, padx=10, pady=10)
button_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
# Iniciar el bucle principal de la ventana
ventana.mainloop()
