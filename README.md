# Playwright E2E Test Automation

[![Playwright checks](https://github.com/oddinokiy/nexxie_aqa_practice/actions/workflows/playwright.yml/badge.svg)](https://github.com/oddinokiy/nexxie_aqa_practice/actions/workflows/playwright.yml)

Portfolio project with **12 end-to-end UI test scenarios** for a web-based social and chat platform. The suite covers critical user journeys, negative checks, authenticated flows, and sandbox payment scenarios.

## What is covered

| Area | Example scenarios |
| --- | --- |
| Authentication | Sign in, saved session, rejected login after account deletion |
| Registration | New user registration, email verification, reuse of a deleted email |
| Account lifecycle | Profile update, photo upload, account deletion |
| Messaging | Open chat, send a message, prevent an empty message |
| Sandbox payments | Purchase coins and an incognito subscription |

Detailed scenarios and expected results are documented in [docs/TEST_CASES.md](docs/TEST_CASES.md).

## Tech stack

- Python 3.11+
- Playwright
- Pytest and pytest-playwright
- Allure results with screenshots on failure
- GitHub Actions
- Page objects for reusable registration, profile, and chat actions

## Project structure

```text
.
├── .github/workflows/     # CI checks
├── auth/                  # Local storage state (JSON is not committed)
├── docs/                  # Test case documentation
├── pages/                 # Reusable page objects
├── tests/                 # E2E scenarios and test assets
├── conftest.py            # Browser context and Allure screenshot hook
├── pytest.ini             # Pytest configuration and markers
└── requirements.txt
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install --with-deps chromium
pytest --collect-only -q
```

Tests marked `manual_verification` pause for email confirmation. Tests marked `payment` use sandbox card data. Both groups are excluded from the default run. To run the remaining automated scenarios:

```bash
pytest -m "not manual_verification and not payment" --alluredir=allure-results
```

## Authenticated scenarios

Authenticated tests use Playwright storage state from `auth/user.json`. Create it locally:

```bash
playwright codegen --save-storage=auth/user.json https://dashboard4.nx-sandbox.com
```

The file can contain cookies and session data, so it is excluded from Git. CI reads the state from the `AUTH_USER_JSON` repository secret. Existing-user credentials are read from `NX_TEST_USERNAME` and `NX_TEST_PASSWORD`; they are never stored in the repository.

## CI

Every push to `main` installs the dependencies, executes the default non-manual and non-payment scenarios, and uploads Allure results as a workflow artifact. The workflow can also be started manually from GitHub Actions.

## Author

[Nikita Sharoiko-Shakhrai](https://www.linkedin.com/in/nikita-sharoiko-shakhrai-543aba267/) — QA Engineer focused on Python test automation.
