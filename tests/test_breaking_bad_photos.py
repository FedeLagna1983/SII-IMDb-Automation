from pages.home_page import HomePage
from pages.menu_page import MenuPage
from pages.title_page import TitlePage
from pages.photos_page import PhotosPage


def test_breaking_bad_photos_danny_trejo(page):
    home = HomePage(page)
    menu = MenuPage(page)
    title_page = TitlePage(page)
    photos_page = PhotosPage(page)

    home.open()

    menu.open_menu()
    menu.go_to_top_250_tv_shows()

    assert "toptv" in page.url

    page.get_by_role("link", name="Breaking Bad").first.click()

    title_page.open_photos()

    photos_page.open_gallery()
    photos_page.open_filter_prompt()
    photos_page.select_person_filter("Danny Trejo")
    photos_page.close_filter_prompt()
    assert photos_page.is_person_filter_applied("Danny Trejo")
    photos_page.click_second_filtered_image()

    assert "/mediaviewer/" in page.url
