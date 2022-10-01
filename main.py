from menuhandlers import menu_actions
from constants import welcome_message, menu, errors

def main():
    print(welcome_message)
    trading_data = []
    stock_price = {}
    actions = menu_actions(trading_data, stock_price)
    selected_menu = -1
    while selected_menu != 7:
        try:
            print(menu)
            selected_menu = int(input(">>>"))
            if selected_menu not in actions:
                print(errors["invalid_selection"])
            else:
                actions[selected_menu]()
        except:
            print(errors["something_went_wrong"])


if __name__ == "__main__":
    main()
