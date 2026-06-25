import re

from playwright.sync_api import Playwright, expect


def test_already_reg(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    email = "shapka"
    password = "12121212"
    message = "Sorry, shawty im busy right now"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Login
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Username/Email: Name").fill(email)
    page.get_by_role("textbox", name="Password:").fill(password)
    page.locator("form[name='formHolder.loginForm']").get_by_role("button", name="Sign In").click()

    # Open Browse
    page.get_by_title("Browse").click()
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    # Open first user profile
    first_profile = page.locator(".profile-details").first
    expect(first_profile).to_be_visible(timeout=30000)
    first_profile.click()

    # Open chat with this user
    page.get_by_title("Chat").nth(1).click()

    # Send message
    message_input = page.get_by_role("textbox", name="Your Message")
    expect(message_input).to_be_visible(timeout=10000)
    message_input.fill(message)

    page.locator(".send-btn").click()