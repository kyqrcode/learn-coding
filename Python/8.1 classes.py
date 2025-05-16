#classes are special data values like str, int, bol which can be defined by the user
class chinese_menu: #"menu" is a class that can be defined by the parameters

    def make_friedrice(self): 
        print("The chef served you fried rice")

    def make_dimsum(self):
        print("The chef served you xiao long bao")

    def make_special_order(self):
        print("The chef served you orange chicken") 

'''
    def (self, parameter1, parameter2): 
        self.parameter1 = parameter1
        self.parameter2 = parameter2
'''
#parameter1 and parameter2 are to be defined by object
#self.parameter is a variable that passes on the value to the parameter
#class functions can also be defined in the class folder, to modify the objects
#we define certain attributes and functions in the class, and we can "inherit" those functionality and attributes to another class