# Funções para funcionamento do sistema

# para tratamento da data e hora
from datetime import datetime

# lista de todas as linhas cadastradas
linhas_cadastradas = []

# reservas não concluidas
reservas_nao_realizadas = []

# inicia o total vendido como zero
total_vendas = 0.0

# dias da semana
dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

# número de assentos
ASSENTOS_TOTAIS=20


# garantir que a entrada nao seja null ou entrada vazia
def input_nao_vazio(msg):
    """
    Garante que o input não aceite null ou conteúdo vazio
    """

    while True:
        
        # faz o input
        valor = input(msg).strip()

        # se o valor for vazio
        if valor == "":
            # mostra o print e ele solicita novamente a resposta
            print("Entrada inválida! O campo não pode estar vazio.")

        # se estiver tudo certo, ele implementa
        else:
            return valor


# garantir que a entrada seja float
def input_float(msg):
    """
    Garante que o input não aceite vazio e só aceite float
    """

    while True:

        # aceita valores separados com ,
        #transforma em .
        valor = input(msg).strip().replace(",", ".")

        # verifica se está vazio
        if valor == "":
            print("Entrada inválida! O campo não pode estar vazio.")
            continue
        
        # tenta transformar em float
        try:
            return float(valor)
        
        # se der erro, ele pede novamente
        except ValueError:
            print("Valor inválido! Digite um número ;)")


# mostra o menu (principal) para escolha da ação 
def menu():
    """Menu para escolha da ação"""

    print(f"\n--- MENU ---\n")
    print(f"1 - Inserir linha")
    print(f"2 - Remover linha")
    print(f"3 - Alterar linha")
    print(f"4 - Consultar horarios para uma determinada cidade")
    print(f"5 - Consultar assentos disponiveis")
    print(f"6 - Gerar relatórios")
    print(f"7 - Ler reserva de um arquivo")
    print(f"8 - Mostrar as reservas que não puderam ser realizadas")
    print(f"9 - Mostrar todas as linhas")
    print(f"0 - Sair")


# mostrar as linhas e onibus cadastrados
def mostrar_linhas():

    """
    Mostra as linhas cadastradas e seus respectivos ônibus
    """
    
    print ("\n--- LINHAS CADASTRADAS ---\n")

    # se a lista de linhas cadastrada estiver vazia
    if not linhas_cadastradas:

        print("Nenhuma linha cadastrada ainda :(\n")
        return
    

    # lista todas as linhas_cadastradas
    for i, linha in enumerate (linhas_cadastradas):

        print(f"Linha {i+1}:")
        print(f"{linha['cid_origem']} para {linha['cid_destino']}")
        print(f"Horarios: {', '.join(linha['horario'])}")
        print(f"Valor da passagem: R${linha['valor']}")
        
        print(f"\n  Ônibus cadastrados: \n")

        if not linha['partidas']:
            
            print("    Nenhum ônibus cadastrado ainda :(\n")

        else:

            for j, onibus in enumerate(linha['partidas']):
                
                assentos = onibus['assentos']
                livres = contar_assentos_livres(onibus['assentos'])
                ocupados = len(assentos) - livres
                
                print(f"    Ônibus {j+1}:")
                print(f"    Data da partida: {onibus['data']}")
                print(f"    Horario: {onibus['horario']}")
                print(f"    Assentos livres: {livres}")
                print()

        
        print()


# criar 20 assentos
def criar_assento():
    """Cria a matriz de assentos vazios para o ônibus"""
    assentos = [['1',  '2',  '|  |', '4',  '3'],
                ['5',  '6',  '|  |', '8',  '7'],
                ['9', '10', '|  |', '12', '11'],
                ['13','14', '|  |', '16','15'],
                ['17','18', '|  |', '20','19']]
    # 20 assentos livre por ônibus
    return assentos


def contar_assentos_livres(assentos):
    """Conta assentos disponíveis (não marcados com X)."""
    return sum(1 for linha in assentos for a in linha if a.isdigit() and a != 'X')


# marcar os assentos vendidos (ocupados -> X)
def marcar_assento(onibus, valor):

    """
    Marcar os assentos vendidos (ocupados -> X)
    
    :param onibus: onibus analizado
    :param valor: número do assento
    """

    # percorre a matriz toda procurando o assento escolhido (valor)
    for i, linha in enumerate(onibus['assentos']):

        for j, item in enumerate(linha):

            if item == valor:

                # troca o valor encontrado por X (ocupado)
                onibus['assentos'][i][j] = "X"   
                # retorna True se achou e marcou que foi ocupado
                return True 

    # retorna False se alguma etapa falhar         
    return False


# verifica se o ônibus ainda tem assentos vazios
def existem_assentos_vazios(onibus):

    """
    Verifica se o ônibus ainda tem assentos vazios
    """

    # busca pela matriz o assento
    for linha in onibus['assentos']:

        for item in linha:

            # se achar um número então o assento está vazio
            if item.isdigit():   

                # retorna True se estiver vazio
                return True
            
    # retorna False se estiver ocupado (X)
    return False


# mostra o mapa de assentos do ônibus
def mostrar_mapa_assentos(ônibus):
        
        """
        Mostra o mapa de assentos do ônibus
        """
        
        print("Mapa do ônibus:\n")
        
        # mostra o mapa com os assentos 
        for linha in ônibus['assentos']: 

            print("  ".join(linha))


# efetuar a venda do assento 
# -> aumenta o total recebido da linha
# -> registra a venda para relatórios futuros
# -> OPCIONAL - escreve no arquivo de relatorios
def fazer_venda(linha):
    """
    efetuar a venda do assento 
    
    -> aumenta o total recebido da linha
    -> registra a venda para relatórios futuros
    -> OPCIONAL - escreve no arquivo de relatorios
    """

    # registra data da venda (hoje)
    data_venda = datetime.now()

    valor_passagem = float(linha['valor'])

    # acumula total na linha
    linha['valor recebido'] += valor_passagem

    # registra venda para relatórios futuros
    linha['vendas'].append({
        "data": data_venda,
        "valor": valor_passagem
    })

    # escreve no arquivo (opcional)
    with open("relatorioVenda.txt", "a", encoding="utf8") as arq:
        arq.write("\nVenda realizada:\n")
        arq.write(f"Data da venda: {data_venda.strftime('%d/%m/%Y %H:%M')}\n")
        arq.write(f"Origem: {linha['cid_origem']}\n")
        arq.write(f"Destino: {linha['cid_destino']}\n")
        arq.write(f"Valor: R${valor_passagem:.2f}\n")
        arq.write("---------------------------------------\n")


