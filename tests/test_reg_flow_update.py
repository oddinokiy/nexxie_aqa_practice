# Scenario 1
# 1. Open site
# 2. Click Register
# 3. Fill registration form
# 4. Submit form
# 5. Check registration success
# 6. Open chat
# 7. Send message
# 8. Check message is visible


from playwright.sync_api import Page, expect
import re


def test_reg_scenario_1(page:Page):
    # Registered user verifies email, opens chat with a user, and sends a message

    # page.locator("#gender").get_by_label("Select box activate").click()
    # page.get_by_role("link", name="a female").click()
    # page.locator("#lookingFor").get_by_label("Select box activate").click()
    # page.get_by_role("link", name="a male").click()

    # page.locator("#country").get_by_label("Select box activate").click()
    # page.get_by_role("link", name="Spain").click()


    # Test data for registration and message sending
    username = "userok21"
    email = "tyisocxq4iyxb-sdfdf@chapsmail.com"  # Change email before each test run
    password = "21212121"
    city = "London"
    message = "Hi, how are u?"

    # Open the application
    page.goto("https://dashboard4.nx-sandbox.com/")

    # Fill registration form
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # Select date of birth
    page.get_by_text("DD").click()
    page.get_by_role("link", name="7", exact=True).click()  # exact=True means exact text match
    page.get_by_text("MM").click()
    page.get_by_role("link", name="7", exact=True).click()
    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2007").click()

    # Select city from searchable dropdown
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
    first_profile = page.locator(".profile-details").first

# Если Browse завис на загрузке, тест обновляет страницу и пробует открыть первого пользователя еще раз.
    try:
        expect(first_profile).to_be_visible(timeout=7000)
    except AssertionError:
        page.reload()
        page.get_by_title("Browse").click()
        expect(first_profile).to_be_visible(timeout=15000)

    first_profile.click()

    page.locator('div[ng-click="context.goToChat()"]').first.click()

    # Send message
    page.get_by_placeholder("Your Message").fill(message)
    page.locator(".send-btn").click()

    # Check that sent message is visible in chat
    chat_container = page.locator("#chat-msg-list-container")
    expect(chat_container.get_by_text(message, exact=True)).to_be_visible(timeout=10000)

