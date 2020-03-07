#By Guilherme Freitas da Silva
#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

valor = str(2 ** 1000000)
qntDigitos = len(valor)
print("2 elevado a um milhão possui %d digitos",qntDigitos)