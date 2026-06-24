from playwright.sync_api import Playwright

 # сделать код максимально простым, чтобы я мог понять как это работает и по хорошему разобраться самостоятельно

def test_already_reg(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://dashboard4.nx-sandbox.com/")

    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("textbox", name="Username/Email: Name").click()
    page.get_by_role("textbox", name="Username/Email: Name").fill("shapka")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("12121212")
    page.locator("form[name=\"formHolder.loginForm\"]").get_by_role("button", name="Sign In").click()
    page.get_by_text("Chat", exact=True).click()
    page.get_by_role("textbox", name="Your Message").click()
    page.get_by_role("textbox", name="Your Message").fill("Sorry, shawty i'm busy right now")
    page.locator(".send-btn").click()

