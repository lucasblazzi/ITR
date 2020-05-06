import requests
import time
import sys

def busca_doc(ticker, ano):                                                     #ATRIBUI O NUMERO SEQUENCIAL DOCUMENTO PARA CONSULTA B --> VALORES TESTE
    doc = 666
    ano = int(ano)
    if ticker == 'MGLU3':                                                       #os documentos sao organizados pela b3 a partir do parametro - NumeroSequencialDocumento - variando conforme o periodo requisitado
        if ano == 2019:
            doc = 88872
        elif ano == 2017:
            doc = 69380
        elif ano == 2015:
            doc = 51427

    elif ticker == 'VVAR3':
        if ano == 2019:
            doc = 86693
        elif ano == 2017:
            doc = 69261
        elif ano == 2015:
            doc = 60197

    elif ticker == 'WHRL3' or ticker == 'WHRL4':
        if ano == 2019:
            doc = 89496
        elif ano == 2017:
            doc = 69989
        elif ano == 2015:
            doc = 51375

    elif ticker == 'EMBR3':
        if ano == 2019:
            doc = 89272
        elif ano == 2017:
            doc = 69302
        elif ano == 2015:
            doc = 51106

    elif ticker == 'CVCB3':
        if ano == 2019:
            doc = 89180
        elif ano == 2017:
            doc = 69574
        elif ano == 2015:
            doc = 51552

    elif ticker == 'LREN3':
        if ano == 2019:
            doc = 88815
        elif ano == 2017:
            doc = 69238
        elif ano == 2015:
            doc = 51050

    elif ticker == 'OIBR4':
        if ano == 2019:
            doc = 89882
        elif ano == 2017:
            doc = 69856
        elif ano == 2015:
            doc = 51559

    elif ticker == 'CGAS5':
        if ano == 2019:
            doc = 89079
        elif ano == 2017:
            doc = 69534
        elif ano == 2015:
            doc = 51335
    return doc

def animation():                                                                #funcao encontrada pronta
    print("Buscando arquivo:")
    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(3)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


def escreve_arquivo(ticker,ano,demon,dados):                                    #salva a saida de dados no arquivo csv com nome ticker_ano_demon.csv
    f = (open(ticker+'_'+ano+'_'+demon+'.csv', "x"))
    f.write(dados)
    return True


def demonstrativo(token, doc):                                                  #Request para iniciar o projeto
    doc = str(doc)
    params = {
      "api_key": "t14QhaR-0UJq",
      "start_url": "https://www.rad.cvm.gov.br/ENETCONSULTA/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento="+doc+"&CodigoTipoInstituicao=2",
    }
    r = requests.post('https://www.parsehub.com/api/v2/projects/'+token+'/run', data=params)
    #print(r.text)
    run_token = str(r.text[15:27])
    print()
    print("Importando os dados...")
    print("(Aproximadamente 20 segundos)")
    animation()
#    time.sleep(30)


    params = {                                                                  #Request para pegar raw data do projeto iniciado anteriormente
      "api_key": "t14QhaR-0UJq",
      "format": "csv",
    }
    demo = requests.get('https://www.parsehub.com/api/v2/runs/'+run_token+'/data', params=params)
    #print('https://www.parsehub.com/api/v2/runs/'+run_token+'/data')
    print(demo.text)
    dados = demo.text
    return dados



def body(ticker, ano, demon, token):
    doc = busca_doc(ticker, ano)
    dados = demonstrativo(token, doc)
    aux = escreve_arquivo(ticker,ano,demon,dados)
    if aux == True:
        print('Arquivo '+ticker+'_'+ano+'_'+demon+'.csv'' gerado com sucesso!!!')
    else:
        print("Falha na cópia do arquivo!!!")


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
        print('Digite: sair para encerrar o programa')
        return


def modo2(ticker):
    ano = 2015
    for ano in range(2015, 2020, 2):
        ano = str(ano)
        body(ticker, ano, demon, 'tUgYN4_k8zKU')        #gera DR
        body(ticker, ano, demon, 'tStJKRY4WWN_')        #gera BPA
        body(ticker, ano, demon, 't3fX3x4OODkW')        #gera BPP
        body(ticker, ano, demon, 'tD1m6nCLOBRu')        #gera DFC



def main():

    print("---------------------------------------------------------------------------------")
    print("                            RELATORIOS HISTORICOS B3"                             )
    print("---------------------------------------------------------------------------------")
    print("Disponiveis: MGLU3 - EMBR3 - CVCB3 - LREN3 - OIBR4 - CGAS5 - VVAR3 - WHRL3/WHRL4")
    print()


    print('1- Demonstrativo em um periodo')
    print('2- Conjunto de demonstrativos (DR + BPA + BPP + DFC --> 6 anos)')
    modo = int(input('Opção:'))
    if modo == 1:
        while True:
            ticker = input("Ticker: ")
            ano = input("Ano: ")
            demon = input("Demonstrativo: ")
            modo1(ticker,ano,demon)

    elif modo == 2:
        ticker = input('Ticker:')
        modo2(ticker)

    else:
        print('Opção Invalida')
        exit()

main()
