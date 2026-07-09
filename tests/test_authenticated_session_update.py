

from playwright.sync_api import Page, expect

# The user is already logged in because conftest.py uses auth/user.json

def test_my_simple_login(page: Page):

    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")
    # открывает внутреннюю страницу приложения
    # Verify the session works and we are not redirected to the login screen
    expect(page).to_have_url("https://dashboard4.nx-sandbox.com/#/session/search")
    # убедится что после нас реально пустило на внутреннюю страницу search

    page.get_by_text("nik", exact=True).click()
    expect(page).to_have_url("https://dashboard4.nx-sandbox.com/#/session/my/edit-profile")
    # Verify the profile settings page is successfully opened
    # после клика пользователь должен попасть на стр редактирования профиля



# Что делает auth/user.json
# Это как “сохраненный браузер после входа”.
# Этот файл хранит cookies/session/localStorage, то есть состояние браузера после логина.
