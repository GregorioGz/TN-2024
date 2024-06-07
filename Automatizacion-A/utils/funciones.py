from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Importamos la clase Keys para poder usar las teclas especiales
from selenium.webdriver.chrome.service import Service as ChromeService
#driver = webdriver.chrome(executable_path= r"C:\Users\Usuario\Desktop\chromedriver\chromedriver.exe")
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
from config.credentials import *

class Selectores:
    agregar_carrito = (By.CSS_SELECTOR, "input.js-addtocart.js-prod-submit-form.btn.btn-primary.btn-block.mb-4.cart[value='Agregar al carrito'][data-store='product-buy-button'][data-component='product.add-to-cart']")
    ver_carrito = (By.CSS_SELECTOR, "a.js-modal-open.js-fullscreen-modal-open.btn.btn-link.ml-1.text-primary[data-toggle='#modal-cart'][data-modal-url='modal-fullscreen-cart']")
    iniciar_compra = (By.ID, "ajax-cart-submit-div")
    email_input = (By.ID, "contact.email")
    cp_input = (By.ID, "shippingAddress.zipcode")
    continuar_1 = (By.XPATH, "//div[@id='' and contains(@class, 'pull-right') and contains(@class, 'text-uppercase') and contains(@class, 'm-top-half') and contains(@class, 'm-bottom-half') and contains(@class, 'btn') and contains(@class, 'btn-primary') and contains(@class, 'btn-submit-step') and @data-testid='btnSubmitZipcode']")
class UtilidadesPruebas:
    """
    Clase que contiene las funcionalidades base para las pruebas automatizadas
    """
    def __init__(self, driver):
        self.driver = driver
        self.Selectores = Selectores

    def cargar_pagina(self, url):
        """
        Función que carga la página principal que definamos en nuestra prueba
        """
        print(f"Cargando la página {url}")
        self.driver.get(url)
        self.driver.maximize_window()
        print("Página cargada")
        # assert "login" in self.driver.current_url, "La página no se cargo correctamente"
        
    def esperar_por_los_elementos(self, localizador, timeout=10):
        """
        Función que espera por los elementos de la página
        """
        try:
            # Espere a que el elemento esté presente en el DOM y sea visible
            elemento = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(localizador))
            
            # Espera a que el elemento sea visible
            
            WebDriverWait(self.driver, timeout).until(EC.visibility_of(elemento))
            
            # Espera a que el elemento esté habilitado para hacer click
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(elemento))
            
            return elemento
        except TimeoutException:
            
            raise AssertionError(f"El elemento {localizador} no estuvo listo")
        except NoSuchElementException:
            raise AssertionError(f"El elemento {localizador} no se encontró en la página")
        except ElementNotInteractableException:
            raise AssertionError(f"El elemento {localizador} no es interactuable")

    def cambiar_a_iframe(self):
        entrar_iframe = self.esperar_por_los_elementos(self.selectores.iframe_efectivo)
        self.driver.switch_to.frame(entrar_iframe)
        print("Logro entrar al iframe del boton efectivo")
        
    def salir_iframe(self):
        self.driver.switch_to.default_content()
        print("Logro salir del iframe del boton efectivo")

    def click_btn(self, selector_btn):
        """
        Función que hace click en el botón de iniciar compra
        """
        print("Haciendo click en el botón iniciar compra")
        click_boton = self.esperar_por_los_elementos(selector_btn)
        click_boton.click()
        print("Botón iniciar compra")
        print("inicio compra exitosamente!!!!!")
        
    def ingresar_txt(self, selector, txt):
        """
        Función que ingresa DNI en el campo DNI o CUIL
        """
        print(f"Ingresando el DNI {txt}")
        elemento = self.esperar_por_los_elementos(selector)
        elemento.clear()
        elemento.send_keys(txt)
        assert elemento.get_property("value") == txt, "El DNI no se ingreso correctamente"
        print("DNI ingresado")
        