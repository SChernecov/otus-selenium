import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome",
        help="Browsers: chrome, firefox, opera or yandex"
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


@pytest.fixture()
def browser(request):
    headless = request.config.getoption("--headless")
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
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

    driver.url = request.config.getoption("--url")

    yield driver

    driver.close()
