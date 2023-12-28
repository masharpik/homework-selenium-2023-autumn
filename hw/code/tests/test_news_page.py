
def test_news_page_has_title(news_page):
    assert news_page.get_title() in 'Новости VK Рекламы — все обновления рекламной платформы'


def test_news_page_has_header(news_page):
    assert news_page.header.get_text() in 'Новости'


def test_news_page_has_subtitle(news_page):
    assert news_page.subtitle.get_text() in 'Обновления платформы, которые сделают вашу рекламу еще эффективнее'


def test_news_preview_widget(news_page):
    assert news_page.preview_date.is_presented()
    assert news_page.preview_image.is_presented()
    assert news_page.preview_title.is_presented()
