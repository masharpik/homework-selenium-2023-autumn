from .base import WebPage
from .elements import WebElement


class PartnerHelpPage(WebPage):
    search_input = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[1]/div/div/div/label/input')

    authorization = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[1]/div/div/span/span')
    ad_settings = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[3]/div/div/span/span')
    ad_tools = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[5]/div/div/span/span')
    statistics_and_finance = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[7]/div/div/span/span')
    documents = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[9]/div/div/span/span')
    simplified_cabinet = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[11]/div/div/span/span')
    faq = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[13]/div/div/span/span')
    partner_cabinet = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[1]/div[2]/div[15]/div/div/span/span')

    beginning_work = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[1]/a/div/div/span')
    partner_documents = WebElement(
        xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[2]/a/div/div/span')
    advertising_on_sites = WebElement(
        xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[3]/a/div/div/span')
    advertising_in_apps = WebElement(
        xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[4]/a/div/div/span')
    integration_documentation = WebElement(
        xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[5]/a/div/div/span')
    partner_cabinet_statistics = WebElement(
        xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[6]/a/div/div/span')
    vk_ad_network_api = WebElement(
        xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[7]/a/div/div/span')
    help_section = WebElement(xpath='//*[@id="help-layout"]/div[2]/div[2]/div/div/div/div[2]/div[8]/a/div/div/span')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/help/categories/partner'
        super().__init__(web_driver, url)
