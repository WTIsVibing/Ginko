import csv
import hako_1
import hako_3

ticker = "AAPL"
age = 25
salary = 0
employers =  ["H&S V.O.F.", "VOF Cafetaria Den Dre"]
path_csv_bank = input("Enter the folder of your bank csv file:").strip('"').strip("'")
stock = yf.Ticker(ticker)
stock_history = stock.history(start="2024-04-10", end="2024-04-11")
with open(path_csv_bank, 'r') as csv_file:
    balance = csv.reader(csv_file)

    next(balance, None)                                     # skipping the headers
    for i, row in enumerate(balance):                       # The enumerate() function adds a counter as the key of the enumerate object.
        if row[9] in employers:
            #print("found employer at row: " + str(i+2))    # uncomment <- part if you are curious about which entry in a sheet
            raw_money = float(row[6].replace(",","."))      # rabobank has 7th column as the mutations
            salary += raw_money

print("Total salary is " + str(salary) + " euro")
        

income_tax = hako_1.calc_tax(salary,age)
print(income_tax)
print(stock_history['Close'])