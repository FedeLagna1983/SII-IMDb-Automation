import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chromium", "firefox"])
def browser_context(request):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=False, slow_mo=300)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            locale="en-US"
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(20000)
    yield page
    page.close()