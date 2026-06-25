
from playwright.sync_api import Playwright, expect


def test_already_reg(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    email = "shapka"
    password = "12121212"
    message = "Sorry, shawty i'm busy right now"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Login
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Username/Email: Name").fill(email)
    page.get_by_role("textbox", name="Password:").fill(password)
    page.get_by_role("button", name="Sign In").click()

    # Open chat
    page.get_by_text("Chat", exact=True).click()

    # Send message
    message_input = page.get_by_role("textbox", name="Your Message")
    expect(message_input).to_be_visible(timeout=10000)
    message_input.fill(message)

    page.locator(".send-btn").click()

    # Check message was sent
    expect(page.locator("#chat-msg-list-container").get_by_text(message, exact=True)).to_be_visible(timeout=10000)


