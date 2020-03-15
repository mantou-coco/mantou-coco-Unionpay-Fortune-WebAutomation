from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import allure


class Jdhome(BaseAction):
    search_edit_text_jd = By.XPATH, "//*[@id='key']"
    search_button_jd = By.CLASS_NAME, "button"

    @allure.step(title="搜索框输入物品")
    def input_search_jd(self, text):
        self.input(self.search_edit_text_jd, text)

    @allure.step(title="点击查找")
    def click_search_jd(self):
        self.click(self.search_button_jd)

    @allure.step(title="根据输入标题切换句柄(页面)")
    def switch_page(self, title):
        self.get_page(title)
