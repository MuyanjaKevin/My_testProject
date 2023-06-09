from src.common.BaseWrapper import BaseWrapper


class NavigationPageForAuthUser(BaseWrapper):
    USERNAME = '//*[@id="nav-link-accountList-nav-line-1"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_userName(self):
        self.find_element_by_xpath(self.USERNAME).text
