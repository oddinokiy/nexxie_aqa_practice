# Scenario 3: Registration with deleted email
# 1. Create unverified user
# 2. Delete account
# 3. Register new user with the same email
# 4. Check registration succeeds

import re
import time
from playwright.sync_api import Playwright, expect


def test_register_with_deleted_email(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    username_first = f"userone{unique_id}"
    second_username = f"usertwo{unique_id}"
    email = f"deletedemail{unique_id}@getmule.com"
    password = "12121212"
    city = "London"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # --- CREATE FIRST USER ---
    page.locator("#land-content-container input[name='username']").fill(first_username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="3", exact=True).click()

    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="4", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2007").click()

    page.locator("[name='location']").click()
    page.locator("[name='location'] input.ui-select-search").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    page.get_by_role("checkbox").check()
    page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()

    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    # --- DELETE ACCOUNT ---
    page.get_by_title("Settings").click()
    page.get_by_text("Account").click()

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

    # --- REGISTER SECOND USER WITH SAME EMAIL ---
    page.goto("https://dashboard4.nx-sandbox.com/")

    page.locator("#land-content-container input[name='username']").fill(second_username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2008").click()

    page.locator("[name='location']").click()
    page.locator("[name='location'] input.ui-select-search").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    page.get_by_role("checkbox").check()
    page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()

    # --- CHECK REGISTRATION SUCCEEDED ---
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    browser.close()