from BaseComplexObject3D import BaseComplexObject3D
from Object3D import Object3D


class Robot(BaseComplexObject3D):
    def __init__(self, scene):
        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 4, 7, 3],
            [1, 5, 6, 2],
            [0, 1, 5, 4],
            [3, 2, 6, 7]
        ]

        self.leftneg = Object3D(scene, [
            [-5, -14, 2, 1],
            [-5, -6, 2, 1],
            [-1, -6, 2, 1],
            [-1, -14, 2, 1],
            [-5, -14, -2, 1],
            [-5, -6, -2, 1],
            [-1, -6, -2, 1],
            [-1, -14, -2, 1]
        ], faces)

        self.rightneg = Object3D(scene, [
            [1, -14, 2, 1],
            [1, -6, 2, 1],
            [5, -6, 2, 1],
            [5, -14, 2, 1],
            [1, -14, -2, 1],
            [1, -6, -2, 1],
            [5, -6, -2, 1],
            [5, -14, -2, 1],
        ] , faces)

        self.body = Object3D(scene, [
            [-5, -6, 2, 1],
            [-5, 6, 2, 1],
            [5, 6, 2, 1],
            [5, -6, 2, 1],
            [-5, -6, -2, 1],
            [-5, 6, -2, 1],
            [5, 6, -2, 1],
            [5, -6, -2, 1],
        ], faces)
               
        self.leftarm = Object3D(scene, [
            [-7, 0, 2, 1],
            [-7, 6, 2, 1],
            [-5, 6, 2, 1],
            [-5, 0, 2, 1],
            [-7, 0, -2, 1],
            [-7, 6, -2, 1],
            [-5, 6, -2, 1],
            [-5, 0, -2, 1],
        ], faces)

        self.rightarm = Object3D(scene, [
            [5, 0, 2, 1],
            [5, 6, 2, 1],
            [7, 6, 2, 1],
            [7, 0, 2, 1],
            [5, 0, -2, 1],
            [5, 6, -2, 1],
            [7, 6, -2, 1],
            [7, 0, -2, 1],
        ], faces)
              
        self.neck = Object3D(scene, [
            [-1, 6, 2, 1],
            [-1, 8, 2, 1],
            [1, 8, 2, 1],
            [1, 6, 2, 1],
            [-1, 6, -2, 1],
            [-1, 8, -2, 1],
            [1, 8, -2, 1],
            [1, 6, -2, 1],
        ], faces)
            
        self.head = Object3D(scene, [
            [-3, 8, 2, 1],
            [-3, 14, 2, 1],
            [3, 14, 2, 1],
            [3, 8, 2, 1],
            [-3, 8, -2, 1],
            [-3, 14, -2, 1],
            [3, 14, -2, 1],
            [3, 8, -2, 1],
        ], faces)
        
        self.parts = [
            self.head,
            self.neck,
            self.body,
            self.leftarm,
            self.rightarm,
            self.leftneg,
            self.rightneg
        ]