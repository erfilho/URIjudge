a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

maiorAB = int((a+b+abs(a-b))/2)
maiorAB = int((maiorAB + c + abs(maiorAB-c))/2)

print(f'{maiorAB} eh o maior')