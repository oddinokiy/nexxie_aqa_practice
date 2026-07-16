from playwright.sync_api import Page


def test_user_can_update_profile_information(page: Page):

    page.goto("https://dashboard4.nx-sandbox.com/#/session/search")

    # Open the profile.
    page.get_by_text("nik", exact=True).click()

    # Click the edit icon
    page.locator(".edit-icon").first.click()

    # Update date of birth.
    page.get_by_text("Day 13").click()
    page.get_by_role("link", name="10").click()

    page.get_by_text("Month 9").click()
    page.get_by_role("link", name="5").click()

    page.get_by_text("Year 1992").click()
    page.get_by_role("link", name="1995").click()

    # Update location.
    page.locator("span").filter(has_text="UK").first.click()
    page.get_by_role("link", name="Spain").click()

    # Scope Save to the profile dialog to avoid strict-mode conflicts.
    page.locator("#edit-profile-dialog").get_by_role("button", name="Save").click()

    # Update physical attributes.
    page.locator("#height").click()
    page.get_by_role("link", name="1.81m").click()

    page.locator("#weight").click()
    page.get_by_role("link", name="62kg").click()

    page.locator("#eyeColor").click()
    page.get_by_role("link", name="Blue").click()

    page.locator("#smokingHabits").click()
    page.get_by_role("link", name="No", exact=True).click()

    # Update interests.
    page.get_by_role("button", name="Add").click()
    page.get_by_text("69", exact=True).click()
    page.get_by_text("Anal").click()

    # Scope Save to the interests dialog when several buttons are present.

    # Save interests
    page.locator("#edit-interests-dialog").get_by_role("button", name="Save").click()
