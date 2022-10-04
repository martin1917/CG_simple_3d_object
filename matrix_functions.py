import math
import numpy as np
import Consts

def translate(dx, dy, dz):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [dx, dy, dz, 1],
    ])

def scale(k):
    return np.array([
        [k, 0, 0, 0],
        [0, k, 0, 0],
        [0, 0, k, 0],
        [0, 0, 0, 1],
    ])

def rotate_x(a):
    a = math.radians(a)
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0],
        [0, -math.sin(a), math.cos(a), 0],
        [0, 0, 0, 1],
    ])

def rotate_y(a):
    a = math.radians(a)
    return np.array([
        [math.cos(a), 0, -math.sin(a), 0],
        [0, 1, 0, 0],
        [math.sin(a), 0, math.cos(a), 0],
        [0, 0, 0, 1],
    ])

def rotate_z(a):
    a = math.radians(a)
    return np.array([
        [math.cos(a), math.sin(a), 0, 0],
        [-math.sin(a), math.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

def perspective_proj(z_center):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -1/z_center],
        [0, 0, 0, 1],
    ])

def isometric_proj(y_sign = -1, x_sign = 1):
    m11, m12, m22, m31, m32 = 0.707, 0.408, 0.816, 0.707, 0.408
    m12 = m12 if (y_sign * x_sign > 0) else -m12
    m31 = m31 if y_sign > 0 else -m31
    m32 = m32 if x_sign < 0 else -m32
    return np.array([
        [m11, m12, 0, 0],
        [0, m22, 0, 0],
        [m31, m32, 0, 0],
        [0, 0, 0, 1],
    ])

def oblique_proj(type, a):
    if type == "kavalye":
        return __oblique_projection(1, a)
    if type == "kabine":
        return __oblique_projection(0.5, a)

def __oblique_projection(f, a):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [-f*math.cos(a), -f*math.sin(a), 0, 0],
        [0, 0, 0, 1],
    ])

def to_screen():
    return np.array([
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, 0, 0],
    [Consts.CENTER_X, Consts.CENTER_Y, 0, 1]
])