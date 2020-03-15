from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import allure

class Goodspage(BaseAction):

    first_image = By.XPATH, "//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img"

    @allure.step(title="点击商品图标")
    def click_first_image(self):
        self.click(self.first_image)

