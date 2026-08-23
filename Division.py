import tkinter as tk
from tkinter import messagebox

def abrir_division(ventana_principal):
    ventana = tk.Toplevel(ventana_principal)
    ventana.title("División - Neón Dark")
    ventana.geometry("400x620")
    ventana.resizable(False, False)
    ventana.configure(bg="#1E1E2E")  # Fondo oscuro elegante

    # Estilos de color
    COLOR_FONDO = "#1E1E2E"
    COLOR_TARJETA = "#2A2A3C"
    COLOR_TEXTO = "#CDD6F4"
    COLOR_AZUL = "#89B4FA"
    COLOR_VERDE = "#A6E3A1"
    COLOR_ROJO = "#F38BA8"

    # Título Principal
    tk.Label(
        ventana, text="DIVISIÓN", font=("Segoe UI", 20, "bold"),
        bg=COLOR_FONDO, fg=COLOR_AZUL
    ).pack(pady=(15, 10))

    # Marco de entradas (Tarjeta centrada)
    frame_entradas = tk.Frame(ventana, bg=COLOR_TARJETA, bd=0, relief="flat", padx=15, pady=10)
    frame_entradas.pack(pady=5, fill="x", padx=25)

    def estilo_focus(entry, activo):
        color = COLOR_AZUL if activo else COLOR_TARJETA
        entry.config(highlightbackground=color, highlightcolor=color, highlightthickness=2)

    # Campo Número 1
    tk.Label(frame_entradas, text="Numerador (Dividendo):", font=("Segoe UI", 10), bg=COLOR_TARJETA, fg=COLOR_TEXTO).pack(anchor="w")
    numero1 = tk.Entry(frame_entradas, font=("Segoe UI", 14), justify="center", bg="#181825", fg=COLOR_TEXTO, bd=0)
    numero1.pack(pady=(2, 10), fill="x", ipady=4)
    numero1.bind("<FocusIn>", lambda e: estilo_focus(numero1, True))
    numero1.bind("<FocusOut>", lambda e: estilo_focus(numero1, False))

    # Campo Número 2
    tk.Label(frame_entradas, text="Denominador (Divisor):", font=("Segoe UI", 10), bg=COLOR_TARJETA, fg=COLOR_TEXTO).pack(anchor="w")
    numero2 = tk.Entry(frame_entradas, font=("Segoe UI", 14), justify="center", bg="#181825", fg=COLOR_TEXTO, bd=0)
    numero2.pack(pady=(2, 10), fill="x", ipady=4)
    numero2.bind("<FocusIn>", lambda e: estilo_focus(numero2, True))
    numero2.bind("<FocusOut>", lambda e: estilo_focus(numero2, False))

    # Campo Resultado
    tk.Label(frame_entradas, text="Resultado:", font=("Segoe UI", 10, "bold"), bg=COLOR_TARJETA, fg=COLOR_VERDE).pack(anchor="w")
    resultado = tk.Entry(frame_entradas, font=("Segoe UI", 16, "bold"), justify="center", bg="#181825", fg=COLOR_VERDE, bd=0)
    resultado.pack(pady=(2, 5), fill="x", ipady=5)

    # Lógica de Cálculo
    def calcular():
        try:
            n1 = float(numero1.get())
            n2 = float(numero2.get())

            if n2 == 0:
                messagebox.showerror("Error Matemático", "¡No es posible dividir entre cero!")
                return

            total = round(n1 / n2, 6)
            resultado.delete(0, tk.END)
            resultado.insert(0, str(total))
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor ingresa números válidos.")

    def escribir(valor):
        widget = ventana.focus_get()
        if widget in (numero1, numero2):
            widget.insert(tk.END, valor)

    def borrar_caracter():
        widget = ventana.focus_get()
        if widget in (numero1, numero2):
            texto = widget.get()
            widget.delete(0, tk.END)
            widget.insert(0, texto[:-1])

    def limpiar_todo():
        numero1.delete(0, tk.END)
        numero2.delete(0, tk.END)
        resultado.delete(0, tk.END)
        numero1.focus_set()

    # Teclado Táctil Interactivo
    teclado = tk.Frame(ventana, bg=COLOR_FONDO)
    teclado.pack(pady=10)

    botones = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("DEL", 0, 3),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("C", 1, 3),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("=", 2, 3),
        ("0", 3, 0), (".", 3, 1)
    ]

    for item in botones:
        texto, fila, col = item[0], item[1], item[2]
        
        # Asignar funciones según el botón
        if texto == "DEL":
            cmd, color_btn = borrar_caracter, COLOR_ROJO
        elif texto == "C":
            cmd, color_btn = limpiar_todo, "#FAB387"
        elif texto == "=":
            cmd, color_btn = calcular, COLOR_VERDE
        else:
            cmd, color_btn = lambda v=texto: escribir(v), COLOR_AZUL

        btn = tk.Button(
            teclado, text=texto, width=5, height=1,
            font=("Segoe UI", 12, "bold"), bg=COLOR_TARJETA, fg=color_btn,
            activebackground=color_btn, activeforeground=COLOR_FONDO,
            bd=0, cursor="hand2", command=cmd
        )
        
        if texto == "=":
            btn.grid(row=2, column=3, rowspan=2, sticky="nsew", padx=3, pady=3)
        elif texto in ("0", "."):
            btn.grid(row=fila, column=col, padx=3, pady=3)
            if texto == ".":
                btn.grid(columnspan=2, sticky="nsew")
        else:
            btn.grid(row=fila, column=col, padx=3, pady=3)

    # Botón Volver
    tk.Button(
        ventana, text="← VOLVER AL MENÚ", font=("Segoe UI", 10, "bold"),
        bg=COLOR_TARJETA, fg=COLOR_TEXTO, bd=0, cursor="hand2",
        command=ventana.destroy
    ).pack(pady=15, ipadx=10, ipady=5)

    # Foco inicial por defecto
    numero1.focus_set()