# apresenta o relatorio de vendas do mes corrente
def relatorio_vendas_mes_corrente():

    """
    Apresenta o relatorio de vendas do mes corrente
    """

    hoje = datetime.now()
    mes = hoje.month
    ano = hoje.year

    texto = "\n--- RELATÓRIO DE VENDAS DO MÊS CORRENTE ---\n\n"

    for linha in linhas_cadastradas:
        total_mes = sum(
            venda["valor"]
            for venda in linha['vendas']
            if venda["data"].month == mes and venda["data"].year == ano
        )

        texto += f"Linha: {linha['cid_origem']} → {linha['cid_destino']}\n"
        texto += f"Total arrecadado: R${total_mes:.2f}\n"
        texto += "-----------------------------------------\n"

    salvar_ou_exibir(texto)


# apresenta o relatorio de ocupação por dia da semana
def ocupacao_por_dia_semana():

    """Apresenta o relatorio de ocupação por dia da semana"""


    texto = "\n--- OCUPAÇÃO POR DIA DA SEMANA ---\n\n"

    for linha in linhas_cadastradas:
        matriz = [0] * 7
        vendas_por_dia = [0] * 7

        for venda in linha["vendas"]:
            vendas_por_dia[venda["data"].weekday()] += 1

        for i in range(7):
            if vendas_por_dia[i] > 0:
                matriz[i] = round((vendas_por_dia[i] / ASSENTOS_TOTAIS) * 100, 2)

        texto += f"Linha: {linha['cid_origem']} → {linha['cid_destino']}\n"
        for i in range(7):
            texto += f"{dias_semana[i]}: {matriz[i]}%\n"
        texto += "----------------------------------------\n"

    salvar_ou_exibir(texto)


# mostra as opções e o usuario faz a escolha de relatorio a ser apresentado
def gerar_relatorios():
    
    """
    mostra as opções e o usuario faz a escolha de relatorio a ser apresentado
    """

    print("\n1 - Total arrecadado por linha no mês atual")
    print("2 - Ocupação média por dia da semana")
    print("0 - Voltar")
 
    op = int(input("Escolha: "))

    if op == 1:
        relatorio_vendas_mes_corrente()
    elif op == 2:
        ocupacao_por_dia_semana()


# vender os assentos de determinado ônibus
def vender_assentos(onibus,linha_onibus):
    
    """
    vender os assentos de determinado ônibus
    """

    vendendo=0 #variavel limite do while
    while vendendo==0:
        encontrou=False

        if existem_assentos_vazios(onibus): # confere se é possivel comprar assentos desse onibus 
            print(f'\n--- MAPA DOS ASSENTOS DO ÔNIBUS ---\n')
            print(f'OS QUE ESTÃO MARCADOS COM "X" ESTÃO OCUPADOS:') #explica que os lugares marcados pelo X ja estao ocupados
            mostrar_mapa_assentos(onibus)
            assento=(input('\nDigite o número do assento desejado:   ')).strip()
            for linha in onibus['assentos']: #procura o assento da pessoa pelo numero digitado , como string
                if assento in linha and assento != 'X':

                    encontrou = True
                    break
        
            if encontrou:
                    print("\nAssento reservado para você")  
                    fazer_venda(linha_onibus)
                    marcar_assento(onibus,assento)  #se encontrar o assento como livre ele passa a estar ocupado
                    mostrar_mapa_assentos(onibus)
                    print('--------------------------------------------------')
                    vendendo=int(input('\nDigite 0 se ainda deseja comprar outro assento (para sair digite qualquer outro caracter): '))

            else:
                print("\nAssento não está disponível")
                registrar_reserva_nao_realizada(f'{linha_onibus['cid_origem']} para {linha_onibus['cid_destino']}, Data: {onibus['data']}, {assento}', "Assento não está disponível")
                vendendo=int(input('\nSe dejesa tentar comprar outro assento digite 0 (para sair digite qualquer outro caracter): '))
        else:
            print('\nESSE ÔNIBUS POSSUI TODOS OS ASSENTOS OCUPADOS')
            vendendo=1


# cria o dicionario ônibus
def criar_onibus(data_partida, horario):
    
    """Cria o ônibus de cada linha"""

    # dicionario ônibus
    ônibus = {

        # data fornecida do ônibus
    
        'data': data_partida,
        # horario do ônibus
    
        'horario': horario,
        # criar 20 assentos (padrão)
        'assentos': criar_assento()


    }


    return ônibus


# cria o dicionario linha
# -> horario é uma lista de horarios para aquela linha
# -> partida é uma lista de ônibus daquela linha
def criar_linha(cid_origem, cid_destino, valor):


    """
    Cria a linha
    
    -> horario é uma lista de horarios para aquela linha
    -> partida é uma lista de ônibus daquela linha
    -> vendas é uma lista de vendas realizadas para aquela linha
    """

    # dicionario linha
    linha = {

        # cidade de origem
        'cid_origem': cid_origem,
        # cidade destino
        'cid_destino': cid_destino,
        # horario da saida
        'horario': [],
    
        # valor da passagem
        'valor': valor,
        # criar lista de ônibus
        'partidas': [],
        # lista de vendas
        'vendas': [],
        # valor total recebido
        'valor recebido': 0

    }


    return linha


# valida se o formato da hora inserida é valido
# -> hh:mm
# -> 0 <= hora <= 23
# -> 0 <= minuto <= 59
def validar_hora(horario_str):
    
    """
    valida se o formato da hora inserida é valido

    -> hh:mm
    -> 0 <= hora <= 23
    -> 0 <= minuto <= 59
    """

    try:
        # tamanho deve ser 5
        if len(horario_str) != 5:
            return False

        # deve ter ":" na posição 2
        if horario_str[2] != ":":
            return False

        h, m = horario_str.split(":")

        # hora e minuto precisam ter 2 dígitos
        if len(h) != 2 or len(m) != 2:
            return False

        hora = int(h)
        minuto = int(m)

        return (0 <= hora <= 23) and (0 <= minuto <= 59)
    
    except:
        return False


# valida se o formato do dia está certo e se o dia existe
# -> dd/mm/aaaa
def validar_data(data_str):
    
    """
    valida se o formato do dia está certo e se o dia existe

    -> dd/mm/aaaa
    """

    try:

        dia, mes, ano = map(int, data_str.split("/"))

        # verifica se a data existe
        datetime(ano, mes, dia)

        # se a data existir e estiver no formato certo, vai retornar True
        return True

    except:

        # se der errado alguma etapa retorna False
        return False
    

