from pages.base_page import BasePage


class TopBoxOfficePage(BasePage):
    URL_FRAGMENTS = ("boxoffice", "box-office")
    LIST_ITEM_SELECTOR = "li.ipc-metadata-list-summary-item"

    def is_open(self) -> bool:
        current_url = self.page.url.lower()
        return any(fragment in current_url for fragment in self.URL_FRAGMENTS)

    def open_second_title(self):
        items = self.page.locator(self.LIST_ITEM_SELECTOR)
        items.nth(1).wait_for(state="visible")
        second_item = items.nth(1)
        second_item.locator("a[href^='/title/tt']").first.click()
        self.page.wait_for_url("**/title/tt*/**")
