import alpaca_trade_api as tradeapi


def getRestApiInterface():
    #authentication and connection details
    api_key = 'PK88YTDVNV64L62GF2DO'
    api_secret = '/5v3oTnWpQv89BjTUoCcEG1VAkVUxSZbW/MNFCAF'
    base_url = 'https://paper-api.alpaca.markets'
    #instantiate REST API
    return tradeapi.REST(api_key, api_secret, base_url, api_version='v2')


def getRestApiInterfaceInverse():
    ##Inverse
    api_key = 'PKLW4891U0DACFSEZ41B'
    api_secret = 'Jxw5u8qcQW9J6V9BPXj/YkMIgktG8bcfzLkvgB2h'
    base_url = 'https://paper-api.alpaca.markets'
    #instantiate REST API
    return tradeapi.REST(api_key, api_secret, base_url, api_version='v2')