# verifica se a data e hora do ônibus esta no passado
def data_hora_valida(data_str, horario_str):
    
    """
    verifica se a data e hora do ônibus esta no passado
    """

    try:

        # formata a data e horario
        dia, mes, ano = map(int, data_str.split("/"))
        hora, minuto = map(int, horario_str.split(":"))

        # data+horario do ônibus e data+hora de agora
        data_onibus = datetime(ano, mes, dia, hora, minuto)
        agora = datetime.now()

        # se a data+hora do ônibus estiver no futuro, ou seja, depois da data+hora de agora, ele retorna True
        return data_onibus >= agora
    
    except:

        # se qualquer etapa der errado ele retorna False
        return False
    

# adicionar horario
def adicionar_horario(linha, horario):

    """Adicionar o horario na lista de horarios da linha"""

    linha['horario'].append(horario)
    print(f"\nO horario foi adicionado ({horario}) :D \n")


# adicionar ônibus na lista de ônibus da linha.
# -> verifica a validade da d
#ata [validar_data()]
# -> verifica se a data+hora está no futuro [data_hora_valida()]
def adicionar_onibus_linha(linha):
    

    """
    adicionar ônibus na lista de ônibus da linha.

    -> verifica a validade da data [validar_data()]
    -> verifica se a data+hora está no futuro [data_hora_valida()]
    """

    print("\n --- CADASTRANDO ONIBUS ---\n")
    
    print("Opções de horarios: ")

    # lista os horarios cadastrados para a linha
    for i, horario, in enumerate (linha['horario']):
        print(f"{i+1} - {horario}")

    
    # escolhe o horario cadastrado
    try:

        escolha = int(input("\nDigite o número do horário: "))

    # caso de entrada invalida
    except ValueError:

        print("\nEntrada inválida. Digite um número")
        return
    
    # caso de opção invalida
    if (escolha < 1) or (escolha > len(linha['horario'])):

        print("\nOpção inválida! Digite outra ;)")
        return
    
    # implementa o horario escolhido no dicionario ônibus
    idx = escolha - 1
    horario = linha['horario'][idx]


    # verificando se a data é valida

    while True:

        data_partida = input("\nDigite a data de partida do ônibus (dd/mm/aaaa): ")

        # se a data for valida e a data+hora estiver no futuro, ele sai do loop
        if validar_data(data_partida):

            if data_hora_valida(data_partida, horario):

                novo_onibus = criar_onibus(data_partida, horario)
                linha['partidas'].append(novo_onibus)

                print(f"\nOnibus criado com sucesso!")
                print(f"Linha: {linha['cid_origem']} para {linha['cid_destino']}")
                print(f"Data: {data_partida}")
                print(f"Horario: {horario}")

                break

            else:

                print("\nA data+hora está no passado. Tente outra ;)")

        else:

            print("\nA data é invalida! Tente novamente (dd/mm/aaaa) ;)")

        
# inserir os dados a uma nova linha (criar uma linha)
# -> cria a linha [criar_linha()]
# -> verifica se o horario a ser cadastrado é valido [validar_hora()]
# -> adiciona o horario a lista de horarios [adicionar_horario()]
# -> adiciona ônibus a linha [adicionar_onibus_linha()] 
def inserir_linha():
    
    """
    inserir os dados a uma nova linha (criar uma linha)

    -> não permitir o input null
    -> o valor deve ser float
    -> cria a linha [criar_linha()]
    -> verifica se o horario a ser cadastrado é valido [validar_hora()]
    -> adiciona o horario a lista de horarios [adicionar_horario()]
    -> adiciona ônibus a linha [adicionar_onibus_linha()] 
    """

    print("\n--- INSERINDO UMA NOVA LINHA ---\n")

    # recebe os valores e implementa no dicionario
    
    cid_origem = input_nao_vazio("Digite a cidade de saída do ônibus: ")

    cid_destino = input_nao_vazio("Digite a cidade destino do ônibus: ")

    # dps fazer com que fique em float (melhoria)
    valor = input_float("Digite o valor da passagem: ")

    # cria a linha com as informações básica, sem a lista de horarios e onibus (vai ser implementado a seguir)
    linha = criar_linha(cid_origem, cid_destino, valor)


    while True:
        # primeiro horario da linha
        horario = input_nao_vazio("Digite o horario de saída (hh:mm): ")

            # se a validação der certo
        if validar_hora(horario):

            # adiciona o horario na lista de horarios da linha
            adicionar_horario(linha, horario)

            break

        else:

           print("\nHorário inválido. Tente novamente (hh:mm) ;)\n")

    
    # se o usuario quiser adicionar mais horarios a linha

    continuar = 'm'

    while (continuar != 'n') or (continuar != 'N'):

        continuar = input("\nQuer adicionar mais um horário (s/n)? ")

        # se o usuario quiser adicionar outro horario
        if (continuar == 's') or (continuar == 'S'):

            horario = input("\nDigite o horario de saída (hh:mm): ")

            # se a validação der certo
            if validar_hora(horario):

                # adiciona o horario na lista de horarios da linha
                adicionar_horario(linha, horario)


            
            # se o horario não for valido
            else:

                print("\nHorário inválido. Tente novamente (hh:mm) ;)\n")

        # se o usuario não quiser adicionar mais horarios ele continua com o cadastro
        elif (continuar == 'n') or (continuar == 'N'):

            print("\nCerto! Continue com o cadastro :D")

            break

        # para opções invalidas
        else:

            print("\nOpção inválida! Tente outra ;)")
    

    # se o usuario quiser adicionar onibus a linha
    opcao = 'm'

    while (opcao != 'n') or (opcao != 'N'):

        opcao = input("\nDeseja adicionar um ônibus a linha (s/n)? ")

        # se quiser adicionar
        if (opcao == 's') or (opcao == 'S'):

            adicionar_onibus_linha(linha)

        # se não quiser adicionar mais 
        elif (opcao == 'n') or (opcao == 'N'):

            print("\nCerto! Cadastro finalizado :D\n")
            break

        # se a opção for invalida
        else:

            print("\nOpção inválida. Digite outra ;)\n")

    
    linhas_cadastradas.append(linha)


