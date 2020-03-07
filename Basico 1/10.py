#By Guilherme Freitas da Silva
# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite a quantidade de anos que fumou: "))
dias = ((10*0.6)/24) * (cigarros*anos*365)
print ("A quantidade de dias perdido eh igual a: ",dias)