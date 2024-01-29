#gera filas e cotações de acordo com o dia da semana pegando as moedas(USD, EUR,CAD,ETC...)
#como intuinto de validação de valores das cotações dos dias atuais, com algumas regras...
#se for feriado replicar filas para o dia seguinte
#se for sexta replicar filas para o sabado e o domingo 
#as filas criadas são consumidas como o usuario preferir.
#Há comparações do (usd-1 e usd-2) referente ao dia anterior ou 2 dias anteriores...

import requests
from datetime import datetime, timedelta
import time
import toolbox as tool


data_atual = datetime.now()

data_atual_formatada = data_atual.strftime('%d/%m/20%y')
data_Hoje = data_atual.strftime('%d%m20%y')
data_inicio = (data_atual - timedelta(days=10)).strftime("%d/%m/%Y")
data_fim = data_atual_formatada
data_JSON = data_atual.strftime('%d.%m.20%y')
Data_sabado = (data_atual + timedelta(days=1)).strftime('%d.%m.20%y')
Data_domingo = (data_atual + timedelta(days=2)).strftime('%d.%m.20%y')

USD = '61'
EUR = '222'
GBP = '115'
CHF = '97'
CAD = '48'
NOK = '19'
CLP = '158'
MXN = '165'
COP = '159'

Moeda_USD = 'USD'
Moeda_USDt2 = 'BRL'

Moeda_USD1 = 'USD-1'
Moeda_USD1t2 = 'USD'

Moeda_USD2 = 'USD-2'
Moeda_USD2t2 = 'BRL'

Moeda_EUR = 'EUR'
Moeda_EURt2 = 'BRL'

Moeda_EUR1 = 'EUR-1'
Moeda_EURUSD = 'EUR'

Moeda_GBP = 'GBP'
Moeda_GBPt2 = 'BRL'

Moeda_GBPUSD = 'GBP'

Moeda_CHF = 'CHF'
Moeda_CHFt2 = 'BRL'

Moeda_CHFUSD = 'CHF'

Moeda_CAD = 'CAD'
Moeda_CADt2 = 'BRL'

Moeda_CADUSD = 'CAD'

Moeda_NOK = 'NOK'
Moeda_NOKt2 = 'BRL'

Moeda_NOKUSD = 'NOK'

Moeda_CLP = 'CLP'
Moeda_CLPt2 = 'BRL'

Moeda_CLPUSD = 'CLP'

Moeda_MXN = 'MXN'
Moeda_MXNt2 = 'BRL'

Moeda_MXNUSD = 'MXN'

Moeda_COP = 'COP'
Moeda_COPt2 = 'BRL'

Moeda_COPUSD = 'COP'

lista = [USD, EUR, GBP, CHF, CAD, NOK, CLP, MXN, COP]
cont = 0

