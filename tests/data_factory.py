from uuid import uuid4


def unique_account(email_domain: str) -> tuple[str, str, str]:
    """Return isolated test credentials for a single scenario run."""
    suffix = uuid4().hex[:8]
    username = f"qa{suffix}"
    email = f"qa_{suffix}@{email_domain}"
    password = "TestPass2121!"
    return username, email, password
