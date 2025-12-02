# Sistema de Reserva de Passagens de Ônibus

Este projeto é um sistema de gerenciamento de linhas de ônibus desenvolvido em Python. Ele permite cadastrar linhas, ônibus, consultar horários, vender passagens, gerar relatórios, etc. O sistema é baseado em um menu interativo no terminal, onde o usuário pode realizar operações de CRUD (Criar, Ler, Atualizar, Deletar) em linhas e ônibus, além de funcionalidades de reserva e relatórios.

## Como Funciona o Projeto

O sistema é dividido em dois arquivos principais:
- `funcao.py`: Contém todas as funções e lógica do sistema, como validações, manipulação de dados, relatórios, etc.
- `trabalho2.py`: Arquivo principal que executa o loop do menu e chama as funções de `funcao.py`.

Os dados são armazenados em memória (listas e dicionários) durante a execução. Relatórios e vendas são salvos em arquivos de texto (como `relatorioVenda.txt` e `relatorio.txt`). Reservas não realizadas são registradas para análise posterior.

### Pré-requisitos
- Python 3.x instalado no sistema.

### Como Executar

1. Certifique-se de que os arquivos `funcao.py` e `trabalho2.py` estão no mesmo diretório.
2. Abra o terminal no diretório do projeto.
3. Execute o comando:
   ```
   python trabalho2.py
   ```
4. O sistema iniciará mostrando o menu principal.

## COMO INICIAR/TERMINAR

### Iniciar o Sistema
- Execute o comando `python trabalho2.py` no terminal.
- O sistema exibirá o menu principal com as opções numeradas de 1 a 9, mais a opção 0 para sair.

### Terminar o Sistema
- No menu principal, digite `0` e pressione Enter.
- O sistema exibirá a mensagem "Fechando sistema..." e encerrará a execução.

Durante a execução, o sistema permanece em loop até que o usuário escolha sair. Todas as operações são realizadas via entrada no terminal (input).

## OPÇÕES OFERECIDAS

O sistema oferece as seguintes opções no menu principal:

1. **Inserir linha**: Permite cadastrar uma nova linha de ônibus, incluindo cidades de origem e destino, valor da passagem e horários. Opcionalmente, é possível adicionar ônibus à linha.
2. **Remover linha**: Lista todas as linhas cadastradas e permite remover uma delas pelo número.
3. **Alterar linha**: Permite modificar detalhes de uma linha existente, como cidades, valor da passagem, horários (adicionar/remover) e gerenciamento de ônibus (adicionar, remover ou alterar data/horário).
4. **Consultar horários para uma determinada cidade**: Submenu para consultar ônibus disponíveis ou indisponíveis com destino ou saída de uma cidade específica.
5. **Consultar assentos disponíveis**: Permite consultar assentos livres em um ônibus específico (informando cidade destino, horário e data). Se houver assentos disponíveis, oferece a opção de reservar.
6. **Gerar relatórios**: Submenu para gerar relatórios de vendas do mês corrente ou ocupação média por dia da semana. Os relatórios podem ser exibidos na tela ou salvos em arquivo.
7. **Ler reserva de um arquivo**: Lê reservas de um arquivo de texto (formato: cidade_destino, horario, data, assento) e processa as reservas válidas, registrando vendas ou erros.
8. **Mostrar as reservas que não puderam ser realizadas**: Salva em um arquivo de texto todas as reservas não realizadas, incluindo motivos (ex.: assento ocupado, ônibus não encontrado).
9. **Mostrar todas as linhas**: Exibe todas as linhas cadastradas, incluindo ônibus associados e assentos livres.
0. **Sair**: Encerra o sistema.

## PRINCIPAIS TELAS

O sistema é baseado em interface de texto no terminal. As principais "telas" são os menus e prompts de entrada:

- **Tela Principal (Menu)**: Exibe o menu com as opções numeradas. É a tela inicial e de retorno após cada operação.
- **Tela de Inserção de Linha**: Prompts para inserir cidades, valor, horários e adicionar ônibus.
- **Tela de Consulta de Ônibus**: Lista ônibus disponíveis/indisponíveis para uma cidade, com detalhes como data, horário e assentos livres.
- **Tela de Mapa de Assentos**: Mostra o layout dos assentos do ônibus (matriz 5x5 com assentos numerados, "X" para ocupados).
- **Tela de Relatórios**: Exibe ou salva relatórios de vendas e ocupação.
- **Tela de Alteração**: Submenus para alterar linhas, horários e ônibus, com listas e prompts para seleção.

Todas as telas são interativas, com validações de entrada (ex.: datas no formato dd/mm/aaaa, horários hh:mm, valores numéricos).

## CONCLUSÃO

Este sistema é uma ferramenta completa para gerenciamento de reservas de ônibus, adequada para pequenos operadores ou como protótipo educacional. Ele demonstra conceitos de programação orientada a objetos (embora em Python procedural), validações de dados, manipulação de arquivos e relatórios.

### Limitações
- Dados não são persistidos entre execuções (tudo fica em memória); relatórios são salvos em arquivos, mas linhas e ônibus são perdidos ao fechar.
- Interface limitada ao terminal.
- Validações básicas; não trata casos extremos como fusos horários ou múltiplas vendas simultâneas.
- Capacidade fixa de 20 assentos por ônibus.
- Não há autenticação de usuários ou controle de acesso.
- Relatórios são simples e salvos em texto plano.

### Problemas Conhecidos
- Dependência de entrada manual; erros de digitação podem causar loops ou falhas.
- Não há backup automático de dados; perda de informações em caso de erro.
- Processamento de reservas de arquivo pode falhar se o formato não for exato.
- Não suporta reservas múltiplas em lote eficientemente.

Futuras melhorias poderiam incluir banco de dados para persistência, interface gráfica e integração com APIs de pagamento.
