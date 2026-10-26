import os
import platform
import time
from datetime import datetime
from includes import functions
from includes import constants

# 1. Setup /logs/ folder and session log file
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

session_time = datetime.now()
timestamp_str = session_time.strftime("%Y-%m-%d_%H-%M-%S")
log_filepath = os.path.join(LOGS_DIR, f"test_run_{timestamp_str}.log")

def log(level, message):
    """Writes formatted entry to console and log file."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{now_str} | {level:<5} | {message}\n"
    print(entry.strip())
    with open(log_filepath, "a", encoding="utf-8") as f:
        f.write(entry)

# Array of tests (including the negative test)
text_url_array = {
   # constants.HOME_TEXT: constants.HOME_URL,
    constants.ABOUT_TEXT: constants.ABOUT_URL,
    constants.PORTFOLIO_TEXT: constants.PORTFOLIO_URL,
    constants.SERVICES_TEXT: constants.SERVICES_URL,
    constants.CONTACT_TEXT: constants.CONTACT_URL,
    constants.MISSING_TEXT: constants.MISSING_URL  # Negative test
}

# 2. RUN START Header
run_start_time = time.time()
browser_version = functions.driver.capabilities.get("browserVersion", "Chrome")
os_info = f"{platform.system()} {platform.release()}"

log("INFO", f"RUN START | portfolio: {constants.TEST_URL} | browser: Chrome {browser_version} | OS: {os_info}")

passed_count = 0
failed_count = 0

# 3. Loop through and run each test
for test_name, test_url in text_url_array.items():
    test_id = constants.TEST_IDS.get(test_name, "TC-00")

    status, expected, actual, duration, screenshot = functions.test_click_item(
        constants.TEST_URL, test_url, test_name, test_id
    )

    if status == "PASS":
        passed_count += 1
        log("INFO", f"{test_id} | Click \"{test_name}\" | expected: {expected} | actual: {actual} | PASS | {duration}")
    else:
        failed_count += 1
        extra = f" | screenshot: {screenshot}" if screenshot else ""
        log("ERROR", f"{test_id} | Click \"{test_name}\" | expected: {expected} | actual: {actual} | FAIL | {duration}{extra}")

# 4. RUN END Summary
total_duration = f"{time.time() - run_start_time:.1f} s"
total_tests = passed_count + failed_count
log("INFO", f"RUN END | total: {total_tests} | passed: {passed_count} | failed: {failed_count} | duration: {total_duration}")

functions.close_browser()
print(f"\nTest finished! Log file written to: {log_filepath}")