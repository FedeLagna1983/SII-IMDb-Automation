from pages.born_today_page import BornTodayPage


def test_born_yesterday(page):
    born_today_page = BornTodayPage(page)

    born_today_page.open_home()
    born_today_page.open_menu()
    born_today_page.go_to_born_today()
    born_today_page.validate_born_today_url_matches_today()
    born_today_page.expand_birthday_if_needed()
    born_today_page.set_birthday_to_previous_day_from_input()
    born_today_page.click_third_person()
    born_today_page.take_screenshot()