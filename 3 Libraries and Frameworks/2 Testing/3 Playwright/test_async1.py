import pytest
from playwright.async_api import async_playwright

# Reusable browser fixture
@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest.mark.asyncio
async def test_login_success(browser):
    page = await browser.new_page()
    await page.goto("https://www.drupal.cz/user/login")  # Replace with your login URL

    await page.fill('input[name="name"]', "jstefl")
    await page.fill('input[name="pass"]', "DRpokus,123")
    await page.click('button[type="submit"]')

    # Example: check for a dashboard element after login
    await page.wait_for_selector("text=Můj účet")
    assert await page.inner_text("h2") == "My articles"
