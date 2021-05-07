cpi, npi, vupi = input().split(" ")
cpii, npii, vupii = input().split(" ")

cpi = int(cpi)
npi = int(npi)
vupi = float(vupi)

cpii = int(cpii)
npii = int(npii)
vupii = float(vupii)

vtotali = (npi * vupi) + (npii * vupii)
print(f'VALOR A PAGAR: R$ {vtotali:.2f}')
