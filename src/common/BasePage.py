from src.Pages.LandingPage import LandingPage
from src.Pages.AllSectionPage import AllSection
from src.Pages.NavigationPageForAuthorizedUser import NavigationPageForAuthUser
from src.Pages.SignInPage import SignInUp
from src.common.BaseWrapper import BaseWrapper


class BasePage(BaseWrapper):
    def __init__(self, driver) -> None:
        super().__init__(driver)

        self.landing = LandingPage(driver)
        self.allSection = AllSection(driver)
        self.signIn_up = SignInUp(driver)
        self.navigationAdmin = NavigationPageForAuthUser(driver)
