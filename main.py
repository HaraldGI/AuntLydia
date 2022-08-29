import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xpvar

USERNAME = 'hgf'
PASSWORD = 'hgf'
lydia_tiltak = []

driver = webdriver.Chrome('chromedriver')
driver.get('https://lydiaweb.itea.ntnu.no/Lydia/Account/Login.aspx?returnUrl=https%3a%2f%2flydiaweb.itea.ntnu.no%2fLydia%2fDefault.aspx')

def program(username, password):
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    # Find and update username.
    username_login = driver.find_element(By.XPATH, xpvar.username_var)
    username_login.send_keys(username)
    # Find and update password.
    password_login = driver.find_element(By.XPATH, xpvar.password_var)
    password_login.send_keys(password)
    # Find and click the login-button.
    login_button = driver.find_element(By.XPATH, xpvar.loginbutton)
    login_button.click()
    # Sleep for letting all elements load
    # TODO Use WebDriverWait?
    time.sleep(3)
    arbeidslistebtn = driver.find_element(By.XPATH, xpvar.arbeidsliste)
    arbeidslistebtn.click()
    # TODO Use WebDriverWait?
    time.sleep(10)
    antall_tiltak = len(driver.find_elements(By.XPATH, xpvar.tiltaksnr))
    print("Forbereder innlasting av tiltak..")
    visefremtiltak = input("Vise tiltak? skriv JA eller NEI")
    for x in range(0, antall_tiltak):
        tiltaksnr = driver.find_elements(By.XPATH, xpvar.tiltaksnr)[x].text
        tiltaksnavn = driver.find_elements(By.XPATH, xpvar.tiltaksnavn)[x].text
        tiltakstekst = driver.find_elements(By.XPATH, xpvar.tiltakstekst)[x].get_attribute('textContent')
        bygg = driver.find_elements(By.XPATH, xpvar.bygg)[x].get_attribute('textContent')
        #TODO Dette fungerer ikke: TypeError: 'WebElement' object is not subscriptable
        nytt_tiltak = {'Tiltaksnummer': tiltaksnr, 'Bygg': bygg, 'Tiltaksnavn': tiltaksnavn, 'Beskrivelse': tiltakstekst}
        lydia_tiltak.append(nytt_tiltak)
        if visefremtiltak == 'JA':
            print(f"Tiltaksnummer {x} i listen:")
            print(f"Tiltak: {lydia_tiltak[x]['Tiltaksnummer']}")
            print(f"Bygg: {bygg}")
            print(f"Tiltaksnavn: {lydia_tiltak[x]['Tiltaksnavn']}")
            print(f"Beskrivelse: {lydia_tiltak[x]['Beskrivelse']}")
            print("--------------------------------------------------")
        else:
            continue
    driver.close()




if __name__ == '__main__':
    program(USERNAME, PASSWORD)


