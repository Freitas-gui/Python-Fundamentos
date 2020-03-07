#By Guilherme Freitas da Silva
#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
#Calcule o total em segundos.

d = int(input("Digite a quantidade de dias "))
h = int(input("Digite a quantidade de horas "))
m = int(input("Digite a quantidade de minutos "))
s = int(input("Digite a quantidade de segundos "))
s = s + (d*24*60*60) + (h*60*60) + (m*60)
print ("total em segundos eh igual ",s)