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
from playwright.sync_api import Page, expect


# показывает что код рабочий а поле в sign in не заполнились визуально

# также проверить там чуть код поменялся и надо понять как работает

def test_del_Scenario_2(page: Page):
    # --- Test data ---
    username = "userok21"
    email = "tyisocxq4iyxb-lkmp@givmail.com"  # Change email before each test run
    password = "21212121"
    city = "Cambridge"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # --- Step 1: Register unverified user ---
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Date of birth
    page.get_by_text("DD").click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_text("MM").click()
    page.get_by_role("link", name="7", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="1999").click()

    # City
    page.locator("[name='location']").click()
    page.get_by_role("textbox", name="Select box").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    # Submit registration form
    page.get_by_role("checkbox").check()
    page.locator("form").get_by_role("button", name="Register").click()

    # Registration should be successful
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    # --- Step 2: Open account settings ---
    page.get_by_title("Settings").click()
    page.get_by_text("Account", exact=True).click()

    # --- Step 3: Delete account ---
    page.get_by_role("button", name="Delete My Account").click()

    page.get_by_placeholder("Your password...").fill(password)
    page.get_by_role("button", name="Why 😞").click()

    page.get_by_text("Other:", exact=True).click()
    page.get_by_role("button", name="Submit").click()

    # Confirm account deletion
    page.get_by_role("button", name="Delete", exact=True).click()

    # Close final deletion confirmation popup
    page.get_by_role("button", name="X", exact=True).click()

    # User should be redirected outside dashboard after account deletion
    expect(page).not_to_have_url(re.compile(r".*dashboard4\.nx-sandbox\.com.*"), timeout=15000)

    # Close extra tabs opened by the website
    for opened_page in page.context.pages:
        if opened_page != page:
            opened_page.close()

    # --- Step 4: Open Sign In page ---
    page.goto("https://dashboard4.nx-sandbox.com/#/signin")
    page.wait_for_load_state("networkidle")

    login_form = page.locator('form[name="formHolder.loginForm"]')

    # --- Step 5: Try login with deleted account credentials ---
    login_form.locator("input[name='username']").fill(email)
    login_form.locator("input[name='password']").fill(password)

    login_form.get_by_role("button", name="Sign In").click()
    page.wait_for_load_state("networkidle")

    # --- Step 6: Check login failed ---
    expect(page).not_to_have_url(re.compile(r".*/#/session/search"))
    expect(login_form.get_by_role("button", name="Sign In")).to_be_visible()