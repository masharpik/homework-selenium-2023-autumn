import pytest

@pytest.fixture
def enter_to_creating_audience(web_browser, commerce_center_page):
    commerce_center_page.create_catalog_button.click()
    commerce_center_page.wait_page_loaded()
    commerce_center_page.create_catalog_button.click()
    commerce_center_page.wait_page_loaded()


# def test_commerce_center_page_create_catalog_popup(web_browser, commerce_center_page):
#     commerce_center_page.create_catalog_button.click()
#     commerce_center_page.wait_page_loaded()
#     commerce_center_page.create_catalog_button.click()
#     commerce_center_page.wait_page_loaded()
#     assert commerce_center_page.create_catalog_popup.is_presented()


def test_commerce_center_create_catalog(web_browser, commerce_center_page, enter_to_creating_audience):
    commerce_center_page.marketplace_tab.click()
    commerce_center_page.wait_page_loaded()
    commerce_center_page.marketplace_url_input.send_keys("badtext")
    commerce_center_page.wait_page_loaded()
    commerce_center_page.submit_button.click()
    commerce_center_page.wait_page_loaded()
    assert 'Необходимо указать протокол http(s)' in commerce_center_page.error_message.get_text()