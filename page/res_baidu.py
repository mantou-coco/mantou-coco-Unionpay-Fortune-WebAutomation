from base.base_action import BaseAction
from selenium.webdriver.common.by import By





class Resbaidu(BaseAction):
    jd_button = By.XPATH, '//*[@id="content_left"]//a'

    def click_jd(self):
        self.click(self.jd_button, 10, 1)





