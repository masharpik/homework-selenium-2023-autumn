import time

import pytest

from pages.partner_page import PartnerPage


@pytest.mark.parametrize('element_name, expected_url, opens_in_new_tab', [
    ('spravka_button', 'https://ads.vk.com/help/categories/partner', True),
    ('my_cabinet', 'https://id.vk.com', True),
])
def test_partner_sections(web_browser, partner_page, element_name, expected_url, opens_in_new_tab):
    # Сохраняем идентификатор текущего окна
    original_window = web_browser.current_window_handle

    element = getattr(partner_page, element_name)
    # import pdb; pdb.set_trace()
    element.click()
    element._page.wait_page_loaded()
    # import pdb; pdb.set_trace()

    # Переключаемся на новую вкладку
    if opens_in_new_tab:
        for window_handle in web_browser.window_handles:
            if window_handle != original_window:
                web_browser.switch_to.window(window_handle)
                break

    # Проверяем URL новой вкладки
    assert expected_url in web_browser.current_url


@pytest.mark.parametrize('element_name, expected_text, for_element', [
    ('instream', 'Instream', 'for_sites'),
    ('banner', 'Баннер', 'for_sites'),
    ('adaptive_block', 'Адаптивный блок', 'for_sites'),
    ('inpage', 'InPage', 'for_sites'),
    ('fullscreen_block', 'Полноэкранный блок', 'for_sites'),
    ('sticky_banner', 'Sticky-баннер', 'for_sites'),
    ('banner_apps', 'Баннер', 'for_apps'),
    ('native_format', 'Нативный формат', 'for_apps'),
    ('fullscreen_block_apps', 'Полноэкранный блок', 'for_apps'),
    ('video_reward', 'Видео за вознаграждение', 'for_apps')
])
def test_text_in_elements(web_browser, partner_page, element_name, expected_text, for_element):
    click_element = getattr(partner_page, for_element)

    classes = click_element.find().get_attribute('class')
    if partner_page.cookie.is_presented():
        partner_page.cookie.click()

    if 'Tabs_tabActive__jugMQ' not in classes:
        # actions = ActionChains(web_browser)
        if click_element.is_clickable(timeout=1):
            # import pdb;
            # pdb.set_trace()
            # try:
            # actions.move_to_element(click_element.find().click()).perform()
            web_browser.execute_script("arguments[0].click();", click_element.find())

            click_element._page.wait_page_loaded()
            # except:
            #     web_browser.save_screenshot("debug_screenshot.png")

    # Получаем элемент
    element = getattr(partner_page, element_name)
    # import pdb;
    # pdb.set_trace()
    # Проверяем, что текст элемента соответствует ожидаемому
    assert expected_text in element.get_text()


def test_button_clickable_after_form_filling(web_browser, partner_page):
    if partner_page.cookie.is_presented():
        partner_page.cookie.click()

    partner_page.name_field.find().send_keys('MyName')
    partner_page.email_field.find().send_keys('example@example.org')
    # import pdb;
    # pdb.set_trace()
    assert partner_page.submit_button.find().is_enabled()


def test_message_after_form_submit(web_browser, partner_page):
    if partner_page.cookie.is_presented():
        partner_page.cookie.click()

    partner_page.name_field.find().send_keys('MyName')
    partner_page.email_field.find().send_keys('example@example.org')
    # import pdb;
    # pdb.set_trace()
    web_browser.execute_script("arguments[0].click();", partner_page.submit_button.find())
    assert 'Спасибо, ваша заявка принята' in partner_page.thanks_message.get_text()
