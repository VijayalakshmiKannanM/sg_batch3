from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
base_url = "https://the-internet.herokuapp.com"

# 1. Test Login Page
driver.get(f"{base_url}/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
assert "You logged into a secure area!" in driver.page_source

# 2. Test Checkboxes
driver.get(f"{base_url}/checkboxes")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
assert all(cb.is_selected() for cb in checkboxes)

# 3. Test JavaScript Alerts
driver.get(f"{base_url}/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
Alert(driver).accept()
assert "You successfully clicked an alert" in driver.page_source

# 4. Test Dropdown
driver.get(f"{base_url}/dropdown")
dropdown = driver.find_element(By.ID, "dropdown")
dropdown.find_element(By.XPATH, "//option[text()='Option 2']").click()
selected = dropdown.find_element(By.XPATH, "//option[@selected='selected']")
assert selected.text == "Option 2"

# 5. Test File Upload
driver.get(f"{base_url}/upload")
upload_input = driver.find_element(By.ID, "file-upload")
upload_input.send_keys("C:/path/to/your/testfile.txt")  # Replace with a valid file path
driver.find_element(By.ID, "file-submit").click()
assert "File Uploaded!" in driver.page_source

# Cleanup
driver.quit()
