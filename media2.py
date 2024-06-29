#Media com 3 notas

#Variáveis / Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#Início / Processamento
media = ( nota1 + nota2 + nota3 ) / 3

if media >= 15:
    print("Aprovado") # Saída
else:
    print('Reprovado') # Saída
#Fim
