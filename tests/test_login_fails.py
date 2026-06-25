# Scenario 2

# 1. Open site
# 2. Fill registration form with new email
# 3. Submit form
# 4. Check registration success
# 5. Delete account
# 6. Open login page
# 7. Enter same email and password
# 8. Click Login
# 9. Check login fails

import re
from playwright.sync_api import Playwright, expect


def test_login_fails_after_account_delete(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # --- Data ---

    username = "userok12"
    email = "tyisocxq4iyxb-yey@blondmail.com"  # Change email before each test run
    password = "12121212"
    city = "London"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # --- CREATE UNVERIFIED USER ---
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="2", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2007").click()

    page.locator("[name='location']").click()
    page.locator("[name='location'] input.ui-select-search").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    page.get_by_role("checkbox").check()
    page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()

    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    # --- acc settings ---
    page.get_by_title("Settings").click()
    page.get_by_text("Account").click()

    # --- delete acc ---
    page.get_by_role("button", name="Delete My Account").click()

    page.get_by_role("textbox", name="Your password...").fill(password)
    page.get_by_role("button", name="Why 😞").click()

    page.get_by_role("listitem").filter(has_text="Other:").click()
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("button", name="Delete", exact=True).click()

    expect(page.get_by_text("Account deleted")).to_be_visible(timeout=15000)
    page.get_by_role("button", name="X", exact=True).click()

    # Wait until redirect after deletion is finished
    expect(page.get_by_role("button", name="Join for free")).to_be_visible(timeout=15000)

    # Close extra tabs opened by the website
    for opened_page in context.pages:
        if opened_page != page:
            opened_page.close()

    # --- try log with del acc ---
    page.bring_to_front()
    page.goto("https://dashboard4.nx-sandbox.com/#/signin")

    email_field = page.get_by_role("textbox", name="Username/Email: Name")
    password_field = page.get_by_role("textbox", name="Password:")

    email_field.fill(email)
    password_field.fill(password)

    expect(email_field).to_have_value(email)
    expect(password_field).to_have_value(password)

    page.locator("form[name='formHolder.loginForm']").get_by_role("button", name="Sign In").click()

    # --- check login failed ---
    expect(page.get_by_text("Username/password combination not found")).to_be_visible(timeout=10000)

