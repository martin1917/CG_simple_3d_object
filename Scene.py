import pygame as pg
from Camera import Camera
from Robot import Robot
import Consts

class Scene:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Consts.WIDTH, Consts.HEIGHT))
        self.clock = pg.time.Clock()
        self.camera = Camera(self, [1, 1, 0])
        self.objects = []
        self.create_objects()
    
    def create_objects(self):
        self.objects.append(Robot(self))

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        [obj.draw() for obj in self.objects]

    def run(self):
        while True:
            self.clock.tick(Consts.FPS)
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            self.draw()
            self.camera.handle_key_pressed()
            pg.display.flip()