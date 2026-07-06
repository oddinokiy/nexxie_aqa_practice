# 🧪 E2E Test Automation — Chat Application (Playwright)

This repository contains End-to-End (E2E) automated tests for a web-based chat application using **Playwright (Python)**.

The goal of this test suite is to validate critical user journeys such as registration, email verification, messaging, and account deletion.

---

# 📌 Test Coverage Overview

The test suite covers **4 main business flows**:

---

## 🟢 1. Registration + Chat Success Flow

This flow validates that a new user can successfully register, verify email, and interact in chat.

**Steps:**
- Open site
- Register user
- Verify email
- Navigate to Browse page
- Open user profile
- Open chat
- Send message
- Validate message is visible

---

## 🔴 2. Registration Negative Flows

This flow ensures the system correctly handles invalid or duplicate registration attempts.

**Scenarios:**
- Register with existing email → ❌ Expected failure
- Register with invalid or empty fields → ❌ Expected failure

---

## 🔵 3. Delete Account Flow

This flow validates account lifecycle behavior after deletion.

**Steps:**
- Register user
- Delete account
- Attempt login after deletion → ❌ Should fail
- Re-register with same email → behavior depends on system rules

---

## 🟣 4. Messaging Validation Flow

This flow ensures messaging rules are enforced correctly.

**Scenario:**
- Attempt to send an empty message → ❌ Message should NOT be sent

---

# 🧠 System Behavior Summary

- Users must register and verify email before accessing chat features
- Deleted accounts should no longer be able to log in
- The system prevents sending empty messages
- Duplicate or invalid registrations are rejected

---

# 📊 Visual Representation

A visual E2E flow diagram is available below:

👉 (insert Mermaid diagram here or link to mermaid.live export)

---

# 🛠 Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM structure recommended)

---

# 🔐 Saved Authentication State

Most tests can start already logged in by using Playwright `storageState`.

Create the saved login state once:

```bash
playwright codegen --save-storage=auth/user.json https://dashboard4.nx-sandbox.com
```

In the opened browser, log in manually with an existing user account, then close the browser.

After that, normal tests that use the `page` fixture will start with this authenticated session.

Important:
- Do not put login or registration steps into tests that only check internal pages.
- Keep registration, sign-in, and delete-account tests marked with `@pytest.mark.no_auth`, because those scenarios need a clean public session.
- `auth/user.json` is ignored by Git because it contains private session data.

---

# 🎯 Purpose of this Project

This project demonstrates:

- E2E automation design skills
- Real user journey validation
- QA system thinking (not just test scripting)
- Ability to translate test cases into business logic

---

# 📌 Notes

- All tests are designed to simulate real user behavior
- Some scenarios are expected failures (negative testing)
- Focus is on system reliability and user flow correctness

---

# 🚀 Author

QA Automation Engineer (Intern)
