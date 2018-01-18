import sympy

K = sympy.Matrix([[6, 24, 1],
                 [13, 16, 10],
                 [20, 17, 15]])
print(K.inv_mod(26))
