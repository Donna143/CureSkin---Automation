# import allure
# from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options

from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver

# from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = ''
bs_key = ''

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome(executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/chromedriver.exe')
    # context.driver = webdriver.Firefox(executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/geckodriver.exe')
    # context.driver = webdriver.Firefox(executable_path='/Users/svetlanalevinsohn/JobEasy/11-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Safari()

    # # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/chromedriver.exe'
    # )

    # options = webdriver.FirefoxOptions()
    # options.headless = True
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/geckodriver.exe'
    # )

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(
    #         executable_path='C:/Users/thebe/Documents/Careerist/Automation/python-selenium-automation/chromedriver.exe'
    #     ),
    #     MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # for browerstack web ###
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'os_version': '11',
    #     'os': 'Mac',
    #     'name': test_name,
    #     'projectName': 'CureSkin',
    #     'sessionName': 'Search'
    # }
    # bs_user = 'thebestlifeever_OH80xE'
    # bs_key = 'zvfa6sUsD8KeXkFhnsC4'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # for browerstack mobile ###
    desired_cap = {
        'bstack:options': {
            "osVersion": "10.0",
            "deviceName": "Samsung Galaxy S20",
            "projectName": "CureSkin - Automation",
            "buildName": "Mobile",
            "sessionName": "iPhone 14",
            "local": "false",
        },
    }

    bs_user = 'thebestlifeever_OH80xE'
    bs_key = 'zvfa6sUsD8KeXkFhnsC4'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # Mobile Emulation
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(chrome_options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
