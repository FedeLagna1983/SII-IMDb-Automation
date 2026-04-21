from pages.base_page import BasePage


class MenuPage(BasePage):
    def open_menu(self):
        self.page.get_by_label("Open Navigation Drawer").click()

    def go_to_top_box_office(self):
        self.page.get_by_label("Go to Top box office").click()

    def go_to_top_250_tv_shows(self):
        self.page.wait_for_selector('[data-testid="panel"]')
        top_250 = self.page.get_by_label("Go to Top 250 TV shows").first
        top_250.wait_for(state="attached")

        try:
            top_250.click()
        except Exception:
            tv_section = self.page.get_by_label("Expand TV shows nav links")
            if tv_section.count() > 0:
                tv_section.first.click(force=True)
            top_250.evaluate("el => el.click()")

    def go_to_born_today(self):
        self.page.wait_for_timeout(500)
        born_today = self.page.get_by_label("Go to Born today").first
        born_today.wait_for(state="attached")

        try:
            born_today.click(timeout=5000)
        except Exception:
            href = born_today.get_attribute("href")
            assert href, "Born today link does not contain href"
            self.page.goto(f"https://www.imdb.com{href}")

        self.page.wait_for_load_state("domcontentloaded")