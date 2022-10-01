from badrequest import BadRequest

def read_file():
    filename = input("Enter filename:")
    if not filename.strip():
        raise BadRequest("Cannot be blank.")
    file = open(filename)
    return file

def print_trade_details(date_of_trade, ticker, flag, quantity, cost):
    print('{0}\t{1}\t{2}\t{3} for $\t{4}'.format(date_of_trade, ticker, flag,
                                                 quantity, cost))


def append_to_trading_data(trading_data, props):
    trading_data.append(props)
