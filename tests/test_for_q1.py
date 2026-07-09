import re
import pytest
import allure
from playwright.sync_api import Page, expect


@pytest.mark.no_auth
def test_sign_in_update_flow(page: Page):
    username = "shapka"
    password = "12121212"
    message = "Wassup, how are you?"

    with allure.step("Open application"):
        page.goto("https://dashboard4.nx-sandbox.com/")

    with allure.step("Open sign in form"):
        page.get_by_role("button", name="Sign In").click()

    with allure.step("Fill sign in form"):
        page.locator("#land-content-container input[name='username']").fill(username)
        page.locator("input[name='password']").fill(password)

    with allure.step("Submit sign in form"):
        page.locator("form").get_by_role("button", name="Sign In").click()

    with allure.step("Close popup if it appears"):
        close_popup = page.locator(".modal-content .close, .popup .close, button.close").first

        if close_popup.is_visible(timeout=5000):
            close_popup.click()

    with allure.step("Open Browse page"):
        page.get_by_title("Browse").click()

    with allure.step("Verify Browse page is opened"):
        expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    with allure.step("Open first user profile"):
        open_first_profile = page.locator(".profile-details").first
        expect(open_first_profile).to_be_visible(timeout=30000)
        open_first_profile.click()

    with allure.step("Open chat with selected user"):
        page.locator('div[ng-click="context.goToChat()"]').first.click()

    with allure.step("Send message"):
        page.get_by_placeholder("Your Message").fill(message)
        page.locator(".send-btn").click()

    with allure.step("Verify sent message is visible in chat"):
        chat_container = page.locator("#chat-msg-list-container")
        expect(chat_container.get_by_text(message, exact=True)).to_be_visible(timeout=10000)