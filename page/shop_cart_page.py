from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class ShopCartPage(BaseAction):

    res_label = By.XPATH, "//*[@id='result']/div/div/div[1]/div[1]/h3"
    res_subscribe = By.XPATH, "//*[@id='yuyue_msg_p']/text()"

    def get_res_text(self):
        return self.get_text(self.res_label)

    def get_res_subscribe_text(self):
        return self.get_text(self.res_subscribe)

