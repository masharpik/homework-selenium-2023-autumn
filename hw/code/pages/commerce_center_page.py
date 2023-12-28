from .base import WebPage
from .elements import WebElement


class CommerceCenterPage(WebPage):
    create_catalog_button = WebElement(xpath='//*[@id="catalogs"]/div/div/section/div/div/div/div[2]/div/div[2]/button[1]')
    create_catalog_popup = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div')
    marketplace_tab = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/section/div/div[2]/div/div[2]')
    marketplace_url_input = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/section/div/div[3]/div[1]/span[1]/input')
    submit_button = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[2]/div/button[1]')
    error_message = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/section/div/div[3]/div[1]/span[2]/div')


    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/hq/ecomm/catalogs'
        super().__init__(web_driver, url)
