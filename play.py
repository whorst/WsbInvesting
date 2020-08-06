import common.accountOperations
from RedditScraperService.paperTrading import paperTradingUtilities

if __name__ == "__main__":
    api = common.accountOperations.getRestApiInterface()
    # print(api.get_account())
    # print(api.get_account().__getattr__("portfolio_value"))
    # print(api.get_calendar())
    # print(api.list_positions())
    print(api.get_portfolio_history(date_start="2020-07-06", date_end="2020-07-10", timeframe="1H"))