# remove a linha de onibus
def remover_linha():
    
    """
    Remover a linha de onibus
    """

    print("\n--- REMOVER LINHA \n")

    # se não tiver nenhuma linha cadastrada
    if not linhas_cadastradas:

        print("\nNenhuma linha cadastrada ainda :(")


    # mostra as linhas
    for i, linha in enumerate (linhas_cadastradas):

        print(f"\nLinha {i + 1}: ")
        print(f"{linha['cid_origem']} para {linha['cid_destino']}")
        print(f"Horarios: {', '.join(linha['horario'])}")

    
    # usuario escolhe qual a linha vai remover
    try:
        
        escolha = int(input("\n Digite o número da linha que você quer remover: "))
    
    # erro de entrada
    except ValueError:

        print("Entrada inválida. Digite um número.")
        return

    # opção invalida
    if (escolha < 1) or (escolha > len(linhas_cadastradas)):

        print("Opção inválida! Digite um número existente.")
        return
    
    # remove a linha escolhida pelo usuario
    linha_removida = linhas_cadastradas.pop(escolha - 1)

    # mostra que a linha foi removida
    print(f"\nA linha foi removida :D")
    print(f"{linha_removida['cid_origem']} para {linha_removida['cid_destino']}\n")


# altera a linha
# -> mostra as opções para alterar
# -> alterar a cidade de origem
# -> alterar a cidade de destino
# -> alterar o valor da passagem
# -> gerenciar horarios (adicionar horario e remover (o onibus tem que mudar de horario ou ser apagado tbm))
# -> gerenciar onibus (adicionar, excluir ou alterar)
def alterar_linha():
    
    """
    altera a linha de onibus

    -> mostra as opções para alterar
    -> alterar a cidade de origem
    -> alterar a cidade de destino
    -> alterar o valor da passagem
    -> gerenciar horarios (adicionar horario e remover (o onibus tem que mudar de horario ou ser apagado tbm))
    -> gerenciar onibus (adicionar, excluir ou alterar)
    """

    print("\n--- ALTERAR LINHA ---\n")

    # se não tiver linhas cadastradas
    if not linhas_cadastradas:
        
        print("\nNenhuma linha cadastrada para alterar.")
        return
    
    # exibe todas as linhas do sistema
    for i, linha in enumerate (linhas_cadastradas):

        print(f"\nLinha {i+1}: ")
        print(f"{linha['cid_origem']} para {linha['cid_destino']}")
        print(f"Horário(s): {', '.join(linha['horario'])}")

    # usuario escolhe qual linha ele quer alterar
    try:
        escolha = int(input("\nDigite o número da linha que você quer alterar: "))

    # erro de entrada
    except ValueError:

        print("Entrada inválida. Digite um número.")
        return
    
    # erro de opção invalida
    if (escolha < 1) or (escolha > len(linhas_cadastradas)):

        print("Opção inválida! Digite outra ;)")
        return
    
    # salva qual linha vai ser alterada
    linha = linhas_cadastradas[escolha-1]


    # menu de opções para alteração
    while True:

        print("\n--- OPÇÕES PARA ALTERAR ---\n")
        print("1 - Cidade de origem")
        print("2 - Cidade de destino")
        print("3 - Valor da passagem")
        print("4 - Gerenciar horários")
        print("5 - Gerenciar ônibus")
        print("0 - Sair")

        try:
            opcao_principal = int(input("\nDigite a opção desejada: "))

        # erro de entrada
        except ValueError:
            print("\nOpção inválida! Digite outra ;)")
            return

        
        match opcao_principal:

            # mudar a cidade de saida do onibus
            case 1:

                nova = input_nao_vazio("\nDigite a nova cidade de origem: ")
                # atribuir o valor ao dicionario
                linha['cid_origem'] = nova
                print("\nA cidade de origem foi alterada :)")

            # mudar a cidade destino
            case 2:

                nova = input_nao_vazio("\nDigite a nova cidade de destino: ")
                # atribuir o valor ao dicionario
                linha['cid_destino'] = nova
                print("\nA cidade de destino foi alterada :)")

            # mudar o valor da passagem
            case 3:

                nova = input_float("\nDigite o novo valor da passagem: ")
                # atribuir o valor ao dicionario
                linha['valor'] = nova
                print("\nO valor da passagem foi alterado :)")

            # gerenciar os horarios
            case 4:

                # menu de opções para mudança nos horarios
                while True:

                    print(f"\nHorarios atuais: ", ", ".join(linha['horario']))
                    print("1 - Adicionar horario a linha")
                    print("2 - Remover horário")
                    print("0 - Voltar")

                    try:
                        opcao_horario = int(input("\nDigite a ação desejada: "))

                    # erro de entrada
                    except ValueError:

                        print("\nEntrada inválida! Digite um número ;)")
                        return

                    match opcao_horario:
                        
                        # adicionar um novo horario
                        case 1:
                            
                            novo_horario = input("\nDigite o novo horário (hh:mm): ")

                            if validar_hora (novo_horario):

                                linha['horario'].append(novo_horario)
                                print("\nHorário adicionado :D")
                                break

                            else: 

                                print("Horario invalido! Tente novamente ;) (hh:mm)")

                            

                        # remover horario
                        # os onibus ligados ao horario ou serão excluidos ou mudarão de horario
                        case 2:
                            
                            # se não tiver horarios cadastrados para essa linha
                            if not linha['horario']:

                                print("\nNão há horários para remover.")
                                continue
                            
                            # se tiver mostra todos os horarios
                            print("\n--- HORÁRIOS ---\n")
                            
                            for i, horario in enumerate(linha['horario']):

                                print(f"{i+1} - {horario}")

                            # escolhe o horario que o usuario quer modificar
                            try:

                                horario = int(input("Digite o horario desejado: "))

                            # erro de entrada
                            except ValueError:

                                print("Entrada inválida! Digite um número ;)")
                                return

                            # se digitar uma opção que não existe
                            if (horario < 1) or (horario > len(linha['horario'])):

                                print("Opção inválida! Digite outra ;)")
                                return

                            removido = linha['horario'][horario - 1]

                            print(f"\nVocê está removendo o horário: {removido}")

                            # procurar onibus que possuem o horario excluido
                            onibus_afetados = [on for on in linha['partidas'] if on ['horario'] == removido]

                            # se houver alguma onibus afetado
                            if onibus_afetados:
                                print(f"\nExistem {len(onibus_afetados)} ônibus com esse horário.")
                                
                                # verifica se há algum outro horario cadastrado para trocar o do onibus
                                horarios_restantes = [h for h in linha['horario'] if (h != removido)]
                                
                                # verificar qual ação o usuario quer tomar para cada onibus
                                for onibus in onibus_afetados:

                                    print(f"\nÔnibus data {onibus['data']}\n")

                                    print("1 - Remover o ônibus")
                                    print("2 - Alterar horário do ônibus")
                                    

                                    # usuario digita a ação desejada
                                    try:
                                        opcao_onibus = int(input("\nDigite a opção desejada: "))
                                    
                                    # erro de entrada
                                    except ValueError:

                                        print("\nEntrada inválida! Digite um número ;)")
                                        return

                                    match opcao_onibus:

                                        # só remover o ônibus 
                                        case 1:

                                            linha['partidas'].remove(onibus)
                                            print("\nÔnibus foi removido :D")

                                        case 2:

                                            # melhoria -> permitir que o usuario adiciona um horario novo 
                                            if not horarios_restantes:

                                                print ("\nNenhum horário restante disponível. O ônibus será removido! ")
                                                linha['partidas'].remove(onibus)
                                                continue

                                            # mostra os horarios disponiveis 
                                            print("\nHorários disponíveis: ")
                                            for i, hora in enumerate(horarios_restantes):

                                                print(f"{i+1} - {hora}")

                                            # o usuario escolhe o horario
                                            try:

                                                nova_hora = int(input("\nDigite a opção do novo horario desejado: "))
                                                nhora = horarios_restantes[nova_hora - 1]
                                            
                                            # erro de entrada
                                            except ValueError:

                                                print("\nEntrada invalida! Digite um número ;)")
                                                return

                                            # se digitarem algo alem das opções dadas
                                            if (nova_hora < 1) or (nova_hora > len(horarios_restantes)):

                                                print("\nOpção inválida! Digite outra ;)")
                                                return
                                            
                                            # se tudo der certo, modifica o onibus, atribuindo o novo horario para ele
                                            onibus['horario'] = nhora
                                            print(f"\nNovo horario do ônibus: {nhora}")
                                        
                                        # se digitarem algo diferente das opções dadas
                                        case _:

                                            print("\nOpção inválida! Digite outra ;)")
                                            return
                            

                            # depois de todos os processos o horario é removido
                            linha['horario'].remove(removido)
                            print(f"\nO horário '{removido}' foi removido :D")

                        case 0:

                            print("\nVoltando...")
                            break

                        case _:

                            print("\nOpção inválida! Digite outra ;)")

            # gerenciar ônibus
            case 5:

                while True:

                    print("\n1 - Adicionar ônibus a linha")
                    print("2 - Remover ônibus")
                    print("3 - Alterar ônibus")
                    print("0 - Voltar")

                    try:

                        opcao_onibus = int(input("\nDigite a opção desejada: "))

                    except ValueError:

                        print("\nEntrada inválida! Digite um número ;)")
                        return
                    

                    match opcao_onibus:

                        # adicionar novo onibus a linha
                        case 1:

                            adicionar_onibus_linha(linha)

                        # remover onibus da linha
                        case 2:

                            # se a linha não tiver onibus 
                            if not linha['partidas']:

                                print("\nNenhum ônibus para remover. ")
                                continue

                            # lista todos os onibus da linha
                            for i, onibus in enumerate (linha['partidas']):
                                
                                print(f"\nOnibus {i+1}: ")
                                print(f"Data: {onibus['data']}")
                                print(f"Horário: {onibus['horario']}")
                                print(f"Assentos livres: {contar_assentos_livres(onibus['assentos'])}")

                            # o usuario escolhe o onibus para remover
                            try:
                                
                                onibus_remover = int(input("\nDigite o onibus que você quer remover: "))

                            # erro de entrada
                            except ValueError:
                                print("\nEntrada inválida! Digite um número ;)")
                                return
                            
                            # opção invalida
                            if (onibus_remover < 1) or (onibus_remover > len(linha['partidas'])):

                                print("\nOpção inválida! Digite outra ;)")
                                return
                            
                            # remove o onibus da lista de partidas
                            removido = linha['partidas'].pop(onibus_remover - 1)
                            print(f"\nO ônibus da data {removido['data']} foi removido :D")

                        
                        # alterar onibus
                        case 3: 

                            # se não tiver onibus cadastrados na linha
                            if not linha['partidas']:
                                print("\nNenhum ônibus cadastrado.")
                                continue
                            

                            # mostra os onibus cadastrados
                            print("\nÔnibus cadastrados: ")

                            for i, onibus in enumerate (linha['partidas']):
                                
                                print(f"\nOnibus {i+1}: ")
                                print(f"Data: {onibus['data']}")
                                print(f"Horário: {onibus['horario']}")
                                print(f"Assentos livres: {contar_assentos_livres(onibus['assentos'])}")

                            # escolhe qual onibus o usuario que alterar
                            try:

                                escolha_onibus = int(input("\nDigite o número do ônibus para alterar: "))

                            # erro de entrada
                            except ValueError:

                                print("\nEntrada inválida! Digite um número")
                                return
                            
                            # opção invalida
                            if (escolha_onibus < 1) or (escolha_onibus > len(linha['partidas'])):
                                
                                print("\nOpção inválida! Digite outra ;)")
                                return
                            
                            idx = escolha_onibus - 1
                            onibus = linha['partidas'][idx]
                            

                            # menu de alteração do onibus

                            while True:

                                print("\nO que você quer alterar no ônibus?")
                                print("1 - Data da partida")
                                print("2 - Horário")
                                print("0 - Voltar")

                                try:

                                    menu_onibus = int(input("\nDigite a ação desejada: "))

                                except ValueError:

                                    print("\nEntrada inválida! Digite outra ;)")
                                    return
                                
                                match menu_onibus:

                                    # alterar a data do onibus 
                                    case 1:

                                        while True: 

                                            nova_data = input("\nDigite a nova data(dd/mm/aaaa): ")

                                            if validar_data(nova_data):

                                                if data_hora_valida(nova_data, onibus['horario']):

                                                    onibus['data'] = nova_data
                                                    print(f"\nA data foi alterada :D")
                                                    break

                                                else:

                                                    print("\nA data+hora está no passado. Tente outra ;)")
                                            
                                            else:

                                                print("\nA data é inválida! Tente novamente (dd/mm/aaaa)")
                                    
                                    # alterar o horario do onibus
                                    case 2:

                                        # lista todos os horarios cadastrados na linha
                                        print("\nOpções de horários: ")

                                        for i, horario in enumerate (linha['horario']):

                                            print(f"{i+1} - {horario}")

                                        
                                        # o usuario escolhe o novo horario
                                        try: 
                                            
                                            nv_horario = int(input("\nDigite o número do horário: "))

                                        except ValueError:

                                            print("\nEntrada inválida. Digite um número ;)")
                                            return
                                        
                                        if (nv_horario < 1) or (nv_horario > len(linha['horario'])):

                                            print("\nOpção inválida! Digite outra ;)")
                                            return
                                        
                                        # coloca o novo horario no onibus
                                        idx = nv_horario - 1
                                        onibus['horario'] = linha['horario'][idx]

                                        print("\nHorário atualizado :D")


                                    case 0:

                                        print("\nVoltando...")
                                        break

                                    case _:

                                        print("\nOpção inválida. Digite outra ;)")

                        # voltar      
                        case 0: 

                            print("\nVoltando...")
                            break

                        case _:

                            print("\nOpção inválida! Digite outra ;)")


            # sair do menu de alteração  
            case 0: 

                print("\nSaindo...")
                break


            case _:

                print("\nOpção inválida! Digite outra ;)")


