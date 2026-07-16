# QA Automation Test Cases Archive

This file is a personal archive of QA automation practice cases for future CV,
portfolio, and interview use.

New cases should be added here over time instead of replacing older ones. The
main README can describe the current project, while this file keeps the full
case history.

Project: Nx Sandbox Dashboard

Tech stack: Python, Pytest, Playwright

Base URL: `https://dashboard4.nx-sandbox.com`

---

## Case Index

| ID | Case | Status | Test File |
| --- | --- | --- | --- |
| TC-001 | Logged-in user can access profile page | Automated | `tests/test_authenticated_session.py` |
| TC-002 | Logged-in user can upload profile photo | Automated | `tests/test_profile_pic.py` |
| TC-003 | Logged-in user can buy coins | Automated | `tests/test_buy_coins.py` |
| TC-004 | New unverified user can delete account | Automated | `tests/test_delete_account.py` |
| TC-005 | Deleted user cannot sign in | Automated | `tests/test_deleted_account_login.py` |
| TC-006 | Deleted email can be used for new registration | Automated | `tests/test_deleted_email_registration.py` |
| TC-007 | Existing user can sign in and send chat message | Automated | `tests/test_sign_in_chat.py` |
| TC-008 | New registered user can verify email and send message | Manual verification | `tests/test_registration_chat.py` |
| TC-009 | New verified user can open chat from Browse page | Manual verification | `tests/test_registration_open_chat.py` |
| TC-010 | Empty chat message cannot be sent | Manual verification | `tests/test_empty_message.py` |
| TC-011 | Logged-in user can update profile information | Automated | `tests/test_user_info.py` |
| TC-012 | Logged-in user can purchase incognito subscription | Payment sandbox | `tests/test_subscription.py` |

---

## How to Add New Cases

When a new task is completed, add it as the next case number:

```text
TC-012 - Case Name
```

Use the same structure:

- Priority
- Type
- Status
- Test file
- Preconditions
- Steps
- Expected result
- Automation notes

This keeps the file clean and easy to reuse for CV explanations.

---

## TC-001 - Logged-In User Can Access Profile Page

Priority: High

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_authenticated_session.py
```

Preconditions:

- User already has a valid account.
- Logged-in browser session is saved in `auth/user.json`.

Steps:

1. Open `https://dashboard4.nx-sandbox.com/#/session/search`.
2. Check that the internal search page is opened.
3. Click the profile area.
4. Check that the profile edit page is opened.

Expected result:

- User can access the internal dashboard page.
- Profile edit page is available for the logged-in user.

Automation notes:

- The test uses saved authentication state from `auth/user.json`.
- The test does not repeat login or registration steps.

---

## TC-002 - Logged-In User Can Upload Profile Photo

Priority: Medium

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_profile_pic.py
```

Preconditions:

- User already has a valid account.
- Logged-in browser session is saved in `auth/user.json`.

Steps:

1. Open `https://dashboard4.nx-sandbox.com/#/session/search`.
2. Click `Settings`.
3. Click `Account`.
4. Create a temporary PNG image file.
5. Upload the image through the file input.
6. Check that the page shows a success result.

Expected result:

- Profile photo upload is accepted by the application.
- User sees a visible success or saved state after upload.

Automation notes:

- The test creates a small PNG file during runtime.
- The upload uses `input[type='file']`.
- The final assertion checks a visible UI result, not only file selection.

---

## TC-003 - Logged-In User Can Buy Coins

Priority: High

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_buy_coins.py
```

Preconditions:

- User already has a valid account.
- Logged-in browser session is saved in `auth/user.json`.
- Test payment card data is available.

Steps:

1. Open `https://dashboard4.nx-sandbox.com`.
2. Click `My Wallet`.
3. Select the `Intro 200 Coins` package.
4. Fill cardholder name.
5. Fill test card number.
6. Fill expiry date.
7. Fill CVC.
8. Uncheck saved card option.
9. Click `Confirm & Pay`.
10. Check that `Start Chatting` is visible.

Expected result:

- Payment flow is completed successfully with test card data.
- Application shows the `Start Chatting` button after purchase.

Automation notes:

- The test validates the full coin purchase flow from wallet to confirmation.
- The final assertion checks the visible post-payment state.

---

## TC-004 - New Unverified User Can Delete Account

Priority: High

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_delete_account.py
```

Preconditions:

- New unique user data is available.
- The public registration page is available.

Steps:

1. Open `https://dashboard4.nx-sandbox.com`.
2. Register a new unverified user.
3. Wait until the internal dashboard page is opened.
4. Open `Settings`.
5. Open `Account`.
6. Click `Delete My Account`.
7. Fill required password and feedback fields.
8. Confirm account deletion.
9. Wait for the `Account deleted` confirmation.
10. Close the confirmation modal.
11. Check that the public `Join for free` page is visible.

Expected result:

- New unverified user account is deleted successfully.
- User is redirected back to the public page.
- `Join for free` is visible after deletion.

Automation notes:

- Use unique username and email values for every run.
- Wait for the real public-page end state before continuing.
- Prefer readable Playwright locators such as `get_by_role` and `get_by_text`.

---

## TC-005 - Deleted User Cannot Sign In

Priority: High

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_deleted_account_login.py
```

Preconditions:

- A user account was created and deleted during the same test flow.
- Deleted user's email and password are still available in test data.

Steps:

1. Complete account deletion flow.
2. Wait until the public `Join for free` page is visible.
3. Open `https://dashboard4.nx-sandbox.com/#/signin`.
4. Fill deleted user's email.
5. Fill deleted user's password.
6. Click `Sign In`.
7. Check the visible error message.

