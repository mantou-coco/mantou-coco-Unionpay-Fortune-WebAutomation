from base.base_action import BaseAction
from selenium.webdriver.common.by import By



class Jdhome(BaseAction):
    search_edit_text_jd = By.ID, "key"
    search_button_jd = By.CLASS_NAME, "button"

    def input_search_jd(self, text):
        self.input(self.search_edit_text_jd, text)

    def click_search_jd(self):
        self.click(self.search_button_jd)

    def switch_page(self, title):
        self.get_page(title)
