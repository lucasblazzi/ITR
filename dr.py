import requests

#89272 - 2019 Embraer


#Request para iniciar o projeto
def demonstrativo(token):
    params = {
      "api_key": "t14QhaR-0UJq",
      "start_url": "https://www.rad.cvm.gov.br/ENETCONSULTA/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=89272&CodigoTipoInstituicao=2",
    }
    r = requests.post('https://www.parsehub.com/api/v2/projects/'+token+'/run', data=params)
    print(r.text)

    #Request para pegar raw data do projeto iniciado anteriormente
    params = {
      "api_key": "t14QhaR-0UJq",
      "format": "json",
    }
    dr = requests.get('https://www.parsehub.com/api/v2/projects/'+token+'/last_ready_run/data', params=params)
    print(dr.text)

def main():

    print("--------------------------------------------------------------------")
    print("                     RELATORIOS HISTORICOS B3"                       )
    print("--------------------------------------------------------------------")
    print()

    while True:
        ticker = input("Ticker: ")
        ano = input("Ano: ")
        demon = input("Demonstrativo: ")

        if (demon == 'dr'):                     # tUgYN4_k8zKU eh o token do projeto para DR
            demonstrativo('tUgYN4_k8zKU',);
#        elif (demon == 'bpa' or demon = 'BPA'):
#        elif (demon == 'bpp' or demon = 'BPP'):
#        else:
#            print('Demonstrativo nao encontrado.')
#            print('Digite: DR para Demonstracao dos Resultados')
#            print('Digite: BPA para Balanco Patrimonial Ativo')
#            print('Digite: BPP para Balanco Patrimonial Passivo')
#            continue;
main()
