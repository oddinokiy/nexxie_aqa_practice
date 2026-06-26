# Scenario 2

# 1. Open site
# 2. Fill registration form with new email
# 3. Submit form
# 4. Check registration success
# 5. Delete account
# 6. Open login page
# 7. Enter same email and password
# 8. Click Login
# 9. Check login fails


import re
from playwright.sync_api import Page, expect


# показывает что код рабочий а поле в sign in не заполнились визуально

def test_del_Scenario_2(page:Page):
    username = "userok21"
    email = "tyisocxq4iyxb-dga@vomoto.com"  # Change email before each test run
    password = "21212121"
    city = "Cambridge"

    page.goto("https://dashboard4.nx-sandbox.com/")

    # Registration
    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    page.get_by_text("DD").click()
    page.get_by_role("link", name="1", exact=True).click()  # что значит exact=True?
    page.get_by_text("MM").click()
    page.get_by_role("link", name="7", exact=True).click()
    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="1999").click()

    page.locator("[name='location']").click()  # еще раз потом разобраться почему так
    page.get_by_role("textbox", name="Select box").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    page.get_by_role("checkbox").check()
    # связывание (Chaining). через точку
    page.locator("form").get_by_role("button", name="Register").click()

    # --- open acc settings ---
    page.get_by_title("Settings").click()
    page.get_by_text("Account",exact=True).click()

    page.get_by_role("button", name="Delete My Account").click()

    page.get_by_placeholder("Your password...").fill(password)
    page.get_by_role("button", name="Why 😞").click()

    page.get_by_text("Other:", exact=True).click()
    page.get_by_role("button", name="Submit").click()

    # 5. Подтверждение удаления
    page.get_by_role("button", name="Delete", exact=True).click()
    page.get_by_role("button", name="X", exact=True).click()


    # Ждем, пока сайт успешно удалит аккаунт и выкинет нас на внешний сайт
    # Это подтверждает, что кнопка Delete сработала!
    page.wait_for_url(re.compile(r".*saucydates\.com.*"), timeout=15000)

    # ХИТРОСТЬ: Полностью очищаем куки и локальное хранилище,
    # чтобы сайт забыл старую сессию и не логинил нас автоматически
    page.context.clear_cookies()
    page.context.clear_signatures = lambda: None  # на всякий случай

    # 6. Open login page заново
    page.goto("https://dashboard4.nx-sandbox.com/#/signin")
    page.wait_for_load_state("networkidle")

    # ХИТРОСТЬ: Находим конкретную форму входа на странице
    login_form = page.locator('form[name="formHolder.loginForm"]')

    # 7. Enter same email and password (теперь ищем строго внутри login_form)
    login_form.locator("input[name='username']").fill(email)
    login_form.locator("input[name='password']").fill(password)

    # 8. Click Login
    login_form.get_by_role("button", name="Sign In").click()
    page.wait_for_load_state("networkidle")

    # 9. Check login fails
    expect(page).not_to_have_url(re.compile(r".*/#/session/search"))
    expect(login_form.get_by_role("button", name="Sign In")).to_be_visible()






# старый код



# def test_login_fails_after_account_delete(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     page = context.new_page()
#
#     # --- Data ---
#
#     username = "userok12"
#     email = "tyisocxq4iyxb-yey@blondmail.com"  # Change email before each test run
#     password = "12121212"
#     city = "London"
#
#     page.goto("https://dashboard4.nx-sandbox.com/")
#
#     # --- CREATE UNVERIFIED USER ---
#     page.locator("#land-content-container input[name='username']").fill(username)
#     page.locator("#land-content-container input[name='email']").fill(email)
#     page.locator("input[name='password']").fill(password)
#
#     page.get_by_label("Select box activate").nth(2).click()
#     page.get_by_role("link", name="1", exact=True).click()
#
#     page.get_by_label("Select box activate").nth(3).click()
#     page.get_by_role("link", name="2", exact=True).click()
#
#     page.get_by_text("YYYY").click()
#     page.get_by_role("link", name="2007").click()
#
#     page.locator("[name='location']").click()
#     page.locator("[name='location'] input.ui-select-search").fill(city)
#     page.get_by_role("option", name=city, exact=True).click()
#
#     page.get_by_role("checkbox").check()
#     page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()
#
#     expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)
#
#     # --- acc settings ---
#     page.get_by_title("Settings").click()
#     page.get_by_text("Account").click()
#
#     # --- delete acc ---
#     page.get_by_role("button", name="Delete My Account").click()
#
#     page.get_by_role("textbox", name="Your password...").fill(password)
#     page.get_by_role("button", name="Why 😞").click()
#
#     page.get_by_role("listitem").filter(has_text="Other:").click()
#     page.get_by_role("button", name="Submit").click()
#
#     page.get_by_role("button", name="Delete", exact=True).click()
#
#     expect(page.get_by_text("Account deleted")).to_be_visible(timeout=15000)
#     page.get_by_role("button", name="X", exact=True).click()
#
#     # Wait until redirect after deletion is finished
#     expect(page.get_by_role("button", name="Join for free")).to_be_visible(timeout=15000)
#
#     # Close extra tabs opened by the website
#     for opened_page in context.pages:
#         if opened_page != page:
#             opened_page.close()
#
#     # --- try log with del acc ---
#     page.bring_to_front()
#     page.goto("https://dashboard4.nx-sandbox.com/#/signin")
#
#     email_field = page.get_by_role("textbox", name="Username/Email: Name")
#     password_field = page.get_by_role("textbox", name="Password:")
#
#     email_field.fill(email)
#     password_field.fill(password)
#
#     expect(email_field).to_have_value(email)
#     expect(password_field).to_have_value(password)
#
#     page.locator("form[name='formHolder.loginForm']").get_by_role("button", name="Sign In").click()
#
#     # --- check login failed ---
#     expect(page.get_by_text("Username/password combination not found")).to_be_visible(timeout=10000)
#
