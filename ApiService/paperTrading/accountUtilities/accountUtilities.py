from common.accountOperations import *

def getPositionHistorySinceDate(start, end, timeframe):
    api = getRestApiInterface()
    print(api.get_portfolio_history(date_start="2020-07-06", date_end="2020-07-10", timeframe="1H"))



    'base_value'
    'equity'
    'profit_loss'
    'profit_loss_pct'
    'timeframe'
    'timestamp'