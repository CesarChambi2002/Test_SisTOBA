from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

class TestSistemaVentas:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/Ventas/login/")

    def teardown_method(self):
        self.driver.quit()

    def test_login_exitoso(self):
        self.driver.find_element(By.NAME, "email").send_keys("grover@gmail.com")
        self.driver.find_element(By.NAME, "password_user").send_keys("12345678")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Ingresar')]").click()
        time.sleep(2)
        actual_url = self.driver.current_url
        esperada_url = "http://localhost/Ventas/index.php"
        assert esperada_url in actual_url
