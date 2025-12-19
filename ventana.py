import random
import tkinter as tk
from Clases.personajes import Personaje
from Clases.premio import premio
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("GOTY of the year")
ventana.geometry("800x700")

canvas_width = 800
canvas_height = 700
img_fondo = Image.open("assets/suelo.jpg")
imagen_resize = img_fondo.resize((800,700),Image.LANCZOS)
imgtk = ImageTk.PhotoImage(imagen_resize)
label_img = tk.Label(ventana, image=imgtk)
escenario_canvas = tk.Canvas(label_img, width=canvas_width, height=canvas_height, bg="#2c3e50")
escenario_canvas.pack(fill=tk.BOTH, expand=True)
label_img.pack(padx=10, pady=10)

# Crear Mini PEKKA en el centro
x_centro = canvas_width // 2
y_centro = canvas_height // 2
mini_pekka = Personaje(escenario_canvas, "Mini PEKKA", x_centro, y_centro)
mini_pekka.dibujar()

# creamos el "premio"
x=random.randint(2,798)
y=random.randint(2,698)
tortita = premio (escenario_canvas, "Pancake", x, y)
tortita.dibujar()
tortita.spawn()

# Movimiento
def mover_izquierda(event):
    mini_pekka.mover(-10, 0)
def mover_derecha(event):
    mini_pekka.mover(10, 0)
def mover_arriba(event):
    mini_pekka.mover(0, -10)
def mover_abajo(event):
    mini_pekka.mover(0, 10)

# Vincular teclas para el movimiento
ventana.bind("<Left>", mover_izquierda)
ventana.bind("<Right>", mover_derecha)
ventana.bind("<Up>", mover_arriba)
ventana.bind("<Down>", mover_abajo)

ventana.mainloop()