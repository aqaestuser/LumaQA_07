from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


class FooterPage(BasePage):
    locators = BasePageLocators()

    def check_visibility_advanced_search_link(self):
        """This method verifies if the advanced search link is visible on the footer"""
        return self.is_visible(self.locators.LINK_ADVANCED_SEARCH)
