# Scenario 2
# Verified user can open chat from Browse page

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
import pytest

from playwright.sync_api import Page, expect

# понять логику кода и строчки что делают

@pytest.mark.no_auth
def test_reg_scenario_2(page:Page):

    # Test data for registration
    username = "userok21"
    email = "tyisocxq4iyxb-lkjjn@fivermail.com"  # Change email before each test run
    password = "21212121"
    city = "Cambridge"

    # Open the application
    page.goto("https://dashboard4.nx-sandbox.com/")

    # Fill registration form
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Select date of birth
    page.get_by_text("DD").click()
    page.get_by_role("link", name="8", exact=True).click()  # exact=True means exact text match
    page.get_by_text("MM").click()
    page.get_by_role("link", name="5", exact=True).click()
    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2005").click()

    # Select city
    page.locator("[name='location']").click()
    page.get_by_role("textbox", name="Select box").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    # Accept terms and submit registration form
    page.get_by_role("checkbox").check()
    page.locator("form").get_by_role("button", name="Register").click()

    # Close notification popup if it appears
    no_thx_button = page.get_by_role("button", name="No Thanks")
    page.add_locator_handler(no_thx_button, lambda: no_thx_button.click())

    # Open email verification chat and click Verify
    page.get_by_text("Chat", exact=True).click()
    page.get_by_text("Verify your email", exact=True).click()
    page.get_by_role("button", name="Verify").click()

    # Manual step: confirm email, then click Resume in Playwright Inspector
    page.pause()
    page.reload()

    # Open Browse page
    page.get_by_title("Browse").click()

    # Wait because after registration the app can redirect back to welcome chat
    # тип мы можем оставаться на вкладке где ток подтвердили почту и поэтому нам нужно подождать
    page.wait_for_timeout(3000)

    # If Browse did not stay open, click Browse again
    if "search" not in page.url:
        page.get_by_title("Browse").click()

    # Check that Browse page is opened
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)
    page.wait_for_load_state("networkidle")

    # Find first user profile in Browse
    first_profile = page.locator(".profile-details").first

    # Protection against endless loading state
    try:
#Если Browse завис на загрузке, тест обновляет страницу и пробует открыть первого пользователя еще раз.
        # Wait for the first user profile to appear
        expect(first_profile).to_be_visible(timeout=7000)
    except AssertionError:
        # If profiles did't load, reload the page and try again
        print("Сайт завис на трех точках! Перезагружаем...")
        page.reload()
        page.get_by_title("Browse").click()
        page.wait_for_load_state("networkidle")

        # Wait again after reload
        expect(first_profile).to_be_visible(timeout=15000)

    # Open first user profile and start chat
    first_profile.click()
    page.locator('div[ng-click="context.goToChat()"]').first.click()

    # Wait until chat page is loaded
    page.wait_for_load_state("networkidle")

    # Check that chat message input is visible
    expect(page.get_by_role("textbox", name="Your Message")).to_be_visible(timeout=10000)
