import time

import pytest

from pages.partner_page import PartnerPage


@pytest.mark.parametrize('element_name', [
    ('second_radio_button'),
])
def test_partner_sections(web_browser, start_page, element_name):
    start_page.cookie.click()

    first_text = start_page.h1_text.get_text()
    element = getattr(start_page, element_name)

    element.click()
    element._page.wait_page_loaded()

    assert first_text != start_page.h1_text.get_text()
