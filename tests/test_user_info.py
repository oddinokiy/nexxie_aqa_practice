from playwright.sync_api import Page


def test_update_profile(page: Page):

    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    #Open the profile
    page.get_by_text("nik", exact=True).click()

    # Click the edit icon
    page.locator(".edit-icon").first.click()

    # Выбираем конкретное число
    # Используем link/"option", потому что в коде у элемента стоит role= link/"option",
    # так как на сайте тип есть выбор по DOM

    #Update Date of Birth
    #Expand the dropdowns and select the exact values.
    page.get_by_text("Day 13").click()
    page.get_by_role("link", name="10").click()

    page.get_by_text("Month 9").click()
    page.get_by_role("link", name="5").click()

    page.get_by_text("Year 1992").click()
    page.get_by_role("link", name="1995").click()

    # 3 Update location
    page.locator("span").filter(has_text="UK").first.click()  # забей тут просто через codegen
    page.get_by_role("link", name="Spain").click()

    # Сохраняем основную инфу
    # Ищем "Save" строго внутри окна профиля (через ID родителя #edit-profile-dialog).
    page.locator("#edit-profile-dialog").get_by_role("button", name="Save").click() 

    # Update Physical Attributes
    page.locator("#height").click()
    page.get_by_role("link", name="1.81m").click()

    page.locator("#weight").click()
    page.get_by_role("link", name="62kg").click()

    page.locator("#eyeColor").click()
    page.get_by_role("link", name="Blue").click()

    page.locator("#smokingHabits").click()
    page.get_by_role("link", name="No", exact=True).click()

    #Update Interests
    page.get_by_role("button", name="Add").click()
    page.get_by_text("69", exact=True).click()
    page.get_by_text("Anal").click()

    # Ищем "Save" строго внутри окна интересов (через ID родителя #edit-interests-dialog).
    # Чейнинг нужен, чтобы не словить strict mode error, если кнопок Save на сайте несколько.

    # Save interests
    page.locator("#edit-interests-dialog").get_by_role("button", name="Save").click()
