from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parent
AUTH_STATE = PROJECT_ROOT / "auth" / "user.json"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "no_auth: run this test without saved authentication state",
    )


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    if not AUTH_STATE.exists():
        return browser_context_args

    return {
        **browser_context_args,
        "storage_state": str(AUTH_STATE),
    }


@pytest.fixture
def page(request, browser_context_args):
    if request.node.get_closest_marker("no_auth"):
        browser = request.getfixturevalue("browser")
        context = browser.new_context()
    else:
        if not AUTH_STATE.exists():
            pytest.fail(
                "Missing auth/user.json. "
                "Create it once with: playwright codegen --save-storage=auth/user.json "
                "https://dashboard4.nx-sandbox.com"
            )
        browser = request.getfixturevalue("browser")
        context = browser.new_context(**browser_context_args)

    page = context.new_page()
    yield page
    context.close()
