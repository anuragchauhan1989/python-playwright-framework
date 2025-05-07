class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_and_click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def wait_for_dom_content_loaded(self):
        # Wait for the DOM to be fully loaded
        self.page.wait_for_load_state("domcontentloaded")

    def wait_for_locator_visible(self, locator):
        locator.wait_for(state="visible")
        
    def wait_for_loader_to_disappear(self, selector: str):
        self.page.wait_for_selector(selector, state="hidden")

    def wait_for_full_load(self):
        self.page.wait_for_load_state("load")


        