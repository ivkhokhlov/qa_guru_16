"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture()
def browser_init():
    browser.config.base_url = 'https://github.com/'
    browser.config.driver_name = 'chrome'
    browser.config.timeout = 10

@pytest.fixture(params=[(1920, 1080), (360, 800)], ids=['desktop', 'mobile'])
def browser_window_type(browser_init, request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    return request.node.callspec.id


def test_github_desktop(browser_window_type):
    if browser_window_type != 'desktop':
        pytest.skip(reason=f'{browser_window_type} test found')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('.signup-text-prompt').should(have.text('Enter your email'))


def test_github_mobile(browser_window_type):
    if browser_window_type != 'mobile':
        pytest.skip(reason=f'{browser_window_type} test found')
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('h1').should(have.text('Sign in to GitHub'))
