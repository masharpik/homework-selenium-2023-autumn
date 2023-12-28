import os
import pytest
import time
from selenium.webdriver import ActionChains
from _pytest.fixtures import FixtureRequest


def test_create_campaign(personal_area_page):
    personal_area_page.button_create_campaign.click()
    personal_area_page.wait_page_loaded()
    assert 'https://ads.vk.com/hq/new_create/ad_plan' in personal_area_page.get_current_url()

def test_create_campaign_without_budget(personal_area_page):
    personal_area_page.enter_to_creating_campaign()
    personal_area_page.input_advertised_site.send_keys("openai.com")
    personal_area_page.button_continue.click()
    assert personal_area_page.text_required_field.is_visible()


def test_create_campaign_invalid_advertised_site(personal_area_page):
    personal_area_page.enter_to_creating_campaign()
    personal_area_page.input_advertised_site.send_keys("fgsfg")
    personal_area_page.button_continue.click()
    assert personal_area_page.text_invalid_url.is_visible()

def test_create_campaign_invalid_date(web_browser, personal_area_page):
    personal_area_page.enter_to_creating_campaign()
    personal_area_page.input_start_year.click()
    ActionChains(web_browser).send_keys("1970\n").perform()
    assert not personal_area_page.input_start_year.get_text() in "1970"
    
def test_create_campaign_valid_date(web_browser, personal_area_page, enter_to_creating_campaign):
    personal_area_page.input_start_year.click()
    ActionChains(web_browser).send_keys("2024\n").perform()
    assert personal_area_page.input_start_year.get_text() in "2024"

def test_create_campaign_invalid_budget(personal_area_page):
    personal_area_page.enter_to_creating_campaign()
    personal_area_page.input_advertised_site.send_keys("openai.com")
    personal_area_page.input_budget.send_keys("50")
    personal_area_page.button_continue.click()
    assert personal_area_page.text_little_budget.is_visible()

def test_create_campaign_go_to_step_2(personal_area_page):
    personal_area_page.go_to_step_2()
    assert personal_area_page.icon_complete_step_0.is_visible()
    assert personal_area_page.icon_active_step_1.is_visible()


def test_create_campaign_change_coverage_after_choose_region(personal_area_page):
    personal_area_page.go_to_step_2()
    old_texts = personal_area_page.texts_prediction_7_day.get_text()
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    new_texts = personal_area_page.texts_prediction_7_day.get_text()
    for i, old_text in enumerate(old_texts):
        assert old_text != new_texts[i]


@pytest.mark.parametrize('search_text, is_found', [
    ('Кампания', True),
    ('sfsdfsf', False),
])
def test_search_campaigns_in_drafts(personal_area_page, search_text, is_found):
    personal_area_page.go_to_step_2()
    personal_area_page.icon_root.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_drafts.click()
    
    assert personal_area_page.draft_items.count() > 0
    
    personal_area_page.input_search.send_keys(search_text)
    personal_area_page.wait_page_loaded()
    if is_found:
        assert personal_area_page.draft_items.count() > 0
    else:
        assert personal_area_page.text_create_first_campaign.is_visible()


def test_continue_create_campaign_from_draft(personal_area_page):
    personal_area_page.go_to_step_2()
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    personal_area_page.icon_root.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_drafts.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.edit_draft(0)
    assert personal_area_page.icon_active_step_0.is_visible()


def test_create_campaign_without_media_on_step_3(personal_area_page):
    personal_area_page.go_to_step_2()
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_continue.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.inputs_ads[0].send_keys("Заголовок")
    personal_area_page.textarea_ads[0].send_keys("Описание")
    personal_area_page.button_publish.click()
    personal_area_page.wait_page_loaded()
    assert personal_area_page.text_error_non_media.is_visible()

def test_add_new_campaign(personal_area_page):
    personal_area_page.wait_page_loaded()
    count_old_campaigns = 0
    if not personal_area_page.text_create_first_campaign.is_visible():
        count_old_campaigns = personal_area_page.campaign_items.count()
    personal_area_page.create_campaign_full()
    assert personal_area_page.campaign_items.count() == count_old_campaigns + 1


def test_delete_all_campaigns(personal_area_page):
    personal_area_page.create_campaign_full()
    count_checkbox = personal_area_page.checkbox_action_campaign.count()
    personal_area_page.checkbox_action_campaign[count_checkbox - 1].click()
    personal_area_page.selector_actions.click()
    personal_area_page.action_delete_into_selector.click()
    personal_area_page.wait_page_loaded()
    assert personal_area_page.text_create_first_campaign.is_visible()
