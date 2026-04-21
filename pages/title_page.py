from pages.base_page import BasePage


class TitlePage(BasePage):
    def open_your_rating_modal(self):
        self.page.locator(
            "[data-testid='hero-rating-bar__user-rating'] button[aria-label^='Rate ']:visible"
        ).first.click()
        self.page.locator("[data-testid='promptable__pc']").wait_for(state="visible")

    def rate_five_stars_and_confirm(self):
        dialog = self.page.locator("[data-testid='promptable__pc']")
        dialog.get_by_role("button", name="Rate 5").first.click(force=True)
        confirm_button = dialog.locator(
            "button[class*='rating-prompt__rate-button'][aria-disabled='false']"
        )
        confirm_button.wait_for(state="visible")
        confirm_button.click()

    def is_sign_in_required(self) -> bool:
        current_url = self.page.url.lower()
        return "signin" in current_url or "registration" in current_url

    def is_rating_modal_closed(self) -> bool:
        return self.page.locator("[data-testid='promptable__pc']").count() == 0

    def open_photos(self):
        self.page.get_by_test_id("hero__photo-link").click()