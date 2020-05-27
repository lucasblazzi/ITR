import sqlite3

conn = sqlite3.connect('demonstrativos.db')
cur = conn.cursor()

def busca_doc(ticker, ano):
	cur.execute('SELECT num_doc FROM Demonstrativos WHERE ticker = ? AND ano = ? ', (ticker,ano, ))			#SELECT num_doc FROM Demonstrativos WHERE nome_empresa LIKE ? AND ano = ?
	try:
		return cur.fetchone()[0]
	except TypeError:
		return 0

def disponiveis():
    print('* MGLU3 - MAGAZINE LUIZA S.A.')
    print('* VVAR3 - VIA VAREJO S.A.')
    print('* WHRL3 - WHIRLPOOL S.A.')
    print('* LREN3 - LOJAS RENNER S.A.')
    print('* CGAS5 - CIA GAS DE SAO PAULO - COMGAS')
    print('* OIBR4 - OI S.A.')
    print('* TIMP3 - TIM PARTICIPACOES S.A.')
    print('* VIVT3 - TELEFÔNICA BRASIL S.A')
    print('* TELB3 - TELEC BRASILEIRAS S.A. TELEBRAS')
    print('* EMBR3 - EMBRAER S.A.')
    print('* CVCB3 - CVC BRASIL OPERADORA E AGÊNCIA DE VIAGENS S.A.')
