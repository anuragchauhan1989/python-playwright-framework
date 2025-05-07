import pytest
from playwright.sync_api import Page

from pages.search_results_page import SearchResultsPage
from pages.home_page import HomePage
import logging

logger = logging.getLogger(__name__)

def test_article_search_exact_match(page: Page):
    # Navigate to BH home page
    page.goto("https://www.brighthorizons.com/")
    home = HomePage(page)
    home.get_cookies_accept()

    logger.info("====click on seach icon====")
    home.open_search()

    assert home.is_search_visible(), "Search field is not visible."

    query = "Employee Education in 2018: Strategies to Watch"
    home.perform_search(query)

    results = SearchResultsPage(page)
    
    logger.info("\n =====match the typed search string with the first result string")
    first_result = results.get_first_result_text()
    assert first_result.strip() == query, f"Expected '{query}', but got '{first_result}'"
