import csv
import time as datetime
import json

class BadRequest(Exception):

    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message

def read_file():
    filename = input("Enter filename:")
    if not filename.strip():
        raise BadRequest("Cannot be blank.")
    file = open(filename)
    return file

def test_valid_file_name_and_extension(filename, extension):
  if filename.split(".")[1:] in [[extension]] and filename[0].isalpha() and sum(c.isdigit() for c in filename) < 4:
    return True
  else:
    raise BadRequest("Invalid File")

def buy_or_sell(flag):
    if (flag == "b"):
        return "BUY"
    elif (flag == "s"):
        return "SELL"
    raise BadRequest("Error with file format.")

def format_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except:
        raise BadRequest("Error with file format.")

def test_stock_details(value, datatype):
    if (datatype(value) > 0):
        return datatype(value)
    raise BadRequest("Error with file format.")

def load_trading_data(trading_data):
    flag = 0
    while flag != 1:
        try:
            file = read_file()
            csvreader = csv.reader(file)
            for ticker, flag, quantity, cost, date_of_trade in csvreader:
                trading_data.append([
                    format_date(date_of_trade), ticker,
                    buy_or_sell(flag),
                    test_stock_details(quantity, int),
                    test_stock_details(cost, float)
                ])
            print(trading_data)
            flag = 1
        except FileNotFoundError:
            print("Please enter a valid filename.")
        except BadRequest as Error:
            print(Error)

def load_stock_prices(stock_prices):
    flag = 0
    while flag != 1:
        try:
            file = read_file()
            data = json.load(file)
            for key in data:
                stock_prices[key] = data[key]
            print(stock_prices)
            flag = 1
        except BadRequest as Error:
            print(Error)
        except:
            print("Error with file format.")

def manually_enter_trade(trading_data):
    try:
        ticker = input("Ticker:\t")
        flag = buy_or_sell(input("Buy or sell:\t"))
        quantity = test_stock_details(input("Quantity of stock:\t"), int)
        cost = test_stock_details(input("Total cost(including brokerage):\t"),
                                  float)
        date_of_trade = format_date(input("Date:\t"))
        trading_data.append([date_of_trade, ticker, flag, quantity, cost])
        print('{0}\t{1}\t{2}\t{3} for $\t{4}'.format(date_of_trade, ticker, flag, quantity,
                                                cost))
        print("Trade added to system")
    except:
        print("Error in input")


def view_trading_data(trading_data):
    sorted_data = trading_data.copy()
    ticker = input("Ticker (leave blank for all):\t")
    sort_date = input("Sort dates in reverse chronological order? (y/n)\t")
    if sort_date == "y":
        sorted_data.sort(key=lambda trading_data: trading_data[0], reverse=True)
    if ticker:
      sorted_data =  [
            filtered_data for filtered_data in sorted_data
            if ticker in filtered_data
        ]
    for [date_of_trade, ticker, flag, quantity, cost] in sorted_data:
        print('{0}\t{1}\t{2}\t{3} for $\t{4}'.format(date_of_trade, ticker, flag, quantity,
                                                cost))

def add_or_reduce_stocks(flag, current_value, quantity):
  if(flag == "BUY"):
    return current_value+quantity
  else:
    return current_value-quantity

def view_current_portfolio(trading_data, stock_prices):
  portfolio = {}
  for stock in trading_data:
    data_of_trade, ticker, flag, quantity, cost = stock
    is_stock_price_available = ticker in stock_prices
    if ticker in portfolio:
      portfolio[ticker]["units"] = add_or_reduce_stocks(flag, portfolio[ticker]["units"], quantity)
      if is_stock_price_available:
        portfolio[ticker]["value"] =round(float(portfolio[ticker]["units"]*stock_prices[ticker]),2)
    else:
      units = add_or_reduce_stocks(flag, 0, quantity)
      value = round(float(units * stock_prices[ticker]), 2) if is_stock_price_available else "Current value unknown."
      portfolio[ticker] = {
        "units": units,
        "value": value
      }
      
  for key in sorted(portfolio.keys()):
    print("{0}\nTotal units:\t{1}\nTotal value: $\t{2}\n".format(key, portfolio[key]["units"], portfolio[key]["value"]))

def save_trading_data(trading_data):
  flag = 0
  while flag != 1:
    try:
      filename = input("Enter filename:")
      if not filename.strip():
        raise BadRequest("Cannot be blank.")
      test_valid_file_name_and_extension(filename, "csv")
      with open(filename, 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        for row in trading_data:
          writer.writerow(row)
      print("Data save to {0}.".format(filename))
      flag = 1
    except BadRequest as Error:
      print(Error)

def thank_you():
    print("Thanks for using the Trade Assistant")


def main():
    welcome_message = """Welcome  to the Trader Assistant
Programmed by <<Your Name>>"""

    print(welcome_message)
    trading_data = []
    stock_price = {}
    actions = {
        1: lambda: load_trading_data(trading_data),
        2: lambda: load_stock_prices(stock_price),
        3: lambda: manually_enter_trade(trading_data),
        4: lambda: view_trading_data(trading_data),
      5: lambda: view_current_portfolio(trading_data, stock_price),
      6: lambda: save_trading_data(trading_data),
        7: lambda: thank_you()
    }
    selected_menu = -1
    while selected_menu != 7:
        try:
            menu = """Please choose from  the options below 
1. Load trading data
2. Load current stock prices
3. Manually enter a new trade
4. View trading data
5. View current portfolio
6. Save trading data
7. Quit"""
            print(menu)
            selected_menu = int(input(">>>"))
            if selected_menu not in actions:
                print("Invalid selection")
            else:
                actions[selected_menu]()
        except:
            print("Something went wrong, Please try again!")

if __name__ == "__main__":
    main()
