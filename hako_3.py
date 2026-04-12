import yfinance as yf

def calculate_yearly_difference(ticker_symbol, year):
    """
    Fetches a full year's data and calculates the difference
    between the first and last available trading day.
    """
    print(f"Fetching data for {ticker_symbol} in the year {year}...\n")
    
    # 1. Connect the ticker symbol to yfinance
    stock = yf.Ticker(ticker_symbol)
    
    # 2. Determine the start and end date. 
    # Start = January 1st of the chosen year.
    # End = January 1st of the NEXT year (so Dec 31st is included).
    start_date = f"{year}-01-01"
    end_date = f"{year + 1}-01-01"
    
    # 3. Fetch all historical data for that year
    historical_data = stock.history(start=start_date, end=end_date)
    
    # 4. Check if data was actually found
    if not historical_data.empty:
        
        # .iloc[0] grabs the first row (the first trading day of the year)
        start_price = historical_data['Close'].iloc[0]
        
        # .iloc[-1] grabs the very last row (the last trading day of the year)
        end_price = historical_data['Close'].iloc[-1]
        
        # Calculate the difference
        difference = end_price - start_price
        
        # Print the results nicely to the screen
        print(f"Results for {ticker_symbol}:")
        print(f"Price at the start of {year}: ${start_price:.2f}")
        print(f"Price at the end of {year}:   ${end_price:.2f}")
        
        # Determine if the difference is positive or negative for the output text
        if difference > 0:
            print(f"The stock INCREASED this year by: ${difference:.2f}")
        else:
            # We make the number positive with abs() for a cleaner sentence
            print(f"The stock DECREASED this year by: ${abs(difference):.2f}")
            
    else:
        print(f"No data found for the year {year}.")

# --- Settings you can change yourself ---
my_stock = "AAPL" 
my_year = 2023  # Type the year in numbers here (without quotes)

# --- Run the function ---
calculate_yearly_difference(my_stock, my_year)