import re
from playwright.sync_api import Page, expect


def test_sign_in_update(page:Page):
    # Scenario:
    # Existing user logs in, opens first profile, starts chat, and sends a message

    username = "shapka"
    password = "12121212"
    message = "Sorry, shawty im busy right now"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Open login form
    page.get_by_role("button", name="Sign In").click()

    # Fill login form
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("input[name='password']").fill(password)

    # Submit login form
    page.locator("form").get_by_role("button", name="Sign In").click()

    # Open Browse page
    page.get_by_title("Browse").click()
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    # Open first user profile
    open_first_profile = page.locator(".profile-details").first
    expect(open_first_profile).to_be_visible(timeout=30000)
    open_first_profile.click()

    # Open chat with this user
    page.locator('div[ng-click="context.goToChat()"]').first.click()

    # Send message
    page.get_by_placeholder("Your Message").fill(message)
    page.locator(".send-btn").click()
