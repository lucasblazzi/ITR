import pandas as pd
import xlsxwriter

#arquivo csv headers - Conta_numero, Conta_descricao, Conta_data1, Conta_data2
def compila_demon(ticker, demon, ano_ini, ano_fim):
    ano  = ano_fim
    frames = list()

    while ano != ano_ini:
        try:
            df = pd.read_csv(ticker+'_'+str(ano)+'_'+demon+'.csv', encoding='ANSI', header=0)
        except:
            print('\nDemonstrativo não encontrado. Certifique-se de que os demonstrativos requisitados já foram baixados!\n\n')
            return;

        contanivel = df[df.Conta_numero.map(len)<=7]                            #seleciona contas ate o terceiro nivel      (ex: 1.0.1 - 3 niveis /// 1.1 - 2 niveis)
        if ano == ano_fim:
            column_data = contanivel[['Conta_numero', 'Conta_descricao', 'Conta_data1', 'Conta_data2']]         #monta a base da tabela baseando-se na conta do ultimo ano      --> opt2 --> column_data = contanivel.iloc[:, 0:4]
        else:
            column_data = contanivel['Conta_data2']                                #adiciona somente a coluna referente ao ano especifico

        column_data = column_data.reset_index(drop=True)                        #reseta os indices das linhas, ja que a linha 110 deixa os indices desordenados
        frames.append(column_data)                                              #salva o dataframe em uma lista para compilação posterior
        ano = ano - 1

    result = pd.concat(frames, ignore_index=True, axis=1)          #axis=1 --> concatena como coluna
    result.to_csv(ticker+'_'+demon+'.csv', header=False, index=False, encoding='ANSI')
    return result



def busca_dado(conta, qtd_columns, bp_df):
    for index, row in bp_df.iterrows():
        if bp_df.iloc[index,1] == conta:
            lista = []
            for i in range(2,qtd_columns+2,1):
                dado = bp_df.iloc[index,i]
                lista.append(dado)
            return lista


def balanco_gerencial(ticker, ano_ini, ano_fim):
    bpa_df = compila_demon(ticker, 'BPA', ano_ini, ano_fim)         #armazena os dataframes de bpa e bpp
    bpp_df = compila_demon(ticker, 'BPP', ano_ini, ano_fim)
    bpa_df.fillna(0, inplace=True)                                  #substitui valores NaN para 0
    bpp_df.fillna(0, inplace=True)
    qtd_columns = ano_fim - ano_ini + 1                             #calcula a quantidade de anos inseridos
    print(bpa_df)
    print(bpp_df)

    #busca dados utilizados para calcular os atributos utilizados na analise dos demonstrativos
    caixa_equiv = busca_dado('Caixa e Equivalentes de Caixa', qtd_columns, bpa_df)
    aplic_fin = busca_dado('Aplicações Financeiras', qtd_columns, bpa_df)
    ativo_Ncirc = busca_dado('Ativo Não Circulante', qtd_columns, bpa_df)
    ativo_circ = busca_dado('Ativo Circulante', qtd_columns, bpa_df)
    passivo_circ = busca_dado('Passivo Circulante', qtd_columns, bpp_df)
    emprest_Financ = busca_dado('Empréstimos e Financiamentos', qtd_columns, bpp_df)
    passivo_Ncirc = busca_dado('Passivo Não Circulante', qtd_columns, bpp_df)
    pl_cons = busca_dado('Patrimônio Líquido Consolidado', qtd_columns, bpp_df)

    #define as listas que armazenarao os dados calculados
    ncg = list()
    caixa_Equiv = list()
    ativ_fix_liq = list()
    cap_inv_total = list()
    div_curto = list()
    financ_longo = list()
    div_longo = list()
    patri_acion = list()
    capital_total = list()
    ativo_circ_op = list()
    passivo_circ_op = list()

    # calcula os atributos utilizados na composicao da analise
    for i in range(qtd_columns):
        caixa_Equiv.append( int(str(caixa_equiv[i]).replace('.','')) + int(str(aplic_fin[i]).replace('.','')) )
        ativo_circ_op.append( int(str(ativo_circ[i]).replace('.','')) - int(str(caixa_equiv[i]).replace('.','')) - int(str(aplic_fin[i]).replace('.','')))
        passivo_circ_op.append(int(str(passivo_circ[i]).replace('.','')) - int(str(emprest_Financ[i]).replace('.','')))
        ncg.append(ativo_circ_op[i] - passivo_circ_op[i])
        ativ_fix_liq.append(int(str(ativo_Ncirc[i]).replace('.','')))
        cap_inv_total.append(caixa_Equiv[i] + ncg[i] + ativ_fix_liq[i])
        div_curto.append(int(str(emprest_Financ[i]).replace('.','')))
        div_longo.append(int(str(passivo_Ncirc[i]).replace('.','')))
        patri_acion.append(int(str(pl_cons[i]).replace('.','')))
        financ_longo.append(div_longo[i] + patri_acion[i])
        capital_total.append(div_curto[i] + financ_longo[i])


    # adiciona o nome do atributo na posicao 0 da lista de dados
    caixa_Equiv.insert(0,'Caixa e Equivalentes de Caixa')
    ncg.insert(0, 'Necessidades de Capital de Giro (NCG)')
    ativ_fix_liq.insert(0, 'Ativos Fixos Liquidos')
    cap_inv_total.insert(0, 'Capital Investido Total ou Ativos Liquidos Totais')
    div_curto.insert(0, 'Dívidas de Curto Prazo')
    financ_longo.insert(0, 'Financiamento de Longo Prazo')
    div_longo.insert(0, 'Dívidas de Longo prazo')
    patri_acion.insert(0, 'Patrimônio dos Acionistas')
    capital_total.insert(0, 'Capital Aplicado Total')
    ativo_circ_op.insert(0,'Ativo Circulante Operacional')
    passivo_circ_op.insert(0, 'Passivo Circulante Operacional')


