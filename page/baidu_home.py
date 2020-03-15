from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import allure



class Baiduhome(BaseAction):
    search_edit_text = By.ID, "kw"
    search_button = By.ID, "su"

    @allure.step(title="输入'京东'")
    def input_search(self, text):
        self.input(self.search_edit_text, text)

    @allure.step(title="点击百度一下")
    def click_search(self):
        self.click(self.search_button)


