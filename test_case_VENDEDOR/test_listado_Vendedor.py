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

    def test_interaccion_productos_clientes(self):
        self.driver.find_element(By.NAME, "email").send_keys("grover@gmail.com")
        self.driver.find_element(By.NAME, "password_user").send_keys("12345678")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Ingresar')]").click()
        time.sleep(2)
        self.driver.get("http://localhost/Ventas/ventas/")
        time.sleep(2)

        productos_button = self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-primary') and contains(.,'Productos')]")
        productos_button.click()
        time.sleep(1)

        cerrar_modal_productos = self.driver.find_element(By.XPATH, "//div[@class='modal fade show']//button[@class='close']")
        cerrar_modal_productos.click()
        time.sleep(1)

        cliente_button = self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-warning')]")
        cliente_button.click()
        time.sleep(1)

        cerrar_modal_clientes = self.driver.find_element(By.XPATH, "//div[@class='modal fade show']//button[@class='close']")
        cerrar_modal_clientes.click()
        time.sleep(1)

    def test_interaccion_botones_acciones(self):
        self.driver.find_element(By.NAME, "email").send_keys("grover@gmail.com")
        self.driver.find_element(By.NAME, "password_user").send_keys("12345678")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Ingresar')]").click()
        time.sleep(2)
        self.driver.get("http://localhost/Ventas/ventas/")
        time.sleep(2)

        ver_button = self.driver.find_element(By.XPATH, "//td/a[contains(@class,'btn-info')]")
        ver_button.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        borrar_button = self.driver.find_element(By.XPATH, "//td/a[contains(@class,'btn-danger')]")
        borrar_button.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        imprimir_button = self.driver.find_element(By.XPATH, "//td/a[contains(@class,'btn-success')]")
        imprimir_button.click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def test_buscar_y_eliminar_texto(self):
        self.driver.find_element(By.NAME, "email").send_keys("grover@gmail.com")
        self.driver.find_element(By.NAME, "password_user").send_keys("12345678")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Ingresar')]").click()
        time.sleep(2)

        self.driver.get("http://localhost/Ventas/ventas/")
        time.sleep(2)

        buscador = self.driver.find_element(By.XPATH, "//input[@type='search']")
        buscador.send_keys("700")
        time.sleep(2)

        buscador.clear()
        time.sleep(2)
