from selenium import webdriver
from page.page import Page
from time import sleep
import pytest




class Test_Jd:

    @pytest.fixture(autouse=True, params=["Chrome"])
    def setup(self, request):
        self.driver = eval("webdriver.%s()" % request.param)
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_add_cart(self):
        self.page.Baiduhome.input_search("京东")
        self.page.Baiduhome.click_search()
        self.page.Resbaidu.click_jd()
        self.page.Jdhome.switch_page("京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
        self.page.Jdhome.input_search_jd("apple11promax")
        self.page.Jdhome.click_search_jd()
        self.page.Goodspage.click_first_image()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.page.GoodsDetailPage.click_add_shop_cart()
        # self.page.GoodsDetailPage.click_add_subscribe()
        # assert self.page.ShopCartPage.get_res_subscribe_text() == "预约成功，已获得抢购资格"
        # assert self.page.ShopCartPage.get_res_text() == "商品已成功加入购物车！"
        assert "商品已成功加入" in self.page.ShopCartPage.get_res_text()





