# Scenario 2

# 1. Open site
# 2. Fill registration form
# 3. Submit form
# 4. Check registration success
# 5. Open email verification chat
# 6. Click Verify email
# 7. Confirm email manually
# 8. Open Browse page
# 9. Open first user profile
# 10. Click Chat
# 11. Check message input is visible

import re
from playwright.sync_api import Playwright, expect

# проблема в том что идет загрузка и дальше скрпит не проходит, надо будет заново прогнать и понять в чем проблема

def test_registered_user_can_open_chat(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    username = "userok21"
    email = "tyisocxq4iyxb-jreg@tafmail.com"  # Change email before each test run
    password = "21212121"
    city = "Cambridge"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Registration
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Birth date
    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="7", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="1999").click()

    # City
    page.locator("[name='location']").click()
    page.locator("[name='location'] input.ui-select-search").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    # Submit registration
    page.get_by_role("checkbox").check()
    page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()

    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    # Close popup if it appears
    no_thanks = page.get_by_role("button", name="No Thanks")
    if no_thanks.is_visible(timeout=5000):
        no_thanks.click()

    # Email verification
    page.get_by_text("Chat", exact=True).click()
    page.get_by_text("Verify your email", exact=True).click()
    page.get_by_role("button", name=re.compile("Verify", re.I)).click()

    # Confirm email manually, then click Resume in Playwright Inspector
    page.pause()

    # Close popup after email confirmation if it appears
    close_popup = page.locator(".modal-content .close, .popup .close, button.close").first
    if close_popup.is_visible(timeout=5000):
        close_popup.click()

    # Open first profile from Browse
    page.get_by_title("Browse").click()
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    first_profile = page.locator(".profile-details").first
    expect(first_profile).to_be_visible(timeout=30000)
    first_profile.click()

    # Open chat and check message field
    page.get_by_title("Chat").nth(1).click()
    expect(page.get_by_role("textbox", name="Your Message")).to_be_visible(timeout=10000)

