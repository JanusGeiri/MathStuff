from sympy import *
init_printing(use_unicode=True)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
A = Matrix([[1, 2, 1], [0, 1, 1], [0, 0, 4], [0, 0, 0]])
print(A.rref())
=======
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
>>>>>>> parent of 5f97061... 1
=======
A = Matrix([[1, -1, 1], [1, -1, 0], [0, 0, 0]])
print(A.rref())
print(A**2)
print(A**3)
print(A.rank(), (A**3).rank())
>>>>>>> parent of 1f9c072... 26.11.2020
=======
A = Matrix([[1, 2, 1], [0, 1, 1], [0, 0, 4], [0, 0, 0]])
print(A.rref())
>>>>>>> parent of f43f239... 66
=======
A = Matrix([[1, -1, 1], [1, -1, 0], [0, 0, 0]])
print(A.rref())
print(A**2)
print(A**3)
print(A.rank(), (A**3).rank())
>>>>>>> parent of 1f9c072... 26.11.2020
