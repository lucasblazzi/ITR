import requests
import time
import sys
from base_doc import busca_doc
from base_doc import disponiveis
import pandas as pd


def animation():                                                                #funcao pronta stackoverflow
    print("Buscando arquivo:")
    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(3)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")



def escreve_arquivo(ticker,ano,demon,dados):                                    #salva a saida de dados no arquivo csv com nome ticker_ano_demon.csv
    try:
        f = (open(ticker+'_'+ano+'_'+demon+'.csv', "x"))
        f.write(dados)
        return True
    except:
        return False



def demonstrativo(token, doc):                                                  #Funcao para iniciar o projeto
    doc = str(doc)                                                              #Faz um POST Request para a api do ParseHub conforme a documentacao oferecida pelo site
    params = {
      "api_key": "t14QhaR-0UJq",
      "start_url": "https://www.rad.cvm.gov.br/ENETCONSULTA/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento="+doc+"&CodigoTipoInstituicao=2",
    }
    r = requests.post('https://www.parsehub.com/api/v2/projects/'+token+'/run', data=params)
    #print(r.text)
    run_token = str(r.text[15:27])                                              #salva o token do processo gerado ao executar o projeto
    print()
    print("Importando os dados...")
    print("(Aproximadamente 30 segundos)")
    print()
    animation()
    #time.sleep(30)

    params = {                                                                  #GET Request para pegar raw data do projeto iniciado anteriormente
      "api_key": "t14QhaR-0UJq",                                                #passa o token gerado anteriormente como parametro para buscar os dados gerados pela execucao do processo anterior
      "format": "csv",
    }
    demo = requests.get('https://www.parsehub.com/api/v2/runs/'+run_token+'/data', params=params)
    #print(demo.text)
    dados = demo.text
    return dados



def body(ticker, ano, demon, token):
    doc = busca_doc(ticker, ano)
    dados = demonstrativo(token, doc)
    aux = escreve_arquivo(ticker,ano,demon,dados)
    if aux == True:
        print('Arquivo '+ticker+'_'+ano+'_'+demon+'.csv'' gerado com sucesso!!!')
    else:
        print("Falha na cópia do arquivo!!! / Arquivo ja existente")



def modo1(ticker, ano, demon):                                                                    #Busca de um relatorio a partir de ticker + ano + demonstrativo
    if demon == 'dr' or demon == 'DR':
        body(ticker, ano, demon, 'tUgYN4_k8zKU')        #gera DR

    elif demon == 'bpa' or demon == 'BPA':
        body(ticker, ano, demon, 'tStJKRY4WWN_')        #gera BPA

    elif demon == 'bpp' or demon == 'BPP':
        body(ticker, ano, demon, 't3fX3x4OODkW')        #gera BPP

    elif demon == 'dfc' or demon == 'DFC':
        body(ticker, ano, demon, 'tD1m6nCLOBRu')        #gera DFC

    else:
        print('Demonstrativo nao encontrado...')
        print('Digite: DR para Demonstracao dos Resultados')
        print('Digite: BPA para Balanco Patrimonial Ativo')
        print('Digite: BPP para Balanco Patrimonial Passivo')
        print('Digite: DFC para Demonstração de Fluxos de Caixa')
        return



def modo2(ticker):
    ano = 2015
    for ano in range(2015, 2020, 1):
        ano = str(ano)
        body(ticker, ano, 'DR', 'tUgYN4_k8zKU')        #gera DR
        body(ticker, ano, 'BPA', 'tStJKRY4WWN_')        #gera BPA
        body(ticker, ano, 'BPP', 't3fX3x4OODkW')        #gera BPP
        body(ticker, ano, 'DFC', 'tD1m6nCLOBRu')        #gera DFC



def modo4(ticker, demon):
    ano = 2019
    #monta a base da tabela baseando-se na conta 2019
    try:
        main_df = pd.read_csv(ticker+'_'+str(ano)+'_'+demon+'.csv', encoding='ANSI', header=0)
    except:
        print('\nDemonstrativo não encontrado. Certifique-se de que os demonstrativos requisitados já foram baixados!\n\n')
        return;
    contanivel = main_df[main_df.Conta_numero.map(len)<=7]          #seleciona contas ate o terceiro nivel
    column_data = contanivel.iloc[:, 0:3]
    column_data = column_data.reset_index(drop=True)
    frames = [column_data]

    #concatena os demais anos ate 2014
    while ano != 2014:
        df = pd.read_csv(ticker+'_'+str(ano)+'_'+demon+'.csv', encoding='ANSI', header=0)
        contanivel = df[df.Conta_numero.map(len)<=7]          #seleciona contas ate o terceiro nivel
        column_data = contanivel.iloc[:, 3]
        column_data = column_data.reset_index(drop=True)
        frames.append(column_data)
        ano = ano - 1

    result = pd.concat(frames, axis=1)          #axis=1 --> concatena como coluna
    result.to_csv(ticker+'_'+demon+'.csv', header=False, index=False, encoding='ANSI')



def main():

    print("_________________________________________________________________________________")
    print("                          DEMONSTRATIVOS FINANCEIROS B3                          ")
    print("_________________________________________________________________________________")
    print()
    while True:
        print("__________________________ DOWNLOAD DE DEMONSTRATIVOS ___________________________")
        print()
        print('1- Demonstrativo individual por ano')
        print('2- Conjunto de demonstrativos (DR + BPA + BPP + DFC (2015-2019))')
        print()
        print("________________________________ OUTRAS FUNCOES _________________________________")
        print()
        print('3- Listar empresas disponíveis para consulta')
        print('4- Compilar demonstrativos')
        print('5- Sair do programa')
        print("_________________________________________________________________________________")
        print()
        modo = int(input('Opção:'))
        print()
        if modo == 1:
            while True:
                ticker = input("Ticker: ")
                ano = input("Ano: ")
                demon = input("Demonstrativo: ")
                modo1(ticker,ano,demon)

        elif modo == 2:
            ticker = input('Ticker:')
            modo2(ticker)
            print("Todos os demonstrativos foram baixados!!!")
            print("Encerrando o programa...")
            exit()

        elif modo == 3:
            disponiveis()
            print('\n\n')

        elif modo == 4:
            ticker = input('Ticker: ')
            demon = input('Demonstrativo: ')
            modo4(ticker, demon)

        elif modo == 5:
            print('Encerrando o programa...')
            exit()

        else:
            print('Opção Invalida')
            exit()

    print("_________________________________________________________________________________")
main()
