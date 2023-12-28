import pytest
import time

@pytest.mark.parametrize('section_index, expected_url', [
    (0, '/help/categories/authorization'),
    (1, '/help/categories/general'),
    (2, '/help/categories/features'),
    (3, '/help/categories/statistics'),
    (4, '/help/categories/documents'),
    (5, '/help/categories/mini_ads'),
    (6, '/help/categories/faq'),
    (7, '/help/categories/partner'),
])
def test_ref_sections(web_browser, ref_page, section_index, expected_url):
    web_browser.execute_script(f'window.scrollTo(0, {(section_index // 3) * 600});')
    time.sleep(0.5)
    ref_page.sections[section_index].click()
    ref_page.wait_page_loaded()
    assert expected_url in ref_page.get_current_url(), f'Incorrect URL [{ref_page.get_current_url()}] after clicking social icon {section_index+1}'

@pytest.mark.parametrize('search_query, has_results', [
    ("api", True),
    ("статистика", True),
    ("дыоапдырапаыврп", False)
])
def test_search_suggestions(ref_page, search_query, has_results):
    ref_page.input_search.send_keys(search_query)
    if has_results:
        assert ref_page.suggections.count() > 0
    else:
        assert ref_page.suggections.count() == 0
    ref_page.button_clear.click()
    assert ref_page.input_search.find().get_attribute('value') == '', 'Search input is not cleared after pressing the clear button'

def test_search_suggestions_click(ref_page):
    ref_page.input_search.send_keys("api")
    ref_page.suggections[4].click()
    ref_page.wait_page_loaded()
    assert "https://ads.vk.com/help/articles/partners_reporting_api" in ref_page.get_current_url()


def test_search_press_enter(ref_page):
    ref_page.input_search.send_keys("api\n")
    assert "https://ads.vk.com/help/search?search=api" in ref_page.get_current_url()


def test_selector(ref_page):
    ref_page.sections[0].click()
    ref_page.wait_page_loaded()
    ref_page.selector_sections[1].click()
    ref_page.wait_page_loaded()
    ref_page.section_utm_marks[1].click()
    ref_page.wait_page_loaded()
    assert "https://ads.vk.com/help/articles/utm" in ref_page.get_current_url()


def test_ref_click_button_ref(article_ref_page):
    article_ref_page.button_ref[0].click()
    article_ref_page.wait_page_loaded()
    assert "https://ads.vk.com/help" in article_ref_page.get_current_url()

def test_ref_click_button_back_to_adds(article_ref_page):
    article_ref_page.button_back_to_adds.click()
    article_ref_page.wait_page_loaded()
    assert "https://ads.vk.com/help/categories/features" in article_ref_page.get_current_url()

@pytest.mark.parametrize('hyperlink_index', [
    (0),
    (1),
])
def test_ref_click_hyperlinks_header(article_ref_page, hyperlink_index):
    article_ref_page.hyperlinks_header[hyperlink_index].click()
    article_ref_page.wait_page_loaded()
    assert "https://ads.vk.com/help" in article_ref_page.get_current_url()

    
