from .base import WebPage
from .elements import WebElement


class NewsPage(WebPage):
    header = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div/div[1]/div/h1')
    subtitle = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div/div[1]/div/h2')

    preview_date = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div/div[1]/div/div/time')
    preview_title = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div/div[2]/div/div')
    preview_image = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div/div[1]/div/span/img')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/news'
        super().__init__(web_driver, url)
