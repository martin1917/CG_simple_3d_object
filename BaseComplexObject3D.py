class BaseComplexObject3D():
    def __init__(self):
        self.parts = None

    def draw(self):
        for part in self.parts:
            part.draw()
    
    def translate(self, dx, dy, dz):
        for part in self.parts:
            part.translate(dx, dy, dz)

    def scale(self, k):
        for part in self.parts:
            part.scale(k)

    def rotate_x(self, alpha):
        for part in self.parts:
            part.rotate_x(alpha)

    def rotate_y(self, alpha):
        for part in self.parts:
            part.rotate_y(alpha)

    def rotate_z(self, alpha):
        for part in self.parts:
            part.rotate_z(alpha)