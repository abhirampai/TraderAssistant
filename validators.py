from badrequest import BadRequest
import time as datetime

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

def test_valid_file_name_and_extension(filename, extension):
    if filename.split(".")[1:] in [[
            extension
    ]] and filename[0].isalpha() and sum(c.isdigit() for c in filename) < 4:
        return True
    else:
        raise BadRequest("Invalid File")