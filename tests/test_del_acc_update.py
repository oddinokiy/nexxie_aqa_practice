# Scenario 1

# 1. Open site
# 2. Fill registration form with new email
# 3. Submit form
# 4. Check registration success
# 5. Open account settings
# 6. Delete account
# 7. Check account is deleted


import re
from playwright.sync_api import Page, expect

# вроде бы как код работает, но лучше перепроверить

def test_del_Scenario_1(page: Page):

    # --- Test data ---
    username = "userok21"
    email = "tyisocxq4iyxb-jhkllo@givmail.com"  # Change email before each test run
    password = "21212121"
    city = "Cambridge"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Register unverified user
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

    # Open account settings
    page.get_by_title("Settings").click()
    page.get_by_text("Account", exact=True).click()

    # Start account deletion
    page.get_by_role("button", name="Delete My Account").click()

    page.get_by_placeholder("Your password...").fill(password)
    page.get_by_role("button", name="Why 😞").click()

    # Select deletion reason and submit feedback
    page.get_by_text("Other:", exact=True).click()
    page.get_by_role("button", name="Submit").click()

    # Confirm account deletion
    page.get_by_role("button", name="Delete", exact=True).click()

    # Close final deletion confirmation popup
    page.get_by_role("button", name="X", exact=True).click()

    # Verify that user is redirected outside the internal dashboard
    expect(page).not_to_have_url(re.compile(r".*dashboard4\.nx-sandbox\.com/.*"), timeout=15000)