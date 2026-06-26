# Scenario 1

# 1. Open site
# 2. Fill registration form with new email
# 3. Submit form
# 4. Check registration success
# 5. Open account settings
# 6. Delete account
# 7. Check account is deleted

from playwright.sync_api import Page

# вроде бы как код работает, но лучше перепроверить

def test_del_Scenario_1(page:Page):
    username = "userok21"
    email = "tyisocxq4iyxb-yurtuj@chapsmail.com"  # Change email before each test run
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

    page.get_by_role("button", name="Delete", exact=True).click()
    page.get_by_role("button", name="X", exact=True).click()










#
#
# import re
# from playwright.sync_api import Playwright, expect
#
#
# def test_user_reg(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     page = browser.new_page()
#
#     username = "vasilis283"
#     email = "tyisocxq4iyxb-nik23@temptami.com" # каждый раз когда тестишь надо менять почту, чтобы работало
#     password = "21212121"
#     city = "London"
#
#     page.goto("https://dashboard4.nx-sandbox.com/")
#
#     # --- Reg ---
#     page.locator("#land-content-container input[name='username']").fill(username)
#     page.locator("#land-content-container input[name='email']").fill(email)
#     page.locator("input[name='password']").fill(password)
#
#     # --- Date of birth ---
#     page.get_by_label("Select box activate").nth(2).click()
#     page.get_by_role("link", name="1", exact=True).click()
#
#     page.get_by_label("Select box activate").nth(3).click()
#     page.get_by_role("link", name="7", exact=True).click()
#
#     page.get_by_text("YYYY").click()
#     page.get_by_role("link", name="1999").click()
#
#     # --- City ---
#     page.locator("[name='location']").click()
#     page.locator("[name='location'] input.ui-select-search").fill(city)
#     page.get_by_role("option", name=city, exact=True).click()
#
#     # --- Submit ---
#     page.get_by_role("checkbox").check()
#     page.locator("form[name='profileForm']").get_by_role("button", name="Register").click()
#
#     expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=25000)
#
#     # --- open acc settings ---
#     page.get_by_title("Settings").click()
#     page.get_by_text("Account").click()
#
#     # --- del acc ---
#     page.get_by_role("button", name="Delete My Account").click()
#
#     page.get_by_role("textbox", name="Your password...").fill(password)
#     page.get_by_role("button", name="Why 😞").click()
#
#     page.get_by_role("listitem").filter(has_text="Other:").click()
#     page.get_by_role("button", name="Submit").click()
#
#     # Confirm deletion in feedback popup
#     page.get_by_role("button", name="Delete", exact=True).click()

    # # Close final "Account deleted" popup
    # expect(page.get_by_text("Account deleted")).to_be_visible(timeout=15000)
    # page.get_by_role("button", name="X", exact=True).click()
    #
    # # User should be redirected to the public site after account deletion
    # expect(page.get_by_role("button", name="Join for free")).to_be_visible(timeout=15000)






