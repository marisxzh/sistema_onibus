from funcao import menu
from funcao import inserir_linha
from funcao import mostrar_linhas
from funcao import remover_linha
from funcao import alterar_linha
from funcao import achar_onibus_para_x
from funcao import achar_onibus_de_x
from funcao import consultar_assento_disponivel
from funcao import gerar_relatorios
from funcao import ler_reservas_txt
from funcao import salvar_reservas_nao_realizadas



opcao = -1

while (opcao != 0):

    menu()

    opcao = int(input("\nDigite a opção desejada: "))

    match opcao:

        # cadastrar linha nova
        case 1:

            inserir_linha()
            

        # remover linha      
        case 2:
            
            remover_linha()

        # alterar linha
        case 3:

            alterar_linha()

        # consultar horarios para uma determinada cidade
        case 4:
            
            while True: 
            
                print("\nVocê quer consultar para: ")
                print("1 - Cidade destino")
                print("2 - Cidade da saída do ônibus")
                print("0 - Voltar")

                try:
                    
                    escolha = int(input("Digite a opção desejada: "))

                except ValueError:

                    print("Entrada inválida! Digite um número ;)")
                
                match escolha:

                    case 1: 

                        achar_onibus_para_x()

                    case 2:

                        achar_onibus_de_x()

                    case 0:

                        print("\nVoltando...")
                        break

                    case _:

                        print("Opção inválida! Digite outra ;)")

        # consultar assentos disponiveis
        case 5:

            consultar_assento_disponivel()
            

        # gerar relatorio
        case 6:

            gerar_relatorios()

        # ler reserva de um arquivo de texto
        case 7:

            ler_reservas_txt()


        # mostrar as reservas que não puderam ser realizadas
        case 8:

            salvar_reservas_nao_realizadas()


        case 9:

            mostrar_linhas()
            
        
        # sair
        case 0:

            print ("\nFechando sistema...")



        case _:

            print("\nOpção inválida. Digite outra :)")


    
    print("\n")





