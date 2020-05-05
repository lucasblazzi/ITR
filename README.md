## projeto_b3 -> Dados Históricos
 Projeto para importar dados históricos b3


### Requirements
 Python 3.x
 requests  -> pip install requests
 time      -> pip install time

 [ParseHub](https://www.parsehub.com/) - Utilizado para crawl dos dados AJAX


### Passo a Passo
  1. Criar conta no ParseHub (fazer download da aplicação ou utilizar a versão online).
  2. Após a criação da conta no ParseHub, você possuirá uma api_key.
  3. Adicionar sua key em todas as variaveis api_key do arquivo dados_historicos.py.
  4. Importar os projetos para sua conta ParseHub - os três projetos utilizados estão na pasta parsehub_projetos.
  5. Caso necessário, substituir os tokens do projeto no arquivo dados_historicos.py.
    ** dados = demonstrativo('t3fX3x4OODkW', doc)   --> token : t3fX3x4OODkW
  6. O programa é executado a com a entrada do usuário em três parâmetros (ticker, ano, demonstrativo).
  7. A execução correta do programa resultará em um arquivo csv.
  8. O arquivo csv é entitulado como ticker_ano_demonstrativo.csv (ex: MGLU3_2019_DR)
  9. O projeto acompanha o VBA do excel para uma formatação automática.
