from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.name_search_results_page import NameSearchResultsPage


def test_born_40_years_ago(page):
    home = HomePage(page)
    menu = MenuPage(page)
    results = NameSearchResultsPage(page)

    home.open()
    menu.open_menu()
    menu.go_to_born_today()

    results.remove_default_birthday_filter_if_present()
    results.expand_birth_date_if_needed()
    results.set_birth_date_40_years_ago()
    results.click_first_link_in_first_result_description_if_any()
    results.take_screenshot()