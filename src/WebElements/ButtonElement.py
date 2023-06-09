from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from src.common.BaseWrapper import BaseWrapper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ButtonElement(BaseWrapper):
    def __init__(self, selector, driver) -> None:
        super().__init__(driver)
        self.selector = selector

    def click_btn_by_xpath(self) -> None:
        button_element = self.find_element_by_xpath(self.selector)
        button_element.click()

    def click_btn_by_Css(self) -> None:
        button_element = self.find_element_by_css(self.selector)
        button_element.click()

    def hover_and_click_by_css(self, wait_time=10) -> None:
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(By.CSS_SELECTOR, self.selector))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def click_btn_by_index_css(self, index: int) -> None:
        button = self.find_element_by_css(self.selector.format(index))
        button.click()

    def click_btn_by_name_by_xpath(self, btn_name) -> None:
        elements = self.find_elements_by_xpath(self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return
