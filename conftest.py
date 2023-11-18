import os
import datetime

import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

""" Information about tests results """


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome",
        help="Browsers: chrome, firefox, opera or yandex"
    )
    parser.addoption(
        "--chrome_driver_path",
        default="C:\Drivers\chromedriver_win32\chromedriver.exe",
        help="Path to chrome driver"
    )
    parser.addoption(
        "--yandex_driver_path",
        default="C:\Drivers\yandexdriver\yandexdriver.exe",
        help="Path to yandex driver"
    )
    parser.addoption(
        "--opera_driver_path",
        default="C:\Drivers\operadriver\operadriver.exe",
        help="Path to opera driver"
    )
    parser.addoption(
        "--opera_browser_path",
        default="C:\Opera\opera.exe",
        help="Path to opera driver"
    )
    parser.addoption(
        "--max", action="store_true",
        help="Maximize browser window"
    )
    parser.addoption(
        "--headless", action="store_true",
        help="Headless mode without displaying the web page on a screen"
    )
    parser.addoption(
        "--url", help="Base application url"
    )
    parser.addoption(
        "--log_level",
        default="DEBUG",
        help="Logging level: DEBUG, INFO, WARNING, ERROR or CRITICAL"
    )
    parser.addoption(
        "--remote",
        help="Url to remote machine with selenium"
    )
    parser.addoption(
        "--vnc",
        action="store_true",
        help="VNC option"
    )
    parser.addoption(
        "--bv",
        help="Browser version"
    )
    parser.addoption(
        "--video",
        action="store_true",
        help="Video recording"
    )
    parser.addoption(
        "--logs",
        action="store_true",
        help="Logs"
    )


@pytest.fixture()
def browser(request):
    headless = request.config.getoption("--headless")
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    remote = request.config.getoption("--remote")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    video = request.config.getoption("--video")
    logs = request.config.getoption("--logs")

    remote_url = f"http://{remote}:4444/wd/hub"

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log",
                                       mode="w")
    file_handler.setFormatter(logging.Formatter(
        "%(levelname)s - %(asctime)s - %(message)s - %(name)s - %(filename)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("=== Test <%s> started ===" % (
        request.node.name))

    if browser_name == "chrome":
        options = ChromeOptions()
        service = Service(
            executable_path=request.config.getoption("--chrome_driver_path"))
        if headless:
            options.add_argument("--headless=new")
        if remote:
            driver = webdriver.Remote(remote_url, options=options)
        else:
            driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "yandex":
        options = ChromeOptions()
        service = Service(
            executable_path=request.config.getoption("--yandex_driver_path"))
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "opera":
        service = Service(
            request.config.getoption("--opera_driver_path"))
        service.start()
        options = ChromeOptions()
        options.binary_location = request.config.getoption(
            "--opera_browser_path")
        options.add_experimental_option('w3c', True)
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Remote(service.service_url,
                                  options=options)
    else:
        raise ValueError(
            f"Browser {browser_name} not supported."
            f" Chose between chrome, firefox, opera or yandex")

    if request.config.getoption("--max"):
        driver.maximize_window()

    if request.config.getoption("--remote"):
        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "screenResolution": "1280x2000",
                "enableVideo": video,
                "enableLog": logs,
                "timeZone": "Europe/Moscow"
            },
            "acceptInsecureCerts": True
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )

    driver.url = request.config.getoption("--url")

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("== Browser %s started ==" % browser_name)

    yield driver

    driver.close()

    logger.info("== Browser %s closed ==" % browser_name)
