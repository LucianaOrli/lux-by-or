import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # headless=False para você ver o navegador abrindo
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
