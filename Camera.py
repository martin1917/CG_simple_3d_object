import numpy as np
import pygame as pg
import matrix_functions

class Camera:
    def __init__(self, scene, position):
        self.scene = scene
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.right = np.array([1, 0, 0, 1])
        self.up = np.array([0, 1, 0, 1])
        self.moving_speed = 0.3
        self.rotate_speed = 0.5
    
    def handle_key_pressed(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if keys[pg.K_d]:
            self.position += self.right * self.moving_speed
        if keys[pg.K_q]:
            self.position -= self.up * self.moving_speed
        if keys[pg.K_e]:
            self.position += self.up * self.moving_speed
        if keys[pg.K_w]:
            self.position -= self.forward * self.moving_speed
        if keys[pg.K_s]:
            self.position += self.forward * self.moving_speed

        if keys[pg.K_LEFT]:
            self.camera_yaw(-self.rotate_speed)
        if keys[pg.K_RIGHT]:
            self.camera_yaw(self.rotate_speed)
        if keys[pg.K_UP]:
            self.camera_pitch(-self.rotate_speed)
        if keys[pg.K_DOWN]:
            self.camera_pitch(self.rotate_speed)
    
    def camera_pitch(self, angle):
        rotate = matrix_functions.rotate_x(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_yaw(self, angle):
        rotate = matrix_functions.rotate_y(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate
    
    def translate(self):
        x, y, z, _ = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])
    
    def rotate(self):
        rx, ry, rz, _ = self.right
        fx, fy, fz, _ = self.forward
        ux, uy, uz, _ = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.translate() @ self.rotate()