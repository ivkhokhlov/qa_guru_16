"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture()
def browser_setup(request):
    browser.config.base_url = 'https://github.com/'
    browser.config.driver_name = 'chrome'
    browser.config.timeout = 10
    if request.param == 'mobile':
        browser.config.window_width = 360
        browser.config.window_height = 800
    elif request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        raise 'Platform is not defined'
    yield
    browser.quit()


@pytest.mark.parametrize('browser_setup', ['desktop'], indirect=True)
def test_github_desktop(browser_setup):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('.signup-text-prompt').should(have.text('Enter your email'))


@pytest.mark.parametrize('browser_setup', ['mobile'], indirect=True)
def test_github_mobile(browser_setup):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('h1').should(have.text('Sign in to GitHub'))
