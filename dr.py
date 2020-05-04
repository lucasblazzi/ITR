import requests

#89272 - 2019 Embraer
#DEMONSTRACAO DOS RESULTADOS - DR

#Request para iniciar o projeto
def dr():
    params = {
      "api_key": "t14QhaR-0UJq",
      "start_url": "https://www.rad.cvm.gov.br/ENETCONSULTA/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=89272&CodigoTipoInstituicao=2",
    }
    r = requests.post('https://www.parsehub.com/api/v2/projects/tUgYN4_k8zKU/run', data=params)
    print(r.text)


    #Request para pegar raw data do projeto iniciado anteriormente
    params = {
      "api_key": "t14QhaR-0UJq",
      "format": "json",
    }
    dr = requests.get('https://www.parsehub.com/api/v2/projects/tUgYN4_k8zKU/last_ready_run/data', params=params)
    print(dr.text)


print("--------------------------------------------------------------------")
print("                     RELATORIOS HISTORICOS B3")
print("--------------------------------------------------------------------")
