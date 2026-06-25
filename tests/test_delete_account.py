# Scenario 1

# 1. Open site
# 2. Fill registration form with new email
# 3. Submit form
# 4. Check registration success
# 5. Open account settings
# 6. Delete account
# 7. Check account is deleted



import re
from playwright.sync_api import Playwright, expect


def test_user_reg(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    username = "vasilis283"
    email = "tyisocxq4iyxb-nik23@temptami.com" # каждый раз когда тестишь надо менять почту, чтобы работало
    password = "21212121"
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
    page.get_by_role("link", name="7", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="1999").click()

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

    page.get_by_role("listitem").filter(has_text="Other:").click()
    page.get_by_role("button", name="Submit").click()

    # Confirm deletion in feedback popup
    page.get_by_role("button", name="Delete", exact=True).click()

    # Close final "Account deleted" popup
    expect(page.get_by_text("Account deleted")).to_be_visible(timeout=15000)
    page.get_by_role("button", name="X", exact=True).click()

    # User should be redirected to the public site after account deletion
    expect(page.get_by_role("button", name="Join for free")).to_be_visible(timeout=15000)
