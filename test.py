import yfinance as yf

stocks = {
    "NVDA" : 1,
    "AMD" : 1,
    "INTC" : 5
}

def calc_yearly_diff_stocks(stocks, year):

    # stocks is an dictionary of all owned stocks and the amount owned

    tickers_list = list(stocks.keys())
    value_start = 0
    value_end = 0
    data = yf.download(tickers_list, start=f"{year-1}-01-01", end=f"{year}-01-01")

    close_prices_start_year = data["Close"].iloc[0]
    close_prices_end_year = data["Close"].iloc[-1]

    if data.empty:
        print("No data was found betweeen this period.")
        return
    else:
        for i, stock in enumerate(stocks.values()):
            value_start = value_start + stock * close_prices_start_year[tickers_list[i]]
            value_end = value_end + stock * close_prices_end_year[tickers_list[i]]
        value_year_diff = value_end - value_start
    return print("Yearly difference of your stocks is " + str(value_year_diff) + " euro")

# Yay it works but market is close at 1-1 of each year so the data for start is at 2-1
