#Sistema Backend de Gestão de Pátio.
patio = []
while True:
    print("===Sistema Backend de Gestão de Pátio.===:")
    print("Escolha uma opção:")
    print("[1] Registrar Entrada de Caminhão")
    print("[2] Consultar Status do Pátio")
    print("[3] Liberar Caminhão / Doca")
    print("[4] Encerrar Sistema")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == '1':
        print("\n--- REGISTRAR ENTRADA ---")
        placa = input("Digite a placa do caminhão: ").upper()
        motorista = input("Digite o nome do motorista: ")
        carga = input("Digite o tipo de carga: ")
        caminhao = {
            'placa': placa,
            'motorista': motorista,
            'carga': carga,
            'status': 'aguardando'
        }
        patio.append(caminhao)
        print("Caminhão registrado com sucesso!\n")

    elif opcao == '2':
        print("\n--- STATUS DO PÁTIO ---")
        if len(patio) == 0:
            print("O pátio está totalmente vazio.")
        else:
            for caminhao in patio:
                print(f"Placa: {caminhao['placa']} | Motorista: {caminhao['motorista']} | Carga: {caminhao['carga']} | Status: {caminhao['status']}")
        print("-----------------------\n")
    elif opcao == '3':
        print("\n--- LIBERAR CAMINHÃO ---")
        if len(patio) == 0:
            print("Não há caminhões no pátio para liberar.")
        else:
            placa_saida = input("Digite a placa do caminhão que está de saída: ").upper()
            caminhao_encontrado = False 
            for caminhao in patio:
                if caminhao['placa'] == placa_saida:
                    patio.remove(caminhao) 
                    print(f"Caminhão placa {placa_saida} liberado com sucesso!")
                    caminhao_encontrado = True
                    break 
            if caminhao_encontrado == False:
                print("Erro: Placa não localizada no pátio.")
    elif opcao == '4':
        print("Encerrando o sistema. Até mais!")
        break        
    else:
        print("Opção inválida. Por favor, tente novamente.")






                               
            
    
                               

        