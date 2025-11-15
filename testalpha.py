####################
## TEST SCANNER CON SELENIUM
####################

# LIBRERIAS
from art import *
import os, sys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from openai import OpenAI 

##### IA
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

############

def main(): 
    while True:
        os.system("clear")
        tprint("DEXTER", "poison")
        print("")
        print("[1] . Manual Web Scanner")
        print("[2] . IA Web Scanner")
        print("[3] . Exit")
        print("")

        op_str = input(">>> ").strip()
        if not op_str:
            print("No ingresaste nada...")
            input("ENTER para continuar...")
            continue
        if not op_str.isdigit():
            print("Debes ingresar un número...")
            input("ENTER para continuar...")
            continue

        op = int(op_str)

        if op == 1:
            manualscann()
        elif op == 2:
            iascann()
        elif op == 3:
            print("bye :)")
            input("ENTER para salir...")
            os.system("clear") 
            sys.exit()
        else:
            print("Opción inválida")
            input("ENTER para continuar...")

def manualscann():
    print("Ejecutando Manual Web Scanner...")
    input("ENTER para volver al menú...")

def iascann():
    result = IAScan()
    if result:
        prompt = preparar_prompt(result)
        print("\n=== PROMPT PARA IA ===\n")
        print(prompt)
    input("\nENTER para volver al menú...")

def IAScan():
    URL = input("Ingresar URL >>> ").strip()
    if not URL:
        print("Ingresa una URL")
        return None
    
    if not URL.startswith(("http://", "https://")):
        URL = "http://" + URL

    opciones = webdriver.FirefoxOptions()
    opciones.add_argument("--headless")

    try:
        driver = webdriver.Firefox(options=opciones)
        driver.get(URL)
        print("cargando...")

        # HTML completo
        html = driver.page_source
        print("HTML [COMPLETE]")

        # Todos los CSS linkeados
        css_links = [link.get_attribute("href") 
                     for link in driver.find_elements("tag name", "link") 
                     if link.get_attribute("rel") == "stylesheet"]
        print("CSS [COMPLETE]")

        # Todos los scripts
        js_links = [script.get_attribute("src") 
                    for script in driver.find_elements("tag name", "script") 
                    if script.get_attribute("src")]
        print("JavaScript [COMPLETE]")

        # Imágenes
        images = [img.get_attribute("src") 
                  for img in driver.find_elements("tag name", "img")]
        print("Images [COMPLETE]")

        return {
            "html": html,
            "css_links": css_links,
            "js_links": js_links,
            "images": images
        }

    except WebDriverException as e:
        print(f"✗ Error al cargar la página: {e}")
        return None
    finally:
        try:
            driver.quit()
        except:
            pass

def preparar_prompt(scan_result):
    resumen = f"""
Eres un Agente de IA creado para una herramienta de Ethical Hacking llamada DEXTER SCANNER.
Debes responder brevemente a lo solicitado:
- Resalta vulnerabilidades encontradas
- Resalta errores y comentarios
- Resalta lo importante
- Si no hay nada, escribe: NADA ENCONTRADO

CSS encontrados: {scan_result['css_links']}
JS encontrados: {scan_result['js_links']}
Imágenes: {len(scan_result['images'])} recursos
HTML (primeros 500 caracteres): 
{scan_result['html'][:500]}
"""
    return resumen



def enviar_a_ia(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",   # podés usar gpt-4.1 o gpt-4.1-mini
            messages=[
                {"role": "system", "content": "Eres un analista de seguridad web."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al consultar IA: {e}"






############

if __name__ == "__main__":
    main()
####################
## TEST DEXTER 
####################

# LIBRERIAS
from art import *
import os, sys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

############

def main(): 
    while True:
        os.system("clear")
        tprint("DEXTER", "poison")
        print("")
        print("[1] . Manual Web Scanner")
        print("[2] . IA Web Scanner")
        print("[3] . Exit")
        print("")

        op_str = input(">>> ").strip()
        if not op_str:
            print("No ingresaste nada...")
            input("ENTER para continuar...")
            continue
        if not op_str.isdigit():
            print("Debes ingresar un número...")
            input("ENTER para continuar...")
            continue

        op = int(op_str)

        if op == 1:
            manualscann()
        elif op == 2:
            iascann()
        elif op == 3:
            print("bye :)")
            input("ENTER para salir...")
            os.system("clear") 
            sys.exit()
        else:
            print("Opción inválida")
            input("ENTER para continuar...")

def manualscann():
    print("Ejecutando Manual Web Scanner...")
    input("ENTER para volver al menú...")

def iascann():
    result = IAScan()
    if result:
        prompt = preparar_prompt(result)
        print("\n=== PROMPT PARA IA ===\n")
        print(prompt)
    input("\nENTER para volver al menú...")

def IAScan():
    URL = input("Ingresar URL >>> ").strip()
    if not URL:
        print("Ingresa una URL")
        return None
    
    if not URL.startswith(("http://", "https://")):
        URL = "http://" + URL

    opciones = webdriver.FirefoxOptions()
    opciones.add_argument("--headless")

    try:
        driver = webdriver.Firefox(options=opciones)
        driver.get(URL)
        print("cargando...")

        # HTML completo
        html = driver.page_source
        print("HTML [COMPLETE]")

        # Todos los CSS linkeados
        css_links = [link.get_attribute("href") 
                     for link in driver.find_elements("tag name", "link") 
                     if link.get_attribute("rel") == "stylesheet"]
        print("CSS [COMPLETE]")

        # Todos los scripts
        js_links = [script.get_attribute("src") 
                    for script in driver.find_elements("tag name", "script") 
                    if script.get_attribute("src")]
        print("JavaScript [COMPLETE]")

        # Imágenes
        images = [img.get_attribute("src") 
                  for img in driver.find_elements("tag name", "img")]
        print("Images [COMPLETE]")

        return {
            "html": html,
            "css_links": css_links,
            "js_links": js_links,
            "images": images
        }

    except WebDriverException as e:
        print(f"✗ Error al cargar la página: {e}")
        return None
    finally:
        try:
            driver.quit()
        except:
            pass

def preparar_prompt(scan_result):
    resumen = f"""
Eres un Agente de IA creado para una herramienta de Ethical Hacking llamada DEXTER SCANNER.
Debes responder brevemente a lo solicitado:
- Resalta vulnerabilidades encontradas
- Resalta errores y comentarios
- Resalta lo importante
- Si no hay nada, escribe: NADA ENCONTRADO

CSS encontrados: {scan_result['css_links']}
JS encontrados: {scan_result['js_links']}
Imágenes: {len(scan_result['images'])} recursos
HTML (primeros 500 caracteres): 
{scan_result['html'][:500]}
"""
    return resumen

############

if __name__ == "__main__":
    main()
