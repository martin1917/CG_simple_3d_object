import math
import numpy as np
import pygame as pg
import matrix_functions
import Consts


class Object3D:
    def __init__(self, scene, vertexes: list[list[float]], faces: list[list[int]]):
        self.vertexes = np.array([np.array(v) for v in vertexes])
        self.faces = np.array([np.array(f) for f in faces])
        self.scene = scene

    def draw(self):
        vertexes = self.vertexes @ self.scene.camera.camera_matrix()
        vertexes = vertexes @ matrix_functions.perspective_proj(10)
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes = vertexes @ matrix_functions.scale(20)
        vertexes = vertexes @ matrix_functions.to_screen()

        for face in self.faces:
            count_point = len(face)
            for i in range(count_point):
                num_point1 = face[i]
                num_point2 = face[(i+1) % count_point]
                point1, point2 = vertexes[num_point1], vertexes[num_point2]
                start_pos = (point1[0], point1[1])
                end_pos = (point2[0], point2[1])
                pg.draw.aaline(self.scene.screen, (255, 255, 255), start_pos, end_pos)
    
    def translate(self, dx, dy, dz):
        self.vertexes = self.vertexes @ matrix_functions.translate(dx, dy, dz)

    def scale(self, k):
        self.vertexes = self.vertexes @ matrix_functions.scale(k)

    def rotate_x(self, alpha):
        self.vertexes = self.vertexes @ matrix_functions.rotate_x(alpha)

    def rotate_y(self, alpha):
        self.vertexes = self.vertexes @ matrix_functions.rotate_y(alpha)

    def rotate_z(self, alpha):
        self.vertexes = self.vertexes @ matrix_functions.rotate_z(alpha)