# pesquisar todos os onibus disponiveis com o destino em x cidade destino
# -> achar todos as linhas (e consequentemente onibus) com a cidade destino em x
# -> separar por disponiveis ou não (tanto por assentos quanto por data+hora de saida)
def achar_onibus_para_x():
    
    """
    pesquisar todos os onibus disponiveis com o destino em x cidade destino

    -> achar todos as linhas (e consequentemente onibus) com a cidade destino em x
    -> separar por disponiveis ou não (tanto por assentos quanto por data+hora de saida)
    """
    
    print("\n--- CONSULTAR ÔNIBUS PARA UMA CIDADE DESTINO ---\n")

    # caso não tenha linhas cadastradas
    if not linhas_cadastradas:

        print("\nNenhuma linha cadastrada ainda :(")
        return
    
    # recebe a cidade destino
    cidade = input_nao_vazio("Digite o nome da cidade destino: ").strip()

    # cria as listas dos dois tipos de onibus (disponiveis ou não)
    onibus_disponiveis = []
    onibus_indisponiveis = []

    # data e hora de agora, para fazer a validação se o onibus ja partiu
    agora = datetime.now()

    # procura em todas as linhas cadastradas a cidade destino
    for linha in linhas_cadastradas:

        # se achar uma linha com a cidade destino igual a recebida
        if (linha['cid_destino'].lower() == cidade.lower()):

            # verifica todos os onibus dessa linha
            for onibus in linha['partidas']:

                # conta quantos assentos livres tem
                assentos_livres = contar_assentos_livres(onibus['assentos'])


                # salva a data+hora do ônibus para comparar com agora
                dia, mes, ano = map(int, onibus['data'].split("/"))
                hora, minuto = map(int, onibus['horario'].split(":"))

                data_onibus = datetime(ano, mes, dia, hora, minuto)

                # verifica a disponibilidade do onibus
                if (assentos_livres > 0) and (data_onibus > agora):
                    onibus_disponiveis.append((linha, onibus))
                
                else:
                    onibus_indisponiveis.append((linha, onibus))

    # mostrar a disponibilidade dos ônibus

    if (not onibus_disponiveis) and (not onibus_indisponiveis):
        print(f"\nNão há nenhum ônibus para a cidade {cidade}")
        return
    
    if onibus_disponiveis:

        print("\n--- Ônibus disponiveis: ---\n")

        for linha, onibus in onibus_disponiveis:

            livres = contar_assentos_livres(onibus['assentos'])
            print(f"\nLinha {linha['cid_origem']} para {linha['cid_destino']}")
            print(f"Data: {onibus['data']}")
            print(f"Horario: {onibus['horario']}")
            print(f"Assentos livres: {livres}")

    else:

        print(f"\nNenhum ônibus disponível para {cidade}")

    
    if onibus_indisponiveis:

        print("\n--- Ônibus indisponiveis: ---\n")

        for linha, onibus in onibus_indisponiveis:

            livres = contar_assentos_livres(onibus['assentos'])
            print(f"\nLinha {linha['cid_origem']} para {linha['cid_destino']}")
            print(f"Data: {onibus['data']}")
            print(f"Horario: {onibus['horario']}")
            print(f"Assentos livres: {livres}")

    else:

        print(f"\nNenhum ônibus indisponível para {cidade}")
    

