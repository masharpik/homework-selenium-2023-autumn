from .base import WebPage
from .elements import WebElement


class EventsPage(WebPage):
    events_preview = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/div/a[1]')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/insights'
        super().__init__(web_driver, url)
