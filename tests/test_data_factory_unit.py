import re

from tests.data_factory import unique_account


def test_unique_account_returns_valid_email_and_strong_test_password():
    username, email, password = unique_account("example.test")

    assert username
    assert email == f"qa_{username.removeprefix('qa')}@example.test"
    assert re.fullmatch(r"qa_[a-f0-9]{8}@example\.test", email)
    assert len(password) >= 12
    assert any(character.isupper() for character in password)
    assert any(character.isdigit() for character in password)


def test_unique_account_generates_distinct_accounts():
    first = unique_account("example.test")
    second = unique_account("example.test")

    assert first[0] != second[0]
    assert first[1] != second[1]
