import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import var


def getinfolydia(username, password):
    lydia_tiltak = []
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get('https://lydiaweb.itea.ntnu.no/Lydia/Account/Login.aspx?returnUrl=https%3a%2f%2flydiaweb.itea.ntnu.no'
               '%2fLydia%2fDefault.aspx')
    WebDriverWait(driver, 10000).until(ec.visibility_of_element_located((By.TAG_NAME, 'body')))
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
    # Gå gjennom hvert tiltak
    for x in range(0, antall_tiltak):
        tiltaksnr = driver.find_elements(By.XPATH, var.tiltaksnr)[x].text
        tiltaksnavn = driver.find_elements(By.XPATH, var.tiltaksnavn)[x].text
        tiltakstekst = driver.find_elements(By.XPATH, var.tiltakstekst)[x].get_attribute('textContent')
        bygg = driver.find_elements(By.XPATH, var.bygg)[x].get_attribute('textContent')
        nytt_tiltak = {'Tiltaksnummer': tiltaksnr,
                       'Bygg': bygg,
                       'Tiltaksnavn': tiltaksnavn,
                       'Beskrivelse': tiltakstekst}
        lydia_tiltak.append(nytt_tiltak)
    driver.close()
    return lydia_tiltak


def sendmail(send_tiltak, valg):
    print("Sender mail nå. Vennligst vent.")
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content = f"""Hei, trenger ordre på denne:
------------------------------------------------------
| Tiltaksnummer: {send_tiltak[valg]['Tiltaksnummer']}
| Tiltaksnavn: {send_tiltak[valg]['Tiltaksnavn']}
| Bygg: {send_tiltak[valg]['Bygg']}
------------------------------------------------------
Beskrivelse av tiltak: {send_tiltak[valg]['Beskrivelse']}
------------------------------------------------------
"""
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = var.your_address
    message['To'] = var.receiver_address
    message['Subject'] = f"Ordre for {send_tiltak[valg]['Tiltaksnummer']} på {send_tiltak[valg]['Bygg']}"
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)
    # Enable security
    session.starttls()
    session.login(var.your_address, var.app_key)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(var.your_address, var.receiver_address, text)
    session.quit()
    # send_tiltak contains dictionary from getinfolydia().
    print(f"Mail for tiltaksnummer: {send_tiltak[valg]['Tiltaksnummer']} er sendt.")
