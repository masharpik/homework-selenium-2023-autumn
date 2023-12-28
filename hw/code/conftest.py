#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is example shows how we can manage failed tests
# and make screenshots after any failed test case.

import pytest
import allure
import uuid

from pages.audience_page import AudiencePage
from pages.ads_main_page import AdsMainPage
from pages.reference_page import RefPage
from pages.forum_page import ForumPage
from pages.personal_area_page import PersonalAreaPage
from pages.partner_page import PartnerPage
from pages.start_page import StartPage
from pages.partner_help_page import PartnerHelpPage
from pages.news_page import NewsPage
from pages.cases_page import CasesPage
from pages.insights_page import InsightsPage
from pages.events_page import EventsPage
from pages.commerce_center_page import CommerceCenterPage
from pages.article_reference_page import ArticleRefPage
from _pytest.fixtures import FixtureRequest

COOKIES_AND_LOCAL_STORAGE_FROM_FILE = True


@pytest.fixture
def ads_main_page(web_browser):
    return AdsMainPage(web_browser)


@pytest.fixture
def ref_page(web_browser):
    return RefPage(web_browser)


@pytest.fixture
def article_ref_page(web_browser):
    return ArticleRefPage(web_browser)


@pytest.fixture
def forum_page(web_browser):
    return ForumPage(web_browser)


@pytest.fixture
def personal_area_page(web_browser, require_login):
    return PersonalAreaPage(web_browser)


@pytest.fixture
def audience_page(web_browser, require_login):
    return AudiencePage(web_browser)


@pytest.fixture
def commerce_center_page(web_browser, require_login):
    return CommerceCenterPage(web_browser)



@pytest.fixture
def partner_page(web_browser):
    return PartnerPage(web_browser)

@pytest.fixture
def start_page(web_browser):
    return StartPage(web_browser)


@pytest.fixture
def partner_help_page(web_browser):
    return PartnerHelpPage(web_browser)


@pytest.fixture
def news_page(web_browser):
    return NewsPage(web_browser)


@pytest.fixture
def insights_page(web_browser):
    return InsightsPage(web_browser)


@pytest.fixture
def events_page(web_browser):
    return EventsPage(web_browser)



@pytest.fixture
def cases_page(web_browser):
    return CasesPage(web_browser)


def credentials_from_file():
    cred = {}
    with open('.env', 'r') as file:
        for line in file:
            key, value = line.split('=', 1)
            if 'json' in key:
                cred[key] = eval(value)
            else:
                cred[key] = value

    # import pdb;
    # pdb.set_trace()
    return cred


@pytest.fixture(scope="session")
def login(request: FixtureRequest):
    web_browser = request.getfixturevalue('web_browser')
    mainPage = AdsMainPage(web_browser)
    mainPage.button_go_to_office.click()
    cred = credentials_from_file()
    mainPage.wait_page_loaded()
    mainPage.input_login.send_keys(cred['phone_number'])
    mainPage.button_submit.click()
    mainPage.wait_page_loaded()
    mainPage.input_password.send_keys(cred['password'])
    mainPage.button_submit.click()

    # capcha...
    # import pdb; pdb.set_trace()

    mainPage.wait_page_loaded()
    cookies = web_browser.get_cookies()

    local_storage = web_browser.execute_script("return Object.entries(localStorage);")
    local_storage_dict = dict(local_storage)

    web_browser.quit()

    return [cookies, local_storage_dict]


@pytest.fixture(scope='function')
def require_login(request: FixtureRequest):
    if COOKIES_AND_LOCAL_STORAGE_FROM_FILE:
        cred = credentials_from_file()
        cookies = cred['json_cookie']
        local_storage = cred['json_local_storage']
    else:
        cookies_and_local_storage = request.getfixturevalue('login')
        cookies = cookies_and_local_storage[0]
        local_storage = cookies_and_local_storage[1]

    web_browser = request.getfixturevalue('web_browser')
    mainPage = AdsMainPage(web_browser)
    mainPage.wait_page_loaded()
    for key, value in local_storage.items():
        web_browser.execute_script(f"localStorage.setItem('{key}', '{value}');")

    for cookie in cookies['cookie']:
        web_browser.add_cookie(cookie)

    web_browser.refresh()


# ---------------- system ---------------- 

@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):
    browser = selenium
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Attach screenshot to Allure report:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # For happy debugging:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass  # just ignore any errors here


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
