a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorABC = (maiorAB+c+abs(maiorAB-c))/2

print(f'{maiorABC} eh o maior')