# pesquuisar todos os onibus disponiveis com a cidade de origem em x
# -> achar todos as linhas (e consequentemente onibus) com a cidade de saida em x
# -> separar por disponiveis ou não (tanto por assentos quanto por data+hora de saida)
def achar_onibus_de_x():
    
    """
    pesquuisar todos os onibus disponiveis com a cidade de origem em x

    -> achar todos as linhas (e consequentemente onibus) com a cidade de saida em x
    -> separar por disponiveis ou não (tanto por assentos quanto por data+hora de saida)
    """
    
    print("\n--- CONSULTAR ÔNIBUS DE UMA CIDADE DE SAÍDA ---\n")

    # caso não tenha linhas cadastradas
    if not linhas_cadastradas:

        print("\nNenhuma linha cadastrada ainda :(")
        return
    
    # recebe a cidade saida
    cidade = input_nao_vazio("Digite o nome da cidade de saída: ").strip()

    # cria as listas dos dois tipos de onibus (disponiveis ou não)
    onibus_disponiveis = []
    onibus_indisponiveis = []

    # data e hora de agora, para fazer a validação se o onibus ja partiu
    agora = datetime.now()

    # procura em todas as linhas cadastradas a cidade destino
    for linha in linhas_cadastradas:

        # se achar uma linha com a cidade destino igual a recebida
        if (linha['cid_origem'].lower() == cidade.lower()):

            # verifica todos os onibus dessa linha
            for onibus in linha['partidas']:

                # conta quantos assentos livres tem
                assentos_livres = contar_assentos_livres(onibus['assentos'])


                # salva a data+hora do ônibus para comparar com agora
                dia, mes, ano = map(int, onibus['data'].split("/"))
                hora, minuto = map(int, onibus['horario'].split(":"))

                data_onibus = datetime(ano, mes, dia, hora, minuto)

                # verifica a disponibilidade do onibus
                if (assentos_livres > 0) and (data_onibus > agora):
                    onibus_disponiveis.append((linha, onibus))
                
                else:
                    onibus_indisponiveis.append((linha, onibus))

    # mostrar a disponibilidade dos ônibus

    if (not onibus_disponiveis) and (not onibus_indisponiveis):
        print(f"\nNão há nenhum ônibus com saída da cidade {cidade}")
        return
    
    if onibus_disponiveis:

        print("\n--- Ônibus disponiveis: ---\n")

        for linha, onibus in onibus_disponiveis:

            livres = contar_assentos_livres(onibus['assentos'])
            print(f"\nLinha {linha['cid_origem']} para {linha['cid_destino']}")
            print(f"Data: {onibus['data']}")
            print(f"Horario: {onibus['horario']}")
            print(f"Assentos livres: {livres}")

    else:

        print(f"\nNenhum ônibus disponível com saída da cidade {cidade}")

    
    if onibus_indisponiveis:

        print("\n--- Ônibus indisponiveis: ---\n")

        for linha, onibus in onibus_indisponiveis:

            livres = contar_assentos_livres(onibus['assentos'])
            print(f"\nLinha {linha['cid_origem']} para {linha['cid_destino']}")
            print(f"Data: {onibus['data']}")
            print(f"Horario: {onibus['horario']}")
            print(f"Assentos livres: {livres}")

    else:

        print(f"\nNenhum ônibus indisponível com saída da cidade {cidade}")


