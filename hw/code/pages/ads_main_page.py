#!/usr/bin/python3
# -*- encoding=utf8 -*-

from .base import WebPage
from .elements import WebElement
from .elements import ManyWebElements


class AdsMainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/'

        super().__init__(web_driver, url)

    # cookie
    button_cookie_accept = WebElement(xpath='//div[contains(@class, "CookieBanner_wrapper")]//button')

    # footer
    footer_section = WebElement(xpath='//*[contains(@class, "Footer_footer")]')
    button_go_to_office = WebElement(
        xpath='//div[contains(@class, "Footer_leftContent")]/a[contains(@class, "ButtonCabinet_primary")]')

    footer_icons = ManyWebElements(
        xpath='//div[contains(@class, "Footer_leftControls")]//a[contains(@class, "Footer_control")]')
    footer_sections = ManyWebElements(
        xpath='//ul[contains(@class, "Footer_items")]/li[contains(@class, "Footer_item")]/a')
    button_about = WebElement(xpath='//a[contains(@class, "Footer_about")]')

    # footer lang
    selector_lang = WebElement(xpath='//div[contains(@class, "SelectLanguage_desktopSelect")]')
    button_logo = WebElement(xpath='//div[contains(@class, "Footer_controls")]/a')
    button_english = WebElement(xpath='//div[contains(@class, "vkuiPopper")]//*[text()="English"]')

    # auth
    input_login = WebElement(xpath='//input[@name="login"]')
    input_password = WebElement(xpath='//input[@name="password"]')
    button_submit = WebElement(xpath='//button[@type="submit"]')
    
    def is_visible_footer(self):
        JS_IS_VISIBLE_IN_VIEWPORT = "var elem = arguments[0], box = elem.getBoundingClientRect(), cx = box.left + box.width / 2, cy = box.top + box.height / 2, e = document.elementFromPoint(cx, cy); for (; e; e = e.parentElement) { if (e === elem) return true; } return false;"
        return self._web_driver.execute_script(JS_IS_VISIBLE_IN_VIEWPORT, self.footer_section.find())

    def click_social_icon(self, icon_index):
        footer_icons = self.footer_icons.find()    
        footer_icons[icon_index].click()
