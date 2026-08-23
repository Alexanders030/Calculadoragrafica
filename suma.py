import tkinter as tk
from tkinter import messagebox
import random


def abrir_suma(ventana_principal):

    ventana = tk.Toplevel(ventana_principal)

    ventana.title("Suma")
    ventana.geometry("450x700")
    ventana.resizable(False, False)

    # ==========================
    # TÍTULO
    # ==========================

    titulo = tk.Label(
        ventana,
        text="SUMA",
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=15)


    # ==========================
    # PRIMER NÚMERO
    # ==========================

    tk.Label(
        ventana,
        text="Primer número:",
        font=("Arial", 12)
    ).pack()

    numero1 = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center",
        width=15
    )

    numero1.pack(pady=5)


    # ==========================
    # SEGUNDO NÚMERO
    # ==========================

    tk.Label(
        ventana,
        text="Segundo número:",
        font=("Arial", 12)
    ).pack()

    numero2 = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center",
        width=15
    )

    numero2.pack(pady=5)


    # ==========================
    # RESULTADO
    # ==========================

    tk.Label(
        ventana,
        text="Resultado:",
        font=("Arial", 12)
    ).pack(pady=(10, 0))

    resultado = tk.Entry(
        ventana,
        font=("Arial", 18, "bold"),
        justify="center",
        width=15,
        state="readonly"
    )

    resultado.pack(pady=5)


    # ==========================
    # FRASE MATEMÁTICA
    # ==========================

    frase = tk.Label(
        ventana,
        text="",
        font=("Arial", 11, "italic"),
        fg="#1F4E79",
        wraplength=380,
        justify="center"
    )

    frase.pack(pady=5)


    # ==========================
    # FRASES
    # ==========================

    frases_matematicos = [
        "Las matemáticas son el alfabeto con el cual Dios ha escrito el universo. — Galileo Galilei",

        "La esencia de las matemáticas no es hacer las cosas simples complicadas, sino hacer las cosas complicadas simples. — Stanisław Ulam",

        "Las matemáticas no conocen razas ni fronteras geográficas. — David Hilbert",

        "La matemática es la ciencia del orden y la medida. — Aristóteles",

        "Sin matemáticas no hay conocimiento sólido. — Roger Bacon"
    ]


    # ==========================
    # FUNCIÓN CALCULAR
    # ==========================

    def calcular():

        try:

            n1 = float(numero1.get())
            n2 = float(numero2.get())

            total = n1 + n2

            # Habilitar temporalmente el campo resultado
            resultado.config(state="normal")

            resultado.delete(0, tk.END)

            resultado.insert(0, str(total))

            resultado.config(state="readonly")

            # Mostrar una frase aleatoria
            frase_elegida = random.choice(frases_matematicos)

            frase.config(
                text=frase_elegida
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese números válidos."
            )


    # ==========================
    # TECLADO NUMÉRICO
    # ==========================

    teclado = tk.Frame(ventana)

    teclado.pack(pady=10)


    botones = [
        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),

        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),

        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),

        ("0", 3, 1),
        (".", 3, 2)
    ]


    # ==========================
    # ESCRIBIR EN LOS CAMPOS
    # ==========================

    def escribir(valor):

        widget = ventana.focus_get()

        if widget in (numero1, numero2):

            widget.insert(tk.END, valor)


    # Crear botones
    for texto, fila, columna in botones:

        tk.Button(
            teclado,
            text=texto,
            width=5,
            height=2,
            font=("Arial", 14),
            command=lambda valor=texto: escribir(valor)
        ).grid(
            row=fila,
            column=columna,
            padx=5,
            pady=5
        )


    # ==========================
    # BOTÓN CALCULAR
    # ==========================

    boton_calcular = tk.Button(
        ventana,
        text="CALCULAR",
        width=25,
        height=2,
        font=("Arial", 12, "bold"),
        bg="#28A745",
        fg="white",
        activebackground="#218838",
        command=calcular
    )

    boton_calcular.pack(pady=10)


    # ==========================
    # BOTÓN VOLVER
    # ==========================

    boton_volver = tk.Button(
        ventana,
        text="VOLVER",
        width=25,
        height=2,
        font=("Arial", 12, "bold"),
        bg="#DC3545",
        fg="white",
        activebackground="#C82333",
        command=ventana.destroy
    )

    boton_volver.pack(pady=5)