import pytest
from selenium.webdriver.support import expected_conditions as EC

def test_footer_visible_after_scroll(ads_main_page):
    is_visible_before_scroll = ads_main_page.is_visible_footer()
    ads_main_page.scroll_down()
    is_visible_after_scroll = ads_main_page.is_visible_footer()
    assert not is_visible_before_scroll
    assert is_visible_after_scroll

@pytest.fixture
def accept_cookie(ads_main_page):
    if ads_main_page.button_cookie_accept.is_visible():
        ads_main_page.button_cookie_accept.click()


@pytest.mark.parametrize('icon_index, expected_url', [
    (0, 'https://vk.com/vk_ads'),
    (1, 'https://ok.ru/group/64279825940712'),
    (2, 'https://t.me/vk_ads')
])
def test_footer_social_icons_redirect(ads_main_page, accept_cookie, icon_index, expected_url):
    ads_main_page.scroll_down()
    ads_main_page.click_social_icon(icon_index)
    ads_main_page.switch_to_window(1)
    assert ads_main_page.get_current_url() == expected_url, f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking social icon {icon_index+1}'


def test_footer_redirect_button_go_to_office(ads_main_page):
    ads_main_page.scroll_down()
    ads_main_page.button_go_to_office.click()
    ads_main_page.wait_page_loaded()
    assert 'https://id.vk.com/auth' in ads_main_page.get_current_url(), f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking the "Go to Office" button '


@pytest.mark.parametrize('section_index, expected_url, is_new_tab', [
    (0, 'https://ads.vk.com/news', False), 
    (1, 'https://expert.vk.com/', True),
    (2, 'https://ads.vk.com/insights', False),
    (3, 'https://ads.vk.com/cases', False),
    (4, 'https://ads.vk.com/events', False),
    (5, 'https://ads.vk.com/help', False),
    (6, 'https://ads.vk.com/documents', False),
    (7, 'https://ads.vk.com/partner', True)
])
def test_footer_redirect_to_selections(ads_main_page, section_index, expected_url, is_new_tab):
    ads_main_page.scroll_down()
    footer_sections = ads_main_page.footer_sections[section_index].click()
    if is_new_tab:
        ads_main_page.switch_to_window(1)
    ads_main_page.wait_page_loaded()
    assert ads_main_page.get_current_url() == expected_url, f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking on section'

def test_footer_redirect_button_button(ads_main_page):
    ads_main_page.scroll_down()
    ads_main_page.button_logo.click()
    ads_main_page.switch_to_window(1)
    ads_main_page.wait_page_loaded()
    assert ads_main_page.get_current_url() == 'https://vk.company/ru/company/business/', \
        f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking the logo button'


def test_footer_about_button_redirect(ads_main_page):
    ads_main_page.scroll_down()
    ads_main_page.button_about.click()
    ads_main_page.switch_to_window(1)
    ads_main_page.wait_page_loaded()
    assert ads_main_page.get_current_url() == 'https://vk.company/ru/', \
        f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking the about button'


def test_footer_language_selector(ads_main_page, accept_cookie):
    ads_main_page.scroll_down()
    ads_main_page.selector_lang.click()
    ads_main_page.button_english.click()
    ads_main_page.wait_page_loaded()
    assert "News" in ads_main_page.get_page_source()
