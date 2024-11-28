# 1a
# not_priv_fruit.py
# class Fruit:
#     def __init__(self, factor):
#         self.__factor = factor
#     def op1(self):
#         print('Op1 with factor {}...'.format(self.__factor))

# class Apple(Fruit): subclass
#     def op2(self, factor):
#         self.__factor = factor
#         print('Op2 with factor {}...'.format(self.__factor))

# obj = Apple('red')
# obj.op1()  Op1 with factor red...
# obj.op2('green') Op2 with factor green...
# obj.op1()  This should be red, but isn't

# 1b
# print(obj.__dict__.keys())

# 2
# class Form_X:
#     def __init__(self, f_name):
#         self._f_name = f_name

    # placeholder
    # @property
    # def f_name(self):
    #     return self._f_name

    # placeholder
    # @f_name.setter
    # def f_name(self, new_f_name):
    #     if not isinstance(new_f_name, str):
    #         raise ValueError("first name must be a string.")
    #     self._f_name = new_f_name


# Form_X = Form_X("Sabine")
# print(Form_X.f_name)
# Form_X.f_name = "Hera"
# print(Form_X.f_name)

# try:
#     Form_X.f_name = 2187
# except ValueError as e:
#     print(e)

# 4ab
class Menu:
    # Constructs a menu with no options.
    def __init__(self):
        self._options = []

    # Adds an option to the end of menu.
    # @param option the option to add
    def addOption(self, option):
        self._options.append(option)

    # Displays the menu, with options numbered starting with 1, and prompts
    # the user for input. Repeats until a valid input is supplied.
    # @return the number that the user supplied
    def getInput(self):
        done = False
        while not done:
            print('-' * 80, '\n')
            for i, option in enumerate(self._options, 1):
                print(f"{i}. {option}")

            userChoice = int(input("Enter your choice: "))
            if userChoice < 1 or userChoice > len(self._options):
                print('Enter a valid choice number.')
            else:
                done = True
                return userChoice


def main():
    mainMenu = Menu()

    def buildOptions():
        mainMenu.addOption("Start New Game")
        mainMenu.addOption("Load Game")
        mainMenu.addOption("Exit")

    # placeholder
    buildOptions()
    choice = mainMenu.getInput()
    if choice == 1:
        print("Starting a new game")
    elif choice == 2:
        print("Loading a game")
    elif choice == 3:
        print("Goodbye")


if __name__ == '__main__':
    main()
