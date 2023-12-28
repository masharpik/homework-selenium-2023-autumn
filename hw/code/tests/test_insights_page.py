def test_insights_page_click_more_button(web_browser, insights_page):
    current_url = insights_page.get_current_url()
    insights_page.more_button.locate_element_in_center()
    assert insights_page.more_button.is_presented()
    # insights_page.more_button.click()
    web_browser.execute_script("arguments[0].click();", insights_page.more_button.find())
    insights_page.wait_page_loaded()

    assert current_url != insights_page.get_current_url()


def test_insights_page_click_on_material(web_browser, insights_page):
    current_url = insights_page.get_current_url()
    insights_page.first_material.locate_element_in_center()
    assert insights_page.first_material.is_presented()

    web_browser.execute_script("arguments[0].click();", insights_page.first_material.find())
    insights_page.wait_page_loaded()

    assert current_url != insights_page.get_current_url()
