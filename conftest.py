import json
import os
import pytest
from playwright.sync_api import sync_playwright
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level = logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")

def browser_context(browser_name, browser_type_launch_args):
    with sync_playwright() as p:
        browser_type_launch_args = {
            "headless": False,
        }
        if browser_name == "chromium":
            browser = p.chromium.launch(**browser_type_launch_args)
        elif browser_name == "firefox":
            browser = p.firefox.launch(**browser_type_launch_args)
        elif browser_name == "webkit":
            browser = p.webkit.launch(**browser_type_launch_args)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        logger.info("=======browser launched======")
        # Deny all permissions (including geolocation)
        context = browser.new_context(
            permissions=[]  # deny geolocation and all other permissions
        )

        yield context  # yield the context (not the browser)
        context.close()
        browser.close()  # <--- Close after the test is done

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()



