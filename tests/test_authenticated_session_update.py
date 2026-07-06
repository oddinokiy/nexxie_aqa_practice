import re

from playwright.sync_api import Page, expect

# код работает, потом разобраться как работает и как легче всего мне потом написать код чтобы я мог объяснить
# руководству. Потому что на данный момент я не понимаю и мне сложно понять логику так как я делал через codex


def test_authenticated_user_can_open_browse_page(page: Page):
    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)
    expect(page.get_by_role("button", name="Join for free")).not_to_be_visible() # откуда взялась это кнопка и почему мы пишем ее?
    expect(page.get_by_title("Settings")).to_be_visible(timeout=15000)
