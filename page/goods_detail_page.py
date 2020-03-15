from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import allure

class GoodsDetailPage(BaseAction):

    res_label = By.ID, "InitCartUrl"
    res_subscribe = By.ID, "btn-reservation"

    @allure.step(title="添加商品至购物车")
    def click_add_shop_cart(self):
        self.click(self.res_label)

    def click_add_subscribe(self):
        self.click(self.res_subscribe)

    def switch_page(self):
        self.get_page()
