from .base import WebPage
from .elements import WebElement
from .elements import ManyWebElements


class AudiencePage(WebPage):
    audience_tab = WebElement(xpath='//*[@id="tab_audience"]/span[1]')
    user_list_tab = WebElement(xpath='//*[@id="tab_audience.users_list"]/span[1]')
    tab_widget = WebElement(xpath='//*[@id="tab_audience.users_list"]')

    create_audience_button = WebElement(xpath='//*[@id="audience"]/div/div[2]/div/div[2]/div/div/div[2]/button')
    create_audience_form = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[1]/h2')
    create_audience_name_input = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/div/section[1]/div/div/span/input')
    audience_name_input_len = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/div/section[1]/div/div/h5/div/div[2]')
    include_filtered_users_by_title = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/div/section[2]/div/div/h4')
    include_filtered_users_checkbox = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/div/section[2]/div/div/h4/div')
    all_filters_checkbox = WebElement(xpath='/html/body/div[2]/div/div/div[1]/div/div/span')
    at_least_one_filter_checkbox = WebElement(xpath='/html/body/div[2]/div/div/div[2]/div[1]/div/span')
    not_a_single_filter_checkbox = WebElement(xpath='/html/body/div[2]/div/div/div[3]/div/div/span')
    save_button = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[2]/div/button[1]')
    cancel_button = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[2]/div/button[2]')
    add_source_button = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div[1]/div/section[2]/div/div/button')

    add_existing_audience = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[1]/div[1]/div/span')
    add_users_list = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[2]/div[1]/div/span')
    add_by_mobile_app_events = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[3]/div[1]/div/span')
    add_by_keywords = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[4]/div[1]/div/span')
    add_by_events_on_site = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[5]/div[1]/div/span')
    add_group_subscribers = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[6]/div[1]/div/span')
    add_by_add_campaigns = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[7]/div[1]/div/span')
    add_by_lid_form_events = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[8]/div[1]/div/span')
    add_by_musician = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/section/div[1]/div[9]/div[1]/div/span')

    add_source_cancel_button = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/button[2]')
    add_source_x_button = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div/button')
    add_source_modal_form = WebElement(xpath='//*[@id="root"]/div/div[2]/div[2]/div')

    three_dot_button = WebElement(xpath='//*[@id="audience"]/div/div[2]/div/div[1]/div/div/div/button')

    activate_external_audience_button_title = WebElement(xpath='//*[@id="root"]/div/div[1]/div[4]/div/div[1]/div/div[1]/div/span/h5')
    move_audience_from_vk_cabinet_button_title = WebElement(xpath='//*[@id="root"]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/span/h5')

    uses_list_tab_button = WebElement(xpath='//*[@id="tab_audience.users_list"]')
    load_list_button_blue = WebElement(xpath='//*[@id="audience.users_list"]/div/div[2]/div/div[1]/div[1]/div[1]/button')
    load_list_button_grey = WebElement(xpath='//*[@id="audience.users_list"]/div/div[2]/div/div[2]/div/div/div[2]')
    user_list_tab_three_dot_button = WebElement(xpath='//*[@id="audience.users_list"]/div/div[2]/div/div[1]/div[1]/div[1]/div/button')
    share_list_button = WebElement(xpath='//*[@id="audience.users_list"]/div/div[2]/div/div[1]/div[1]/div[2]/button')
    users_list_search_input = WebElement(xpath='//*[@id="audience.users_list"]/div/div[2]/div/div[1]/div[2]/div/label/input')

    new_users_list_input = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div[1]/section/div[1]/form/div/div[1]/div/div/span/input')
    users_list_input_len = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div[1]/section/div[1]/form/div/div[1]/div/div/div')
    as_filename_checkbox = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div[1]/section/div[1]/form/div/div[1]/div/label/div[4]/div')

    list_type_label = WebElement(xpath='//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div[1]/section/div[1]/form/div/div[2]/label')

    def get_tab_index(self):
        self.tab_widget._web_driver = self._web_driver
        return self.tab_widget.find().get_attribute('tabindex')

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/hq/audience'
        super().__init__(web_driver, url)
