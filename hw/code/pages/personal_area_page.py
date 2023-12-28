#!/usr/bin/python3
# -*- encoding=utf8 -*-

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from selenium.webdriver import ActionChains

class PersonalAreaPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ads.vk.com/hq'
        super().__init__(web_driver, url)
    
    # personal area
    button_create_campaign = WebElement(xpath='//a[@data-testid="create-button"]')
    
    # create campaign
    button_site = WebElement(xpath='//div[@data-id="site_conversions"]')

    # step 1
    input_advertised_site = WebElement(xpath='//div[@data-name="object"]//input')
    input_budget = WebElement(xpath='//input[@data-testid="targeting-not-set"]')
    input_start_year = WebElement(xpath='//span[@data-testid="start-date"]//span[@aria-label="Изменить год"]')
    
    text_invalid_url = WebElement(xpath='//div[text()="Неверный формат URL"]')
    text_required_field = WebElement(xpath='//div[text()="Обязательное поле"]')
    text_little_budget = WebElement(xpath='//div[text()="Бюджет кампании должен быть не меньше 100₽"]')

    # general
    button_continue = WebElement(xpath='//span[@class="vkuiButton__content" and text()="Продолжить"]')
    icon_root = WebElement(xpath='//button[@data-route="root"]')
    text_create_first_campaign = WebElement(xpath='//span[text()="Создайте первую рекламную кампанию"]')
    input_search = WebElement(xpath='//input[@type="search"]')
    campaign_items = ManyWebElements(xpath='//div[@class="BaseTable__table BaseTable__table-main"]//div[@class="BaseTable__row BaseTable__row--customized"]')

    # progress creating campaign
    icon_active_step_0 = WebElement(xpath='//div[@data-step-id="0" and @class="Steps_step__48miE Steps_step_active__01Yfd"]')
    icon_complete_step_0 = WebElement(xpath='//div[@data-step-id="0" and @class="Steps_step__48miE Steps_step_completed__hkHzb"]')
    icon_active_step_1 = WebElement(xpath='//div[@data-step-id="1" and @class="Steps_step__48miE Steps_step_active__01Yfd"]')

    # step 2
    button_display_regions = WebElement(xpath='//h3[text()="Регионы показа"]')
    buttons_regions = ManyWebElements(xpath='//div[@class="RegionsQuickSelection_wrapper__7kX9f"]//button')
    texts_prediction_7_day = ManyWebElements(xpath='//div[@class="PredictionItem_PredictionItem__value__Sd8dg"]')

    # draft
    button_drafts = WebElement(xpath='//button[@data-testid="drafts-button"]')
    draft_items = ManyWebElements(xpath='//div[@class="BaseTable__table BaseTable__table-main"]//div[contains(@data-entityid,"AdPlanDraft") and @role="row"]')
    campaigns_draft = ManyWebElements(xpath='//div[@class="nameCellContent_content__TyfEC"]')
    campaigns_draft_edit = ManyWebElements(xpath='//span[@class="vkuiCaption vkuiCaption--level-1 vkuiCaption--weight-3"]')

    # step 3
    inputs_ads = ManyWebElements(xpath='//input[@data-testid="text-field"]')
    textarea_ads = ManyWebElements(xpath='//textarea[@data-testid="text-field"]')
    text_error_non_media = WebElement(xpath='//div[text()="Для выбранных мест размещений не хватает медиафайлов"]')
    media_uploader = WebElement(xpath='//div[@class="MediaFileSelector_wrapper__yG-SE UnionMediaContentGroup_selector__RN2Ea LocalFileSelector_container__W4cfb"]')
    button_publish = WebElement(xpath='//span[text()="Опубликовать"]')
    checkbox_action_campaign = ManyWebElements(xpath='//div[@class="vkuiCheckbox__icon vkuiCheckbox__icon--off"]')
    selector_actions = WebElement(xpath='//span[@data-testid="select-options"]')
    action_delete_into_selector = WebElement(xpath='//*[contains(text(), "Удалить")]')

    # step 3 - select picture
    choose_from_media_lib = WebElement(xpath='//div[@data-testid="set-global-image"]')
    button_photobank = WebElement(xpath='//div[@data-id="photobank"]')
    photos_photobabk = ManyWebElements(xpath='//div[@class="ImageItems_imageItem__jdlt3 ImageItems_active__wH2sS"]')
    button_add = WebElement(xpath='//span[@class="vkuiButton__content" and contains(text(),"Добавить")]')

    def enter_to_creating_campaign(self):
        self.button_create_campaign.click()
        self.wait_page_loaded()
        self.button_site.click()
        self.wait_page_loaded()

    def go_to_step_2(self):
        self.enter_to_creating_campaign()
        self.input_advertised_site.send_keys("openai.com")
        self.input_budget.send_keys("333")
        self.button_continue.click()
        self.wait_page_loaded()

    def create_campaign_full(self):
        self.go_to_step_2()
        self.buttons_regions[0].click()
        self.wait_page_loaded()
        self.button_continue.click()
        self.wait_page_loaded()
        self.inputs_ads[0].send_keys("Заголовок")
        self.textarea_ads[0].send_keys("Описание")
        self.choose_from_media_lib.click()
        self.button_photobank.click()
        self.wait_page_loaded()
        self.photos_photobabk[0].click()
        self.button_add.click()
        self.wait_page_loaded()
        self.button_publish.click()
        self.wait_page_loaded()
    
    def edit_draft(self, index_draft):
        ActionChains(self._web_driver).move_to_element(self.campaigns_draft[index_draft]).perform()
        self.campaigns_draft_edit[index_draft].click()
        self.wait_page_loaded()
