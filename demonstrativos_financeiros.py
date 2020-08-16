import requests
import time
import sys
import db_conn
import json
from analise_demon import analise_fundamentalista
from db_conn import busca_doc_cvm
from db_conn import busca_doc
from db_conn import disponiveis


def escreve_arquivo(ticker, ano, demon, dados):  # salva a saida de dados no arquivo csv com nome ticker_ano_demon.csv
    try:
        f = (open(ticker + '_' + ano + '_' + demon + '.csv', "x"))
        f.write(dados)
        return True
    except:
        return False


def demonstrativo(token, doc):  # Funcao para iniciar o projeto ParseHub
    doc = str(doc)  # Faz um POST Request para a api do ParseHub conforme a documentacao oferecida pelo site
    params = {
        "api_key": "t14QhaR-0UJq",
        "start_url": "https://www.rad.cvm.gov.br/ENETCONSULTA/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=" + doc + "&CodigoTipoInstituicao=2",
    }
    r = requests.post('https://www.parsehub.com/api/v2/projects/' + token + '/run', data=params)
    #print(r.text)
    run_info = json.loads(r.text)
    run_token = str(run_info["run_token"])  # salva o token do processo gerado ao executar o projeto
    #print(run_token)
    print()
    print("Importando os dados...")
    print("(Aproximadamente 30 segundos)")
    print()

    params = {  # GET Request para pegar raw data do projeto iniciado anteriormente
        "api_key": "t14QhaR-0UJq",
        "format": "csv",
    }
    demo = requests.get('https://www.parsehub.com/api/v2/runs/' + run_token + '/data', params=params)
    print('https://www.parsehub.com/api/v2/runs/' + run_token + '/data')
    #print(demo)
    #print(demo.text)
    aux_time = 0
    print('Buscando...')
    while demo.status_code != 200:
        time.sleep(2)
        demo = requests.get('https://www.parsehub.com/api/v2/runs/' + run_token + '/data', params=params)
        aux_time += 2
        if aux_time % 10 == 0:  # print buscando de 10 em 10 segundos
            print('Buscando...')

    dados = demo.text
    return dados


def body(ticker, ano, demon, token):  # funcao base para buscar um demonstrativo e salvar em .csv
    doc = busca_doc(ticker, ano)  # busca o numero do documento no banco de dados
    if doc == 0:
        print('Demonstrativo nao encontrado')
        return
    dados = demonstrativo(token, doc)  # faz a busca do demonstrativo a utilizando a API
    aux = escreve_arquivo(ticker, ano, demon, dados)  # salva o demonstrativo em um arquivo csv
    if aux == True:
        print('Arquivo ' + ticker + '_' + ano + '_' + demon + '.csv'' gerado com sucesso!!!')
    else:
        print("Falha na cópia do arquivo!!! / Arquivo ja existente")


def busca_demon(ticker, ano, demon):  # Busca de um relatorio a partir de ticker + ano + demonstrativo
    if demon == 'DR':
        body(ticker, ano, demon,
             'tUgYN4_k8zKU')  # gera DR --> passa como parametro o codigo para execucao do projeto DR (tUgYN4_k8zKU)

    elif demon == 'BPA':
        body(ticker, ano, demon, 'tStJKRY4WWN_')  # gera BPA

    elif demon == 'BPP':
        body(ticker, ano, demon, 't3fX3x4OODkW')  # gera BPP

    elif demon == 'DFC':
        body(ticker, ano, demon, 'tD1m6nCLOBRu')  # gera DFC

    else:
        print('Demonstrativo nao encontrado...')
        print('Digite: DR para Demonstracao dos Resultados')
        print('Digite: BPA para Balanco Patrimonial Ativo')
        print('Digite: BPP para Balanco Patrimonial Passivo')
        print('Digite: DFC para Demonstração de Fluxos de Caixa')
        return


def conj_demon(ticker, ano_ini, ano_fim):  # Busca conjunto de demonstrativos, executando a busca individual para todos demons de 2015 a 2019
    for ano in range(ano_ini, ano_fim + 1, 1):
        ano = str(ano)
        body(ticker, ano, 'BPA', 'tStJKRY4WWN_')
        body(ticker, ano, 'BPP', 't3fX3x4OODkW')
        body(ticker, ano, 'DR', 'tUgYN4_k8zKU')
        body(ticker, ano, 'DFC', 'tD1m6nCLOBRu')


def demonstrativo_cvm(ticker, cod_cvm, ano, trim, versao, demon):
    if demon == 'DR':
        token = 'tUgYN4_k8zKU'
    elif demon == 'BPA':
        token = 'tStJKRY4WWN_'
    elif demon == 'BPP':
        token = 't3fX3x4OODkW'
    elif demon == 'DFC':
        token = 'tD1m6nCLOBRu'

    doc = busca_doc_cvm(cod_cvm, ano, trim, versao)
    if doc == 0:
        print('Demonstrativo nao encontrado')
        return

    dados = demonstrativo(token, doc)  # faz a busca do demonstrativo a utilizando a API
    aux = escreve_arquivo(ticker, ano, demon, dados)  # salva o demonstrativo em um arquivo csv
    if aux == True:
        print('Arquivo ' + ticker + '_' + ano + '_' + demon + '.csv'' gerado com sucesso!!!')
    else:
        print("Falha na cópia do arquivo!!! / Arquivo ja existente")


if __name__ == '__main__':
    print("                                                                           v2.0.1  ")
    print("_________________________________________________________________________________  ")
    print()
    while True:
        print("__________________________ DOWNLOAD DE DEMONSTRATIVOS ___________________________")
        print()
        print('1- Demonstrativo individual por ano')
        print('2- Conjunto de demonstrativos (DR + BPA + BPP + DFC (2015-2019))')
        print('3- Demonstrativo individual por codigo cvm')
        print()
        print("________________________________ OUTRAS FUNCOES _________________________________")
        print()
        print('4- Listar empresas disponíveis para consulta')
        print('5- Analise Fundamentalista (Balanço Gerencial + Analise de Liquidez)')
        print('6- Sair do programa')
        print("_________________________________________________________________________________")
        print()
        modo = int(input('Opção:'))
        print()
        if modo == 1:
            while True:
                ticker = input("\nTicker: ")
                if len(ticker) < 1: break
                ano = input("Ano: ")
                demon = input("Demonstrativo: ")
                busca_demon(ticker, ano, demon)

        elif modo == 2:
            ticker = input('Ticker:')
            print('Periodo:')
            ano_ini = int(input('\tAno incial:'))
            ano_fim = int(input('\tAno final:'))
            conj_demon(ticker, ano_ini, ano_fim)
            print("Todos os demonstrativos foram baixados!!!")
            print("Encerrando o programa...")
            exit()

        elif modo == 3:
            print("Para busca do codigo CVM:")
            print("https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx\n")
            ticker = input('Ticker: ')
            cod_cvm = input('Codigo CVM: ')
            ano = input('Ano: ')
            trim = input('Trimestre: ')
            versao = input('Versão: ')
            demon = input('Demonstrativo: ')
            demonstrativo_cvm(ticker, cod_cvm, ano, trim, versao, demon)

        elif modo == 4:
            disponiveis()
            print('\n\n')

        elif modo == 5:
            ticker = input('Ticker: ')
            print('Periodo:')
            ano_ini = int(input('\tAno Inicial: '))
            ano_fim = int(input('\tAno final: '))
            analise_fundamentalista(ticker, ano_ini, ano_fim)

        elif modo == 6:
            print('Encerrando o programa...')
            exit()

        else:
            print('Opção Invalida')
            exit()
