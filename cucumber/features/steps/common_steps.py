from pathlib import Path
import re

from behave import given, then, when

from pages.home_page import HomePage
from pages.menu_page import MenuPage


def _menu_page(context) -> MenuPage:
    if context.menu_page is None:
        context.menu_page = MenuPage(context.page)
    return context.menu_page


@given("I am on the IMDb home page")
def step_open_imdb_home(context):
    context.home_page = HomePage(context.page)
    context.home_page.open()


@when("I open the main menu")
def step_open_main_menu(context):
    _menu_page(context).open_menu()


@when("I navigate to Top Box Office")
def step_navigate_top_box_office(context):
    _menu_page(context).go_to_top_box_office()


@when("I navigate to Top 250 TV Shows")
def step_navigate_top_250_tv_shows(context):
    _menu_page(context).go_to_top_250_tv_shows()


@when("I navigate to Born Today")
def step_navigate_born_today(context):
    _menu_page(context).go_to_born_today()


@then("I capture a screenshot for the scenario")
def step_capture_screenshot_for_scenario(context):
    Path("screenshots").mkdir(exist_ok=True)
    scenario_name = getattr(context.current_scenario, "name", "cucumber_scenario")
    scenario_slug = re.sub(r"[^a-z0-9]+", "_", scenario_name.lower()).strip("_")
    screenshot_path = Path("screenshots") / f"{scenario_slug}.png"
    context.page.screenshot(path=str(screenshot_path), full_page=True)
