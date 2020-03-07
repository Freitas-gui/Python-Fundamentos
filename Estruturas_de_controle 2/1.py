#By Guilherme Freitas da Silva
# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

a = float(input("Digite o primeiro lado do triangulo: "))
b = float(input("Digite o segundo lado do triangulo: "))
c = float(input("Digite o terceiro lado do triangulo: "))
if( (b-c < a < b+c and a-c < b < a+c and a-b < c < a+b) == 0):
    print("nao eh um triangulo, valores invalidos")
elif(a==b and b==c):
    print("triangulo equilatero")
elif(a==b or b==c or a==c):
    print("triangulo isoceles")
else:
    print("triangulo escaleno")
