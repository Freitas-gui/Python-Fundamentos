#By Guilherme Freitas da Silva
#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

c = float(input("Digite o valor em graus Celsius: "))
f = (9*(c/5)) + 32
print("O valor em Fahrenheit eh igual a: %.2f"%f)