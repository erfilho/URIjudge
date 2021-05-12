from math import pow

a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

a_tri = (a*c)/2
pi = 3.14159
a_circ = pi*pow(c,2)
a_trap = ((a+b)*c)/2
a_quad = pow(b, 2)
a_retan = a*b

print(f'TRIANGULO: {a_tri:.3f}\nCIRCULO: {a_circ:.3f}\nTRAPEZIO: {a_trap:.3f}\nQUADRADO: {a_quad:.3f}\nRETANGULO: {a_retan:.3f}')