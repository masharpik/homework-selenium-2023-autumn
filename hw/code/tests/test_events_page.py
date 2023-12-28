def test_click_on_event(web_browser, events_page):
    current_url = events_page.get_current_url()
    events_page.events_preview.locate_element_in_center()
    assert events_page.events_preview.is_presented()
    # insights_page.more_button.click()
    web_browser.execute_script("arguments[0].click();", events_page.events_preview.find())
    events_page.wait_page_loaded()

    assert current_url != events_page.get_current_url()
