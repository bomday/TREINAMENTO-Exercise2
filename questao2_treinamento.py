x = int(input())
z = int(input())
h = pow(((x - 34)**2 + (z - 220)**2), 1/2)
k = pow(((x - 0)**2 + (z - 0)**2), 1/2)
s = pow(((x - 140)**2 + (z - 456)**2), 1/2) 
print(f"Distancia para Hogsmeade: {h:0.2f}")
print(f"Distancia para Kakariko: {k:0.2f}")
print(f"Distancia para Solitude: {s:0.2f}")