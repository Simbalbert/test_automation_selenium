# Test Plan – Portfolio Link Tests (ITLDO801 Assignment 3, Task 1)

**Site under test:** my portfolio (multi-page site: index, about, portfolio, services, contact)  
**Tool:** Selenium WebDriver (Python) with Chrome  
**Repository:** https://github.com/Simbalbert/test_automation_selenium

## Test cases

| Test ID | What is tested | Steps | Expected result |
|---|---|---|---|
| TC-01 | Home page loads | 1. Open the portfolio home page. | Page opens and the page title / main heading is displayed |
| TC-02 | "ABOUT" menu link | 1. Open the home page. 2. Click "ABOUT". | URL ends with `about.html` |
| TC-03 | "PORTFOLIO" menu link | 1. Open the home page. 2. Click "PORTFOLIO". | URL ends with `portfolio.html` |
| TC-04 | "SERVICES" menu link | 1. Open the home page. 2. Click "SERVICES". | URL ends with `services.html` |
| TC-05 | "CONTACT" menu link | 1. Open the home page. 2. Click "CONTACT". | URL ends with `contact.html` |
| TC-06 | External link (e.g. LinkedIn / GitHub) | 1. Open the home page. 2. Click the external link. 3. Switch to the new tab. | New tab opens and URL contains the expected domain |
| TC-07 (negative) | Link "NonExistentPage" (missing on purpose) | 1. Open the home page. 2. Try to click "NonExistentPage". | Test FAILS and is logged as ERROR with message, URL and screenshot |

## Pass / fail rules

- A test **passes** only when the expected result is verified (URL or visible element), not just because the click worked.
- Each test starts from the home page so tests do not affect each other.
- TC-07 is a **negative test**: it is expected to fail, to prove that failures are detected and logged correctly.
- The run continues after a failed test.

## Logging expectations

- A new timestamped log file is created in `logs/` on every run.
- Run header: site, browser and version, operating system.
- Each test: ID, description, expected, actual, PASS/FAIL, duration.
- Levels: INFO (progress/pass), WARNING (unusual, e.g. slow page), ERROR (failure, with message, URL and screenshot).
- Run summary: total, passed, failed, total duration.
