# 1. Open site
# 2. Click Register
# 3. Fill registration form
# 4. Submit form
# 5. Check registration success
# 6. Open chat
# 7. Send message
# 8. Check message is visible


# разобрать код почему так и тд


# from playwright.sync_api import Playwright, expect
# import time
# import re
#
#
# def test_user_reg(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#     page.goto("https://dashboard4.nx-sandbox.com/#/register")
#
#     number = int(time.time()) % 10000
#
#     username = f"shapka{number}"
#
#     # Перед демонстрацией поставь сюда новую реальную почту
#     # Для обычной проверки регистрации можно временно использовать random email:
#     email = f"nexxietest{number}@mail.com"
#
#     # --- REGISTRATION ---
#     page.locator("input[name='username']:visible").fill(username)
#     page.locator("input[name='email']:visible").fill(email)
#     page.locator("input[name='password']:visible").fill("1212121212")
#
#     # --- DATE OF BIRTH ---
#     page.locator("[name='birthday']").click()
#     page.get_by_role("option", name="1", exact=True).click()
#
#     page.locator("[name='birthmonth']").click()
#     page.get_by_role("option", name="1", exact=True).click()
#
#     page.locator("[name='birthyear']").click()
#     page.get_by_role("option", name="2001", exact=True).click()
#
#     # --- LOCATION ---
#     page.locator("[name='location']").click()
#     page.locator("[name='location'] input.ui-select-search").fill("London")
#     page.get_by_role("option", name="London", exact=True).click()
#
#     # --- SUBMIT ---
#     page.locator("input[type='checkbox']:visible").check()
#
#     register_button = page.locator("button.main-register-btn")
#     expect(register_button).not_to_have_class(re.compile("disabled"), timeout=10000)
#     register_button.click()
#
#     # эта строка подтверждает, что регистрация прошла успешно:
#     expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)
#
#     # --- VERIFY EMAIL ---
#     page.get_by_role("button", name="Verify Now").click()
#
#     # Manual step:
#     # 1. Open your email
#     # 2. Confirm registration
#     # 3. Return to the site
#     # 4. Click Resume in Playwright Inspector
#
#     # page.pause()
#
#     # page.reload()
#
#     # --- CHAT ---
#     page.get_by_text("Chat", exact=True).click()
#
#     message = "Hi, im fine"
#     page.get_by_role("textbox", name="Your Message").fill(message)
#     page.locator(".send-btn").click()
#
#     # --- CHECK MESSAGE IS VISIBLE ---
#     expect(page.get_by_text(message, exact=True)).to_be_visible(timeout=10000)






from playwright.sync_api import Playwright


def test_user_reg(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dashboard4.nx-sandbox.com/")
    page.locator("#land-content-container input[name=\"username\"]").click()
    page.locator("#land-content-container input[name=\"username\"]").fill("userok21")
    page.locator("#land-content-container input[name=\"email\"]").click()
    page.locator("#land-content-container input[name=\"email\"]").fill("tyisocxq4iyxb-nikita2@robot-mail.com")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("21212121")
    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="2", exact=True).click()
    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="1", exact=True).click()
    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="2005").click()
    page.get_by_role("link", name="Cambridge").click()

    page.get_by_role("checkbox").check()
    page.locator("form[name=\"profileForm\"]").get_by_role("button", name="Register").click()
    page.get_by_role("button", name="Verify").click()
    page.locator(".menu-item.active > .active > .icon > use").click()
    page.get_by_role("textbox", name="Your Message").fill("Hi, whats poppin?")

#     # я вот хз, я получается написал а отправить я не могу понять оно отправилось или нет
#     # там суть что просто надо будет создать новую почту и



