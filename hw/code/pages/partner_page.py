from .base import WebPage
from .elements import WebElement


class PartnerPage(WebPage):
    spravka_button = WebElement(xpath="//span[contains(@class, 'vkuiButton__content') and text()='Справка']")

    my_cabinet = WebElement(xpath="//span[contains(@class, 'vkuiButton__content') and text()='Перейти в кабинет']")

    instream = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Instream']")
    banner = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Баннер']")
    adaptive_block = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Адаптивный блок']")
    inpage = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='InPage']")
    fullscreen_block = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Полноэкранный блок']")
    sticky_banner = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Sticky-баннер']")
    banner_apps = WebElement(xpath="/html/body/article/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div[2]")
    native_format = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Нативный формат']")
    fullscreen_block_apps = WebElement(xpath="/html/body/article/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]/div[2]")
    video_reward = WebElement(xpath="//div[contains(@class, 'Slider_title__9GkaJ') and text()='Видео за вознаграждение']")

    cookie = WebElement(xpath="/html/body/div/button/span[1]/span")
    for_sites = WebElement(xpath="/html/body/article/div/div[2]/div[2]/div[2]/button[1]")
    for_apps = WebElement(xpath="/html/body/article/div/div[2]/div[2]/div[2]/button[2]")

    name_field = WebElement(xpath='//*[@id="name"]')
    email_field = WebElement(xpath='//*[@id="email"]')
    submit_button = WebElement(xpath='//*[@id="form"]/form/div[2]/button')

    thanks_message = WebElement(xpath='//*[@id="form"]/form/div/div[2]')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/partner'
        super().__init__(web_driver, url)
