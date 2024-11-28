import os


class Menu:
    def __init__(self):
        """Initializes an empty menu options list."""
        self._options = []

    def addOption(self, option):
        """Adds a new option to the menu."""
        self._options.append(option)

    def getInput(self):
        """Collects and validates user input."""
        choice = int(input(""))
        if 1 <= choice <= len(self._options):
            return choice

    def getOptions(self):
        """Returns the list of menu options."""
        return self._options


def run_bash_cmd(some_choice):
    """Executes the Linux commands based on the user's choice."""
    print('-' * 80)
    if some_choice in [1, 2, 3]:
        print('You entered # ' + str(some_choice))

    if some_choice == 1:
        print('The available memory is: ')
        os.system('free -tmh')
    elif some_choice == 2:
        print('The current network connections include: ')
        os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
    elif some_choice == 3:
        print('Available file space is: ')
        os.system('df -h | grep \'Filesystem\\|root\'')
    elif some_choice == 4:
        print("Your Input: 4")
        exit()
