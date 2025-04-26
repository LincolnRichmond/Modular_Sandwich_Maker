class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted"""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: ")) * 1.0
        half_dollars = int(input("how many half dollars?: ")) * 0.5
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return large_dollars + half_dollars + quarters + nickels

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            return True, round(change, 2)
        return False, 0