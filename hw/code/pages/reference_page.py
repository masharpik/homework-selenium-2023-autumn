#!/usr/bin/python3
# -*- encoding=utf8 -*-

from .base import WebPage
from .elements import WebElement
from .elements import ManyWebElements


class RefPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/help'
        super().__init__(web_driver, url)

    # разделы документации
    sections = ManyWebElements(xpath='//a[contains(@class, "CategoryCard_wrapper")]')

    # поиск по документации 
    input_search = WebElement(
        xpath='//div[@class="Search_fullscreen__hU6UF"]//label[@class="vkuiSearch__control"]//input')
    button_clear = WebElement(xpath='//div[@data-test-id="categories-page-vkads"]//div[@class="vkuiSearch__icons"]')
    suggections = ManyWebElements(xpath='//span[contains(@class, "SuggestionItem_title")]')

    # разделы как селектор
    selector_sections = ManyWebElements(
        xpath='//span[@class="NavigationItem_content__dsNgk" and @title="Инструменты рекламы"]')
    section_utm_marks = ManyWebElements(
        xpath='//span[@class="NavigationItem_content__dsNgk NavigationItem_contentNotActive__JI134" and @title="UTM-метки"]')
    suggection_result = WebElement(xpath='//div[contains(@class, "Suggestions_result")]')
