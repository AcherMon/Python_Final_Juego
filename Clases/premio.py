class premio:
    def __init__(self, canvas, nombre, x, y):
        self.canvas = canvas
        self.nombre = nombre
        self.x = x
        self.y = y
        self.color = "#d6a802"

    def dibujar (self):
        radio = 20
        x1, y1 = self.x - radio, self.y - radio
        x2, y2 = self.x + radio, self.y + radio
        self.id_dibujo = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="black")

    def spawn (self, spawn_x, spawn_y):
        dx = spawn_x - self.x
        dy = spawn_y - self.y
        self.canvas.move(self.id_dibujo, dx, dy)
        self.x = spawn_x
        self.y = spawn_y
