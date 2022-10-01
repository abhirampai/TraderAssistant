from badrequest import BadRequest
from constants import errors, input_messages

def read_file():
    filename = input(input_messages["filename"])
    if not filename.strip():
        raise BadRequest(errors["field_blank"])
    file = open(filename)
    return file

def print_trade_details(date_of_trade, ticker, flag, quantity, cost):
    print('{0}\t{1}\t{2}\t{3} for $\t{4}'.format(date_of_trade, ticker, flag,
                                                 quantity, cost))


def append_to_trading_data(trading_data, props):
    trading_data.append(props)

def add_or_reduce_stocks(flag, current_value, quantity):
    if (flag == "BUY"):
        return current_value + quantity
    else:
        return current_value - quantity
