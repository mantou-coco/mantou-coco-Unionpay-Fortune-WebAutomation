from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import allure




class Resbaidu(BaseAction):
    jd_button = By.XPATH, '//*[@id="content_left"]//a'

    @allure.step(title="点击'京东'")
    def click_jd(self):
        self.click(self.jd_button)





