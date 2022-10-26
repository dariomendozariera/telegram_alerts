from binance.client import Client
import time
from datetime import datetime
from waiting import wait
import requests
from concurrent.futures import ThreadPoolExecutor

def sma(series,timeperiod):
    sum=0
    for i in range(timeperiod):
        sum=sum + float(series[i])
    return sum /timeperiod

api_key = "your api key"
api_secret = "your api secret"

tickers_spot = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT','EOSUSDT', 'TUSDUSDT',
         'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT','NULSUSDT', 'VETUSDT', 'LINKUSDT', 'WAVESUSDT',
         'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT','BATUSDT', 'XMRUSDT', 'ZECUSDT',
         'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT',
         'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT',
         'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'COCOSUSDT', 'MTLUSDT', 'TOMOUSDT', 'PERLUSDT',
         'DENTUSDT', 'MFTUSDT', 'KEYUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT',
         'BANDUSDT','BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', 'NKNUSDT',
         'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'TROYUSDT',
         'VITEUSDT', 'FTTUSDT', 'EURUSDT', 'OGNUSDT', 'DREPUSDT', 'TCTUSDT', 'WRXUSDT',
         'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT','AIONUSDT', 'MBLUSDT',
         'COTIUSDT', 'STPTUSDT', 'WTCUSDT', 'DATAUSDT' , 'SOLUSDT',
         'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT', 'GXSUSDT', 'ARDRUSDT', 'MDTUSDT',
         'STMXUSDT', 'KNCUSDT', 'LRCUSDT', 'PNTUSDT', 'COMPUSDT', 'SCUSDT',
         'ZENUSDT', 'SNXUSDT', 'VTHOUSDT', 'DGBUSDT', 'GBPUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT',
         'STORJUSDT' , 'MANAUSDT', 'AUDUSDT', 'YFIUSDT', 'BALUSDT', 'BLZUSDT',
         'IRISUSDT', 'KMDUSDT' , 'JSTUSDT', 'SRMUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT',
         'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', 'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT', 'BZRXUSDT', 'SUSHIUSDT', 'YFIIUSDT',
         'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', 'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'NBSUSDT',
         'OXTUSDT', 'SUNUSDT', 'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'ORNUSDT', 'UTKUSDT', 'XVSUSDT', 'ALPHAUSDT',
         'AAVEUSDT', 'NEARUSDT','FILUSDT', 'INJUSDT','AUDIOUSDT', 'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'DNTUSDT',
         'STRAXUSDT','UNFIUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'SUSDUSDT', 'GRTUSDT', 'JUVUSDT', 'PSGUSDT',
         '1INCHUSDT','REEFUSDT','OGUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'TRUUSDT', 'CKBUSDT',
         'LITUSDT', 'SFPUSDT', 'DODOUSDT', 'CAKEUSDT', 'ACMUSDT', 'BADGERUSDT', 'FISUSDT', 'OMUSDT', 'PONDUSDT', 'DEGOUSDT',
         'ALICEUSDT', 'LINAUSDT', 'PERPUSDT', 'RAMPUSDT', 'SUPERUSDT', 'CFXUSDT', 'EPSUSDT', 'AUTOUSDT', 'TKOUSDT',
         'PUNDIXUSDT', 'TLMUSDT','BTGUSDT', 'MIRUSDT', 'BARUSDT', 'FORTHUSDT', 'BAKEUSDT','TWTUSDT', 'FIROUSDT',
         'BURGERUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT', 'ARUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT',
         'NUUSDT', 'XVGUSDT', 'ATAUSDT', 'GTCUSDT', 'TORNUSDT', 'KEEPUSDT', 'ERNUSDT', 'KLAYUSDT', 'PHAUSDT', 'BONDUSDT',
         'MLNUSDT', 'DEXEUSDT', 'C98USDT', 'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'TVKUSDT', 'MINAUSDT', 'RAYUSDT', 'FARMUSDT',
         'ALPACAUSDT', 'QUICKUSDT', 'MBOXUSDT', 'FORUSDT', 'REQUSDT', 'GHSTUSDT', 'WAXPUSDT', 'TRIBEUSDT', 'GNOUSDT',
         'XECUSDT', 'ELFUSDT', 'DYDXUSDT', 'POLYUSDT', 'IDEXUSDT', 'VIDTUSDT', 'GALAUSDT',
        'ILVUSDT', 'YGGUSDT',  'SYSUSDT', 'DFUSDT', 'FIDAUSDT', 'FRONTUSDT', 'CVPUSDT', 'AGLDUSDT', 'RADUSDT', 'BETAUSDT', 'RAREUSDT']

try:
    client = Client(api_key, api_secret)
    print('connection established with binance api')
except :print("Please check your internet connection!")

def send_msg(text):
    token = "your token"
    chat_id = "your chat id"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

def is_something_ready():
    if (int(str(datetime.now())[14:16])%15) == 0 :
    #and int(str(datetime.now())[17:19]) == 0:
        return True
    else:
        return False

def newscan():
    # print('Scanning...')
    pairs=[]
    def breakoutcheck(symbol):
        # k_lines = client.futures_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
        volume = []
        k_lines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, "1 day ago UTC")
        time.sleep(4)
        if len(k_lines) == 0:
            k_lines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_15MINUTE, "1 day ago UTC")
            time.sleep(10)
        # if len(k_lines)==0:
        #     print(f'could not fetch data of {symbol}')
        #     return 0
        i = 0
        while i < 30:
            # time.sleep(0.05)
            volume.append(k_lines[-i - 1][5])
            i = i + 1
        # print(" volume list :   ", volume[::-1])
        avg_volume = sma(volume[::-1], timeperiod=20)
        vol = volume[::-1]
        # print(avg_volume)
        if float(vol[-1]) > (10.0 * avg_volume):
            # print(symbol, end="  ")
            pairs.append(symbol)
            print(symbol, "     avg_volume : ", avg_volume, '    last candle volume: ', vol[-1])

    with ThreadPoolExecutor(max_workers=100) as exe:
        exe.map(breakoutcheck ,tickers_spot)
        # print(f'all threads started by {datetime.now()}')
    print('pairs   :' ,pairs)
    if len(pairs)==0: print('Nothing found')
    else:
        print(pairs)
        send_msg("5m breakout" + str(pairs))
    #   print(len(npairs),npairs)
    # print(f'\nexited all threads at  {datetime.now()} in {round(time.perf_counter()-t,2)} secs')
    print(f"scan done at    {datetime.now()}")

def time_loop():
    while 1:
        wait(lambda: is_something_ready(), timeout_seconds=3700, waiting_for="Waiting for current candle to close")
        # print(f"after current time : {datetime.now()}")
        newscan()
        time.sleep(200)

if __name__=='__main__':
    time_loop()
    # newscan()
