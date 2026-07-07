

from pathlib import Path
from playwright.sync_api import Page, expect


def test_upload_photo(page: Page):

    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    # Navigate to the user profile via the side menu
    page.locator(".profile-area").click()

    # Pause to visually check the profile page
    page.wait_for_timeout(2000)

    # перед показом поменять фотку чтобы было видно что новая фотка закинута
    # Get the absolute path to the image file
    photo_path = Path("tests/files/dog.png").resolve()

    # Upload the photo directly into the hidden file input
    # Note: Playwright bypasses the OS file dialog, so no physical click is visible here
    page.locator("input[type='file']").first.set_input_files(str(photo_path))

    # Pause to let the image preview load on the UI
    page.wait_for_timeout(3000)

    # Confirm the upload by clicking the UI button
    page.get_by_role("button", name="Upload Photo").click()

    # Final pause to visually verify the successful upload
    page.wait_for_timeout(3000)