# cria o dicionario de reservas não realizadas
def registrar_reserva_nao_realizada(linha_original, motivo):
    
    """
    cria o dicionario de reservas não realizadas
    """

    reservas_nao_realizadas.append({
        'linha_original': linha_original,
        'motivo': motivo
    })


# grava em um arquivo de texto todas as reservas que não puderam ser realizadas
# -> o motivo aparece também
def salvar_reservas_nao_realizadas():
    
    """
    grava em um arquivo de texto todas as reservas que não puderam ser realizadas

    -> o motivo aparece também
    """
    
    if not reservas_nao_realizadas:

        print("\nNão há reservas não realizadas para salvar :)")
        return
    
    nome = input("Digite o nome do arquivo para salvar (ex: erro.txt): ").strip()

    try:

        with open (nome, "w", encoding="utf-8") as arq:

            arq.write("\n--- RESERVAS NÃO REALIZADAS ---\n")

            for r in reservas_nao_realizadas:
                arq.write(f"\n\nReserva: {r['linha_original']}")
                arq.write(f"\nMotivo: {r['motivo']}")

        
        print(f"\nO arquivo '{nome}' foi criado :D")

    
    except:

        print("\nErro ao salvar o arquivo :(")


# ler reservas de um arquivo txt
# -> formato: CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
# -> uma reserva por linha
def ler_reservas_txt():
    
    """
    ler reservas de um arquivo txt

    -> formato: CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
    -> uma reserva por linha
    """

    print("\n--- LENDO RESERVAS DE UM ARQUIVO .TXT ---\n")
    print("Formato: cidade_destino, horario, data, assento")

    nome_arquivo = input("\nDigite o nome do arquivo txt (exemplo: reservas.txt): ").strip()

    try:

        arquivo = open(nome_arquivo, "r", encoding="utf-8")

    except FileNotFoundError:

        print("\nO arquivo não foi encontrado :(")
        return
    
    print("\nProcessando reservas... \n")

    for linha in arquivo:

        # ignora as linhas em branco
        if not linha.strip():
            continue

        # separa cada campo como uma informação
        try:
            cidade, horario, data, assento_str = [x.strip() for x in linha.split(",")]
        
        except:
            print(f"Linha inválida: {linha}")
            registrar_reserva_nao_realizada(linha.strip(), "Linha inválida")
            continue

        # validar hora
        if not validar_hora(horario):

            print(f"Horário inválido na linha: {linha}")
            registrar_reserva_nao_realizada(linha.strip(), "Horário inválido")
            continue

        # validar data
        if not validar_data(data):
            print(f"Data inválida na linha: {linha}")
            registrar_reserva_nao_realizada(linha.strip(), "Data inválida")
            continue

        # verificar assento
        if not assento_str.isdigit():
            print(f"Assento inválido: {assento_str}")
            registrar_reserva_nao_realizada(linha.strip(), "Assento inválido")
            continue

        assento = int(assento_str)


        # procurar a linha pela cidade destino fornecida

        linha_encontrada = None

        for l in linhas_cadastradas:

            if l['cid_destino'].lower() == cidade.lower():

                linha_encontrada = l
                break

        if not linha_encontrada:

            print(f"Nenhuma linha encontrada com o destino para {cidade}")
            registrar_reserva_nao_realizada(linha.strip(), "Cidade destino não encontrada")
            continue

        # procura o ônibus com a data e horario fornecidos

        onibus_encontrado = None

        for o in linha_encontrada['partidas']:

            if o['data'] == data and o['horario'] == horario:

                onibus_encontrado = o
                break

        if not onibus_encontrado:

            print("Nenhum ônibus com essa descrição foi encontrado!")
            registrar_reserva_nao_realizada(linha.strip(), "Ônibus não foi encontrado")
            continue


        # validar se a data+hora está no passado
        if not data_hora_valida(data, horario):
            print(f"Ônibus já saiu: {data} - {horario}")
            registrar_reserva_nao_realizada(linha.strip(), "Ônibus já saiu")
            continue


        # validar assento
        if (assento < 1) or (assento > 20):
            print(f"Assento {assento} inexistente!")
            registrar_reserva_nao_realizada(linha.strip(), "Assento inexistente")
            continue


        assento_livre = False

        # percorre matriz procurando o assento
        for linha_assento in onibus_encontrado['assentos']:
            
            if str(assento) in linha_assento:
            
                pos = linha_assento.index(str(assento))

                if linha_assento[pos] == "X":
            
                    assento_livre = False
            
                else:
            
                    assento_livre = True
                    marcar_assento(onibus_encontrado, str(assento))   # <<< CORRIGIDO
                    fazer_venda(linha_encontrada)

                break

        if not assento_livre:
            print(f"Assento {assento} está ocupado")
            registrar_reserva_nao_realizada(linha.strip(), "Assento já ocupado")
            continue



        # se passar por todas as validações fazer a reserva

        

        print(f"Reserva foi feita :D")
        print(f"{cidade} | {data} | {horario} | Assento {assento}\n")
        
    
    arquivo.close()

    print("\nLeitura finalizada!\n")


def escolher_onibus(onibus_disponiveis):
    if not onibus_disponiveis:
        print("\nNenhum ônibus disponível para essa cidade.")
        return None

    print("\n=== Ônibus disponíveis ===\n")

    # listar os ônibus com número
    for idx, (linha, onibus) in enumerate(onibus_disponiveis, start=1):
        livres = contar_assentos_livres(onibus['assentos'])
        print(f"{idx} - {linha['cid_origem']} → {linha['cid_destino']}  "
        f"{onibus['data']} às {onibus['horario']}  "
        f"(Assentos livres: {livres})")

    # escolha do usuário
    while True:
        try:

            escolha = int(input("\nEscolha o número do ônibus: "))

            if 1 <= escolha <= len(onibus_disponiveis):

                break

            else:

                print("Opção inválida.")

        except ValueError:

            print("Digite um número válido.")

    # retorna o ônibus escolhido
    return onibus_disponiveis[escolha - 1]
    

