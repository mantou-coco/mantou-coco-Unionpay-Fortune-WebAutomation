from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        """
        根据特征找元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 找到的元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10, poll=1):
        """
        根据特征点击某个元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return:
        """
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, text, timeout=10, poll=1):
        """
        根据特征输入元素
        :param feature: 特征
        :param text: 输入的文字
        :param timeout: 超时时间
        :param poll: 频率
        :return:
        """
        self.clear(feature)
        self.find_element(feature, timeout, poll).send_keys(text)

    def clear(self, feature, timeout=10, poll=1):
        """
        根据特征清空某个元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return:
        """
        self.find_element(feature, timeout, poll).clear()

    def get_text(self, feature, timeout=10, poll=1):
        """
        根据特征获取特征元素的文字
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 文字内容
        """
        return self.find_element(feature, timeout, poll).text

    def get_page(self, title):
        """
        根据标题切换至指定句柄页面
        :param title:标题
        :return:如果传进来的标题名称和当前页面获取的标题一致则切换指定句柄窗口页面 如果不一致则循环判断直至跳转为止
        """
        for i in self.driver.window_handles:
            if i != self.driver.current_window_handle:
                self.driver.switch_to.window(i)
                ti = self.driver.title
                if ti == title:
                    return self.driver.switch_to.window(i)
                else:
                    return self.get_page



