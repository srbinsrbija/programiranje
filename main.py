def ucitaj_tekst(filepath):
    try:
        #Ovdje ide logika za čitanje datoteke
        with open (filepath, "r", encoding="utf-8") as file:
            sadrzaj = file.read()
        return sadrzaj 
    except FileNotFoundError:
        print(f"Greška: datoteka na putanji {filepath} ne postoji.")
        return None #Vraća prazan skup podataka ako ne nađe datoteku
   #funkcija koja pročišćava tekst 
def ocisti_tekst(tekst):
        #ovdje ide logika za pročišćavanje teksta
        tekst = tekst.lower()
        interpunkcija = [".",",","!",";",":","(",")","'",'"']
        for znak in interpunkcija:
             tekst = tekst.replace(znak,"")
        lista_rijeci = tekst.split()
        return lista_rijeci



#glavni dio programa
if __name__=="__main__":
    filepath = "tekst.txt"  
    print (f"Učitavam tekst iz datoteke: {filepath}")

    ucitani_tekst = ucitaj_tekst(filepath)

    if ucitani_tekst:
        print("\nTekst uspješno učitan. Slijedi ispis sadržaja:")
        print("-" * 40)
        print(ucitani_tekst)
        print("-" * 40)
    else:
        print("Program se prekida jer tekst nije učitan.")

    prociseni_tekst = ocisti_tekst(ucitani_tekst)
    if prociseni_tekst:
         print ("Pročišćeni tekst je:")
         print("-" * 40)
         print(prociseni_tekst)
         print("-" * 40)
    else:
         print("Program se prekida jer tekst nije učitan.")
