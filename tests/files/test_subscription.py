from playwright.sync_api import Page


def test_to_get_inco_mode(page: Page):
    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    # Navigate to the user profile
    page.locator(".profile-area").click()

    # Pause to visually check the profile page
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Become Incognito now").click()
    page.wait_for_timeout(2000)

    # Fill cardholder name
    page.locator("#rc-cardholder").fill("Double r")

    # Fill test card number
    page.locator("#rc-cardnumber").fill("4242424242424242")

    # Fill card expiry date
    page.locator("#rc-expiryDate").fill("11/27")

    # Fill CVC
    page.locator("#rc-cvcnumber").fill("123")

    # Do not remember this card
    page.locator("#rememberCard").uncheck()

    # Confirm payment
    page.get_by_role("button", name="Confirm & Pay").click()

    page.get_by_role("button", name="Start Exploring").click()
