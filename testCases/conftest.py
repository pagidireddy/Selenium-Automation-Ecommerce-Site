from pytest_metadata.plugin import metadata_key
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser is None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        print("Launching chrome browser.........")
    elif browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        print("Launching chrome browser.........")
    elif browser.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--detach")
        driver = webdriver.Firefox(options=options)
        print("Launching firefox browser.........")
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_html_report_title(report):
    report.title = "Automation html Report!"


def pytest_configure(config):
    config.stash[metadata_key]["Environment"] = "E-Commerce Domain"
    config.stash[metadata_key]["Modules"] = "Important Modules"
    config.stash[metadata_key]["Tested By"] = "Pagidireddy"


def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Platform", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
