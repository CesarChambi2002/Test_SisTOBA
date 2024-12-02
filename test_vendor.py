import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

class TestLogin:
    def setup(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "14"
        options.device_name = "R5CT303H0VA"
        options.automation_name = "UiAutomator2"
        options.app = r"C:\Users\conra\AdministradorTOBA\app\build\outputs\apk\debug\app-debug.apk"
        options.app_package = "com.example.administradortoba"
        options.app_activity = "com.example.administradortoba.LoginActivity"
        options.uiautomator2_server_install_timeout = 60000  

        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
        self.wait = WebDriverWait(self.driver, 20)
    
    def salir(self):
        self.driver.quit()

    def test_login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "edtUsuario"))).send_keys("grover@gmail.com")
        self.wait.until(EC.presence_of_element_located((By.ID, "edtPassword"))).send_keys("12345678")
        self.wait.until(EC.presence_of_element_located((By.ID, "btnLogin"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "btnCerrarSesion"))).click()
