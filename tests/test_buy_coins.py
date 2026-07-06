from playwright.sync_api import Page, expect


def test_to_get_coins(page: Page):
    # Open the website.
    # The user is already logged in because conftest.py uses auth/user.json.
    page.goto("https://dashboard4.nx-sandbox.com")

    # Open the wallet page.
    page.get_by_text("My Wallet").click()

    # Sometimes the app shows coin packages.
    # Sometimes it opens the payment page immediately.
    coin_package = page.get_by_text("Intro 200 Coins", exact=False).first

    try:
        # If the coin package is visible, select it.
        expect(coin_package).to_be_visible(timeout=5000)
        coin_package.click()
    except AssertionError:
        # If the package is not visible, we are probably already on the payment page.
        pass

    # Check that payment form is visible.
    expect(page.get_by_role("textbox", name="Cardholder Name")).to_be_visible(timeout=10000)

    # Fill cardholder name.
    page.get_by_role("textbox", name="Cardholder Name").fill("Double r")

    # Fill test card number.
    page.get_by_role("textbox", name="Card Number").fill("4242424242424242")

    # Fill card expiry date.
    page.get_by_role("textbox", name="Expiry Date").fill("11/27")

    # Fill CVC.
    page.get_by_role("textbox", name="CVC").fill("123")

    # Do not remember this card.
    page.locator("#rememberCard").uncheck()

    # Confirm payment.
    page.get_by_role("button", name="Confirm & Pay").click()

    # Check that payment was successful.
    start_chatting_button = page.get_by_role("button", name="Start Chatting")
    expect(start_chatting_button).to_be_visible(timeout=15000)

    # Finish the flow.
    start_chatting_button.click()