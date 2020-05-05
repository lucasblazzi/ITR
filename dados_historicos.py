import requests
import json
import time


def busca_doc(ticker, ano):         #ATRIBUI O NUMERO SEQUENCIAL DOCUMENTO PARA CONSULTA B --> VALORES TESTE
    doc = 666
    ano = int(ano)
    if ticker == 'MGLU3':
        if ano == 2019:
            doc = 88872
        elif ano == 2017:
            doc = 69380
        elif ano == 2015:
            doc = 51427

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



def escreve_arquivo(ticker,ano,demon,dados):
    f = (open(ticker+'_'+ano+'_'+demon+'.csv', "x"))
    f.write(dados)
    return True



def demonstrativo(token, doc):                                                                            #Request para iniciar o projeto
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
    time.sleep(20)


    params = {                                                                  #Request para pegar raw data do projeto iniciado anteriormente
      "api_key": "t14QhaR-0UJq",
      "format": "csv",
    }
    demo = requests.get('https://www.parsehub.com/api/v2/runs/'+run_token+'/data', params=params)
    #print('https://www.parsehub.com/api/v2/runs/'+run_token+'/data')
    print(demo.text)
    dados = demo.text
    return dados



def main():

    print("--------------------------------------------------------------------")
    print("                     RELATORIOS HISTORICOS B3"                       )
    print("--------------------------------------------------------------------")
    print("Disponiveis: MGLU3 - EMBR3 - CVCB3 - LREN3 - OIBR4 - CGAS5")
    print()

    while True:
        ticker = input("Ticker: ")
        ano = input("Ano: ")
        demon = input("Demonstrativo: ")
        if demon == 'dr' or demon == 'DR':                                                     # tUgYN4_k8zKU = token do projeto DR
            doc = busca_doc(ticker, ano)
            dados = demonstrativo('tUgYN4_k8zKU', doc)
            aux = escreve_arquivo(ticker,ano,demon,dados)
            if aux == True:
                print('Arquivo '+ticker+'_'+ano+'_'+demon+' gerado com sucesso!!!')
            else:
                print('Problema ao gerar arquivo!!!')

        elif demon == 'bpa' or demon == 'BPA':                                 # tStJKRY4WWN_ = token do projeto BPA
            doc = busca_doc(ticker, ano)
            dados = demonstrativo('tStJKRY4WWN_', doc)
            aux = escreve_arquivo(ticker,ano,demon,dados)
            if aux == True:
                print('Arquivo '+ticker+'_'+ano+'_'+demon+' gerado com sucesso!!!')
            else:
                print('Problema ao gerar arquivo!!!')

        elif demon == 'bpp' or demon == 'BPP':                                 # t3fX3x4OODkW = token do projeto BPP
            doc = busca_doc(ticker, ano)
            dados = demonstrativo('t3fX3x4OODkW', doc)
            aux = escreve_arquivo(ticker,ano,demon,dados)
            if aux == True:
                print('Arquivo '+ticker+'_'+ano+'_'+demon+'.csv'' gerado com sucesso!!!')
            else:
                print('Problema ao gerar arquivo!!!')

        elif demon == 'sair':
            break;
        else:
            print('Demonstrativo nao encontrado...')
            print('Digite: DR para Demonstracao dos Resultados')
            print('Digite: BPA para Balanco Patrimonial Ativo')
            print('Digite: BPP para Balanco Patrimonial Passivo')
            print('Digite: sair para encerrar o programa')
            continue;


main()
