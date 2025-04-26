import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Initialize instances
resources = data.resources
recipes = data.recipes
sandwich_maker = SandwichMaker(resources)
cashier = Cashier()


def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            break

        if choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")
            continue

        if choice in recipes:
            size = choice
            ingredients = recipes[size]["ingredients"]
            cost = recipes[size]["cost"]

            if sandwich_maker.check_resources(ingredients):
                print(f"Cost: ${cost}")
                payment = cashier.process_coins()
                success, change = cashier.transaction_result(payment, cost)

                if success:
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    sandwich_maker.make_sandwich(size, ingredients)
                    print(f"{size} sandwich is ready. Bon appetit!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                for item, needed in ingredients.items():
                    if resources[item] < needed:
                        print(f"Sorry there is not enough {item}.")
                        break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()