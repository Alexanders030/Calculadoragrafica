import tkinter as tk


from suma import abrir_suma
from resta import abrir_resta


from multiplicacion import abrir_multiplicacion
from Division import abrir_division

from raiz import abrir_raiz

from potencia import abrir_potencia




# Crear ventana principal
ventana = tk.Tk()

ventana.title("Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)


# Título
titulo = tk.Label(
    ventana,
    text="CALCULADORA",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=20)


# Texto de instrucciones
subtitulo = tk.Label(
    ventana,
    text="Seleccione una operación",
    font=("Arial", 14)
)

subtitulo.pack(pady=5)


# Botón SUMA
boton_suma = tk.Button(
    ventana,
    text="SUMA",
    width=20,
    height=2,
    font=("Arial", 12),
    command=lambda: abrir_suma(ventana)
)

boton_suma.pack(pady=5)


# Botón RESTA
boton_resta = tk.Button(
    ventana,
    text="RESTA",
    width=20,
    height=2,
    font=("Arial", 12),
    command=lambda: abrir_resta(ventana)
)

boton_resta.pack(pady=5)


# Botón MULTIPLICACIÓN
boton_multiplicacion = tk.Button(
    ventana,
    text="MULTIPLICACIÓN",
    width=20,
    height=2,
    font=("Arial", 12),
    command=lambda:  abrir_multiplicacion(ventana)
)

boton_multiplicacion.pack(pady=5)


# Botón DIVISIÓN
boton_division = tk.Button(
    ventana,
    text="DIVISIÓN",
    width=20,
    height=2,
    font=("Arial", 12),
    command=lambda: abrir_division(ventana)
)

boton_division.pack(pady=5)


# Botón POTENCIA
boton_potencia = tk.Button(
    ventana,
    text="POTENCIA",
    width=20,
    height=2,
    font=("Arial", 12),
    command=lambda:  abrir_potencia(ventana)
)

boton_potencia.pack(pady=5)


# Botón RAÍZ CUADRADA
boton_raiz = tk.Button(
    ventana,
    text="RAÍZ CUADRADA",
    width=20,
    height=2,
    font=("Arial", 12),
    command=lambda: abrir_raiz(ventana)
)

boton_raiz.pack(pady=5)


# Salir
boton_salir = tk.Button(
    ventana,
    text="SALIR",
    width=20,
    height=2,
    font=("Arial", 12),
    command=ventana.destroy
)

boton_salir.pack(pady=10)

# Mantener abierta la ventana
ventana.mainloop()
