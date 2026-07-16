from playwright.sync_api import Page, expect


def test_authenticated_user_can_open_profile_settings(page: Page):
    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")
    expect(page).to_have_url("https://dashboard4.nx-sandbox.com/#/session/search")

    page.get_by_text("nik", exact=True).click()
    expect(page).to_have_url(
        "https://dashboard4.nx-sandbox.com/#/session/my/edit-profile"
    )
