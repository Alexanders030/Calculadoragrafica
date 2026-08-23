import tkinter as tk
from tkinter import messagebox


def abrir_resta(ventana_principal):

    ventana = tk.Toplevel(ventana_principal)

    ventana.title("Resta")
    ventana.geometry("400x650")
    ventana.resizable(False, False)

    # -------------------------
    # TÍTULO
    # -------------------------

    tk.Label(
        ventana,
        text="RESTA",
        font=("Arial", 22, "bold")
    ).pack(pady=10)


    # -------------------------
    # PRIMER NÚMERO
    # -------------------------

    tk.Label(
        ventana,
        text="Primer número:",
        font=("Arial", 11)
    ).pack()

    numero1 = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center"
    )

    numero1.pack(pady=3)


    # -------------------------
    # SEGUNDO NÚMERO
    # -------------------------

    tk.Label(
        ventana,
        text="Segundo número:",
        font=("Arial", 11)
    ).pack()

    numero2 = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center"
    )

    numero2.pack(pady=3)


    # -------------------------
    # RESULTADO
    # -------------------------

    tk.Label(
        ventana,
        text="Resultado:",
        font=("Arial", 11)
    ).pack(pady=(8, 0))

    resultado = tk.Entry(
        ventana,
        font=("Arial", 18),
        justify="center",
        state="readonly"
    )

    resultado.pack(pady=3)


    # -------------------------
    # FUNCIÓN CALCULAR
    # -------------------------

    def calcular():

        try:

            n1 = float(numero1.get())
            n2 = float(numero2.get())

            total = n1 - n2

            resultado.config(state="normal")
            resultado.delete(0, tk.END)
            resultado.insert(0, str(total))
            resultado.config(state="readonly")

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese números válidos."
            )


    # -------------------------
    # FUNCIÓN PARA ESCRIBIR
    # -------------------------

    def escribir(valor):

        widget = ventana.focus_get()

        if widget == numero1 or widget == numero2:

            widget.insert(tk.END, valor)


    # -------------------------
    # BORRAR
    # -------------------------

    def borrar():

        widget = ventana.focus_get()

        if widget == numero1 or widget == numero2:

            widget.delete(0, tk.END)


    # -------------------------
    # TECLADO
    # -------------------------

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

        ("0", 3, 0),
        (".", 3, 1),
        ("BORRAR", 3, 2)
    ]


    for texto, fila, columna in botones:

        if texto == "BORRAR":

            comando = borrar

        else:

            comando = lambda valor=texto: escribir(valor)


        tk.Button(
            teclado,
            text=texto,
            width=7,
            height=2,
            font=("Arial", 11),
            command=comando
        ).grid(
            row=fila,
            column=columna,
            padx=3,
            pady=3
        )


    # -------------------------
    # BOTÓN CALCULAR
    # -------------------------

    tk.Button(
        ventana,
        text="CALCULAR",
        width=20,
        height=2,
        font=("Arial", 12, "bold"),
        command=calcular
    ).pack(pady=5)


    # -------------------------
    # BOTÓN VOLVER
    # -------------------------

    tk.Button(
        ventana,
        text="VOLVER",
        width=20,
        height=2,
        font=("Arial", 12),
        command=ventana.destroy
    ).pack(pady=5)