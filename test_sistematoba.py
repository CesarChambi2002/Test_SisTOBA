from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Chrome()

#driver.maximize_window()

#driver.get('http://localhost/Ventas/login/')
#time.sleep(2)
#driver.find_element(By.XPATH, "//input[@name='email']").send_keys("grover@gmail.com")
#time.sleep(2)
#driver.find_element(By.XPATH, "//input[@name='password_user']").send_keys("12345678")
   
class TestInterfaz:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/Ventas/login/')
    
    def teardown_method(self):
        self.driver.quit()
        print("Prueba Visual completada")
    
    time.sleep(2)
    def test_verify_contenido_inicio(self):
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class,'card-header text-center')]//b").text 
        esperada = "Sistema de Ventas"  
        assert esperada in actual, f"Error. actual {actual}, esperado: {esperada}"
        time.sleep(2)
    
    def test_insertar_usuario_contrasena(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("grover@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='password_user']").send_keys("12345678")
        #continuara.....