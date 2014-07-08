import random

class Animal:
    """An animal growth simulation"""

    def __init__(self,growth_rate,food_need,water_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"

    def needs(self):
        return {"food need":self._food_need,"water need":self._water_need}

    def report(self):
        return{"type":self._type,"status":self._status,"weight":self._weight,"days growing":self._days_growing}

    def _update_status(self):
        if self._weight >15:
            self._status = "Obese"
        elif self._weight >10:
            self._status = "Fat"
        elif self._weight >5:
            self._status = "Chubby"
        elif self._weight >0:
            self._status = "Ordinary"
        elif self._weight == 0:
            self.status = "Slim"


    def grow(self,food,water):
        if food >=self._food_need and water >=self._water_need:
            self._weight +=self._growth_rate
        self._days_growing +=1
        self._update_status()

def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,100)
        water= random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    valid=False
    while not valid:
        try:
            food=int(input("Please enter a food value(1,100): "))
            if 1 <= food <= 100:
                valid=True
            else:
                print("Value entered not valid - Please enter a value between 1 and 100")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 100")
    valid=False
    while not valid:
        try:
            water=int(input("Please enter a water value(1,10): "))
            if 1 <= water <= 10:
                valid=True
            else:
                print("Value entered not valid - Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 10")
    animal.grow(food,water)

def display_menu():
    print("1.Grow manually over 1 day")
    print("2.Grow automatically over 30 days")
    print("3.Report status")
    print("0.Exit test program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice():
    option_valid= False
    while not option_valid:
        try:
            choice= int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice


def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")

def main():
    new_animal = Animal(1,4,3)
    manage_animal(new_animal)
    
    

    

if __name__=="__main__":
    main()


        
