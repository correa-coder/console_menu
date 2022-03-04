import unittest
from package import menu


class TestText(unittest.TestCase):
    def test_text_output(self):
        print('-' * 32)
        print("testing menu.Text")

        texts = [
            menu.Text('Success', 'green'),
            menu.Text('Info', 'blue'),
            menu.Text('Error', 'red')
        ]
        
        for text in texts:
            text.show()

    def test_colorize_func(self):
        self.assertEqual(menu.Text.colorize('test', 'red'), '\033[31mtest\033[m')
        self.assertEqual(menu.Text.colorize('test', 'green'), '\033[32mtest\033[m')
        self.assertEqual(menu.Text.colorize('test', 'blue'), '\033[34mtest\033[m')

    def test_menu_item(self):
        print('-' * 32)
        print("testing menu.MenuItem")

        menu_items = [
            menu.MenuItem('Strawberry', color='red'),
            menu.MenuItem('Avocado', lambda: print("This is an Avocado"), color='green'),
            menu.MenuItem('Mango', [], color='blue'), # not a function passed to self.func (edge case)
        ]

        for item in menu_items:
            item.show()
            item.run()


if __name__ == '__main__':
    unittest.main()
