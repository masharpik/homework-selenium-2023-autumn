
def test_cases_page_has_title(cases_page):
    assert cases_page.get_title() in 'Кейсы по таргетированной рекламе — VK Реклама'


def test_cases_page_has_header(cases_page):
    assert cases_page.header.get_text() in 'Кейсы'


def test_cases_page_has_subtitle(cases_page):
    assert cases_page.subtitle.get_text() in 'Как инструменты VK Рекламы помогают разным компаниям продвигать свой бизнес'


def test_cases_page_preview_widget(cases_page):
    assert cases_page.case_preview_date.is_presented()
    assert cases_page.case_preview_image.is_presented()
    assert cases_page.case_preview_title.is_presented()
    assert cases_page.case_preview_subtitle.is_presented()
    assert cases_page.case_preview_description.is_presented()
    assert cases_page.case_preview_more_button.is_presented()
