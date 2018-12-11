# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print()
print("""Selecione o número da operação desejada:

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão""")
print()
opcao = int(input("Digite sua opção (1/2/3/4): "))
print()
primeiro = int(input("Digite o primeiro número: "))
print()
segundo = int(input("Digite o segundo número: "))
print()
if opcao not in (1, 2, 3, 4):
    print("Opção Inválida!")
elif opcao == 1:
    resultado = primeiro + segundo
    print("{} {} {} = {}".format(primeiro, '+', segundo, resultado))
elif opcao == 2:
    resultado = primeiro - segundo
    print("{} {} {} = {}".format(primeiro, '-', segundo, resultado))
elif opcao == 3:
    resultado = primeiro * segundo
    print("{} {} {} = {}".format(primeiro, '*', segundo, resultado))
elif opcao == 4:
    resultado = primeiro / segundo
    print("{} {} {} = {}".format(primeiro, '/', segundo, resultado))