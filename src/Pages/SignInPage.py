import os

from src.WebElements.ButtonElement import ButtonElement
from src.WebElements.InputElements import InputElements
from src.common.BaseWrapper import BaseWrapper


class SignInUp(BaseWrapper):
    SIGN_IN_PAGE = '//*[@id="authportal-main-section"]//form/div/div/div'
    SIGN_IN_BUTTON = '//*[@id="nav-signin-tooltip"]/a/span'
    EMAIL_INPUT = '//*[@id="ap_email"]'
    SIGN_IN_TEXT = 'Sign In'
    PASSWORD_INPUT = '//*[@id="ap_password"]'
    SIGN_IN_SUBMIT_BUTTON = '//*[@id="signInSubmit"]'
    CONTINUE_BUTTON = '//*[@id="continue"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_button = ButtonElement(self.SIGN_IN_BUTTON, driver)
        self.email_input = InputElements(self.EMAIL_INPUT, driver)
        self.password_input = InputElements(self.PASSWORD_INPUT, driver)
        self.sign_submit_button = ButtonElement(self.SIGN_IN_SUBMIT_BUTTON, driver)
        self.continueButtonXpath = ButtonElement(self.CONTINUE_BUTTON, driver)

    def presence_of_Sign_In_Page(self):
        self.find_element_by_xpath(self.SIGN_IN_PAGE)

    def sign_in(self, phoneNumber, passwords):
        self.sign_in_button.click_btn_by_xpath()
        self.email_input.send_data_by_xpath(phoneNumber)
        self.continueButtonXpath.click_btn_by_xpath()
        self.password_input.send_data_by_xpath(passwords)
        self.sign_submit_button.click_btn_by_xpath()
