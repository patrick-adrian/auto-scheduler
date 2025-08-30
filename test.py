from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
CHROME_USER_DATA_DIR = os.path.expanduser("~/Library/Application Support/Google/Chrome")
SELENIUM_PROFILE = "Profile 1"

options = Options()
options.add_argument("--start-maximized")
options.add_argument(f"--user-data-dir={CHROME_USER_DATA_DIR}")
options.add_argument(f"--profile-directory={SELENIUM_PROFILE}")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-gpu")
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()
