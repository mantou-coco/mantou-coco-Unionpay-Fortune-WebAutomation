from selenium import  webdriver
from page.page import Page
from time import sleep
import pytest
import allure


class Test_Jd:

    @pytest.fixture(autouse=True, params=["Firefox", "Chrome"])
    def setup(self, request):
        self.driver = eval("webdriver.%s()" % request.param)
        self.driver.get("https://www.baidu.com/")
        # self.driver.maximize_window()
        self.page = Page(self.driver)
        def teardown():
            sleep(3)
            self.driver.quit()
        request.addfinalizer(teardown)
        return request.param

    @allure.description("添加商品至购物车——商品描述")
    def test_add_cart(self, setup):
        allure.dynamic.title("添加商品至购物车——%s" % setup)
        self.page.Baiduhome.input_search("京东")
        self.page.Baiduhome.click_search()
        self.page.Resbaidu.click_jd()
        self.page.Jdhome.switch_page("京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
        self.page.Jdhome.input_search_jd("apple11promax")
        self.page.Jdhome.click_search_jd()
        self.page.Goodspage.click_first_image()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.page.GoodsDetailPage.click_add_shop_cart()
        assert "加入购物车！" in self.page.ShopCartPage.get_res_text()





