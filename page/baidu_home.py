from base.base_action import BaseAction
from selenium.webdriver.common.by import By




class Baiduhome(BaseAction):
    search_edit_text = By.ID, "kw"
    search_button = By.ID, "su"


    def input_search(self, text):
        self.input(self.search_edit_text, text)

    def click_search(self):
        self.click(self.search_button)


