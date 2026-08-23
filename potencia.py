import tkinter as tk
from tkinter import messagebox

def abrir_potencia(ventana_principal=None):
    # Si no hay ventana principal (cuando pruebas el archivo solo), creamos una temporal
    if ventana_principal is None:
        ventana = tk.Tk()
    else:
        ventana = tk.Toplevel(ventana_principal)
        
    ventana.title("Calculadora de Potencia")
    ventana.geometry("420x750")
    ventana.resizable(False, False)
    
    # -----------------------------
    # DISEÑO Y COLORES
    # -----------------------------
    bg_color = "#000a1a"        # Fondo gris clarito
    btn_bg = "#ffffff"          # Botones blancos
    btn_calc_bg = "#007BFF"     # Botón calcular azul
    btn_calc_fg = "#ffffff"     # Texto blanco para calcular
    text_color = "#333333"      # Texto gris oscuro
    font_main = ("Segoe UI", 12)
    font_title = ("Segoe UI", 24, "bold")
    
    ventana.configure(bg=bg_color)

    # -----------------------------
    # TÍTULO Y SUBTÍTULO
    # -----------------------------
    frame_header = tk.Frame(ventana, bg=bg_color)
    frame_header.pack(pady=(20, 10))

    tk.Label(frame_header, text="POTENCIA", font=font_title, bg=bg_color, fg="#1a1a1a").pack()
    tk.Label(frame_header, text="Calcula una base elevada a un exponente", font=("Segoe UI", 10), bg=bg_color, fg="#666666").pack()

    # -----------------------------
    # ÁREA DE ENTRADA (BASE Y EXP)
    # -----------------------------
    frame_inputs = tk.Frame(ventana, bg=bg_color)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="Base:", font=("Segoe UI", 12, "bold"), bg=bg_color, fg=text_color).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    base = tk.Entry(frame_inputs, font=("Segoe UI", 16), justify="center", width=12, relief="solid", bd=1)
    base.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_inputs, text="Exponente:", font=("Segoe UI", 12, "bold"), bg=bg_color, fg=text_color).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    exponente = tk.Entry(frame_inputs, font=("Segoe UI", 16), justify="center", width=12, relief="solid", bd=1)
    exponente.grid(row=1, column=1, padx=10, pady=5)

    # -----------------------------
    # OPERACIÓN Y RESULTADO
    # -----------------------------
    frame_resultado = tk.Frame(ventana, bg=bg_color)
    frame_resultado.pack(pady=10)

    operacion = tk.Label(frame_resultado, text="Operación: -", font=("Segoe UI", 11, "italic"), bg=bg_color, fg="#555555")
    operacion.pack(pady=(0, 5))

    tk.Label(frame_resultado, text="Resultado:", font=("Segoe UI", 12, "bold"), bg=bg_color, fg=text_color).pack()

    resultado = tk.Entry(frame_resultado, font=("Segoe UI", 18, "bold"), justify="center", width=18, state="readonly", relief="solid", bd=1, readonlybackground="#e9ecef")
    resultado.pack(pady=5)

    # -----------------------------
    # FUNCIONES DE LA CALCULADORA
    # -----------------------------
    def calcular(event=None):
        try:
            texto_base = base.get().strip()
            texto_exponente = exponente.get().strip()

            if texto_base == "" or texto_exponente == "":
                messagebox.showwarning("Datos incompletos", "Por favor, ingresa la base y el exponente.")
                return

            numero_base = float(texto_base)
            numero_exponente = float(texto_exponente)

            if abs(numero_exponente) > 1000:
                messagebox.showwarning("Exponente no válido", "El exponente debe estar entre -1000 y 1000.")
                return

            total = numero_base ** numero_exponente

            resultado.config(state="normal")
            resultado.delete(0, tk.END)
            
            # Quitar decimales inútiles si es número entero
            if total.is_integer():
                resultado.insert(0, str(int(total)))
            else:
                resultado.insert(0, str(total))
            
            resultado.config(state="readonly")
            operacion.config(text=f"Operación: {numero_base:g} ^ {numero_exponente:g} = {total:g}")

        except ValueError:
            messagebox.showerror("Error", "Ingresa únicamente números válidos.")
        except OverflowError:
            messagebox.showerror("Error", "El resultado es demasiado grande para calcularlo.")

    def limpiar():
        base.delete(0, tk.END)
        exponente.delete(0, tk.END)
        resultado.config(state="normal")
        resultado.delete(0, tk.END)
        resultado.config(state="readonly")
        operacion.config(text="Operación: -")
        base.focus()

    def borrar():
        widget = ventana.focus_get()
        if widget in (base, exponente):
            texto = widget.get()
            if len(texto) > 0:
                widget.delete(len(texto) - 1, tk.END)

    def cambiar_signo():
        widget = ventana.focus_get()
        if widget in (base, exponente):
            texto = widget.get()
            if texto.startswith("-"):
                widget.delete(0, 1)
            elif texto != "":
                widget.insert(0, "-")

    def escribir(valor):
        widget = ventana.focus_get()
        if widget in (base, exponente):
            widget.insert(tk.END, valor)

    # -----------------------------
    # TECLADO NUMÉRICO (CORREGIDO)
    # -----------------------------
    teclado = tk.Frame(ventana, bg=bg_color)
    teclado.pack(pady=10)

    botones = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
        ("0", 3, 0), (".", 3, 1), ("+/-", 3, 2)
    ]

    # ¡AQUÍ ESTÁ LA INDENTACIÓN PERFECTA!
    for texto, fila, columna in botones:
        if texto == "+/-":
            accion = cambiar_signo
        else:
            accion = lambda valor=texto: escribir(valor)

        tk.Button(
            teclado, text=texto, width=5, height=2, font=("Segoe UI", 13, "bold"),
            bg=btn_bg, fg=text_color, relief="groove", cursor="hand2", command=accion
        ).grid(row=fila, column=columna, padx=5, pady=5)

    # -----------------------------
    # BOTONES DE ACCIÓN PRINCIPALES
    # -----------------------------
    frame_acciones = tk.Frame(ventana, bg=bg_color)
    frame_acciones.pack(pady=15)

    tk.Button(
        frame_acciones, text="CALCULAR", width=25, height=2, font=("Segoe UI", 12, "bold"),
        bg=btn_calc_bg, fg=btn_calc_fg, relief="flat", cursor="hand2", command=calcular
    ).pack(pady=5)

    tk.Button(
        frame_acciones, text="BORRAR", width=25, height=1, font=font_main,
        bg=btn_bg, relief="groove", cursor="hand2", command=borrar
    ).pack(pady=3)

    tk.Button(
        frame_acciones, text="LIMPIAR", width=25, height=1, font=font_main,
        bg=btn_bg, relief="groove", cursor="hand2", command=limpiar
    ).pack(pady=3)

    tk.Button(
        frame_acciones, text="VOLVER", width=25, height=1, font=font_main,
        bg="#ff4c4c", fg="white", relief="flat", cursor="hand2", command=ventana.destroy
    ).pack(pady=10)

    # -----------------------------
    # ATAJOS DEL TECLADO
    # -----------------------------
    ventana.bind("<Return>", calcular)
    ventana.bind("<Escape>", lambda event: ventana.destroy())
    
    # Cursor inicia en "Base"
    base.focus()

    # Esto permite probar el código dándole "Play" directo a este archivo
    if ventana_principal is None:
        ventana.mainloop()

# Para ejecutar el archivo solo y ver que funcione
if __name__ == "__main__":
    abrir_potencia()