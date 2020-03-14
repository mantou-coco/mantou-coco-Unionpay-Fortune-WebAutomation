from page.baidu_home import Baiduhome
from page.goods_detail_page import GoodsDetailPage
from page.shop_cart_page import ShopCartPage
from page.goods_page import Goodspage
from page.jd_home import Jdhome
from page.res_baidu import Resbaidu






class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def Baiduhome(self):
        return Baiduhome(self.driver)

    @property
    def GoodsDetailPage(self):
        return GoodsDetailPage(self.driver)

    @property
    def ShopCartPage(self):
        return ShopCartPage(self.driver)

    @property
    def Goodspage(self):
        return Goodspage(self.driver)

    @property
    def Jdhome(self):
        return Jdhome(self.driver)

    @property
    def Resbaidu(self):
        return Resbaidu(self.driver)
