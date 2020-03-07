#By Guilherme Freitas da Silva
#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

mercadoria = float(input("Digite o valor da mercadoria "))
desconto = float(input("Digite a porcentagem de desconto "))
preco = mercadoria - mercadoria*desconto*0.01
print("o preco da mercadoria com o desconto aplicado eh igual a ",preco)