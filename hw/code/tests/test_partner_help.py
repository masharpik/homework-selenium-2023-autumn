import time

import pytest
from selenium.webdriver.common.action_chains import ActionChains


def test_partner_help_page_has_title(partner_help_page):
    assert partner_help_page.get_title() in 'Кабинет партнера — Справка Рекламной сети VK'


def test_presense_search_input(partner_help_page):
    assert partner_help_page.search_input.is_presented()


@pytest.mark.parametrize('element_name, expected_text', [
    ('authorization', 'Авторизация'),
    ('ad_settings', 'Как настроить рекламу'),
    ('ad_tools', 'Инструменты рекламы'),
    ('statistics_and_finance', 'Статистика и финансы'),
    ('documents', 'Документы'),
    ('simplified_cabinet', 'Упрощенный кабинет'),
    ('faq', 'FAQ'),
    ('partner_cabinet', 'Кабинет партнера')
])
def test_presense_help_categories(partner_help_page, element_name, expected_text):
    element = getattr(partner_help_page, element_name)

    assert element.get_text() in expected_text

@pytest.mark.parametrize('element_attribute, expected_url', [
    ('beginning_work', 'https://ads.vk.com/help/subcategories/partner_start'),
    ('partner_documents', 'https://ads.vk.com/help/subcategories/partner_documents'),
    ('advertising_on_sites', 'https://ads.vk.com/help/subcategories/partner_site'),
    ('advertising_in_apps', 'https://ads.vk.com/help/subcategories/partner_app'),
    ('integration_documentation', 'https://ads.vk.com/help/subcategories/partner_integration'),
    ('partner_cabinet_statistics', 'https://ads.vk.com/help/subcategories/partner_statistics'),
    ('vk_ad_network_api', 'https://ads.vk.com/help/subcategories/partner_api'),
    ('help_section', 'https://ads.vk.com/help/subcategories/partner_help')
])
def test_urls_after_click_in_page(partner_help_page, web_browser, element_attribute, expected_url):
    element = getattr(partner_help_page, element_attribute)
    # actions = ActionChains(web_browser)
    # actions.move_to_element(element.find()).perform()
    element.locate_element_in_center()
    web_browser.execute_script("arguments[0].click();", element.find())
    element._page.wait_page_loaded()
    assert expected_url in web_browser.current_url
