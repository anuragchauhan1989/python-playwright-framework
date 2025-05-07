from pages.base_page import BasePage
from locators.locators import SearchResultsPageLocators

class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_result = page.locator(SearchResultsPageLocators.FIRST_RESULT_TITLE).first

    def get_first_result_text(self):
        return self.first_result.inner_text()
