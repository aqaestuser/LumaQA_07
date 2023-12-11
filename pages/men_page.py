import random
from base.seleniumbase import BasePage
from locators.men_page_locators import MenPageLocators, MenCategoryPageLocators as MenCPL


class MenPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/men.html'

    def select_tops_from_sidebar_menu(self):
        self.hold_mouse_on_element(MenPageLocators.TOPS_CATEGORY_LINK)
        self.is_clickable(MenPageLocators.TOPS_CATEGORY_LINK).click()

    def select_tops_from_men_dropdown(self):
        self.hold_mouse_on_element(MenPageLocators.MEN_DROPDOWN_BUTTON)
        self.is_clickable(MenPageLocators.TOPS_DROPDOWN_BUTTON).click()

    def select_jackets_from_tops_dropdown(self):
        self.hold_mouse_on_element(MenPageLocators.MEN_DROPDOWN_BUTTON)
        self.hold_mouse_on_element(MenPageLocators.TOPS_DROPDOWN_BUTTON)
        self.hold_mouse_on_element(MenPageLocators.SIDE_BAR_JACKETS)
        self.is_clickable(MenPageLocators.SIDE_BAR_JACKETS).click()

    def select_bottoms_from_men_dropdown(self):
        self.hold_mouse_on_element(MenPageLocators.MEN_DROPDOWN_BUTTON)
        self.is_clickable(MenPageLocators.BOTTOMS_DROPDOWN_BUTTON).click()

    def select_bottoms_from_sidebar_menu(self):
        self.hold_mouse_on_element(MenPageLocators.BOTTOMS_CATEGORY_LINK)
        self.is_clickable(MenPageLocators.BOTTOMS_CATEGORY_LINK).click()


class MenJacketsPage(BasePage):
    def random_choice_item(self):
        num_jackets = 11
        jacket_items = [MenCPL.create_item_list(i) for i in range(1, num_jackets + 1)]
        random_jacket = random.choice(jacket_items)
        self.hold_mouse_on_element(random_jacket)
        return random_jacket

    def check_all_button(self):
        inner_buttons = self.find_element(MenPageLocators.INNER_BUTTONS)
        return inner_buttons

