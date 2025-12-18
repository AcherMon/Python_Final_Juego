class Personaje:
    def __init__(self, canvas, nombre, x, y):
        self.canvas = canvas
        self.nombre = nombre
        self.x = x
        self.y = y
        self.color = "#5a636e"
        self.id_cuerpo = None
        self.id_ojo = None

    def dibujar(self):
        # dibujar el cuerpo
        cuerpo_base = 10
        cuerpo_altura = 25
        x1, y1 = self.x - cuerpo_base, self.y - cuerpo_altura
        x2, y2 = self.x + cuerpo_base, self.y + cuerpo_altura
        self.id_cuerpo = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline="black")

        # dibujar el ojo
        visor_alto = 5
        ox1 = x1
        ox2 = x2
        oy1 = y1 + 8
        oy2 = oy1 + visor_alto
        self.id_ojo = self.canvas.create_rectangle(ox1, oy1, ox2, oy2, fill="blue", outline="black")

    def mover(self, dx, dy):
        # epic movement from Mr.P
        if(self.x>=800):
            self.x=1
        self.canvas.move(self.id_cuerpo, dx, dy)
        self.canvas.move(self.id_ojo, dx, dy)
        self.x += dx
        self.y += dy




