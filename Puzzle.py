


for A in range(1, 10):
    for B in range(1, 10):
        for C in range(1, 10):
            concat = (A * 100) + (B * 10) + C
            if concat/5 == (A*B*C):
                print(str(A) + str(B) + str(C))