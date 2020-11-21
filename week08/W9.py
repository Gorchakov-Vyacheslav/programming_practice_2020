import numpy as np


class vector():
    def __init__(self, *coordinates):
        # размер вектора
        # self.size = len(coordinates)
        self.vector = np.array(coordinates)

    # норма вектора
    def vector_norm():
        return np.linalg.norm(self.vector)

    # умножение вектора на число
    def scalar(self, r):
        return self.vector * r

    # сложение двух векторов
    def add_vectors(self, other):
        return self.vector + other.vector

    # скалярное произведения двух векторов
    def scalar_multiplication(self, other):
        return np.dot(self.vector, other.vector)

    # векторное произведение двух векторов
    def vector_multiplication():
        return np.cross(self.vector, other.vector)

    # расстояние между векторами
    def distance_between_vectors(self, other):
        return np.linalg.norm(self.vector - other.vector)

    # умножение вектора на матрицу
    def matrix_vector_multiply(self, matrix):
        return np.dot(self.vector, matrix)

    # является ли x решением уравнения Ax = b
    def solver(self, matrix, other):
        if (matrix_vector_multiply(self.vector, matrix) == other.vector):
            print("YES")
        else:
            print("NO")

    # проверка двух векторов на перпендикулярность
    def perpendicularity(self, other):
        if (scalar_multiplication(self.vector, other.vector) == 0):
            print("YES")
        else:
            print("NO")

    # угол между векторами
    def angle(self, other):
        return np.arccos(scalar_multiplication(self.vector, other.vector) / (norm(self.vector) * norm(other.vector)))