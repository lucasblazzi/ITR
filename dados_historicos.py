import requests
import json
import time
#89272 - 2019 Embraer

def escreve_arquivo(ticker,ano,demon,dados):
    f = (open(ticker+'_'+ano+'_'+demon+'.json', "x"))
    f.write(dados)
    return True



def demonstrativo(token):                                                       #Request para iniciar o projeto
    params = {
      "api_key": "t14QhaR-0UJq",
      "start_url": "https://www.rad.cvm.gov.br/ENETCONSULTA/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=89272&CodigoTipoInstituicao=2",
    }
    r = requests.post('https://www.parsehub.com/api/v2/projects/'+token+'/run', data=params)
    print(r.text)
    print()
    print("Importando os dados...")
    time.sleep(3)


    params = {                                                                  #Request para pegar raw data do projeto iniciado anteriormente
      "api_key": "t14QhaR-0UJq",
      "format": "json",
    }
    demo = requests.get('https://www.parsehub.com/api/v2/projects/'+token+'/last_ready_run/data', params=params)
    print(demo.text)
    dados = demo.text
    return dados



def main():

    print("--------------------------------------------------------------------")
    print("                     RELATORIOS HISTORICOS B3"                       )
    print("--------------------------------------------------------------------")
    print()

    while True:
        ticker = input("Ticker: ")
        ano = input("Ano: ")
        demon = input("Demonstrativo: ")

        if (demon == 'dr' or demon == 'DR'):                                                     # tUgYN4_k8zKU = token do projeto DR
            dados = demonstrativo('tUgYN4_k8zKU')
            aux = escreve_arquivo(ticker,ano,demon,dados)
            if aux == True:
                print('Arquivo '+ticker+'_'+ano+'_'+demon+' gerado com sucesso!!!')
            else:
                print('Problema ao gerar arquivo!!!')

        elif (demon == 'bpa' or demon == 'BPA'):                                 # tStJKRY4WWN_ = token do projeto BPA
            dados = demonstrativo('tStJKRY4WWN_')
            aux = escreve_arquivo(ticker,ano,demon,dados)
            if aux == True:
                print('Arquivo '+ticker+'_'+ano+'_'+demon+' gerado com sucesso!!!')
            else:
                print('Problema ao gerar arquivo!!!')

        elif (demon == 'bpp' or demon == 'BPP'):                                 # t3fX3x4OODkW = token do projeto BPP
            dados =demonstrativo('t3fX3x4OODkW')
            aux = escreve_arquivo(ticker,ano,demon,dados)
            if aux == True:
                print('Arquivo '+ticker+'_'+ano+'_'+demon+' gerado com sucesso!!!')
            else:
                print('Problema ao gerar arquivo!!!')

        elif(demon == 'sair'):
            break;
        else:
            print('Demonstrativo nao encontrado...')
            print('Digite: DR para Demonstracao dos Resultados')
            print('Digite: BPA para Balanco Patrimonial Ativo')
            print('Digite: BPP para Balanco Patrimonial Passivo')
            print('Digite: sair para encerrar o programa')
            continue;


main()
