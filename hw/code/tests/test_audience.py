import pytest


@pytest.fixture
def enter_to_creating_audience(audience_page):
    audience_page.create_audience_button.click()
    audience_page.wait_page_loaded()


@pytest.fixture
def enter_to_choosing_audience_checkbox(audience_page, enter_to_creating_audience):
    audience_page.include_filtered_users_checkbox.click()
    audience_page.wait_page_loaded()


@pytest.fixture
def enter_to_adding_source(audience_page, enter_to_creating_audience):
    audience_page.add_source_button.click()
    audience_page.wait_page_loaded()


@pytest.fixture
def click_to_three_dot_button(audience_page):
    audience_page.three_dot_button.click()


@pytest.fixture
def enter_users_list_tab(audience_page):
    audience_page.wait_page_loaded()
    audience_page.uses_list_tab_button.click()


@pytest.fixture
def open_load_users_list_modal(audience_page, enter_users_list_tab):
    audience_page.wait_page_loaded()
    audience_page.load_list_button_blue.click()


def test_audience(web_browser, audience_page):
    assert audience_page.get_tab_index() == '-1'
    assert audience_page.audience_tab.get_text() == 'Аудитории'
    assert audience_page.user_list_tab.get_text() == 'Списки пользователей'


def test_audience_show_form_on_button_click(audience_page, enter_to_creating_audience):

    assert audience_page.create_audience_form.is_presented()


def test_audience_form_input(audience_page, enter_to_creating_audience):
    # import pdb;
    # pdb.set_trace()
    assert audience_page.create_audience_name_input.is_presented()
    assert 'Аудитория' in audience_page.create_audience_name_input.get_attribute('value')
    tokens = audience_page.audience_name_input_len.get_text().split('/')
    assert len(tokens) == 2
    assert tokens[1].removeprefix(' ') == '255'


def test_audience_subtitle(audience_page, enter_to_creating_audience):
    # import pdb;
    # pdb.set_trace()
    assert audience_page.include_filtered_users_by_title.is_presented()
    assert 'Включить пользователей, которые соответствуют' in audience_page.include_filtered_users_by_title.get_text()


def test_audience_checkbox(audience_page, enter_to_choosing_audience_checkbox):
    assert audience_page.all_filters_checkbox.is_presented()
    assert audience_page.at_least_one_filter_checkbox.is_presented()
    assert audience_page.not_a_single_filter_checkbox.is_presented()
    assert 'всем условиям' in audience_page.all_filters_checkbox.get_text()
    assert 'хотя бы одному из условий' in audience_page.at_least_one_filter_checkbox.get_text()
    assert 'ни одному из условий' in audience_page.not_a_single_filter_checkbox.get_text()


def test_audience_buttons(audience_page, enter_to_creating_audience):
    assert audience_page.save_button.is_presented()
    assert audience_page.cancel_button.is_presented()
    assert audience_page.add_source_button.is_presented()
    assert 'Сохранить' in audience_page.save_button.get_text()
    assert 'Отмена' in audience_page.cancel_button.get_text()
    assert 'Добавить источник' in audience_page.add_source_button.get_text()


def test_audience_add_source_list(audience_page, enter_to_adding_source):
    # import pdb;
    # pdb.set_trace()
    assert audience_page.add_existing_audience.is_presented()
    assert audience_page.add_users_list.is_presented()
    assert audience_page.add_by_mobile_app_events.is_presented()
    assert audience_page.add_by_keywords.is_presented()
    assert audience_page.add_by_events_on_site.is_presented()
    assert audience_page.add_group_subscribers.is_presented()
    assert audience_page.add_by_add_campaigns.is_presented()
    assert audience_page.add_by_lid_form_events.is_presented()
    assert audience_page.add_by_musician.is_presented()


@pytest.mark.parametrize('element_name', [
    ('add_source_cancel_button'),
    ('add_source_x_button'),
])
def test_audience_closing_add_source_list_form(web_browser, audience_page, enter_to_adding_source, element_name):
    element = getattr(audience_page, element_name)
    # import pdb; pdb.set_trace()
    assert audience_page.add_source_modal_form.is_presented()
    # element.click()
    web_browser.execute_script("arguments[0].click();", element.find())
    # # import pdb; pdb.set_trace()
    audience_page.wait_page_loaded()
    assert not audience_page.add_source_modal_form.is_presented()


def test_audience_three_dot_button_choises(audience_page, click_to_three_dot_button):
    assert audience_page.activate_external_audience_button_title.is_presented()
    assert audience_page.move_audience_from_vk_cabinet_button_title.is_presented()
    assert 'Активировать внешнюю аудиторию' in audience_page.activate_external_audience_button_title.get_text()
    assert 'Перенести аудитории из кабинета ВКонтакте' in audience_page.move_audience_from_vk_cabinet_button_title.get_text()


def test_users_list_tab(audience_page, enter_users_list_tab):
    # pass
    # import pdb; pdb.set_trace()
    audience_page.wait_page_loaded()
    assert audience_page.load_list_button_blue.is_presented(), 'load_list_button_blue is not presented'
    assert audience_page.load_list_button_grey.is_presented(), 'load_list_button_grey is not presented'
    assert audience_page.user_list_tab_three_dot_button.is_presented(), 'user_list_tab_three_dot_button is not presented'
    assert audience_page.share_list_button.is_presented(), 'share_list_button is not presented'
    assert audience_page.users_list_search_input.is_presented(), 'users_list_search_input is not presented'



def test_load_users_list_modal_form(audience_page, open_load_users_list_modal):
    assert audience_page.new_users_list_input.is_presented()
    assert 'Новый список пользователей' in audience_page.new_users_list_input.get_attribute('value')
    audience_page.wait_page_loaded()
    tokens = audience_page.users_list_input_len.get_text().split('/')
    # import pdb;pdb.set_trace()

    assert len(tokens) == 2
    assert tokens[1].removeprefix(' ') == '255'
    assert audience_page.as_filename_checkbox.is_presented()
    assert 'Как имя файла' in audience_page.as_filename_checkbox.get_text()
    assert audience_page.list_type_label.is_presented()