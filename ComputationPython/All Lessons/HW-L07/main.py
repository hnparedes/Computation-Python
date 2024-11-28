from menu import Menu, run_bash_cmd

"""Main function to run the menu-driven program."""
mainMenu = Menu()

# Adding menu options
mainMenu.addOption("Check available memory")
mainMenu.addOption("View network connections")
mainMenu.addOption("Display free ram and swap")
mainMenu.addOption("Quit")

while True:
    # Display the menu
    for i, option in enumerate(mainMenu.getOptions(), 1):
        print("{} {}".format(i, option))

    # Get user input
    choice = mainMenu.getInput()

    # Run the corresponding command
    run_bash_cmd(choice)
