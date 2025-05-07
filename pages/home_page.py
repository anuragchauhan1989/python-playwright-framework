from pages.base_page import BasePage
from locators.locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.COOKIES_ACCEPT = page.locator(HomePageLocators.COOKIES_ACCEPT)
        self.search_icon =  page.locator(HomePageLocators.SEARCH_ICON)
        self.search_field = page.locator(HomePageLocators.SEARCH_FIELD)
        self.search_button = page.locator(HomePageLocators.SEARCH_BUTTON)
        self.find_a_center = page.locator(HomePageLocators.FIND_A_CENTER)


    def get_cookies_accept(self):
        self.wait_and_click(self.COOKIES_ACCEPT)

    def open_search(self):
        self.wait_and_click(self.search_icon)

    def is_search_visible(self):
        return self.search_field.is_visible()

    def perform_search(self, query):
        self.search_field.fill(query)
        self.wait_and_click(self.search_button)

    def click_find_a_center(self):
        self.wait_and_click(self.find_a_center)