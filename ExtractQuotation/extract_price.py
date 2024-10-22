import requests
from datetime import datetime, timedelta
import time
import toolbox as tool

box = tool.ToolBox() 

class ExtractPrice:
    def __init__(self):
        self.data_atual = datetime.now()
        self.data_atual_formatada = self.data_atual.strftime('%d/%m/20%y')
        self.data_Hoje = self.data_atual.strftime('%d%m20%y')
        self.data_inicio = (self.data_atual - timedelta(days=10)).strftime("%d/%m/%Y")
        self.data_fim = self.data_atual_formatada
        self.data_JSON = self.data_atual.strftime('%d.%m.20%y')
        self.Data_sabado = (self.data_atual + timedelta(days=1)).strftime('%d.%m.20%y')
        self.Data_domingo = (self.data_atual + timedelta(days=2)).strftime('%d.%m.20%y')
        #region Codes for use in url
        self.USD = '61'
        self.EUR = '222'
        self.GBP = '115'
        self.CHF = '97'
        self.CAD = '48'
        self.NOK = '19'
        self.CLP = '158'
        self.MXN = '165'
        self.COP = '159'
        #endregion

        #region variables for use
        self.value_usd = None
        self.value_eur = None
        self.value_gbp = None
        self.value_chf = None
        self.value_cad = None
        self.value_nok = None
        self.value_clp = None
        self.value_mxn = None
        self.value_cop = None
        #region variables of parity
        self.value_eur_usd = None
        self.value_gbp_usd = None
        self.value_chf_usd = None
        self.value_cad_usd = None
        self.value_nok_usd = None
        self.value_clp_usd = None
        self.value_mxn_usd = None
        self.value_cop_usd = None


        #endregion
        self.coin = []
        #endregion

        self.queue = [self.USD, self.EUR, self.GBP, self.CHF, self.CAD, self.NOK, self.CLP, self.MXN, self.COP]
    
    def get_json_queue(self,coin:str, value_today:str,value_parity:float,date:datetime,coin_parity:str) -> dict:
        self.json_queue = {
            "Coin": coin,
            "CoinParity": coin_parity,
            "Date": date,
            "ValueCoin": value_today,
            "Value_Parity_usd":value_parity,
            
        }
        return self.json_queue

    def request_url(self):
        for i in self.queue:
            url = f'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda='\
            f'{i}&DATAINI={self.data_inicio}&DATAFIM={self.data_fim}'
            try:
                url_response = requests.get(url)
                data = url_response.text
                lines = data.strip().split('\n')
                lines = lines[-1].split(";")
                _date= lines[0]
                self.date_format = f"{_date[:2]}.{_date[2:4]}.{_date[4:]}"
                coin = lines[3]
                value = lines[5].replace(",",".")
                
                match coin:
                    case "USD":
                        self.value_usd = value
                        self.value_usd_usd = float(self.value_usd)/float(self.value_usd)
                        self.coin.append(coin)

                    case "EUR":
                        self.value_eur = value
                        #parity with usd
                        self.value_eur_usd = float(self.value_eur)/float(self.value_usd)
                        self.coin.append(coin)
                    
                    case "GBP":
                        self.value_gbp = value
                        #parity with usd
                        self.value_gbp_usd = float(self.value_gbp)/float(self.value_usd)
                        self.coin.append(coin)

                    case "CHF":
                        self.value_chf = value
                        #parity with usd
                        self.value_chf_usd = float(self.value_chf)/float(self.value_usd)
                        self.coin.append(coin)
                    case "CAD":
                        self.value_cad = value
                        #parity with usd
                        self.value_cad_usd = float(self.value_cad)/float(self.value_usd)
                        self.coin.append(coin)
                    case "NOK":
                        self.value_nok = value
                        #parity with usd
                        self.value_nok_usd = float(self.value_nok)/float(self.value_usd)
                        self.coin.append(coin)
                    case "CLP":
                        self.value_clp = value
                        #parity with usd
                        self.value_clp_usd = float(self.value_clp)/float(self.value_usd)
                        self.coin.append(coin)
                    case "MXN":
                        self.value_mxn = value
                        #parity with usd
                        self.value_mxn_usd = float(self.value_mxn)/float(self.value_usd)
                        self.coin.append(coin)
                    case "COP":
                        self.value_cop = value
                        #parity with usd
                        self.value_cop_usd = float(self.value_cop)/float(self.value_usd)
                        self.coin.append(coin)

            except Exception as error_msg:
                print(f"Falha no url: {error_msg}")
                sucesso = False

        try:
            self.all_values = [self.value_usd_usd,self.value_eur,self.value_gbp,self.value_chf,self.value_cad,self.value_nok,self.value_clp,
                            self.value_mxn,self.value_cop]
            self.values_parity = [self.value_usd,self.value_eur_usd,self.value_gbp_usd,self.value_chf_usd,self.value_cad_usd,self.value_nok_usd,self.value_clp_usd,
                            self.value_mxn_usd,self.value_cop_usd]
            for i in range(len(self.all_values)):
                response = self.get_json_queue(self.coin[i],self.all_values[i],self.values_parity[i],self.date_format,"USD")
                box.create_archive_json(response)


        except Exception as error:
            print("Error to create queue:",error)
extract = ExtractPrice()
response = extract.request_url()
print(response)