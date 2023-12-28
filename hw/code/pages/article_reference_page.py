#!/usr/bin/python3
# -*- encoding=utf8 -*-

from .base import WebPage
from .elements import WebElement
from .elements import ManyWebElements


class ArticleRefPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/help/articles/utm'
        super().__init__(web_driver, url)

    # ссылки и кнопки на странице в документации
    button_ref = ManyWebElements(xpath='//div[@class="NavigationVKAds_help__QF364"]')
    button_back_to_adds = WebElement(xpath='//div[@class="Summary_leftArrow__gcUOO"]')
    hyperlinks_header = ManyWebElements(xpath='//li[@class="MetaBlock_linkText__NBQUq"]')
