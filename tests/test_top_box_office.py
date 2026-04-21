from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.title_page import TitlePage
from pages.top_box_office_page import TopBoxOfficePage


def test_navigate_to_top_box_office_and_rate_five_stars_without_login(page):
    home = HomePage(page)
    menu = MenuPage(page)
    top_box = TopBoxOfficePage(page)
    title_page = TitlePage(page)

    home.open()
    menu.open_menu()
    menu.go_to_top_box_office()

    assert top_box.is_open()

    top_box.open_second_title()
    title_page.open_your_rating_modal()
    title_page.rate_five_stars_and_confirm()

    assert title_page.is_sign_in_required() or title_page.is_rating_modal_closed()
