# import the menu module
from package import menu

# create the functions for the menu items
def say_hello():
    print("Hello there!")


def dummy():
    print("Dummy function")


# create the menu items
menu_items = [
    menu.MenuItem("Say hello", func=say_hello),
    menu.MenuItem("Dummy", func=dummy, color='blue')
]

# add the menu items to the Menu container
menu_container = menu.Menu("Example Menu", menu_items)

# use the mainloop() method to show the menu items
menu_container.mainloop()
