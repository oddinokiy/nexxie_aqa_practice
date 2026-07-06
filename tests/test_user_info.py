from playwright.sync_api import Page, expect


def test_update_profile(page: Page):
    # 1. Открываем сайт
    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    # ВОТ ЭТОГО НЕ ХВАТАЛО: Сначала открываем сам профиль!
    page.get_by_text("shapka", exact=True).click()

    # А теперь жмём карандашик (с .first, чтобы точно кликнуть нужный)
    page.locator(".edit-icon .icon").first.click()
    # 2. Дата рождения
    page.get_by_text("Day 13").click()
    page.get_by_role("link", name="10").click()

    page.get_by_text("Month 9").click()
    page.get_by_role("link", name="5").click()

    page.get_by_text("Year 1992").click()
    page.get_by_role("link", name="1995").click()

    # 3. Локация
    page.locator("span").filter(has_text="UK").first.click()
    page.get_by_role("link", name="Spain").click()

    # Сохраняем основную инфу
    page.locator("#edit-profile-dialog").get_by_role("button", name="Save").click()

    # 4. Физические данные
    page.get_by_text("Height Not Given").click()
    page.get_by_role("link", name="1.81m").click()

    page.get_by_text("Weight Not Given").click()
    page.get_by_role("link", name="62kg").click()

    page.get_by_text("Eye colour Not Given").click()
    page.get_by_role("link", name="Blue").click()

    page.get_by_text("Smoking habits Not Given").click()
    page.get_by_role("link", name="No", exact=True).click()

    # 5. Интересы
    page.get_by_role("button", name="Add").click()
    page.get_by_text("69", exact=True).click()
    page.get_by_text("Anal").click()
    page.locator("#edit-interests-dialog").get_by_role("button", name="Save").click()