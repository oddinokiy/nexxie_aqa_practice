from pathlib import Path

import allure
import pytest


PROJECT_ROOT = Path(__file__).resolve().parent
AUTH_STATE = PROJECT_ROOT / "auth" / "user.json"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Add saved authentication state when it is available."""
    if not AUTH_STATE.exists():
        return browser_context_args

    return {
        **browser_context_args,
        "storage_state": str(AUTH_STATE),
    }


@pytest.fixture
def page(request, browser_context_args):
    """Create either a clean or authenticated Playwright page."""
    browser = request.getfixturevalue("browser")

    if request.node.get_closest_marker("no_auth"):
        context = browser.new_context()
    else:
        if not AUTH_STATE.exists():
            pytest.fail(
                "Missing auth/user.json. Create a saved session as described in README.md."
            )
        context = browser.new_context(**browser_context_args)

    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach a full-page screenshot to Allure when a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed or "page" not in item.fixturenames:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    allure.attach(
        page.screenshot(full_page=True),
        name="screenshot_on_failure",
        attachment_type=allure.attachment_type.PNG,
    )
