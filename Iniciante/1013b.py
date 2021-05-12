a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2

if c < maiorAB:
	print(f'{maiorAB} eh o maior')
else:
	print(f'{c} eh o maior')