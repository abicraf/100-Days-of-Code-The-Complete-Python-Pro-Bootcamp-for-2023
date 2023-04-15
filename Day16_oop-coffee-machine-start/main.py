from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem
money_machine = MoneyMachine()



while machine_on:
    # ask user what they want while coffee machine is on.
    options = menu.get_items()
    drink = input(f"What would you like? ({options}): ")
    # turn off the coffee machine if user would like to turn it off.
    if drink == 'off':
        machine_on = False
    elif drink == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(drink)
        # if = True, if the resource is sufficient, then make payment
        if coffee_maker.is_resource_sufficient(menu_item):
            # if payment is received, return True, and then make coffee
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)