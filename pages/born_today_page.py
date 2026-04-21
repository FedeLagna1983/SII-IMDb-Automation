from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import re

from playwright.sync_api import expect, TimeoutError as PlaywrightTimeoutError


class BornTodayPage:
    def __init__(self, page):
        self.page = page

        self.menu_button = page.get_by_label("Open Navigation Drawer")
        self.born_today_link = page.get_by_label("Go to Born today").first
        self.birthday_accordion = page.get_by_test_id(
            "accordion-item-birthdayAccordion"
        )

    @staticmethod
    def get_today_mm_dd():
        return datetime.now().strftime("%m-%d")

    def open_home(self):
        self.page.goto("https://www.imdb.com/")
        self.page.wait_for_load_state("domcontentloaded")

    def open_menu(self):
        expect(self.menu_button).to_be_visible()
        self.menu_button.click()
        expect(self.born_today_link).to_be_visible(timeout=10000)

    def go_to_born_today(self):
        expect(self.born_today_link).to_be_visible(timeout=10000)

        try:
            self.born_today_link.click(timeout=10000)
        except PlaywrightTimeoutError:
            # fallback más robusto entre browsers
            href = self.born_today_link.get_attribute("href")
            assert href, "Born today link does not contain href"
            self.page.goto(f"https://www.imdb.com{href}")
        self.page.wait_for_load_state("domcontentloaded")

    def validate_born_today_url_matches_today(self):
        expected_date = self.get_today_mm_dd()
        current_url = self.page.url

        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query)
        actual_date = query_params.get("birth_monthday", [""])[0]

        assert actual_date == expected_date, (
            f"Expected {expected_date}, got {actual_date}"
        )

    def expand_birthday_if_needed(self):
        expect(self.birthday_accordion).to_be_visible(timeout=10000)

        expanded = self.birthday_accordion.get_attribute("aria-expanded")
        if expanded != "true":
            self.birthday_accordion.click()

    def set_birthday_to_previous_day_from_input(self):
        birthday_section = self.page.locator("#accordion-item-birthdayAccordion")
        birthday_input = birthday_section.locator("input").first

        expect(birthday_input).to_be_visible(timeout=10000)

        birthday_input.click()

        current_value = birthday_input.input_value().strip()

        current_date = datetime.strptime(f"2000-{current_value}", "%Y-%m-%d")
        previous_day = current_date - timedelta(days=1)
        previous_day_value = previous_day.strftime("%m-%d")

        birthday_input.fill("")
        birthday_input.type(previous_day_value, delay=80)
        birthday_input.press("Enter")

        chip = self.page.get_by_test_id(
            f"selected-input-chip-list-birthday-{previous_day_value}"
        )
        expect(chip).to_be_visible(timeout=10000)

    def click_third_person(self):
        results = self.page.get_by_test_id("nlib-title")
        third = results.nth(2)

        expect(third).to_be_visible(timeout=10000)

        link = third.locator("a")
        link.scroll_into_view_if_needed()
        link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def take_screenshot(self):
        # to_have_url necesita string o regex, no lambda
        expect(self.page).to_have_url(re.compile(r".*/name/.*"), timeout=10000)

        # esperar algo estable del perfil
        expect(self.page.locator("h1")).to_be_visible(timeout=10000)

        Path("screenshots").mkdir(exist_ok=True)
        self.page.screenshot(path="screenshots/born_yesterday.png", full_page=True)