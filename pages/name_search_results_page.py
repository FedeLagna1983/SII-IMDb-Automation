from datetime import datetime
from pathlib import Path

from playwright.sync_api import expect


class NameSearchResultsPage:
    def __init__(self, page):
        self.page = page

        self.default_birthday_chip = page.locator(
            "[data-testid^='selected-input-chip-list-birthday-']"
        ).first

        self.birth_date_accordion = page.get_by_test_id(
            "accordion-item-birthDateAccordion"
        )

        self.birth_date_from = page.get_by_test_id("birthDate-start")
        self.birth_date_to = page.get_by_test_id("birthDate-end")

        self.result_titles = page.get_by_test_id("nlib-title")
        self.result_bios = page.locator("[data-testid='dli-bio']")
        self.see_results_button = page.get_by_test_id("adv-search-get-results")

    @staticmethod
    def get_date_40_years_ago():
        today = datetime.now()
        return today.replace(year=today.year - 40)

    @staticmethod
    def get_date_40_years_ago_for_date_input():
        return NameSearchResultsPage.get_date_40_years_ago().strftime("%Y-%m-%d")

    def remove_default_birthday_filter_if_present(self):
        if (
            self.default_birthday_chip.count() > 0
            and self.default_birthday_chip.is_visible()
        ):
            self.default_birthday_chip.click()

    def expand_birth_date_if_needed(self):
        expect(self.birth_date_accordion).to_be_visible(timeout=10000)

        expanded = self.birth_date_accordion.get_attribute("aria-expanded")
        if expanded != "true":
            self.birth_date_accordion.click()

        expect(self.birth_date_accordion).to_have_attribute("aria-expanded", "true")

    def set_birth_date_40_years_ago(self):
        target_date = self.get_date_40_years_ago_for_date_input()

        expect(self.birth_date_from).to_be_visible(timeout=10000)
        self.birth_date_from.click()
        self.birth_date_from.fill(target_date)
        expect(self.birth_date_from).to_have_value(target_date)

        expect(self.birth_date_to).to_be_visible(timeout=10000)
        self.birth_date_to.click()
        self.birth_date_to.fill(target_date)
        expect(self.birth_date_to).to_have_value(target_date)

        # Enter (por si aplica el filtro parcial)
        self.birth_date_to.press("Enter")

        # 🔥 NUEVO: click en "See results"
        expect(self.see_results_button).to_be_visible(timeout=10000)
        self.see_results_button.click()

        # 🔥 Esperar resultados reales
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page.locator(".ipc-metadata-list-summary-item").first).to_be_visible(timeout=10000)

    
    def click_first_link_in_first_result_description_if_any(self):
        first_result = self.page.locator(".ipc-metadata-list-summary-item").first
        expect(first_result).to_be_visible(timeout=10000)

        first_bio = first_result.locator("[data-testid='dli-bio']").first
        expect(first_bio).to_be_visible(timeout=10000)

        first_link = first_bio.locator("a").first

        if first_link.count() > 0:
            first_link.scroll_into_view_if_needed()
            first_link.click()
            self.page.wait_for_load_state("domcontentloaded")
            return True
        return False

    def take_screenshot(self, file_name="screenshots/born_40_years_ago.png"):
        Path("screenshots").mkdir(exist_ok=True)
        self.page.wait_for_load_state("domcontentloaded")
        self.page.screenshot(path=file_name, full_page=True)