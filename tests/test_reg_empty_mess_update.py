# Scenario 3

# 1. Register user
# 2. Verify email manually
# 3. Open chat with any user
# 4. Leave message field empty
# 5. Click Send
# 6. Check empty message is not sent

import re
from playwright.sync_api import Page, expect


# понять логику кода и строчки что делают


def test_scenario_3_empty_message(page: Page):
    # Scenario 3:
    # Registered user cannot send an empty message

    username = "userok23"
    email = "tyisocxq4iyxb-rfhgjep@fivermail.com"  # Change email before each test run
    password = "21212121"
    city = "London"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Close notification popup if it appears
    no_thx_button = page.get_by_role("button", name="No Thanks")
    page.add_locator_handler(no_thx_button, lambda: no_thx_button.click())

    # Fill registration form
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Select date of birth
    page.get_by_text("DD").click()
    page.get_by_role("link", name="1", exact=True).click()
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

    # Open email verification chat and click Verify
    page.get_by_text("Chat", exact=True).click()
    page.get_by_text("Verify your email", exact=True).click()
    page.get_by_role("button", name="Verify").click()

    # Manual step: confirm email, then click Resume in Playwright Inspector
    page.pause()
    page.reload()

    # Open Browse page
    page.get_by_title("Browse").click()
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

    # Clear message field
    page.get_by_placeholder("Your Message").fill("")

    # Try to send empty message
    page.locator(".send-btn").click(force=True)

    # Check that Send button is still disabled, so empty message was not sent
    expect(page.locator(".send-btn")).to_have_attribute("disabled", re.compile(r".*"))





# старый код

# import re
# from playwright.sync_api import Playwright, expect
#
#
# def test_user_reg(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#
#     # --- Data ---
#
#     username = "userok21"
#     email = "tyisocxq4iyxb-khk@tafmail.com"  # Change email before each test run
#     password = "21212121"
#     city = "Cambridge"
#     message = " "
#
#     page.goto("https://dashboard4.nx-sandbox.com/")
#
#     # Reg
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
#     # Close notification popup
#     no_thanks = page.get_by_role("button", name="No Thanks")
#     if no_thanks.is_visible(timeout=5000):
#         no_thanks.click()
#
#     # Open email verification chat
#     page.get_by_text("Chat", exact=True).click()
#     page.get_by_text("Verify your email", exact=True).click()
#     page.get_by_role("button", name=re.compile("Verify", re.I)).click()
#
#     # Manually confirm email, then click Resume(Continue) in Playwright Inspector
#     page.pause()
#
#     # Close popup after email confirmation
#     close_popup = page.locator(".modal-content .close, .popup .close, button.close").first
#     if close_popup.is_visible(timeout=5000):
#         close_popup.click()
#
#     # Open user profile and start chat
#     page.get_by_title("Browse").click()
#     expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)
#
#     page.locator(".profile-details").first.click()
#     page.get_by_title("Chat").nth(1).click()
#
#     # Try to send empty message
#     messages_before = page.locator("#chat-msg-list-container span.ng-binding").count()
#
#     page.get_by_role("textbox", name="Your Message").fill(message)
#     page.locator(".send-btn").click()
#
#     # Считает, сколько сообщений в чате после клика по Send.
#     messages_after = page.locator("#chat-msg-list-container span.ng-binding").count()
#
#     # Проверяет, что количество сообщений не изменилось.
#     assert messages_after == messages_before