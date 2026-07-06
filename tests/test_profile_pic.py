from pathlib import Path
from playwright.sync_api import Page, expect


def test_upload_photo(page: Page):
    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    page.get_by_text("nik See your profile").click()

    # Пауза, чтобы глазами увидеть страницу профиля
    page.wait_for_timeout(2000)

    photo_path = Path("tests/files/dog.png").resolve()

    # Загружаем файл в первый input type=file
    page.locator("input[type='file']").nth(0).set_input_files(str(photo_path))

    # Пауза, чтобы увидеть, появилось ли превью/кнопка
    page.wait_for_timeout(3000)

    # Если появилась кнопка Upload Photo, нажимаем её
    page.get_by_role("button", name="Upload Photo").click()

    # Пауза после загрузки
    page.wait_for_timeout(3000)