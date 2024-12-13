from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Setting up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (Windows-specific)
chrome_options.add_argument("--no-sandbox")  # Required for running as root in Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

#loading particular driver of browser

chrome_driver = webdriver.Chrome()
#opening web url
#chrome_driver.get("https://portal.adhocnet.org/")
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)
#selenium can find the elements by id, name, classname, css, selector, xpath

chrome_driver.find_element(By.NAME,"name").send_keys("Admin_user")
time.sleep(1)
chrome_driver.find_element(By.NAME,"email").send_keys("Adminuser@12345")
time.sleep(2)
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("Hellocloud@123")
time.sleep(2)
chrome_driver.find_element(By.ID,"exampleCheck1").click()
dropdown = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
time.sleep(6)
dropdown.select_by_visible_text("Female")
time.sleep(1)
chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
time.sleep(2)
date_picker = chrome_driver.find_element(By.NAME,"bday")
date_picker.clear()
date_picker.send_keys("15-12-2024")
time.sleep(3)
submit_button = chrome_driver.find_element(By.XPATH, "//input[@value='Submit']")  # Replace with actual locator
submit_button.click()
time.sleep(2)
try:
    # Use By.CLASS_NAME to locate the success message by its class
    success_message = WebDriverWait(chrome_driver,5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'alert-success')]"))  
    )
    print("Success Message:", success_message.text)
except Exception as e:
    print("Error: Success message not found or an error occurred.", e)
#printing title
print("page title : ",chrome_driver.title)
#printng url
print("page url: ",chrome_driver.current_url)
#saving screenshot
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")
#closing the driver
chrome_driver.quit()
