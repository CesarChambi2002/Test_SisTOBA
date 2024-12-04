import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options


class TestRegistrarProducto:
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

    def teardown(self):
        self.driver.quit()

    def test_registrar_producto(self):
        self.driver.find_element(By.ID, "edtUsuario").send_keys("grover@gmail.com")
        self.driver.find_element(By.ID, "edtPassword").send_keys("12345678")
        self.driver.find_element(By.ID, "btnLogin").click()

        time.sleep(5)  
        self.driver.find_element(By.ID, "btnIrProductos").click()

        time.sleep(1)
        self.driver.find_element(By.ID, "spnCategorias").click()
        self.driver.find_element(By.XPATH, "//android.widget.CheckedTextView[@text='TECLADOS']").click()

        self.driver.find_element(By.ID, "edtNombre").send_keys("Producto de Prueba")
        self.driver.find_element(By.ID, "edtDescripcion").send_keys("Descripción de prueba")
        self.driver.find_element(By.ID, "edtStock").send_keys("10")
        self.driver.find_element(By.ID, "edtStockMin").send_keys("1")
        self.driver.find_element(By.ID, "edtStockMax").send_keys("20")
        self.driver.find_element(By.ID, "edtPrecioCompra").send_keys("100.50")
        self.driver.find_element(By.ID, "edtPrecioVenta").send_keys("150.75")

        self.driver.find_element(By.ID, "btnGuardarProducto").click()

        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "//android.widget.Toast[1]").text

        assert toast_message == "Producto registrado correctamente.", "Sin exito"
