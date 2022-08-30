import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import var

alle_tiltak = []

def getInfoLydia(username, password):
    lydia_tiltak = []
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://lydiaweb.itea.ntnu.no/Lydia/Account/Login.aspx?returnUrl=https%3a%2f%2flydiaweb.itea.ntnu.no%2fLydia%2fDefault.aspx')
    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    # Find and update username.
    username_login = driver.find_element(By.XPATH, var.username_var)
    username_login.send_keys(username)
    # Find and update password.
    password_login = driver.find_element(By.XPATH, var.password_var)
    password_login.send_keys(password)
    # Find and click the login-button.
    login_button = driver.find_element(By.XPATH, var.loginbutton)
    login_button.click()
    # Sleep for letting all elements load
    time.sleep(3)
    arbeidslistebtn = driver.find_element(By.XPATH, var.arbeidsliste)
    arbeidslistebtn.click()
    time.sleep(10)
    antall_tiltak = len(driver.find_elements(By.XPATH, var.tiltaksnr))
    for x in range(0, antall_tiltak):
        tiltaksnr = driver.find_elements(By.XPATH, var.tiltaksnr)[x].text
        tiltaksnavn = driver.find_elements(By.XPATH, var.tiltaksnavn)[x].text
        tiltakstekst = driver.find_elements(By.XPATH, var.tiltakstekst)[x].get_attribute('textContent')
        bygg = driver.find_elements(By.XPATH, var.bygg)[x].get_attribute('textContent')
        #TODO Dette fungerer ikke: TypeError: 'WebElement' object is not subscriptable
        nytt_tiltak = {'Tiltaksnummer': tiltaksnr, 'Bygg': bygg, 'Tiltaksnavn': tiltaksnavn, 'Beskrivelse': tiltakstekst}
        lydia_tiltak.append(nytt_tiltak)
    driver.close()
    return lydia_tiltak

def sendMail(send_tiltak, valg):
    # send_tiltak inneholder hele dictionary hentet fra getInfoLydia().
    print(send_tiltak[valg]['Tiltaksnummer'])