Expected result:

- Deleted user cannot sign in.
- Application shows `Username/password combination not found`.

Automation notes:

- Do not rely only on URL assertions after sign-in.
- Validate the visible error text to prove the negative login result.
- Wait for the post-deletion redirect before opening the sign-in page.

---

## TC-006 - Deleted Email Can Be Used For New Registration

Priority: High

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_deleted_email_registration.py
```

Preconditions:

- New user data is available.
- The same email can be reused after the previous account is deleted.

Steps:

1. Open `https://dashboard4.nx-sandbox.com`.
2. Register the first user with a new email.
3. Check that registration succeeds.
4. Open account settings.
5. Delete the first account.
6. Open the registration page again.
7. Register a second user with the same email.
8. Check that the second registration succeeds.

Expected result:

- Email from a deleted account can be used again for registration.
- Second registration opens the internal dashboard page.

Automation notes:

- The test validates account deletion cleanup from the registration side.
- The test uses the same email after deleting the first account.

---

## TC-007 - Existing User Can Sign In And Send Chat Message

Priority: High

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_sign_in_chat.py
```

Preconditions:

- Existing user credentials are available.
- Browse page contains at least one user profile.

Steps:

1. Open `https://dashboard4.nx-sandbox.com`.
2. Open the sign-in form.
3. Fill username and password.
4. Submit the sign-in form.
5. Open the Browse page.
6. Open the first user profile.
7. Open chat with this user.
8. Send a message.
9. Check that the sent message is visible in chat.

Expected result:

- Existing user can sign in successfully.
- User can open chat and send a visible message.

Automation notes:

- This test covers a real end-to-end login and chat flow.
- The final assertion checks the message inside the chat container.

---

## TC-008 - New Registered User Can Verify Email And Send Message

Priority: High

Type: E2E automated test with manual email verification step

Status: Automated with manual checkpoint

Test file:

```bash
tests/test_registration_chat.py
```

Preconditions:

- New unique user data is available.
- Email verification can be completed manually during the test.

Steps:

1. Open `https://dashboard4.nx-sandbox.com`.
2. Fill the registration form.
3. Submit registration.
4. Open the email verification chat.
5. Click `Verify`.
6. Complete email verification manually.
7. Reload the page.
8. Open Browse.
9. Open the first user profile.
10. Open chat.
11. Send a message.
12. Check that the sent message is visible.

Expected result:

- New user can register, verify email, open chat, and send a message.
- Sent message appears in the chat container.

Automation notes:

- The test includes `page.pause()` for manual email confirmation.
- It contains recovery logic if the Browse page stays in a loading state.

---

## TC-009 - New Verified User Can Open Chat From Browse Page

Priority: Medium

Type: E2E automated test with manual email verification step

Status: Automated with manual checkpoint

Test file:

```bash
tests/test_registration_open_chat.py
```

Preconditions:

- New unique user data is available.
- Email verification can be completed manually during the test.

Steps:

1. Register a new user.
2. Open email verification chat.
3. Click `Verify`.
4. Complete email verification manually.
5. Reload the page.
6. Open Browse.
7. Open the first user profile.
8. Click Chat.
9. Check that the message input is visible.

Expected result:

- Verified user can open chat from the Browse page.
- Chat message input is visible.

Automation notes:

- This case focuses on chat opening, not message sending.
- It includes loading-state recovery for the Browse page.

---

## TC-010 - Empty Chat Message Cannot Be Sent

Priority: Medium

Type: E2E automated test with manual email verification step

Status: Automated with manual checkpoint

Test file:

```bash
tests/test_empty_message.py
```

Preconditions:

- New unique user data is available.
- Email verification can be completed manually during the test.
- User can open chat with another profile.

Steps:

1. Register a new user.
2. Complete email verification manually.
3. Open Browse.
4. Open the first user profile.
5. Open chat.
6. Leave the message field empty.
7. Try to send the message.
8. Check that the Send button is disabled.

Expected result:

- Empty chat message is not sent.
- Send action is blocked for an empty message.

Automation notes:

- This is a negative validation case for chat input.
- The final assertion checks the disabled state of the Send button.

---

## TC-011 - Logged-In User Can Update Profile Information

Priority: Medium

Type: E2E automated test

Status: Automated

Test file:

```bash
tests/test_user_info.py
```

Preconditions:

- User is already logged in.
- Logged-in browser session is available.

Steps:

1. Open the internal search page.
2. Open the user profile.
3. Click the profile edit icon.
4. Update date of birth.
5. Update location.
6. Save profile changes.
7. Update physical attributes.
8. Update interests.
9. Save interest changes.

Expected result:

- Profile information can be edited and saved.
- Interest changes can be edited and saved.

Automation notes:

- The test uses scoped locators for Save buttons to avoid strict mode conflicts.
- The test covers several profile edit sections in one logged-in flow.

---

## TC-012 - Logged-In User Can Purchase Incognito Subscription

Priority: Medium

Type: E2E sandbox payment test

Status: Automated and excluded from default CI execution

Test file:

```bash
tests/test_subscription.py
```

Preconditions:

- User is already logged in.
- Logged-in browser session is available.
- Sandbox payment form is enabled.

Steps:

1. Open the internal search page.
2. Open the user profile.
3. Select the incognito subscription.
4. Fill the sandbox card details.
5. Confirm the payment.
6. Check that the post-payment action is available.

Expected result:

- Sandbox payment is accepted.
- `Start Exploring` is visible after confirmation.

Automation notes:

- The scenario is marked `payment` to prevent accidental execution on every push.
- The final assertion verifies the visible post-payment state.
