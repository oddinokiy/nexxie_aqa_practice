import re

from playwright.sync_api import Page, expect


def test_reg_update(page:Page):
    username = "userok21"
    email = "tyisocxq4iyxb-ryge@replyloop.com"  # Change email before each test run
    password = "21212121"
    city = "London"
    message = " Hi, how are u?"

    page.goto("https://dashboard4.nx-sandbox.com/")
    page.get_by_label("Username:").fill(username)
    page.get_by_label("Email:").fill(email)
    page.get_by_label("Password:").fill(password)


    page.get_by_text("DD").click()
    page.get_by_role("link", name="1", exact=True).click()           # что значит exact=True?
    page.get_by_text("MM").click()
    page.get_by_role("link", name="7", exact=True).click()
    page.get_by_text("YYYY").click()
    page.get_by_role("link", name="1999").click()

    page.locator("[name='location']").click() # еще раз потом разобраться почему так
    page.get_by_role("textbox").fill(city)
    page.get_by_role("option", name=city, exact=True).click()

    page.get_by_role("checkbox").check()
    #связывание (Chaining). через точку
    page.locator("form").get_by_role("button", name= "Register").click()


    # Теперь эта штука будет работать как невидимый телохранитель твоего теста на протяжении всего сценария.
    # Если попап вылезет — Playwright сам его закроет и продолжит тест.
    # Если не вылезет — тест просто пройдет мимо, ничего не заметив.
    no_thx_button = page.get_by_role("button", name="No Thanks")
    page.add_locator_handler(no_thx_button,lambda: no_thx_button.click())

    page.get_by_text("Chat", exact=True).click()
    page.get_by_text("Verify your email", exact=True).click()
    page.get_by_role("button", name="Verify").click()

    page.pause()
    page.reload()

    page.get_by_title("Browse").click()
    expect(page).to_have_url(re.compile(r".*/#/session/search"), timeout=15000)

    page.locator(".profile-details").first.click()
    page.locator(".profile-details").first.get_by_title("Chat").click()

    page.get_by_placeholder("Your Message").fill(message)
    page.locator(".send-btn").click()

    # Проверка: наше сообщение появилось в контейнере чата
    chat_container = page.locator("#chat-msg-list-container")
    expect(chat_container.get_by_text(message, exact=True)).to_be_visible(timeout=10000)







