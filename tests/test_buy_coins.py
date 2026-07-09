

from playwright.sync_api import Page, expect

# надо будет выбрать именно конкретный тариф, просто чтобы было понимание у них
def test_to_get_coins(page: Page):
    # The user is already logged in because conftest.py uses auth/user.json.
    page.goto("https://dashboard4.nx-sandbox.com")

    # Open the wallet page
    page.get_by_text("My Wallet").click()

    # the app shows coin packages
    coin_package = page.get_by_text("Basic 300 Coins", exact=False).first


    # Если пакет монет виден — выбрать его.
    # Если пакет не виден — значит мы уже на странице оплаты, просто продолжаем заполнять карту.

    try:
        # If we see "Basic 300 Coins", click this package.
        expect(coin_package).to_be_visible(timeout=5000)
        coin_package.click()
    except AssertionError:
        # If we do not see the package, continue.
        # It means the payment form may already be open.
        pass

    # Check that payment form is visible
    expect(page.get_by_role("textbox", name="Cardholder Name")).to_be_visible(timeout=10000)

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

    # Check that payment was successful
    start_chat_button = page.get_by_role("button", name="Start Chatting")
    expect(start_chat_button).to_be_visible(timeout=15000)

    # Finish the flow
    start_chat_button.click()