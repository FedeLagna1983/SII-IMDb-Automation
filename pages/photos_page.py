import re

from pages.base_page import BasePage


class PhotosPage(BasePage):
    def open_gallery(self):
        self.page.locator('[data-testid="mv-gallery-button"]').click()

    def open_filter_prompt(self):
        filter_button = self.page.get_by_label("Open filter prompt")
        filter_button.scroll_into_view_if_needed()
        filter_button.click(force=True)

        self.page.get_by_label("Close Prompt").wait_for(state="visible")

    def select_person_filter(self, name: str):
        person_select = self.page.locator('#Person-filter-select-dropdown').first
        person_select.wait_for(state="visible")
        person_select.select_option(value="nm0001803")

    def close_filter_prompt(self):
        close_button = self.page.get_by_label("Close Prompt")
        if close_button.count() > 0:
            close_button.first.click()

    def is_person_filter_applied(self, name: str) -> bool:
        chip = self.page.get_by_text(name, exact=False).first
        return chip.count() > 0 and chip.is_visible()

    def click_second_filtered_image(self):
        self.page.locator('[data-testid="mosaic-img-0-1"]').click()