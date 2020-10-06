from sympy import *
init_printing(use_unicode=True)
A = Matrix([[1, 3, -2, 1], [2, 5, -3, 2], [-1, 2, -1, 3]])
B = Matrix([[1, 2], [1/2, 3]])
C = Matrix([[-1, 0], [2, 5], [0, 3]])

A = Matrix([[3, 1], [5, 2]])
X = Matrix([[3, 5], [-8, -13]])


V = Matrix([[1/4, 0], [0, 1]])
V_2 = Matrix([[1, -2], [0, 1]])
A = Matrix([[4, 2], [0, 1]])
I = eye(2)
P = Matrix([[1, 1, 1, 1, 1], [1, 2, 1, 1, 1], [
           1, 1, 3, 1, 1], [1, 1, 1, 4, 1], [1, 1, 1, 1, 5]])


print(V*V_2*A)
print(A.inverse_ADJ())
print(V*V_2*I)
print(P.det())
