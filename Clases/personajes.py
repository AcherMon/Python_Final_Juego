class Personaje:
    def __init__(self, canvas, nombre, x, y):
        self.canvas = canvas
        self.nombre = nombre
        # Atributos encapsulados (datos del objeto)
        self.x = x
        self.y = y
        self.color = "#5a636e"  # Color por defecto
        self.id_cuerpo = None
        self.id_ojo = None

    def dibujar(self):
        # Dibujo el cuerpo
        cuerpo_base=10
        cuerpo_altura=25
        x1, y1 = self.x - cuerpo_base, self.y - cuerpo_altura
        x2, y2 = self.x + cuerpo_base, self.y + cuerpo_altura

        self.id_cuerpo = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline="black")

        # Dibujo el ojo
        ojo_base=10
        ojo_altura=5

        ox1, oy1 = self.x - cuerpo_base, self.y - cuerpo_altura
        ox2, oy2 = self.x + cuerpo_base, self.y + cuerpo_altura
