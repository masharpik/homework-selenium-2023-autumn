from .base import WebPage
from .elements import WebElement


class InsightsPage(WebPage):
    more_button = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[1]/a/div/div[2]/button')
    first_material = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/div[2]/a/div/div[1]')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/insights'
        super().__init__(web_driver, url)