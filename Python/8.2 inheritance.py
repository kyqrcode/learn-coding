from classes import chinese_menu

class menu(chinese_menu): 

    def make_chicken(self): 
        print("The chef served you chicken curry")

    def make_fish(self):
        print("The chef served you sushi")

    def make_special_order(self):
        print("The chef served you a5 wagyu steak") #overwrites special order of chinese_menu