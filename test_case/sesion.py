from selenium.webdriver.common.by import By
import time


def insertar_usuario_contrasena(driver):
    # metodo para ingresar uaurio y contraseña mas click
    
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("grover@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@name='password_user']").send_keys("12345678")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
    time.sleep(2)