import re
from playwright.sync_api import Page, expect


def test_sign_in_update_flow(page:Page):
    # Scenario:
    # Existing user logs in, opens first profile, starts chat, and sends a message

    # Test data for existing user
    username = "shapka"
    password = "12121212"
    message = "Wassup, how are you?"

    # Open the application
    page.goto("https://dashboard4.nx-sandbox.com/")

    # Open login form
    page.get_by_role("button", name="Sign In").click()

    # Fill login form
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("input[name='password']").fill(password)

    # Submit login form
    page.locator("form").get_by_role("button", name="Sign In").click()

    close_popup = page.locator(".modal-content .close, .popup .close, button.close").first

    if close_popup.is_visible(timeout=5000):
        close_popup.click()

    # Open Browse page
    page.get_by_title("Browse").click()
    # Verify that Browse page was opened successfully
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    # Open first user profile
    # тут можно сделать и просто чтобы какой нить рандомной бабе написать тип
    open_first_profile = page.locator(".profile-details").first
    # Wait until the first profile is visible on the page
    expect(open_first_profile).to_be_visible(timeout=30000)
    open_first_profile.click()

    # Open chat with this user
    page.locator('div[ng-click="context.goToChat()"]').first.click()

    # Send message
    page.get_by_placeholder("Your Message").fill(message)
    page.locator(".send-btn").click()
    
    # Финальная проверка
    # Verify that the sent message is displayed in the chat messages container
    chat_container = page.locator("#chat-msg-list-container")
    expect(chat_container.get_by_text(message, exact=True)).to_be_visible(timeout=10000)
