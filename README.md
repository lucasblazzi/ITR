## projeto_b3 -> Dados Históricos
 * O projeto foi desenvolvido para automatização na análise de investimentos a partir de dados históricos como: Demonstração de Resultado, Balanço Patrimonial Ativo, Balanço Patrimonial Passivo e Demonstrações de Fluxo de Caixa.
 * Esse programa foi construído para a matéria SIN311 - Contabilidade em Informática (UNIFEI - Sistemas da Informação)

 No momento estão disponíveis os dados das empresas:
 * **MGLU3** - MAGAZINE LUIZA S.A.
 * **EMBR3** - EMBRAER S.A.
 * **CVCB3** - CVC BRASIL OPERADORA E AGÊNCIA DE VIAGENS S.A.
 * **LREN3** - LOJAS RENNER S.A.
 * **OIBR4** - OI S.A.
 * **CGAS5** - CIA GAS DE SAO PAULO - COMGAS
 * **VVAR3** - VIA VAREJO S.A.
 * **WHRL3** - WHIRLPOOL S.A.


### Requirements
 * **[Python 3.x](https://www.python.org/downloads/)**
 * **requests -> (no cmd execute o comando: pip install requests)**
 * **pandas -> pip install pandas**
 * time -> pip install time
 * sys -> pip install sys
 * **Microsoft Excel 2016**

### Arquivos do diretório
  * **Macros Excel** - Essa pasta contem os códigos raw para utilizção no excel
      1. BP_INDIVIDUAL - Formata os arquivos **individuais** de Balanço Patrimonial (BPA e BPP)
      2. DR_DFC_INDIVIDUAL - Formata os arquivos **individuais** de Demonstração de Resultados (DR) e Demonstração de Fluxos de Caixa (DFC)
      3. BP_COMP - Formata os arquivos **compilados** de Balanço Patrimonial (BPA e BPP)
      4. DR_DFC_COMP - Formata os arquivos **compilados** de Demonstração de Resultados (DR) e Demonstração de Fluxos de Caixa (DFC)
  * **base_doc.py** - Dados utilizados para buscar os demonstrativos financeiros de cada empresa.
      1. Para adicionar um novo dado basta seguir o template nos arquivos
      2. No site da b3 cada empresa em determinado ano possui uma variavel chamada NumeroSequencialDocumento que pode ser encontrada na URL do demonstrativo
  * **dados_historicos.py** - Programa principal - pode ser executado no cmd/terminal > python dados_historicos.py

### Passo a Passo
  1. **Execução do programa:**
      1. Navegue até o direório onde o programa foi baixado
      2. Executar o programa a partir do cmd/terminal com o comando --> python dados_historicos.py
          1. Os dados da empresa são disponibilizados a partir do ticker referente.
          2. As empresas/tickers disponíveis para consulta estão listadas na Opção 3 do programa.
          3. O programa permite a busca dos demonstrativos a partir de abreviações (ex: DR, BPA, BPP, DFC) dos anos: 2015-2019
      3. A execução correta do programa resultará em um ou mais arquivos csv.
      4. O arquivo csv gerado é entitulado como ticker_ano_demonstrativo.csv (ex: MGLU3_2019_DR)
  2. **Opções de Execução**
      1. 1- Demonstrativo individual por ano
          1. Será solicitado ticker, ano e demonstrativo
          2. O resultado será um arquivo contendo o demonstrativo individual do período solicitado
      2. 2- Conjunto de demonstrativos (DR + BPA + BPP + DFC (2015-2019))
          1. Será solicitado o ticker da empresa.
          2. O resultado será o conjunto de todos os demonstrativos individuais em todos os períodos (total de 20 arquivos)
      3. 3- Listar empresas disponíveis para consulta
          1. Essa opção retornará todas as empresas disponiveis para consulta
      4. 4- Compilar demonstrativos
          1. Após a execução da opção 2 (Conjunto de demonstrativos) será possível compilar os resultados por demonstrativo
          2. O resultado será um arquivo unico do demonstrativo solicitado, contendo as contas até o terceiro nível de todos os anos

   | Execução do programa |
   | :------: |
   | ![Execução do programa](GIF/execucao.gif) |
  3. **Formatação Excel**
      1. O projeto acompanha macros do excel para uma formatação automática dos arquivos gerados
      2. Importe as macros para seu Excel
      3. Para arquivos excel referentes ao demonstrativo:
          * BPP ou BPA individuais: utilizar a macro BP_INDIVIDUAL
          * DR ou DFC individuais: utilizar a macro DR_DFC_INDIVIDUAL
          * BPP ou BPA compilados: utilizar a macro BP_COMP
          * DR ou DFC compilados: utilizar a macro DR_DFC_COMP

  | Aplicação da macro |
  | :------: |
  ![Aplicação da macro](GIF/excel.gif)

### Doações
  Se o programa for útil, você pode contribuir para o pagamento do meu voucher para a certificação Security+
  [![paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Y7SXJE4L8GZXW&source=url)
