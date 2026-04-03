import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized", "--window-size=1600,900"])
        yield browser
        browser.close()
        
@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={"width": 1600, "height": 900})
    page = context.new_page()
    yield page
    context.close()