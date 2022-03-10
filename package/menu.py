class Text:
    def __init__(self, content='', color='default'):
        self.content = content
        self.color = color

    def show(self):
        print(self.colorize(self.content, self.color))

    @staticmethod
    def colorize(text, color='default'):
        """
        returns a string wrapped with ANSI color code
        """
        color_codes = {
            'red': 31,
            'green': 32,
            'blue': 34
        }

        # if color not in color_codes return the original text
        result = text
        
        if color in color_codes:
            result = f"\033[{color_codes[color]}m{text}\033[m"

        return result


class MenuItem:
    """represents an option in the menu"""
    def __init__(self, title, func=None, color='default'):
        self.title = title
        self.func = func
        self.color = color

    @property
    def value(self):
        """returns the self.title value with the color specified in self.color"""
        return Text.colorize(self.title, self.color)

    def run(self):
        if self.func is not None:
            # check if it's a function
            if callable(self.func):
                self.func()
    

class Menu:
    """container for MenuItem objects"""
    def __init__(self, title='main menu', menu_items=None):
        self.title = title

        if menu_items is None:
            self.menu_items = []
        else:
            self.menu_items = menu_items

    def print_dashes(self):
        """prints dashes of the length of the self.title"""
        print('-' * len(self.title))

    def mainloop(self):
        # show the menu title
        self.print_dashes()
        print(self.title)
        self.print_dashes()

        # show the menu items
        for index, menu_item in enumerate(self.menu_items):
            print(f"{index+1}. {menu_item.value}")

        print("\nEnter 'exit' to quit\n")

        # input for selecting an item in the menu
        selected_index = input("Select an option: ").strip()
        
        if selected_index.isnumeric():
            selected_index = int(selected_index) - 1
            selected_menu = self.menu_items[selected_index]

            # run the function from the selected menu item
            selected_menu.run()

            # restarts the menu
            input("\nPress enter to continue...")
            self.mainloop()


if __name__ == '__main__':
    pass
