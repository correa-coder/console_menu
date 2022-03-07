# API Reference

## MenuItem

```python
MenuItem(title, func=None, color='default', sub_menu=None)
```

Represents an option in the menu, the `title` attribute is the label for the menu item: represents what this menu option should do, `func` is a function that will run when selecting this menu item.

The following colors are available for the `color` attribute:
- red
- green
- blue
- default

&rarr; Menu items works as tree like structure allowing them to have sub menus.

### Methods
`run()`

Calls `self.func()`.

---

## Menu
```python
Menu(title='main menu', menu_items=None)
```

It's a container for `MenuItems` passed as a list to the `menu_items` attribute.

### Methods

`mainloop()`

Starts the main loop which shows the menu options and asks for the user to choose a number representing which item to select. After entering a number that matches with the menu option, it calls the `MenuItem.run()` method.

---

## Text
```python
Text(content='', color='default')
```
Useful for colored output e.g. printing an error message in red or success message in green etc.

### Methods
`show()`

Prints the `Text.content` to the terminal with the color specified in the `Text.color`

---

`colorize(text, color)`

Returns a string wrapped with ANSI color code

Currently accepts the following colors:
- red
- green
- blue
- default

To extend this method with more colors, edit the `color_codes` dictionary inside the method definition.

Example: adding the magenta color

```python
# Text class

@staticmethod
def colorize(text, color='default'):
    """
    returns a string wrapped with ANSI color code
    """
    color_codes = {
        'red': 31,
        'green': 32,
        'blue': 34,
        'magenta': 35 # <---- added color
    }
```