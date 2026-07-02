# Scenario 3
# 1. Open site
# 2. Fill registration form with new email
# 3. Submit form
# 4. Check registration success
# 5. Delete account
# 6. Open site again
# 7. Fill registration form with the same email
# 8. Submit form
# 9. Check registration succeeds

import re
from playwright.sync_api import expect, Page


def test_register_with_deleted_email(page:Page):

    # --- Test data ---
    username_first = "user1"
    username_second = "user2"
    email = "tyisocxq4iyxb-moloko@getmule.com"  # Change email before each run
    password = "12121212"
    city = "London"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Register first unverified user
    page.locator("#land-content-container input[name='username']").fill(username_first)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Date of birth
    page.get_by_text("DD").click()
    page.get_by_role("link", name="3", exact=True).click()

    page.get_by_text("MM").click()
    page.get_by_role("link", name="4", exact=True).click()

    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2004").click()

    # Select city from searchable dropdown
    page.locator("[name='location']").click()
    page.get_by_role("textbox", name="Select box").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    # Submit registration form
    page.get_by_role("checkbox").check()
    page.locator("form").get_by_role("button", name="Register").click()

    # First registration should be successful
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)

    # Open account settings
    page.get_by_title("Settings").click()
    page.get_by_text("Account", exact=True).click()

    # Delete first account
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

    # Register second user with the same email
    page.goto("https://dashboard4.nx-sandbox.com/")

    page.locator("#land-content-container input[name='username']").fill(username_second)
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

    # Second registration with the same email should be successful
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)