#montando a tabela de balanco gerencial
    bg = bpa_df.head(1)                                 # clona a primeira linha do df anterior
    bg = bg.drop(columns=[0])                            # tira a coluna de numero de conta
    bg[1] = 'Capital Investido ou Ativos Líquidos'      #substitui o Conta_descricao
    #aloca os dados na planilha balanço gerencial
    bg.loc[1] = caixa_Equiv
    bg.loc[2] = ncg
    bg.loc[3] = ativ_fix_liq
    bg.loc[4] = cap_inv_total
    bg.loc[5] = bg.iloc[0]              #copia a linha 0
    bg.iloc[5,0] = 'Capital Aplicado ou Fontes de Recursos' #substitui o primeiro termo da linha 0
    bg.loc[6] = div_curto
    bg.loc[7] = financ_longo
    bg.loc[8] = div_longo
    bg.loc[9] = patri_acion
    bg.loc[10] = capital_total
    bg.loc[11] = ativo_circ_op
    bg.loc[12] = passivo_circ_op
    print(bg)


# montando tabela de analise de liquidez
    liq_df = bpa_df.head(1)
    liq_df = liq_df.drop(columns=[0])
    liq_df[1] = 'Medidas de Liquidez Tradicionais'

    print(liq_df)




    writer = pd.ExcelWriter('Analise_'+ticker+'.xlsx', engine='xlsxwriter')
    bpa_df.to_excel(writer, sheet_name='BPA_'+ticker, encoding='ANSI', header=False, index=False)
    bpp_df.to_excel(writer, sheet_name='BPP_'+ticker, encoding='ANSI', header=False, index=False)
    bg.to_excel(writer, sheet_name='BG_'+ticker, encoding='ANSI', header=False, index=False)

    writer.save()






############################## DADOS BUSCADOS NO BPA / BPP ##############################
#    caixa_equiv            - Caixa e Equivalente de Caixa             --> Conta (BPA)
#    aplic_fin              - Aplicações Financeiras                   --> Conta (BPA)
#    ativo_Ncirc            - Ativo Não Circulante                     --> Conta (BPA)
#    ativo_circ             - Ativo Circulante                         --> Conta (BPA)
#    passivo_circ           - Passivo Circulante                       --> Conta (BPP)
#    emprest_Financ         - Empréstimos e Financiamentos (curto)     --> Conta (BPP)
#    passivo_Ncirc          - Passivo Não Circulante                   --> Conta (BPP)
#    pl_cons                - Patrimonio Liquido Consolidado           --> Conta (BPP)
##########################################################################################


######################################################################### DADOS PARA ANALISE #############################################################################
#    ncg                    - Necessidade de Capital de Giro           --> Ativo Circulante Operacional - Passivo Circulante Operacional
#    caixa_Equiv            - Caixa e Equivalente de Caixa             --> BPA('Caixa e Equivalentes de Caixa') + BPA('Aplicações Financeiras')
#    ativ_fix_liq           - Ativos Fixos Liquidos                    --> BPA('Ativo Não Circulante')
#    cap_inv_total          - Capital Investido Total                  --> Caixa e Equivalentes de Caixa + Necessidades de Capital de Giro + Ativos Fixos Liquidos
#    div_curto              - Dividas de Curto Prazo                   --> BPP('Empréstimos e Financiamentos') [no Passivo Circulante]
#    financ_longo           - Financiamento de Longo Prazo             --> Dividas de Longo prazo + Patrimonio dos Acionistas
#    div_longo              - Dividas de Longo Prazo                   --> BPP('Passivo Não Circulante')
#    patri_acion            - Patrimonio dos Acionistas                --> BPP('Patrimônio Líquido Consolidado')
#    capital_total          - Capital Aplicado Total                   --> Dividas de Curto Prazo + Financiamento de Longo Prazo
#    ativo_circ_op          - Ativo Circulante Operacional             --> BPA('Ativo Circulante') - BPA('Caixa e Equivalentes de Caixa') - BPA('Aplicações Financeiras')
#    passivo_circ_op        - Passivo Circulante Operacional           --> BPP('Passivo Circulante') - BPP('Empréstimos e Financiamentos')
###########################################################################################################################################################################
