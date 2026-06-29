# Scenario 1
# 1. Open site
# 2. Click Register
# 3. Fill registration form
# 4. Submit form
# 5. Check registration success
# 6. Open chat
# 7. Send message
# 8. Check message is visible

# rabotaet code

from playwright.sync_api import Page, expect
import re

# понять логику кода и строчки что делают

def test_reg_scenario_1(page:Page):
    # Registered user verifies email, opens chat with a user, and sends a message

    username = "userok21"
    email = "tyisocxq4iyxb-hekjmo@tupmail.com"  # Change email before each test run
    password = "21212121"
    city = "London"
    message = "Hi, how are u?"

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

    # Open email verification chat and click Verify
    page.get_by_text("Chat", exact=True).click()
    page.get_by_text("Verify your email", exact=True).click()
    page.get_by_role("button", name="Verify").click()

    # Manual step: confirm email, then click Resume in Playwright Inspector
    page.pause()
    page.reload()

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

    # Send message
    page.get_by_placeholder("Your Message").fill(message)
    page.locator(".send-btn").click()

    # Check that sent message is visible in chat
    chat_container = page.locator("#chat-msg-list-container")
    expect(chat_container.get_by_text(message, exact=True)).to_be_visible(timeout=10000)
