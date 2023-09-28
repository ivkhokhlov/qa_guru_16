import pytest
from selene import browser, have

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture()
def mobile_browser():
    browser.config.window_width = 360
    browser.config.window_height = 800
    yield
    browser.quit()


@pytest.fixture()
def desktop_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('.signup-text-prompt').should(have.text('Enter your email'))
    pass


def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('h1').should(have.text('Sign in to GitHub'))

