from menuhandlers import menu_actions

def main():
    welcome_message = """Welcome  to the Trader Assistant
Programmed by <<Your Name>>"""

    print(welcome_message)
    trading_data = []
    stock_price = {}
    actions = menu_actions(trading_data, stock_price)
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
