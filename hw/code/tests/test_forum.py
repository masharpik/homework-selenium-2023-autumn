import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
import re


@pytest.mark.parametrize('search_query, has_results', [
    ("Получить", True),
    ("9", True),
    ("fsfsddf", False),
])
def test_search_forum(web_browser, forum_page, search_query, has_results):
    forum_page.input_search.send_keys(search_query)
    if has_results:
        assert forum_page.idea_items.count() > 0
    else:
        assert forum_page.text_not_search_results.is_visible()
    forum_page.button_clear_search.click()
    assert forum_page.idea_items.count() > 0


def test_filter_combination(web_browser, forum_page):
    count_tags = 7
    count_status = 4 
    # перебор всех тегов
    for index_tag in range(count_tags):
        forum_page.selector_theme_and_status[0].click()
        tag_name = forum_page.selector_of_options[index_tag].text
        forum_page.selector_of_options[index_tag].click()
        
        # перебор всех статусов
        for index_status in range(count_status):
            forum_page.selector_theme_and_status[1].click()
            status_name = forum_page.selector_of_options[index_status].text
            forum_page.selector_of_options[index_status].click()

            time.sleep(0.6)
            if forum_page.text_not_search_results.is_visible():
                continue
            
            count_found_ideas = forum_page.idea_items.count()
            many_status = forum_page.statuses_of_ideas_found.find()
            many_tags = forum_page.tags_of_ideas_found.find()

            # подсчет идей с заданным статусом и тегом
            count_found_status = 0
            count_found_tags = 0
            for statusElement in many_status:
                if statusElement.text == status_name:
                    count_found_status += 1
            for tagElement in many_tags:
                if tagElement.text == tag_name:
                    count_found_tags += 1

            assert count_found_status == count_found_ideas
            assert count_found_tags == count_found_ideas


def test_filter_close(web_browser, forum_page):
    forum_page.selector_theme_and_status[0].click()
    forum_page.selector_of_options[0].click()

    forum_page.selector_theme_and_status[1].click()
    forum_page.selector_of_options[0].click()
    
    forum_page.buttons_clear_filter[0].click()
    forum_page.buttons_clear_filter[0].click()
    
    assert forum_page.selector_theme_and_status[0].get_attribute('value') == ''
    assert forum_page.selector_theme_and_status[1].get_attribute('value') == ''


def test_copy_link(web_browser, forum_page):
    forum_page.buttons_copying_idea[0].click()
    assert forum_page.popup_link_copied.is_visible()


def test_like_not_access(web_browser, forum_page):
    forum_page.buttons_like[0].click()
    forum_page.text_not_access_like.is_visible()

def scroll_to_element(web_browser, element):
    web_browser.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(0.5)
    web_browser.execute_script('window.scrollBy(0, -70);')
    time.sleep(0.5)


def test_count_comments_on_button(web_browser, forum_page):
    buttons_add_comment = forum_page.buttons_comments_exists.find()
    for button in buttons_add_comment:
        # на кнопку число существующих комментариев
        count_comments = int(button.text)
        scroll_to_element(web_browser, button)
        button.click()
        assert forum_page.comments_items.count() == count_comments
        button.click()


def test_redirect_to_idea_page(web_browser, forum_page):
    count_idea = forum_page.headers_idea.count()
    for i in range(count_idea // 5):
        header = forum_page.headers_idea[i]
        info = forum_page.text_date_and_id_of_ideas[i].text
        match = re.search(r'id (\d+)', info)
        if match:
            id_number = match.group(1)
        else:
            assert False, "ID idea not found"

        scroll_to_element(web_browser, header)
        header.click()
        forum_page.wait_page_loaded()
        url = forum_page.get_current_url()
        
        match = re.search(r'/(\d+)$', url)
        if match:
            id_number_url = match.group(1)
        else:
            assert False, "ID url not found"
        # проверка совпадения id в idea item и в url странице идеи 
        assert id_number == id_number_url
        forum_page.go_back()


def test_suggest_idea_in_modal_window(web_browser, forum_page):
    forum_page.button_suggest_idea.click()
    forum_page.button_ok_understood.click()
    forum_page.wait_page_loaded()
    assert not forum_page.button_ok_understood.is_visible()
    
    forum_page.button_suggest_idea.click()
    forum_page.button_close_modal_window.click()
    forum_page.wait_page_loaded()
    assert not forum_page.button_ok_understood.is_visible()
    
