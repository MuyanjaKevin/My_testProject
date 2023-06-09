from src.common.BaseWrapper import BaseWrapper
from src.WebElements.ButtonElement import ButtonElement
from src.WebElements.InputElements import InputElements


class LandingPage(BaseWrapper):
    AMAZON_LOGO_LINK_XPATH = '//*[@id="nav-logo-sprites"]'
    SEARCH_BAR_XPATH = '//*[@id="twotabsearchtextbox"]'
    SEARCH_ICON_XPATH = '//*[@id="nav-search-submit-button"]'
    LOCATION_BUTTON_XPATH = '//*[@id="nav-global-location-popover-link"]'
    ALL_DROPDOWN_XPATH = '//*[@id="nav-hamburger-menu"]'
    LANGUAGE_DROPDOWN_XPATH = '//*[@id="icp-nav-flyout"]/span'
    SIGN_IN_DROPDOWN_MENU_XPATH = '//*[@id="nav-link-accountList"]'
    RETURNS_AND_ORDERS_XPATH = '//*[@id="nav-orders"]'
    CART_XPATH = '//*[@id="nav-cart-count-container"]'
    SHOP_GREAT_DEALS_XPATH = '//*[@id="swm-link"]'
    CUSTOMER_SERVICE_LINK_CSS = '#nav-xshop > a:nth-child(2)'
    REGISTRY_LINK_CSS = '#nav-xshop > a:nth-child(3)'
    GIFT_CARDS_LINK_CSS = '#nav-xshop > a:nth-child(4)'
    SELL_LINK_CSS = '#nav-xshop > a:nth-child(5)'
    SEARCH_RESULTS = '// *[ @ id = "search"] / span / div / h1 / div / div[1] / div / div'

    def __init__(self, driver) -> None:
        super().__init__(driver)

        self.amazon_logo_xpath = ButtonElement(self.AMAZON_LOGO_LINK_XPATH, driver)
        self.search_bar_xpath = InputElements(self.SEARCH_BAR_XPATH, driver)
        self.search_icon_xpath = ButtonElement(self.SEARCH_ICON_XPATH, driver)
        self.location_button_xpath = ButtonElement(self.LOCATION_BUTTON_XPATH, driver)
        self.all_drop_down_xpath = ButtonElement(self.ALL_DROPDOWN_XPATH, driver)
        self.language_button_xpath = ButtonElement(self.LANGUAGE_DROPDOWN_XPATH, driver)
        self.sign_in_dropdown_menu_xpath = ButtonElement(self.SIGN_IN_DROPDOWN_MENU_XPATH, driver)
        self.returns_and_orders_xpath = ButtonElement(self.RETURNS_AND_ORDERS_XPATH, driver)
        self.cart_xpath = ButtonElement(self.CART_XPATH, driver)
        self.shop_great_deals_xpath = ButtonElement(self.SHOP_GREAT_DEALS_XPATH, driver)
        self.customer_service_link_css = ButtonElement(self.CUSTOMER_SERVICE_LINK_CSS, driver)
        self.registry_link_css = ButtonElement(self.REGISTRY_LINK_CSS, driver)
        self.sell_link_css = ButtonElement(self.SELL_LINK_CSS, driver)

    def search_for_an_item(self, text: str) -> None:
        self.search_bar_xpath.send_data_by_xpath(text)
        self.search_icon_xpath.click_btn_by_xpath()

    def get_search_results(self):
        self.find_element_by_xpath(self.SEARCH_RESULTS).text
