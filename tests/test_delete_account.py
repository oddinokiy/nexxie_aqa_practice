# 1. Create unverified user
# 2. Login as user
# 3. Open account settings
# 4. Delete account
# 5. Check account is deleted

from playwright.sync_api import Playwright

# сделать код более простым и легким для меня, чтобы я мог объяснить руководству
# и по хорошему разобраться

# def test_del_acc_no_email(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://dashboard4.nx-sandbox.com/")
#     page.locator("#land-content-container input[name=\"username\"]").fill("userok22")
#     page.locator("#land-content-container input[name=\"email\"]").click()
#     page.locator("#land-content-container input[name=\"email\"]").fill("tyisocxq4iyxb-nikita1@getnada.com")
#     page.locator("input[name=\"password\"]").click()
#     page.locator("input[name=\"password\"]").fill("12121212")
#     page.get_by_label("Select box activate").nth(2).click()
#     page.get_by_role("link", name="1", exact=True).click()
#     page.get_by_label("Select box activate").nth(3).click()
#     page.get_by_role("link", name="2", exact=True).click()
#     page.get_by_label("Select box activate").nth(4).click()
#     page.get_by_role("link", name="2006").click()
#     page.get_by_role("textbox", name="Select box").fill("london")
#     page.get_by_role("link", name="London", exact=True).click()
#     page.get_by_role("checkbox").check()
#     page.locator("form[name=\"profileForm\"]").get_by_role("button", name="Register").click()
#     page.get_by_title("Settings").click()
#     page.get_by_text("Account").click()
#     page.get_by_role("button", name="Delete My Account").click()
#     page.get_by_role("textbox", name="Your password...").click()
#     page.get_by_role("textbox", name="Your password...").fill("12121212")
#     page.get_by_role("textbox", name="Your password...").press("Enter")
#     page.get_by_role("button", name="Why 😞").click()
#     page.get_by_role("listitem").filter(has_text="Other:").click()
#     page.get_by_role("button", name="Submit").click()
#     page.get_by_role("textbox", name="Your password...").fill("12121212")
#     page.get_by_role("button", name="Delete", exact=True).click()
#     page.get_by_role("button", name="X", exact=True).click()
#
#     # после того как нажали на Х , нас перекинуло на главную страницу
#     # нужно ли нам делать except в конце после Х или так пойдет?


from playwright.sync_api import Playwright, expect


def test_del_acc_no_email(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # --- OPEN SITE ---
    page.goto("https://dashboard4.nx-sandbox.com/")

    # --- REGISTRATION ---
    username = "userok22"
    email = "tyisocxq4iyxb-nikita1@getnada.com"
    password = "12121212"

    page.locator("#land-content-container input[name='username']").fill(username)
    page.locator("#land-content-container input[name='email']").fill(email)
    page.locator("input[name='password']").fill(password)

    # --- DATE OF BIRTH ---
    page.get_by_label("Select box activate").nth(2).click()
    page.get_by_role("link", name="1", exact=True).click()

    page.get_by_label("Select box activate").nth(3).click()
    page.get_by_role("link", name="2", exact=True).click()

    page.get_by_label("Select box activate").nth(4).click()
    page.get_by_role("link", name="2006").click()

    # --- LOCATION ---
    page.get_by_role("textbox", name="Select box").fill("London")
    page.get_by_role("link", name="London", exact=True).click()

    # --- SUBMIT REGISTRATION ---
    page.get_by_role("checkbox").check()
    page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()

    # --- OPEN ACCOUNT SETTINGS ---
    page.get_by_title("Settings").click()
    page.get_by_text("Account").click()

    # --- DELETE ACCOUNT ---
    page.get_by_role("button", name="Delete My Account").click()

    page.get_by_role("textbox", name="Your password...").fill(password)
    page.get_by_role("textbox", name="Your password...").press("Enter")

    page.get_by_role("button", name="Why 😞").click()
    page.get_by_role("listitem").filter(has_text="Other:").click()
    page.get_by_role("button", name="Submit").click()

    page.get_by_role("textbox", name="Your password...").fill(password)
    page.get_by_role("button", name="Delete", exact=True).click()

    page.get_by_role("button", name="X", exact=True).click()

    # --- CHECK ACCOUNT IS DELETED ---
    expect(page.locator("#land-content-container input[name='username']")).to_be_visible(timeout=15000)
