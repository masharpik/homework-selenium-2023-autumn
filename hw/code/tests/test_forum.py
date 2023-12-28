import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
import re


@pytest.mark.parametrize('search_query, has_results', [
    ("Получить", True),
    ("9", True),
    ("fsfsddf", False),
])
def test_search_forum(forum_page, search_query, has_results):
    forum_page.input_search.send_keys(search_query)
    if has_results:
        assert forum_page.idea_items.count() > 0
    else:
        assert forum_page.text_not_search_results.is_visible()
    forum_page.button_clear_search.click()
    assert forum_page.idea_items.count() > 0

@pytest.fixture(params=[(i, j) for i in range(7) for j in range(4)])
def tag_status_tag_indices(request):
    return request.param

def test_filter_combination(forum_page, tag_status_tag_indices):
    index_tag, index_status = tag_status_tag_indices

    forum_page.selector_theme_and_status[0].click()
    tag_name = forum_page.selector_of_options[index_tag].text
    forum_page.selector_of_options[index_tag].click()
        
    forum_page.selector_theme_and_status[1].click()
    status_name = forum_page.selector_of_options[index_status].text
    forum_page.selector_of_options[index_status].click()

    time.sleep(0.6)
    if forum_page.text_not_search_results.is_visible():
        return
    
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


def test_filter_close(forum_page):
    forum_page.selector_theme_and_status[0].click()
    forum_page.selector_of_options[0].click()

    forum_page.selector_theme_and_status[1].click()
    forum_page.selector_of_options[0].click()
    
    forum_page.buttons_clear_filter[0].click()
    forum_page.buttons_clear_filter[0].click()
    
    assert forum_page.selector_theme_and_status[0].get_attribute('value') == ''
    assert forum_page.selector_theme_and_status[1].get_attribute('value') == ''


def test_copy_link(forum_page):
    forum_page.buttons_copying_idea[0].click()
    assert forum_page.popup_link_copied.is_visible()


def test_like_not_access(forum_page):
    forum_page.buttons_like[0].click()
    forum_page.text_not_access_like.is_visible()

def test_count_comments_on_button(forum_page):
    buttons_add_comment = forum_page.buttons_comments_exists.find()
    for button in buttons_add_comment[:3]:
        # на кнопку число существующих комментариев
        count_comments = int(button.text)
        forum_page.scroll_to_element(button)
        button.click()
        assert forum_page.comments_items.count() == count_comments
        button.click()

@pytest.mark.skip
def test_redirect_to_idea_page(forum_page):
    count_idea = forum_page.headers_idea.count()
    for i in range(count_idea // 5):
        id_number = forum_page.id_by_idea(i)

        header = forum_page.headers_idea[i]
        forum_page.scroll_to_element(header)
        header.click()
        
        forum_page.wait_page_loaded()
        id_number_url = forum_page.id_idea_by_url(forum_page.get_current_url())

        # проверка совпадения id в idea item и в url странице идеи 
        assert id_number == id_number_url
        forum_page.go_back()


def test_suggest_idea_in_modal_window(forum_page):
    forum_page.button_suggest_idea.click()
    forum_page.button_ok_understood.click()
    forum_page.wait_page_loaded()
    assert not forum_page.button_ok_understood.is_visible()
    
    forum_page.button_suggest_idea.click()
    forum_page.button_close_modal_window.click()
    forum_page.wait_page_loaded()
    assert not forum_page.button_ok_understood.is_visible()
    
