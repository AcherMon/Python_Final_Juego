import tkinter as tk
import random


def obtener_posicion_random(self):
    x = random.randint(50, 550)
    y = random.randint(50, 350)
    return x, y

ventana = tk.Tk()
ventana.title("El GOTY Of The Year")
ventana.geometry("800x700")
escenario_canvas = (tk.Canvas(ventana, width=800, height=500, bg="#2c3e50"))
escenario_canvas.pack(fill=tk.BOTH, expand=True)
ventana.mainloop()