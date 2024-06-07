import time
from utils.funciones import *
from config.credentials import *

options = webdriver.ChromeOptions()
#options.add_argument("--headless") #Que no se vea en la pantalla 
# options.add_argument("--sandbox")
# options.add_argument("--disable-dev-shm-usage")

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

utilidades = UtilidadesPruebas(driver)
utilidades.cargar_pagina(login_url)
utilidades.click_btn(Selectores.agregar_carrito)
utilidades.click_btn(Selectores.ver_carrito)
utilidades.click_btn(Selectores.iniciar_compra)
utilidades.ingresar_txt(Selectores.email_input, email)
utilidades.ingresar_txt(Selectores.cp_input, codigo_postal)
utilidades.click_btn(Selectores.continuar_1)



time.sleep(5)