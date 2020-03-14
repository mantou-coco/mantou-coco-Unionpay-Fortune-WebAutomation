from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class Goodspage(BaseAction):

    first_image = By.XPATH, "//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img"

    def click_first_image(self):
        self.click(self.first_image)

