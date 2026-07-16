import pytest
from playwright.sync_api import Page, expect


@pytest.mark.payment
def test_user_can_purchase_incognito_subscription(page: Page):
    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")
    page.locator(".profile-area").click()
    page.get_by_role("button", name="Become Incognito now").click()

    expect(page.get_by_role("textbox", name="Cardholder Name")).to_be_visible(
        timeout=10000
    )
    page.locator("#rc-cardholder").fill("QA Test User")
    page.locator("#rc-cardnumber").fill("4242424242424242")
    page.locator("#rc-expiryDate").fill("11/27")
    page.locator("#rc-cvcnumber").fill("123")
    page.locator("#rememberCard").uncheck()
    page.get_by_role("button", name="Confirm & Pay").click()

    start_exploring = page.get_by_role("button", name="Start Exploring")
    expect(start_exploring).to_be_visible(timeout=15000)
    start_exploring.click()
