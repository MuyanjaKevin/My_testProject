from src.WebElements.ButtonElement import ButtonElement
from src.common.BaseWrapper import BaseWrapper


class AllSection(BaseWrapper):

    HELLO_SIGN_IN_XPATH = '//*[@id="hmenu-customer-name"]/b'
    ALL_MENU = '//*[@id="hmenu-content"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.hello_sign_in_xpath = ButtonElement(self.HELLO_SIGN_IN_XPATH, driver)
        self.all_menu = ButtonElement(self.ALL_MENU, driver)

    def get_hello_sign_in_text(self):
        return self.find_element_by_xpath(self.HELLO_SIGN_IN_XPATH).text()
