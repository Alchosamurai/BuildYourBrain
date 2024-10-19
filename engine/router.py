from screens.menu import Menu
class Router:

    def __init__(self, screen):
        self.__screen = screen

    def go_to_menu(self):
        return Menu(self.__screen)
