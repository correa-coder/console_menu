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
    def __init__(self, title, func=None, color='default', sub_menu=None):
        self.title = title
        self.func = func
        self.color = color
        self.sub_menu = sub_menu

    def show(self):
        """prints the self.title value with the color specified in self.color"""
        print(Text.colorize(self.title, self.color))

    def run(self):
        pass
    

class Menu:
    """container for MenuItem objects"""
    def __init__(self, title='main menu', menu_items=None):
        self.title = title

        if menu_items is None:
            self.menu_items = []
        else:
            self.menu_items = menu_items

    def mainloop(self):
        pass


# quick testing
if __name__ == '__main__':
    # TODO: create a separate test file

    # testing text output in different colors
    dummy_texts = [
        Text('Success', 'green'),
        Text('Info', 'blue'),
        Text('Error', 'red')
    ]
    
    for text in dummy_texts:
        text.show()


    # testing menu items
    menu_items = [
        MenuItem('Strawberry', color='red'),
        MenuItem('Avocado', color='green'),
        MenuItem('Exit', lambda quit: exit)
    ]

    for item in menu_items:
        item.show()
        item.run()
