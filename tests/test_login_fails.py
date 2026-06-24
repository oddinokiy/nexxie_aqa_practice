# Scenario 2: Login attempt after account deletion
# 1. Create unverified user
# 2. Delete account
# 3. Try login with the same email and password
# 4. Check login fails

import re
import time
from playwright.sync_api import Playwright, expect


def test_login_fails_after_account_delete(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    username = "userok12"
    email = "tyisocxq4iyxb-wer@robot-mail.com"
    password = "12121212"
    city = "London"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # --- REGISTRATION ---
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # --- DATE OF BIRTH ---
    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="2", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2007").click()

    # --- CITY ---
    page.locator("[name='location']").click()
    page.locator("[name='location'] input.ui-select-search").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    # --- SUBMIT REGISTRATION ---
    page.get_by_role("checkbox").check()
    page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()

    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    # --- OPEN ACCOUNT SETTINGS ---
    page.get_by_title("Settings").click()
    page.get_by_text("Account").click()

    # --- DELETE ACCOUNT ---
    page.get_by_role("button", name="Delete My Account").click()

    page.get_by_role("textbox", name="Your password...").fill(password)
    page.get_by_role("button", name="Why 😞").click()

    page.get_by_role("listitem").filter(has_text="I found my love").click()
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("button", name="Delete", exact=True).click()

    expect(page.get_by_text("Account deleted")).to_be_visible(timeout=15000)
    page.get_by_role("button", name="X", exact=True).click()

    # Close extra tabs opened after account deletion
    for opened_page in context.pages:
        if opened_page != page:
            opened_page.close()

    # --- TRY LOGIN AFTER DELETE ---
    login_page = context.new_page()
    login_page.goto("https://dashboard4.nx-sandbox.com/#/signin")

    email_field = login_page.get_by_role("textbox", name="Username/Email: Name")
    password_field = login_page.get_by_role("textbox", name="Password:")

    email_field.fill(email)
    password_field.fill(password)

    expect(email_field).to_have_value(email)
    expect(password_field).to_have_value(password)

    sign_in_button = login_page.locator("form[name='formHolder.loginForm']").get_by_role( "button", name="Sign In")

    expect(sign_in_button).to_be_enabled(timeout=10000)
    sign_in_button.click()

    # User should stay on Sign In page because account was deleted
    expect(login_page).to_have_url(re.compile(r".*/#/signin"), timeout=10000)
