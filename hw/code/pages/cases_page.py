from .base import WebPage
from .elements import WebElement


class CasesPage(WebPage):
    header = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div/div[1]/div/h1')
    subtitle = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[1]/div/div/div[1]/div/h2')

    case_preview_date = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/a[1]/div[1]/div/div/time')
    case_preview_image = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/a[1]/div[1]/div/span/img')
    case_preview_title = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/a[1]/div[2]/div/div[3]')
    case_preview_subtitle = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/a[1]/div[2]/div/div[1]')
    case_preview_description = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/a[1]/div[2]/div/div[2]')
    case_preview_more_button = WebElement(xpath='//*[@id="classic-layout"]/div[2]/div/div/div[2]/a[1]/div[2]/div/button')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/cases'
        super().__init__(web_driver, url)
