import os
import re

import allure
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.no_auth
def test_existing_user_can_sign_in_and_send_message(page: Page):
    username = os.getenv("NX_TEST_USERNAME")
    password = os.getenv("NX_TEST_PASSWORD")
    if not username or not password:
        pytest.skip("Set NX_TEST_USERNAME and NX_TEST_PASSWORD to run this scenario")

    message = "Hello from the automated E2E test"

    with allure.step("Open the application and sign in"):
        page.goto("https://dashboard4.nx-sandbox.com/")
        page.get_by_role("button", name="Sign In").click()
        page.locator("#land-content-container input[name='username']").fill(username)
        page.locator("input[name='password']").fill(password)
        page.locator("form").get_by_role("button", name="Sign In").click()

    with allure.step("Open the first available profile"):
        close_popup = page.locator(
            ".modal-content .close, .popup .close, button.close"
        ).first
        if close_popup.is_visible(timeout=5000):
            close_popup.click()

        page.get_by_title("Browse").click()
        expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

        profile = page.locator(".profile-details").first
        expect(profile).to_be_visible(timeout=30000)
        profile.click()
        page.locator('div[ng-click="context.goToChat()"]' ).first.click()

    with allure.step("Send a message and verify it is visible"):
        page.get_by_placeholder("Your Message").fill(message)
        page.locator(".send-btn").click()
        chat = page.locator("#chat-msg-list-container")
        expect(chat.get_by_text(message, exact=True)).to_be_visible(timeout=10000)
