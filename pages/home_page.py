from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.imdb.com/"

    def open(self):
        self.navigate(self.URL)