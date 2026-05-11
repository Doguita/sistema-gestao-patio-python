#tabuada
'''num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")'''
#senha
'''senha_correta = "obene123"
while True:
    tentativas = 3
    senha = input("Digite a senha: ")
    tentativas -= 1
    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")'''

#CALCULADORA
'''def calculadora():
    while True:
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora. Até mais!")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Por favor, tente novamente.")'''
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(70, 1.75)
print(f"Seu IMC é: {imc:.2f}")