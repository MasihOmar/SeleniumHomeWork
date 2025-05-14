import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestInvalidLogin(unittest.TestCase):
    def setUp(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        # Initialize the Chrome webdriver with automatic driver management
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(10)
        
    def test_invalid_login(self):
        # Open the login page
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        # Find username and password fields and submit button
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Enter incorrect credentials
        username_field.send_keys("incorrect_username")
        password_field.send_keys("incorrect_password")
        
        # Click login button
        login_button.click()
        
        # Wait for and verify the error message
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#flash"))
        )
        
        # Verify that the error message indicates invalid credentials
        self.assertIn("Your username is invalid!", error_message.text)
        
        # Add a delay so we can see the result
        time.sleep(3)  # Wait for 3 seconds before closing
        
    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
