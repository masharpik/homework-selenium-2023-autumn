#!/usr/bin/python3
# -*- encoding=utf8 -*-

import re
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class ForumPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/upvote'
        super().__init__(web_driver, url)
    

    # search
    input_search = WebElement(xpath='//input[contains(@class, "vkuiSearch__input ")]')
    text_not_search_results = WebElement(xpath='//div[contains(@class, "vkuiPlaceholder vkuiPlaceholder--withPadding")]')
    button_clear_search = WebElement(xpath='//button[contains(@class, "vkuiIconButton ") and @aria-label="Очистить"]')

    # filter
    buttons_clear_filter = ManyWebElements(xpath='//div[contains(@class, "vkuiIconButton ") and @aria-label="Очистить поле"]')
    selector_theme_and_status = ManyWebElements(xpath='//span[contains(@class, "vkuiFormField") and contains(@class, "vkuiSelect")]')
    selector_of_options = ManyWebElements(xpath='//div[contains(@class, "vkuiCustomSelectOption__children")]')

    
    # ideas found
    idea_items = ManyWebElements(xpath='//div[contains(@class, "Idea_cardVote__KkO0P")]')
    statuses_of_ideas_found = ManyWebElements(xpath='//div[contains(@class, "Status_wrap__JQBPe ")]/span')
    tags_of_ideas_found = ManyWebElements(xpath='//div[contains(@class, "Tag_tag__tmnYB")]/span')
    headers_idea = ManyWebElements(xpath='//a[contains(@class, "vkuiLink")]')
    text_date_and_id_of_ideas = ManyWebElements(xpath='//span[contains(@class, "vkuiSimpleCell__text vkuiSimpleCell__subtitle vkuiFootnote")]')
    
    # copy
    buttons_copying_idea = ManyWebElements(xpath='//button[contains(@class, "vkuiIconButton ") and @aria-label="copy"]')
    popup_link_copied = WebElement(xpath='//div[@class="Idea_cardVote__KkO0P"]/div[contains(@class, "vkuiSnackbar")]')

    # like
    buttons_like = ManyWebElements(xpath='//button[contains(@class, "ButtonVote_button__GYraZ ")]')
    text_not_access_like = WebElement(xpath='//h5[contains(@class, "vkuiSubhead ")]')
    
    # comments
    buttons_comments_exists = ManyWebElements(xpath='//button[contains(@class, "ButtonComment_button__JaLa5 ")]/span[contains(@class, "vkuiButton__in")]/span[contains(@class, "vkuiButton__content")]')
    comments_items = ManyWebElements(xpath='//div[@class="Comment_commentsWrap__ePagG"]/div[contains(@class, "vkuiSimpleCell")]')

    
    # modal window of suggest idea
    button_suggest_idea = WebElement(xpath='//span[contains(text(), "Предложить идею")]')
    button_ok_understood = WebElement(xpath='//span[contains(text(), "Ок, понятно")]')
    button_close_modal_window = WebElement(xpath='//div[@aria-label="Закрыть"]')
    
    def id_by_idea(self, idea_index):
        info = self.text_date_and_id_of_ideas[idea_index].text
        match = re.search(r'id (\d+)', info)
        if match:
            return match.group(1)
        else:
            assert False, "ID idea not found"

    def id_idea_by_url(self, url):
        match = re.search(r'/(\d+)$', url)
        if match:
            return match.group(1)
        else:
            assert False, "ID url not found"
