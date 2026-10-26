# --- START OF FILE functions.py ---

import atexit
import os
import time
from urllib.parse import urljoin

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
atexit.register(driver.quit)


def test_click_item(test_url, target_url, itemname, test_id):
    start_time = time.time()
    expected_url = urljoin(test_url, target_url).rstrip("/")
    expected_desc = f"URL is {expected_url}"

    try:
        driver.get(test_url)

        normalized_name = " ".join(itemname.split()).upper()
        xpath = (
            "//nav//a[translate(normalize-space(.), "
            "'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')="
            f"'{normalized_name}']"
        )
        if normalized_name == "HOME":
            xpath = "//nav//a[contains(@class, 'navbar-brand')]"

        # Wait up to 5s so the negative test fails cleanly and quickly
        link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        link.click()

        WebDriverWait(driver, 5).until(
            lambda browser: browser.current_url.rstrip("/") == expected_url
        )

        duration = f"{time.time() - start_time:.1f} s"
        actual_desc = f"URL is {driver.current_url.rstrip('/')}"
        return "PASS", expected_desc, actual_desc, duration, None

    except (TimeoutException, WebDriverException) as err:
        duration = f"{time.time() - start_time:.1f} s"
        actual_desc = f"element not found or URL mismatch (current: {driver.current_url})"
        
        # Save screenshot for failed test in logs/ folder
        os.makedirs("logs", exist_ok=True)
        screenshot_filename = f"{test_id}_fail.png"
        driver.save_screenshot(os.path.join("logs", screenshot_filename))

        return "FAIL", expected_desc, actual_desc, duration, screenshot_filename


def close_browser():
    driver.quit()