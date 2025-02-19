import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestFraud:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Modern headless mode
        options.add_argument("--no-sandbox")    # Required for server environments
        options.add_argument("--disable-dev-shm-usage")  # Avoids memory issues
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_fraud(self):
        self.driver.get("https://browser.lol/create")
        self.driver.set_window_size(1552, 832)
        self.driver.switch_to.frame(0)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".antipasto"))
        ).click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("http://testingimp.great-site.net")
        self.driver.find_element(By.CSS_SELECTOR, ".card").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

def run_indefinitely():
    while True:
        try:
            # Create a new instance of the test class
            test_instance = TestFraud()
            test_instance.setup_method(None)
            test_instance.test_fraud()
            test_instance.teardown_method(None)
            print("Test completed successfully. Waiting for 12 minutes before restarting...")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Wait for 12 minutes (720 seconds) before restarting
            time.sleep(720)

if __name__ == "__main__":
    run_indefinitely()
