#By Guilherme Freitas da Silva
#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salario "))
taxa = float(input("Digite a porcentagem do aumento "))
salario = salario + salario*taxa*0.01
print("Novo salario eh igual a ",salario)