# Sistema Backend de Gestão de Pátio Logístico
## Descrição
Desenvolvimento de uma aplicação backend em Python (via terminal) para automatizar e registrar o fluxo de carga e descarga em uma transportadora. O projeto aplica a lógica de programação estruturada para resolver regras de negócio reais do setor logístico.

## Funcionalidades (CRUD em Memória)
* **Registrar Entrada:** Captura placa, motorista e tipo de carga, padronizando os dados e atribuindo o status de "Aguardando".
* **Consultar Status:** Lista em tempo real todos os veículos alocados no pátio através de formatação de strings (f-strings).
* **Liberar Caminhão:** Sistema de busca e remoção de dados da memória com base na placa do veículo, incluindo tratamento de erros para placas inexistentes.

## Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Estruturas de Dados:** Listas e Dicionários
* **Controle de Fluxo:** Laços de repetição (`while`, `for`) e Estruturas Condicionais (`if/elif/else`).

## Como Executar
Basta rodar o arquivo `main.py` em qualquer terminal com Python instalado.
