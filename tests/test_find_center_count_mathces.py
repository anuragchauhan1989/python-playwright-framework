from pages.home_page import HomePage
from pages.find_center_page import FindCenterPage
from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

def test_article_search_exact_match(page: Page):
    # Navigate to BH home page
    page.goto("https://www.brighthorizons.com/")
    home = HomePage(page)
    home.get_cookies_accept()
    
    # Click on "Find a Center" option
    logger.info("=====click on find a center option=====")
    home.click_find_a_center()

    assert "/child-care-locator" in page.url, f"Expected URL to contain '/child-care-locator', but got {page.url}"

    # Seach for New York
    center_page = FindCenterPage(page)
    center_page.search_for("New York")

    # Verify numbers of centers matches list
    expected = center_page.get_summary_count()
    actual = center_page.get_displayed_count()
    print("expected: ", expected, "actual: ", actual )
    assert expected == actual, f"Expected {expected} centers, but displayed {actual}"

    # Click on the first center on the list
    name_on_list, address_on_list = center_page.get_first_center_info()
    center_page.click_first_center_card()

    # Verify name and address in popup match the list
    name_on_popup, address_on_popup = center_page.get_popup_center_info()
    
    logger.info("\n =====match the name on list with the name on pop up")
    # Verify if center name and address are the same (on the list and on the popup)
    assert name_on_list == name_on_popup, f"Center name mismatch: list='{name_on_list}', popup='{name_on_popup}'"
    
    logger.info("\n =====match the address on list  with the address on pop up")
    assert address_on_list == address_on_popup, f"Center address mismatch: list='{address_on_list}', popup='{address_on_popup}'"







