from pages.home_page import HomePage
from pages.menu_page import MenuPage


def test_open_menu(page):
    home = HomePage(page)
    menu = MenuPage(page)

    home.open()
    menu.open_menu()