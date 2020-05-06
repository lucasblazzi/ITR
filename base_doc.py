def busca_doc(ticker, ano):                                                     #ATRIBUI O NUMERO SEQUENCIAL DOCUMENTO PARA CONSULTA B3 --> VALORES TESTE
    doc = 666
    ano = int(ano)
    if ticker == 'MGLU3':                                                       #os documentos sao organizados pela b3 a partir do parametro - NumeroSequencialDocumento - variando conforme o periodo requisitado
        if ano == 2019:
            doc = 88872
        elif ano == 2018:
            doc = 78649
        elif ano == 2017:
            doc = 69380
        elif ano == 2016:
            doc = 60258
        elif ano == 2015:
            doc = 51427

    elif ticker == 'VVAR3':
        if ano == 2019:
            doc = 86693
        elif ano == 2018:
            doc = 78262
        elif ano == 2017:
            doc = 69261
        elif ano == 2016:
            doc = 60200
        elif ano == 2015:
            doc = 60197

    elif ticker == 'WHRL3' or ticker == 'WHRL4':
        if ano == 2019:
            doc = 89496
        elif ano == 2018:
            doc = 79193
        elif ano == 2017:
            doc = 69989
        elif ano == 2016:
            doc = 60192
        elif ano == 2015:
            doc = 51375

    elif ticker == 'EMBR3':
        if ano == 2019:
            doc = 89272
        elif ano == 2018:
            doc = 78362
        elif ano == 2017:
            doc = 69302
        elif ano == 2016:
            doc = 60257
        elif ano == 2015:
            doc = 51106

    elif ticker == 'CVCB3':
        if ano == 2019:
            doc = 89180
        elif ano == 2018:
            doc = 89180
        elif ano == 2017:
            doc = 69574
        elif ano == 2016:
            doc = 60355
        elif ano == 2015:
            doc = 51552

    elif ticker == 'LREN3':
        if ano == 2019:
            doc = 88815
        elif ano == 2018:
            doc = 78277
        elif ano == 2017:
            doc = 69238
        elif ano == 2016:
            doc = 60148
        elif ano == 2015:
            doc = 51050

    elif ticker == 'OIBR4':
        if ano == 2019:
            doc = 89882
        elif ano == 2018:
            doc = 79177
        elif ano == 2017:
            doc = 69856
        elif ano == 2016:
            doc = 60577
        elif ano == 2015:
            doc = 51559

    elif ticker == 'CGAS5':
        if ano == 2019:
            doc = 89079
        elif ano == 2018:
            doc = 78699
        elif ano == 2017:
            doc = 69534
        elif ano == 2016:
            doc = 60248
        elif ano == 2015:
            doc = 51335

    else:
        print("Dado não encontrado na base de dados")
        exit()
    return doc


def disponiveis():
    print('* MGLU3 - MAGAZINE LUIZA S.A.')
    print('* EMBR3 - EMBRAER S.A.')
    print('* CVCB3 - CVC BRASIL OPERADORA E AGÊNCIA DE VIAGENS S.A.')
    print('* LREN3 - LOJAS RENNER S.A.')
    print('* OIBR4 - OI S.A.')
    print('* CGAS5 - CIA GAS DE SAO PAULO - COMGAS')
    print('* VVAR3 - VIA VAREJO S.A.')
    print('* WHRL3 - WHIRLPOOL S.A.')
