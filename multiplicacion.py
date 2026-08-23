import tkinter as tk
from tkinter import messagebox


def abrir_multiplicacion(ventana_principal):

    # Crear ventana de multiplicación
    ventana = tk.Toplevel(ventana_principal)

    ventana.title("Multiplicación")
    ventana.geometry("400x780")
    ventana.resizable(False, False)


    # =========================================================
    # TÍTULO
    # =========================================================

    tk.Label(
        ventana,
        text="MULTIPLICACIÓN",
        font=("Arial", 22, "bold")
    ).pack(pady=15)


    # =========================================================
    # PRIMER NÚMERO
    # =========================================================

    tk.Label(
        ventana,
        text="Primer número:",
        font=("Arial", 12)
    ).pack()

    numero1 = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center"
    )

    numero1.pack(pady=5)


    # =========================================================
    # SEGUNDO NÚMERO
    # =========================================================

    tk.Label(
        ventana,
        text="Segundo número:",
        font=("Arial", 12)
    ).pack()

    numero2 = tk.Entry(
        ventana,
        font=("Arial", 16),
        justify="center"
    )

    numero2.pack(pady=5)


    # =========================================================
    # RESULTADO
    # =========================================================

    tk.Label(
        ventana,
        text="Resultado:",
        font=("Arial", 12)
    ).pack(pady=(10, 0))

    resultado = tk.Entry(
        ventana,
        font=("Arial", 18, "bold"),
        justify="center",
        state="readonly"
    )

    resultado.pack(pady=5)


    # =========================================================
    # FUNCIÓN CALCULAR
    # =========================================================

    def calcular():

        try:

            n1 = float(numero1.get())
            n2 = float(numero2.get())

            total = n1 * n2

            resultado.config(state="normal")
            resultado.delete(0, tk.END)
            resultado.insert(0, str(total))
            resultado.config(state="readonly")

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingrese números válidos."
            )


    # =========================================================
    # HISTORIA DE LA MULTIPLICACIÓN
    # =========================================================

    def mostrar_historia():

        historia = """
HISTORIA DE LA MULTIPLICACIÓN

La multiplicación es una de las operaciones
fundamentales de las matemáticas.

Las primeras civilizaciones desarrollaron
diferentes métodos para realizar multiplicaciones.

Los antiguos egipcios utilizaban un método
basado en la duplicación de números.

La multiplicación también puede entenderse
como una suma repetida.

Por ejemplo:

5 × 4 = 20

Es equivalente a:

5 + 5 + 5 + 5 = 20

Actualmente utilizamos los símbolos × y *
para representar esta operación.
"""

        messagebox.showinfo(
            "Historia de la multiplicación",
            historia
        )


    # =========================================================
    # EXPLICACIÓN DE LA MULTIPLICACIÓN
    # =========================================================

    def explicar_multiplicacion():

        try:

            n1 = float(numero1.get())
            n2 = float(numero2.get())

            total = n1 * n2

            texto = (
                f"{n1} × {n2} = {total}\n\n"
                f"La multiplicación puede entenderse "
                f"como una suma repetida.\n\n"
                f"Por ejemplo, {n1} × {n2} "
                f"significa sumar {n1} {int(n2)} veces."
            )

            messagebox.showinfo(
                "¿Cómo funciona?",
                texto
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Primero ingrese números válidos."
            )


    # =========================================================
    # TECLADO NUMÉRICO
    # =========================================================

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


    # =========================================================
    # ESCRIBIR CON EL TECLADO GRÁFICO
    # =========================================================

    def escribir(valor):

        widget = ventana.focus_get()

        if widget == numero1 or widget == numero2:

            widget.insert(tk.END, valor)

        else:

            numero1.focus_set()
            numero1.insert(tk.END, valor)


    # =========================================================
    # BORRAR
    # =========================================================

    def borrar():

        widget = ventana.focus_get()

        if widget == numero1 or widget == numero2:

            contenido = widget.get()

            if contenido:

                widget.delete(len(contenido) - 1, tk.END)


    # =========================================================
    # CREAR BOTONES DEL TECLADO
    # =========================================================

    for texto, fila, columna in botones:

        if texto == "BORRAR":

            accion = borrar

        else:

            accion = lambda valor=texto: escribir(valor)


        tk.Button(
            teclado,
            text=texto,
            width=7,
            height=2,
            font=("Arial", 12),
            command=accion
        ).grid(
            row=fila,
            column=columna,
            padx=4,
            pady=4
        )


    # =========================================================
    # BOTÓN CALCULAR
    # =========================================================

    tk.Button(
        ventana,
        text="CALCULAR",
        width=22,
        height=2,
        font=("Arial", 12, "bold"),
        command=calcular
    ).pack(pady=5)


    # =========================================================
    # BOTÓN HISTORIA
    # =========================================================

    tk.Button(
        ventana,
        text="HISTORIA",
        width=22,
        height=2,
        font=("Arial", 12),
        command=mostrar_historia
    ).pack(pady=5)


    # =========================================================
    # BOTÓN ¿CÓMO FUNCIONA?
    # =========================================================

    tk.Button(
        ventana,
        text="¿CÓMO FUNCIONA?",
        width=22,
        height=2,
        font=("Arial", 12),
        command=explicar_multiplicacion
    ).pack(pady=5)


    # =========================================================
    # BOTÓN VOLVER
    # =========================================================

    tk.Button(
        ventana,
        text="VOLVER",
        width=22,
        height=2,
        font=("Arial", 12),
        command=ventana.destroy
    ).pack(pady=10)


# =============================================================
# PRUEBA INDIVIDUAL
# =============================================================
# Este bloque permite ejecutar multiplicacion.py directamente.
# No afecta el funcionamiento cuando se importa desde main.py.

if __name__ == "__main__":

    ventana_principal = tk.Tk()

    ventana_principal.withdraw()

    abrir_multiplicacion(ventana_principal)

    ventana_principal.mainloop()