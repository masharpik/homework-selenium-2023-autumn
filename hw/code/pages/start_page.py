from .base import WebPage
from .elements import WebElement


class StartPage(WebPage):
    h1_text = WebElement(xpath='//*[@id="title"]')
    second_radio_button = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div[4]/div[2]')
    cookie = WebElement(xpath="/html/body/div/button/span[1]/span")

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/'
        super().__init__(web_driver, url)
