from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class GoodsDetailPage(BaseAction):

    res_label = By.ID, "InitCartUrl"
    res_subscribe = By.ID, "btn-reservation"

    def click_add_shop_cart(self):
        self.click(self.res_label)

    def click_add_subscribe(self):
        self.click(self.res_subscribe)

    def switch_page(self):
        self.get_page()
