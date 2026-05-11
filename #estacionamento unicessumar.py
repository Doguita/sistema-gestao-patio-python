# Sistema UniCesumar Parking
# Aluno: [Seu Nome]

import math

# variaveis que guardam os dados do dia
total = 0.0
isentos = 0
motos = 0
carros = 0
camionetes = 0

# lista que guarda os veiculos registrados
veiculos_registrados = []

# funcao que calcula o valor a pagar
def calcular(minutos):
    if minutos <= 15:
        return 0.0
    elif minutos <= 60:
        return 1.50
    else:
        horas_extras = math.ceil((minutos - 60) / 60)
        return 1.50 + horas_extras * 1.0

# funcao que registra um veiculo
def registrar():
    global total, isentos, motos, carros, camionetes

    print("\n1-Moto  2-Carro  3-Camionete")
    tipo = input("Tipo: ")

    if tipo == "1":
        nome = "Motocicleta"
        motos += 1
    elif tipo == "2":
        nome = "Carro de passeio"
        carros += 1
    elif tipo == "3":
        nome = "Camionete"
        camionetes += 1
    else:
        print("Tipo invalido!")
        return

    # cadastra a placa do veiculo
    placa = input("Placa do veiculo: ").upper()

    # pega os horarios
    he = int(input("Hora entrada: "))
    me = int(input("Minuto entrada: "))
    hs = int(input("Hora saida: "))
    ms = int(input("Minuto saida: "))

    # calcula permanencia em minutos
    permanencia = (hs * 60 + ms) - (he * 60 + me)

    if permanencia < 0:
        print("Horario invalido!")
        return

    valor = calcular(permanencia)
    total += valor

    if valor == 0:
        isentos += 1
        situacao = "ISENTO"
    else:
        situacao = f"R$ {valor:.2f}"

    # salva o registro na lista
    veiculos_registrados.append({
        "placa": placa,
        "tipo": nome,
        "entrada": f"{he:02d}h{me:02d}",
        "saida": f"{hs:02d}h{ms:02d}",
        "permanencia": permanencia,
        "valor": situacao
    })

    # exibe comprovante
    print("\n--- COMPROVANTE ---")
    print(f"Placa      : {placa}")
    print(f"Tipo       : {nome}")
    print(f"Entrada    : {he:02d}h{me:02d}")
    print(f"Saida      : {hs:02d}h{ms:02d}")
    print(f"Permanencia: {permanencia} min")
    print(f"Valor      : {situacao}")

# funcao que lista todos os veiculos registrados
def listar_veiculos():
    if len(veiculos_registrados) == 0:
        print("Nenhum veiculo registrado ainda.")
        return
    print("\n--- VEICULOS REGISTRADOS ---")
    for v in veiculos_registrados:
        print(f"Placa: {v['placa']} | Tipo: {v['tipo']} | Entrada: {v['entrada']} | Saida: {v['saida']} | Valor: {v['valor']}")

# menu principal
print("=== UniCesumar Parking ===")

while True:
    print("\n1-Registrar veiculo")
    print("2-Veiculos por tipo")
    print("3-Total arrecadado")
    print("4-Veiculos isentos")
    print("5-Listar todos os veiculos")
    print("6-Sair")

    op = input("Opcao: ")

    if op == "1":
        registrar()
    elif op == "2":
        print(f"Motos: {motos}")
        print(f"Carros: {carros}")
        print(f"Camionetes: {camionetes}")
    elif op == "3":
        print(f"Total: R$ {total:.2f}")
    elif op == "4":
        print(f"Isentos: {isentos}")
    elif op == "5":
        listar_veiculos()
    elif op == "6":
        print("Encerrando...")
        break
    else:
        print("Opcao invalida!")