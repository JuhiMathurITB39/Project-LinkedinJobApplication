import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables
load_dotenv()

ACCOUNT_EMAIL = os.getenv("LINKEDIN_EMAIL")
ACCOUNT_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
PHONE = os.getenv("PHONE_NUMBER")

def abort_application():
    """Close the application pop-up and discard progress if it's a complex application."""
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    close_button.click()
    time.sleep(2)
    discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps browser open after script ends

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to LinkedIn Jobs
driver.get("https://www.linkedin.com/jobs/search/?keywords=Python%20Developer&location=India")

# Handle cookie pop-up
time.sleep(2)
try:
    reject_button = driver.find_element(By.CSS_SELECTOR, 'button[action-type="DENY"]')
    reject_button.click()
except NoSuchElementException:
    print("No cookie pop-up found, continuing...")

# Sign in
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Wait for manual CAPTCHA verification
input("Press Enter when you have solved the CAPTCHA...")

# Get job listings
time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

# Apply for jobs
for listing in all_listings:
    print("Opening job listing...")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Skipped complex application.")
            continue
        else:
            print("Submitting job application...")
            submit_button.click()

        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