for i in lista:
    url = f'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda='\
    f'{i}&DATAINI={data_inicio}&DATAFIM={data_fim}'
    try:
        url_response = requests.get(url)
        data = url_response.text
        linhas = data.split('\n')

    except Exception as error_msg:
        print(f"Falha no url: {error_msg}")
        sucesso = False
        
    try:
        Lista = []
        for linha in linhas:
            if linha.strip():
                campos = linha.split(';')
                Lista.append(campos)
        if Lista:
            Data = Lista[-1][0]
            Moeda = Lista[-1][3]
            Valor = Lista[-1][5].replace(',', '.')
            if Moeda == 'USD':
                # USD em comparação com R$
                USD = float(Lista[-1][5].replace(',', '.'))
                USD_formatado = Lista[-1][5].replace('.',',')
                # Variaveis com 'old' refere-se a ValorOntem
                USD_old = float(Lista[-2][5].replace(',', '.'))
                USD1 = float(Lista[-1][5].replace(',', '.')) / float(Lista[-2][5].replace(',', '.'))
                USD1_old = float(Lista[-2][5].replace(',', '.'))/ float(Lista[-3][5].replace(',', '.'))

                # USD em comparação com usd
                USD1_old = f'{USD1_old:.5f}'.replace('.', ',')

                # USD em comparação com real
                USD1_BRL = Lista[-2][5]
                USD1_BRL_old = Lista[-3][5]
                USD1 = f'{USD1:.5f}'.replace('.', ',')
                USD2 = Lista[-3][5]
                USD2_old = Lista[-5][5]

            if Moeda == 'EUR':
                EUR = Lista[-1][5]
                EUR_old = Lista[-2][5]
                EUR1 = Lista[-2][5]
                EUR1_old = Lista[-3][5]
                EUR_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                EUR_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                EUR_USD_old = f'{EUR_USD_old:.5f}'.replace('.', ',')
                EUR_USD = f'{EUR_USD:.5f}'
            if Moeda == 'GBP':
                GBP = Lista[-1][5]
                GBP_old = Lista[-2][5]
                GBP_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                GBP_USD = f'{GBP_USD:.5f}'.replace('.', ',')
                GBP_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                GBP_USD_old = f'{GBP_USD_old:.5f}'.replace('.', ',')
            if Moeda == 'CHF':
                CHF = Lista[-1][5]
                CHF_old = Lista[-2][5]
                CHF_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                CHF_USD = f'{CHF_USD:.5f}'.replace('.', ',')
                CHF_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                CHF_USD_old = f'{CHF_USD_old:.5f}'.replace('.', ',')
                time.sleep(0.5)
            if Moeda == 'CAD':
                CAD = Lista[-1][5]
                CAD_old = Lista[-2][5]
                CAD_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                CAD_USD = f'{CAD_USD:.5f}'.replace('.', ',')
                CAD_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                CAD_USD_old = f'{CAD_USD_old:.5f}'.replace('.', ',')
            if Moeda == 'NOK':
                NOK = Lista[-1][5]
                NOK_old = Lista[-2][5]
                NOK_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                NOK_USD = f'{NOK_USD:.5f}'.replace('.', ',')
                NOK_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                NOK_USD_old = f'{NOK_USD_old:.5f}'.replace('.', ',')
            if Moeda == 'CLP':
                CLP = Lista[-1][5]
                CLP = CLP[0:7]
                CLP_old = Lista[-2][5]
                CLP_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                CLP_USD = f'{CLP_USD:.5f}'.replace('.', ',')
                CLP_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                CLP_USD_old = f'{CLP_USD_old:.5f}'.replace('.', ',')
            if Moeda == 'MXN':
                MXN = Lista[-1][5]
                MXN_old = Lista[-2][5]
                MXN_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                MXN_USD = f'{MXN_USD:.5f}'.replace('.', ',')
                MXN_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                MXN_USD_old = f'{MXN_USD_old:.5f}'.replace('.', ',')

            if Moeda == 'COP':
                COP = Lista[-1][5]
                COP = COP[0:7]
                COP_old = Lista[-2][5]
                COP_USD = float(Lista[-1][5].replace(',', '.')) / float(USD)
                COP_USD = f'{COP_USD:.5f}'.replace('.', ',')
                COP_USD_old = float(Lista[-2][5].replace(',', '.')) / float(USD_old)
                COP_USD_old = f'{COP_USD_old:.5f}'.replace('.', ',')
                time.sleep(0.5)

            ListaMoeda = [
                Moeda_USD, Moeda_USD1, Moeda_USD1, Moeda_USD2, Moeda_EUR, Moeda_EUR1, Moeda_EURUSD,
                Moeda_GBP, Moeda_GBPUSD, Moeda_CHF, Moeda_CHFUSD, Moeda_CAD, Moeda_CADUSD,
                Moeda_NOK, Moeda_NOKUSD, Moeda_CLP, Moeda_CLPUSD, Moeda_MXN, Moeda_MXNUSD, Moeda_COP,
                Moeda_COPUSD]
            ListaValor = [USD_formatado, USD1, USD1_BRL, USD2, EUR, EUR1, EUR_USD, GBP, GBP_USD, CHF, CHF_USD,
                          CAD, CAD_USD, NOK, NOK_USD, CLP, CLP_USD, MXN, MXN_USD, COP, COP_USD]

            ListaMoedat2 = [Moeda_USDt2, Moeda_USD, Moeda_USDt2, Moeda_USD2t2, Moeda_EURt2, Moeda_EURt2, Moeda_USD, Moeda_GBPt2, Moeda_USD, Moeda_CHFt2, Moeda_USD,
                            Moeda_CADt2, Moeda_USD, Moeda_NOKt2, Moeda_USD, Moeda_CLPt2, Moeda_USD, Moeda_MXNt2,
                            Moeda_USD, Moeda_COPt2, Moeda_USD]

            ListaValorOld = [USD_old, USD1_old, USD1_BRL_old, USD2_old, EUR_old, EUR1_old, EUR_USD_old, GBP_old, GBP_USD_old,
                             CHF_old, CHF_USD_old, CAD_old, CAD_USD_old, NOK_old, NOK_USD_old, CLP_old,
                             CLP_USD_old, MXN_old, MXN_USD_old, COP_old, COP_USD_old]
            
            for i in range(len(ListaMoeda)):
                JSON_Fila = {
                        "Moeda": ListaMoeda[i],
                        "ValorHoje": str(ListaValor[i]).replace(",", "."),
                        "ValorOntem": str(ListaValorOld[i]).replace(",", "."),
                        "Data": data_JSON,
                        "TipoMoeda": ListaMoeda[i],
                        "TipoMoeda2": ListaMoedat2[i]
                            }
            

                tool.open_json(JSON_Fila)
                cont += 1

                # Logica do final de semana

                # Se hoje for sexta, replicar os mesmos valores da fila para sabado e domingo
                # Se hoje fopr sexta e segunda for feriado, replicar os mesmos valores da fila para sabado, domingo e segunda
                final_de_semana = tool.logic_find(data_JSON)
                if final_de_semana != False:
                    for dias in final_de_semana:
                        JSON_Fila = {

                            "Moeda": ListaMoeda[i],
                            "ValorHoje": str(ListaValor[i]).replace(",", "."),
                            "ValorOntem": str(ListaValorOld[i]).replace(",", "."),
                            "Data": dias,
                            "TipoMoeda": ListaMoeda[i],
                            "TipoMoeda2": ListaMoedat2[i],
                        }

                        tool.open_json(JSON_Fila)
                        cont += 1
                        

                # Logica do feriado

                # Se amanha for feriado, replicar os mesmos valores da fila para amanha
                # Se amanha for feriado e sexta,  replicar os mesmos valores da fila para amanha, sabado e domingo
                feriado = tool.logic_holiday(data_JSON)
                if feriado != False:
                    for dias in feriado:
                        JSON_Fila = {

                            "Moeda": ListaMoeda[i],
                            "ValorHoje": str(ListaValor[i]).replace(",", "."),
                            "ValorOntem": str(ListaValorOld[i]).replace(",", "."),
                            "Data": dias,
                            "TipoMoeda": ListaMoeda[i],
                            "TipoMoeda2": ListaMoedat2[i],
                        }

                        tool.open_json(JSON_Fila)
                        cont += 1

    except:
        #Vai cair aqui quando a lista de moedas não estiver completa ainda
        pass

if cont == 0:
    print('0 filas criadas')

else:
    print(f"{cont} filas criadas com sucesso")
   