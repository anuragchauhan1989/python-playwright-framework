# locators.py

class HomePageLocators:
    COOKIES_ACCEPT = "button#onetrust-accept-btn-handler"
    SEARCH_ICON = "//a[@href='#subnav-search-desktop-top' and contains(@class, 'nav-link-search') and contains(@class, 'track_nav_interact')]"
    SEARCH_FIELD = "//*[@id=\"subnav-search-desktop-top\"]//*[@id=\"search-field\"]"
    SEARCH_BUTTON = "//*[@id=\"subnav-search-desktop-top\"]//button[contains(@class, 'btn-search') and @type='submit']"
    FIND_A_CENTER = "//*[contains(@class,'js-nav-top')]//li[contains(@class, 'nav-item') and contains(@class, 'displayed-desktop')]//a[normalize-space(text())='Find a Center']"

class SearchResultsPageLocators:
    FIRST_RESULT_TITLE = "//h3[@class='title' and text()='Employee Education in 2018: Strategies to Watch']"

class FindCenterPageLocators:
    SEARCH_BOX = "input#addressInput"
    SUMMARY_TEXT = "//span[@class='resultsNumber']"
    CENTER_CARDS = "//div[@class='centerResult infoWindow track_center_select covidOpen']"
    FIRST_CENTER_CARD_NAME = "//*[@id=\"1489\"]/div[1]/div[1]/h3"
    FIRST_CENTER_CARD_ADDRESS = "//*[@id=\"1489\"]/div[1]/div[1]/span[2]"
    POPUP_CARD_NAME = "span.mapTooltip__headline"
    POPUP_CARD_ADDRESS = ".mapTooltip__address"
    CENTER_RESULTS = "div.centerLocator__results"
    CENTER_RESULTS_CONTAINER ="#center-results-container"

    