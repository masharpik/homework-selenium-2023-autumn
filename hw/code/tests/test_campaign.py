import os
import pytest
import time
from selenium.webdriver import ActionChains
from _pytest.fixtures import FixtureRequest


def test_create_campaign(web_browser, personal_area_page):
    personal_area_page.button_create_campaign.click()
    personal_area_page.wait_page_loaded()
    assert 'https://ads.vk.com/hq/new_create/ad_plan' in personal_area_page.get_current_url()

@pytest.fixture
def enter_to_creating_campaign(personal_area_page):
    personal_area_page.button_create_campaign.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_site.click()
    personal_area_page.wait_page_loaded()


def test_create_campaign_without_budget(web_browser, personal_area_page, enter_to_creating_campaign):
    personal_area_page.input_advertised_site.send_keys("openai.com")
    personal_area_page.button_continue.click()
    assert personal_area_page.text_required_field.is_visible()


def test_create_campaign_invalid_advertised_site(web_browser, personal_area_page, enter_to_creating_campaign):
    personal_area_page.input_advertised_site.send_keys("fgsfg")
    personal_area_page.button_continue.click()
    assert personal_area_page.text_invalid_url.is_visible()


def test_create_campaign_invalid_date(web_browser, personal_area_page, enter_to_creating_campaign):
    personal_area_page.input_start_year.click()
    ActionChains(web_browser).send_keys("2024\n").perform()
    assert personal_area_page.input_start_year.get_text() in "2024"
    personal_area_page.input_start_year.click()
    ActionChains(web_browser).send_keys("1970\n").perform()
    assert not personal_area_page.input_start_year.get_text() in "1970"
    assert personal_area_page.input_start_year.get_text() in "2024"
    

def test_create_campaign_invalid_budget(web_browser, personal_area_page, enter_to_creating_campaign):
    personal_area_page.input_advertised_site.send_keys("openai.com")
    personal_area_page.input_budget.send_keys("50")
    personal_area_page.button_continue.click()
    assert personal_area_page.text_little_budget.is_visible()

@pytest.fixture
def go_to_step_2(personal_area_page, enter_to_creating_campaign):
    personal_area_page.input_advertised_site.send_keys("openai.com")
    personal_area_page.input_budget.send_keys("333")
    personal_area_page.button_continue.click()
    personal_area_page.wait_page_loaded()


def test_create_campaign_go_to_step_2(web_browser, personal_area_page, go_to_step_2):
    assert personal_area_page.icon_complete_step_0.is_visible()
    assert personal_area_page.icon_active_step_1.is_visible()


def test_create_campaign_change_coverage_after_choose_region(web_browser, personal_area_page, go_to_step_2):
    old_texts = personal_area_page.texts_prediction_7_day.get_text()
    # personal_area_page.button_display_regions.click()
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    new_texts = personal_area_page.texts_prediction_7_day.get_text()
    for i, old_text in enumerate(old_texts):
        assert old_text != new_texts[i]


def test_search_campaigns_in_drafts(web_browser, personal_area_page, go_to_step_2):
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    personal_area_page.icon_root.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_drafts.click()
    
    assert personal_area_page.draft_items.count() > 0
    
    personal_area_page.input_search.send_keys("Кампания")
    personal_area_page.wait_page_loaded()
    assert personal_area_page.draft_items.count() > 0

    personal_area_page.input_search.send_keys("sfsdfsf")
    personal_area_page.wait_page_loaded()
    assert personal_area_page.text_create_first_campaigh.is_visible()


def test_continue_create_campaign_from_draft(web_browser, personal_area_page, go_to_step_2):
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    personal_area_page.icon_root.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_drafts.click()
    personal_area_page.wait_page_loaded()
    ActionChains(web_browser).move_to_element(personal_area_page.campaigns_draft[0]).perform()
    personal_area_page.campaigns_draft_edit[0].click()
    personal_area_page.wait_page_loaded()
    assert personal_area_page.icon_active_step_0.is_visible()


def test_create_campaign_without_media_on_step_3(web_browser, personal_area_page, go_to_step_2):
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_continue.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.inputs_ads[0].send_keys("Заголовок")
    personal_area_page.textarea_ads[0].send_keys("Описание")
    personal_area_page.button_publish.click()
    personal_area_page.wait_page_loaded()
    assert personal_area_page.text_error_non_media.is_visible()

@pytest.fixture
def create_campaign_full(personal_area_page, go_to_step_2):
    personal_area_page.buttons_regions[0].click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_continue.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.inputs_ads[0].send_keys("Заголовок")
    personal_area_page.textarea_ads[0].send_keys("Описание")
    personal_area_page.choose_from_media_lib.click()
    personal_area_page.button_photobank.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.photos_photobabk[0].click()
    personal_area_page.button_add.click()
    personal_area_page.wait_page_loaded()
    personal_area_page.button_publish.click()
    personal_area_page.wait_page_loaded()


def test_add_new_campaign(web_browser, personal_area_page, request: FixtureRequest):
    personal_area_page.wait_page_loaded()
    count_old_campaigns = 0
    if not personal_area_page.text_create_first_campaign.is_visible():
        count_old_campaigns = personal_area_page.campaign_items.count()
    request.getfixturevalue('create_campaign_full')
    assert personal_area_page.campaign_items.count() == count_old_campaigns + 1


def test_delete_all_campaigns(web_browser, personal_area_page, create_campaign_full):
    count_checkbox = personal_area_page.checkbox_action_campaign.count()
    personal_area_page.checkbox_action_campaign[count_checkbox - 1].click()
    personal_area_page.selector_actions.click()
    personal_area_page.action_delete_into_selector.click()
    personal_area_page.wait_page_loaded()
    assert personal_area_page.text_create_first_campaign.is_visible()