def achar_onibus_com_assentos_disponiveis():

    
    print("\n--- CONSULTAR ÔNIBUS PARA UMA CIDADE DESTINO ---\n")

    # caso não tenha linhas cadastradas
    if not linhas_cadastradas:
        print("\nNenhuma linha cadastrada ainda :(")
        return []

    # recebe a cidade destino
    cidade = input("Digite o nome da cidade destino: ").strip()

    # listas que serão retornadas
    onibus_disponiveis = []
    onibus_indisponiveis = []

    agora = datetime.now()

    # procura em todas as linhas cadastradas pela cidade destino
    for linha in linhas_cadastradas:

        if linha['cid_destino'].lower() == cidade.lower():

            for onibus in linha['partidas']:

                assentos_livres = contar_assentos_livres(onibus['assentos'])

                # monta a data completa para comparação
                dia, mes, ano = map(int, onibus['data'].split("/"))
                hora, minuto = map(int, onibus['horario'].split(":"))
                data_onibus = datetime(ano, mes, dia, hora, minuto)

                # se ainda não partiu e tem assentos → disponível
                if (assentos_livres > 0) and (data_onibus > agora):
                    onibus_disponiveis.append((linha, onibus))
                else:
                    onibus_indisponiveis.append((linha, onibus))

    #Impressões 

    if not onibus_disponiveis and not onibus_indisponiveis:
        print(f"\nNão há nenhum ônibus para {cidade}")
        return []

    if onibus_disponiveis:
        print("\n--- Ônibus disponíveis: ---\n")
        for linha, onibus in onibus_disponiveis:
            livres = contar_assentos_livres(onibus['assentos'])
            print(f"\nLinha {linha['cid_origem']} → {linha['cid_destino']}")
            print(f"Data: {onibus['data']}")
            print(f"Horário: {onibus['horario']}")
            print(f"Assentos livres: {livres}")
    else:
        print(f"\nNenhum ônibus disponível para {cidade}")

    if onibus_indisponiveis:
        print("\n--- Ônibus indisponíveis: ---\n")
        for linha, onibus in onibus_indisponiveis:
            livres = contar_assentos_livres(onibus['assentos'])
            print(f"\nLinha {linha['cid_origem']} → {linha['cid_destino']}")
            print(f"Data: {onibus['data']}")
            print(f"Horário: {onibus['horario']}")
            print(f"Assentos livres: {livres}")
    else:
        print(f"\nNenhum ônibus indisponível para {cidade}")

    #  RETORNA a lista de disponíveis!
    return onibus_disponiveis


# consultar os assentos disponiveis informando a cidade destino, horario, data
# -> data deve ser inferior a 30 dias, contados a partir da data atual
# -> perguntar se o usuario quer reservar algum assento (se houver disponíveis)
# -> nenhuma passagem pode ser comercializada para ônibus que já partiram
def consultar_assento_disponivel():
    
    """
    consultar os assentos disponiveis informando a cidade destino, horario, data
    
    -> data deve ser inferior a 30 dias, contados a partir da data atual
    -> perguntar se o usuario quer reservar algum assento (se houver disponíveis)
    -> nenhuma passagem pode ser comercializada para ônibus que já partiram    """
    
    print("\n--- CONSULTAR ASSENTOS DISPONÍVEIS ---\n")

    if not linhas_cadastradas:

        print("\nNenhuma linha cadastrada ainda :(")
        return
    
    cidade = input("\nDigite a cidade destino: ").strip()

    horario = input("\nDigite o horário (hh:mm): ").strip()
    
    # verificar se o horario é valido
    if not validar_hora(horario):
        print("\nHorário inválido!")
        return
    
    data = input("\nDigite a data (dd/mm/aaaa): ").strip()

    # verificar se a data é valida
    if not validar_data(data):
        print("\nData inválida!")
        return
    

    # verificar se a data está dentro de 30 dias
    dia, mes, ano = map(int, data.split("/"))
    data_consulta = datetime(ano, mes, dia)
    hoje = datetime.now()

    diferenca = (data_consulta - hoje).days

    if (diferenca < 0):

        print("\nA data informada está no passado!")
        return
    
    if (diferenca > 30):
        
        print("\nA data informada não deve passar de 30 dias à frente!")
        return
    

    # procurar linha com destino na cidade desejada

    linha_encontrada = None
    for l in linhas_cadastradas:
        if l['cid_destino'].lower() == cidade.lower():
            linha_encontrada = l
            break

    if not linha_encontrada:
        print(f"\nNenhuma linha foi encontrada para {cidade} :(")
        registrar_reserva_nao_realizada(f"{cidade}, {horario}, {data}", "Cidade destino não encontrada")

        return
    

    # procurar o onibus com a data e hora desejadas

    onibus_encontrado = None
    for o in linha_encontrada['partidas']:

        if (o['data'] == data) and (o['horario'] == horario):
            onibus_encontrado = o
            break

    if not onibus_encontrado:
        print("\nNnehum ônibus foi encontrado com essas informações :(")
        registrar_reserva_nao_realizada(f"{cidade}, {horario}, {data}", "Ônibus não foi encontrado")
        return
    
    if not data_hora_valida(data, horario):
        print("\nO ônibus já partiu. Não é possivel comprar uma passagem")
        registrar_reserva_nao_realizada(f"{cidade}, {horario}, {data}", "Ônibus já saiu")

        return
    

    # Mostrar o mapa de assentos
    print("\nMapa dos Assentos:")
    mostrar_mapa_assentos(onibus_encontrado)

    livres = contar_assentos_livres(onibus_encontrado['assentos'])
    print(f"\nAssentos livres: {livres}")

    if livres == 0:
        print("\nNenhum assento disponível.")
        return

    # Perguntar se deseja reservar
    opc = input("\nDeseja reservar um assento? (s/n): ").strip().lower()

    if opc != "s":
        print("\nNenhuma reserva foi feita. Voltando...")
        return

    # Processo de venda
    vender_assentos(onibus_encontrado, linha_encontrada)
        


def salvar_ou_exibir(texto):
    print("\nDeseja:")
    print("1 - Exibir relatório na tela")
    print("2 - Salvar relatório no arquivo relatorio.txt")
    opc = input("Escolha: ").strip()

    if opc == "1":
        print("\n" + texto)

    elif opc == "2":
        with open("relatorio.txt", "a", encoding="utf-8") as arq:
            arq.write(texto + "\n")
        print("\nRelatório salvo em relatorio.txt")

    else:
        print("Opção inválida.")