#By Guilherme Freitas da Silva
#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 

d = int(input("Digite a distancia a ser percorrida: "))
v = int(input("Digite a velocidade media da viagem: "))
t = d/v
print("O tempo estimado eh igual a %.2f"%t)