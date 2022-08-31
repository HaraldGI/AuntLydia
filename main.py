from funksjoner import *

USERNAME = 'hgf' #input("Login as: ")
PASSWORD = 'hgf' #input("Password: ")


def main():
    print("Alle tiltak lastes inn. Vennligst vent.")
    alle_tiltak = getinfolydia(USERNAME, PASSWORD)
    print("Velg ønsket funksjon:")
    print("1. Print liste med alle lydia avvik")
    print("2. Send ett eller flere avvik som mail.")
    print("ENTER for å avslutte program.")
    valg = int(input(":"))
    while True:
        if valg == 1:
            for tiltak in range(0, len(alle_tiltak)):
                print(f"Tiltaksnummer {tiltak} i listen:")
                print(f"Tiltak: {alle_tiltak[tiltak]['Tiltaksnummer']}")
                print(f"Bygg: {alle_tiltak[tiltak]['Bygg']}")
                print(f"Tiltaksnavn: {alle_tiltak[tiltak]['Tiltaksnavn']}")
                print(f"Beskrivelse: {alle_tiltak[tiltak]['Beskrivelse']}")
                print("--------------------------------------------------")
        if valg == 2:
            print("Velg hvilke tiltak du vil sende som mail. Tast inn siffer ved tiltaksnummer:")
            for tiltak in range(0, len(alle_tiltak)):
                print(f"{tiltak}. {alle_tiltak[tiltak]['Tiltaksnummer']} | {alle_tiltak[tiltak]['Tiltaksnavn']}")
            while True:
                send_tiltak = alle_tiltak
                try:
                    valg = int(input("Hvilket tiltak vil du sende? Legg inn nummer og trykk ENTER. Tast '99' for å avslutte. "))
                    if valg != 99:
                        sendmail(send_tiltak, valg)
                except ValueError:
                    print("Please select a valid number.")
                if valg == 99:
                    break

        else:
            break
    print("Program avsluttes.")


main()
