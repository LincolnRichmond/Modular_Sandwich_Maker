import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = #####
cashier_instance = ######




def main():
    ###  write the rest of the codes ###

if __name__=="__main__":
    main()" sandwich_maker.py: "
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
