import pytest
from selenium.webdriver.support import expected_conditions as EC
import time

JS_IS_VISIBLE_IN_VIEWPORT = "var elem = arguments[0], box = elem.getBoundingClientRect(), cx = box.left + box.width / 2, cy = box.top + box.height / 2, e = document.elementFromPoint(cx, cy); for (; e; e = e.parentElement) { if (e === elem) return true; } return false;"

@pytest.fixture
def scroll_down(ads_main_page):
    ads_main_page.scroll_down()
    time.sleep(1)


def test_footer_visible_after_scroll(web_browser, ads_main_page):
    is_visible_before_scroll = web_browser.execute_script(JS_IS_VISIBLE_IN_VIEWPORT, ads_main_page.footer_section.find())
    ads_main_page.scroll_down()
    time.sleep(1)
    is_visible_after_scroll = web_browser.execute_script(JS_IS_VISIBLE_IN_VIEWPORT, ads_main_page.footer_section.find())
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
def test_footer_social_icons_redirect(web_browser, ads_main_page, accept_cookie, scroll_down, icon_index, expected_url):
    footer_icons = ads_main_page.footer_icons.find()    
    footer_icons[icon_index].click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert ads_main_page.get_current_url() == expected_url, f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking social icon {icon_index+1}'


def test_footer_redirect_button_go_to_office(web_browser, ads_main_page, scroll_down):
    button = ads_main_page.button_go_to_office.find()
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
def test_footer_redirect_to_selections(web_browser, ads_main_page, scroll_down, section_index, expected_url, is_new_tab):
    footer_sections = ads_main_page.footer_sections.find()    
    footer_sections[section_index].click()
    if is_new_tab:
        web_browser.switch_to.window(web_browser.window_handles[1])
    ads_main_page.wait_page_loaded()
    assert ads_main_page.get_current_url() == expected_url, f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking on section'



def test_footer_redirect_button_button(web_browser, ads_main_page, scroll_down):
    ads_main_page.button_logo.click()
    web_browser.switch_to.window(web_browser.window_handles[1]) 
    ads_main_page.wait_page_loaded()
    
    assert ads_main_page.get_current_url() == 'https://vk.company/ru/company/business/', \
        f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking the logo button'


def test_footer_about_button_redirect(web_browser, ads_main_page, scroll_down):
    ads_main_page.button_about.click()
    web_browser.switch_to.window(web_browser.window_handles[1]) 
    ads_main_page.wait_page_loaded()
    assert ads_main_page.get_current_url() == 'https://vk.company/ru/', \
        f'Incorrect URL [{ads_main_page.get_current_url()}] after clicking the about button'


def test_footer_language_selector(web_browser, ads_main_page, accept_cookie, scroll_down):
    ads_main_page.selector_lang.click()
    ads_main_page.button_english.click()
    ads_main_page.wait_page_loaded()
    assert "News" in ads_main_page.get_page_source()
