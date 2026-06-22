from playwright.sync_api import Playwright

# акк уже зареган в системе и просто если что то пойдет не так, то показать им этот варик что тип чел зарегася
# и может написать сообщение и отправить ему

def test_already_reg(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
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
    page.get_by_role("textbox", name="Your Message").fill("nah, i aint wanna")
    page.locator(".send-btn > .ng-isolate-scope > .icon > use").click()

