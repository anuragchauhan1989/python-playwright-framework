from locators.locators import FindCenterPageLocators
from pages.base_page import BasePage

class FindCenterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.search_box= page.locator(FindCenterPageLocators.SEARCH_BOX)
        self.center_results = page.locator(FindCenterPageLocators.CENTER_RESULTS)
        self.center_results_container = page.locator(FindCenterPageLocators.CENTER_RESULTS_CONTAINER)
        self.center_cards = page.locator(FindCenterPageLocators.CENTER_CARDS)
        self.summary_text = page.locator(FindCenterPageLocators.SUMMARY_TEXT)
        self.first_center_card_name = page.locator(FindCenterPageLocators.FIRST_CENTER_CARD_NAME)
        self.first_center_card_address = page.locator(FindCenterPageLocators.FIRST_CENTER_CARD_ADDRESS)
        self.popup_card_name= page.locator(FindCenterPageLocators.POPUP_CARD_NAME)
        self.POPUP_CARD_ADDRESS= page.locator(FindCenterPageLocators.POPUP_CARD_ADDRESS)
    

    def search_for(self, location):

         # Wait for the DOM to be fully loaded
         self.wait_for_dom_content_loaded()

         # Wait for the main container to appear
         self.wait_for_locator_visible(self.center_results_container)
        
         self.wait_for_loader_to_disappear(selector=".elipsesLoader")
       
         self.wait_and_click(self.search_box)
         
         self.search_box.clear()
         
         self.search_box.click()

         self.search_box.fill("")  # Clear any existing text

         self.search_box.type(location, delay=200)  # Simulate real typing
         
         self.search_box.press("Enter")

         self.wait_for_full_load()


    def get_summary_count(self):
        text = self.summary_text.inner_text()
        return int(text)


    def get_displayed_count(self):
        return self.center_cards.count()


    def get_first_center_info(self):
        name = self.first_center_card_name.inner_text()
        address = self.first_center_card_address.inner_text()
        return name, address


    def click_first_center_card(self):
        self.wait_and_click(self.first_center_card_name)


    def get_popup_center_info(self):
        name = self.popup_card_name.inner_text()
        address = self.POPUP_CARD_ADDRESS.inner_text() 
        formatted_address = self.format_address(address)       
        return name, formatted_address


    def format_address(self, address: str) -> str:
        """
        Takes a multi-line address and returns a single-line formatted version.
        Example input: '129 Hudson Street\nNew York, NY 10013'
        Output: '129 Hudson Street New York, NY 10013'
        """
        return ' '.join(line.strip() for line in address.strip().split('\n') if line)

