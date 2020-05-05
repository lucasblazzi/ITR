## projeto_b3 -> Dados Históricos
 * O projeto foi desenvolvido para automatização na análise de investimentos a partir de dados históricos como: Demonstração de Resultado, Balanço Patrimonial Ativo e Balanço Patrimonial Passivo.
 * Esse programa foi construído para a matéria SIN311 - Contabilidade em Informática (UNIFEI - Sistemas da Informação)

 No momento estão disponíveis os dados das empresas:
 * MGLU3 - MAGAZINE LUIZA S.A.
 * EMBR3 - EMBRAER S.A.
 * CVCB3 - CVC BRASIL OPERADORA E AGÊNCIA DE VIAGENS S.A.
 * LREN3 - LOJAS RENNER S.A.
 * OIBR4 - OI S.A.
 * CGAS5 - CIA GAS DE SAO PAULO - COMGAS


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
  6. O programa é executado a com a entrada do usuário em três parâmetros (ticker, ano, demonstrativo).
  7. A execução correta do programa resultará em um arquivo csv.
  8. O arquivo csv é entitulado como ticker_ano_demonstrativo.csv (ex: MGLU3_2019_DR)
  9. O projeto acompanha o VBA do excel para uma formatação automática.
