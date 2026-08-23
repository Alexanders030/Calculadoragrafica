import tkinter as tk
from tkinter import messagebox


def abrir_raiz(ventana_principal):
    ventana = tk.Toplevel(ventana_principal)
    ventana.title("Calculadora - Raíces Generalizadas")
    ventana.geometry("400x680")
    ventana.resizable(False, False)
    ventana.configure(bg="#F5F5F5")

    tk.Label(
        ventana,
        text="CÁLCULO DE RAÍCES",
        font=("Arial", 18, "bold"),
        bg="#F5F5F5",
        fg="#333333"
    ).pack(pady=12)

    # --- Campo para el Índice (n) ---
    tk.Label(
        ventana,
        text="Índice de la raíz (ej. 2=cuadrada, 3=cúbica):",
        font=("Arial", 10, "bold"),
        bg="#F5F5F5",
        fg="#555555"
    ).pack()

    indice_entry = tk.Entry(
        ventana,
        font=("Arial", 14),
        justify="center",
        bd=2,
        relief="groove",
        width=10
    )
    indice_entry.pack(pady=3)
    indice_entry.insert(0, "2")  # Por defecto raíz cuadrada

    # --- Campo para el Radicando/Número (x) ---
    tk.Label(
        ventana,
        text="Número (Radicando):",
        font=("Arial", 10, "bold"),
        bg="#F5F5F5",
        fg="#555555"
    ).pack(pady=(8, 0))

    numero = tk.Entry(
        ventana,
        font=("Arial", 14),
        justify="center",
        bd=2,
        relief="groove"
    )
    numero.pack(pady=3)
    numero.focus()

    # Guarda cuál entrada tuvo el último foco para el teclado en pantalla
    campo_activo = {"widget": numero}

    def al_enfocar(event):
        campo_activo["widget"] = event.widget

    numero.bind("<FocusIn>", al_enfocar)
    indice_entry.bind("<FocusIn>", al_enfocar)

    # --- Campo de Resultado ---
    tk.Label(
        ventana,
        text="Resultado:",
        font=("Arial", 10, "bold"),
        bg="#F5F5F5",
        fg="#555555"
    ).pack(pady=(8, 0))

    resultado = tk.Entry(
        ventana,
        font=("Arial", 16, "bold"),
        justify="center",
        bd=2,
        relief="groove",
        state="readonly",
        fg="#2E7D32"
    )
    resultado.pack(pady=3)

    # --- Lógica de cálculo generalizada ---
    def calcular():
        try:
            base = float(numero.get())
            n_indice = float(indice_entry.get())

            if n_indice == 0:
                messagebox.showerror("Error", "El índice de la raíz no puede ser 0.")
                return

            # Manejo de bases negativas (Permitido solo para índices impares enteros)
            if base < 0:
                if n_indice.is_integer() and int(n_indice) % 2 != 0:
                    total = -((-base) ** (1.0 / n_indice))
                else:
                    messagebox.showerror(
                        "Error Matemático",
                        "No se puede calcular una raíz con índice par de un número negativo."
                    )
                    return
            else:
                total = base ** (1.0 / n_indice)

            total_fmt = int(total) if total.is_integer() else round(total, 4)

            resultado.config(state="normal")
            resultado.delete(0, tk.END)
            resultado.insert(0, str(total_fmt))
            resultado.config(state="readonly")

        except ValueError:
            messagebox.showerror(
                "Error de Entrada",
                "Asegúrate de ingresar números válidos en ambos campos."
            )

    def escribir(valor):
        campo_activo["widget"].insert(tk.END, valor)

    def borrar_ultimo():
        actual = campo_activo["widget"].get()
        if actual:
            campo_activo["widget"].delete(len(actual) - 1, tk.END)

    def limpiar_todo():
        numero.delete(0, tk.END)
        indice_entry.delete(0, tk.END)
        indice_entry.insert(0, "2")
        resultado.config(state="normal")
        resultado.delete(0, tk.END)
        resultado.config(state="readonly")

    # --- Teclado numérico interactivo ---
    teclado = tk.Frame(ventana, bg="#F5F5F5")
    teclado.pack(pady=10)

    botones = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
        ("0", 3, 0), (".", 3, 1), ("⌫", 3, 2)
    ]

    for texto, fila, columna in botones:
        comando = borrar_ultimo if texto == "⌫" else lambda v=texto: escribir(v)

        tk.Button(
            teclado,
            text=texto,
            width=5,
            height=2,
            font=("Arial", 11, "bold"),
            bg="#FFFFFF",
            activebackground="#E0E0E0",
            cursor="hand2",
            command=comando
        ).grid(row=fila, column=columna, padx=3, pady=3)

    # --- Botones de Acción ---
    panel_acciones = tk.Frame(ventana, bg="#F5F5F5")
    panel_acciones.pack(pady=5)

    tk.Button(
        panel_acciones,
        text="LIMPIAR",
        width=12,
        height=2,
        font=("Arial", 10, "bold"),
        bg="#FF9800",
        fg="white",
        cursor="hand2",
        command=limpiar_todo
    ).pack(side="left", padx=5)

    tk.Button(
        panel_acciones,
        text="CALCULAR",
        width=12,
        height=2,
        font=("Arial", 10, "bold"),
        bg="#4CAF50",
        fg="white",
        cursor="hand2",
        command=calcular
    ).pack(side="left", padx=5)

    tk.Button(
        ventana,
        text="VOLVER",
        width=26,
        height=2,
        font=("Arial", 10, "bold"),
        bg="#E53935",
        fg="white",
        cursor="hand2",
        command=ventana.destroy
    ).pack(pady=5)