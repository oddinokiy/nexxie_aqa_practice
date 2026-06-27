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

from playwright.sync_api import Page, expect

# понять логику кода и строчки что делают

# короче прогони тест и пойми есть ли тут смысл подтверждать почту
def test_reg_scenario_2(page:Page):
    # Registered user can open chat page after registration

    username = "userok21"
    email = "tyisocxq4iyxb-hjhtfrr@givmail.com"  # Change email before each test run
    password = "21212121"
    city = "Cambridge"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Fill registration form
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Select date of birth
    page.get_by_text("DD").click()
    page.get_by_role("link", name="1", exact=True).click()  # exact=True means exact text match
    page.get_by_text("MM").click()
    page.get_by_role("link", name="7", exact=True).click()
    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="1999").click()

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

    # Open Browse page
    page.get_by_title("Browse").click()

    # Wait because the site can redirect user back to welcome chat after registration
    page.wait_for_timeout(3000)

    # If user was redirected back to chat, open Browse again
    if "search" not in page.url:
        page.get_by_title("Browse").click()

    # Check that Browse page is opened
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    # Wait until page data is fully loaded
    page.wait_for_load_state("networkidle")

    # Open first user profile and start chat
    page.locator(".profile-details").first.click()
    page.locator('div[ng-click="context.goToChat()"]').first.click()

    page.wait_for_load_state("networkidle")

    # Check that chat message input is visible
    expect(page.get_by_role("textbox", name="Your Message")).to_be_visible(timeout=10000)




# def test_registered_user_can_open_chat(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#
#     # --- Data ---
#     username = "userok21"
#     email = "tyisocxq4iyxb-lohl@guysmail.com"  # Change email before each test run
#     password = "21212121"
#     city = "Cambridge"
#
#     page.goto("https://dashboard4.nx-sandbox.com/")
#
#     # Registration
#     page.locator("#land-content-container input[name='username']").fill(username)
#     page.locator("#land-content-container input[name='email']").fill(email)
#     page.locator("input[name='password']").fill(password)
#
#     # Birth date
#     page.get_by_label("Select box activate").nth(2).click()
#     page.get_by_role("link", name="1", exact=True).click()
#
#     page.get_by_label("Select box activate").nth(3).click()
#     page.get_by_role("link", name="7", exact=True).click()
#
#     page.get_by_text("YYYY").click()
#     page.get_by_role("link", name="1999").click()
#
#     # City
#     page.locator("[name='location']").click()
#     page.locator("[name='location'] input.ui-select-search").fill(city)
#     page.get_by_role("option", name=city, exact=True).click()
#
#     # Submit registration
#     page.get_by_role("checkbox").check()
#     page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()
#
#     expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)
#
#     # Close popup if it appears
#     no_thanks = page.get_by_role("button", name="No Thanks")
#     if no_thanks.is_visible(timeout=5000):
#         no_thanks.click()
#
#     # Email verification
#     page.get_by_text("Chat", exact=True).click()
#     page.get_by_text("Verify your email", exact=True).click()
#     page.get_by_role("button", name=re.compile("Verify", re.I)).click()
#
#     # Confirm email manually, then click Resume in Playwright Inspector
#     page.pause()
#
#     # Close popup after email confirmation if it appears
#     close_popup = page.locator(".modal-content .close, .popup .close, button.close").first
#     if close_popup.is_visible(timeout=5000):
#         close_popup.click()
#
#     page.get_by_title("Browse").click()
#     expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)
#
#
#     first_profile = page.locator(".profile-details").first
#     # Находим первого пользователя в списке Browse.
#
#     try:
#         expect(first_profile).to_be_visible(timeout=30000) # ждем 30 сек пока первый появится юзер
#     except AssertionError: # Если за 30 секунд пользователь не появился, значит список завис или не загрузился
#         page.reload()
#         page.get_by_title("Browse").click()
#         expect(first_profile).to_be_visible(timeout=30000)
#
#     first_profile.click()
#
#     # Open chat and check message field
#     page.get_by_title("Chat").nth(1).click()
#     expect(page.get_by_role("textbox", name="Your Message")).to_be_visible(timeout=10000)