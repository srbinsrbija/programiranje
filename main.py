STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'mu', 'joj', 'ih']

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




#funkcija za brojanje frekvencije rijeci u tekstu
def broji_frekvenciju(lista_rijeci):
     #1.Kreiramoprazan rječnik koji će čuvati rezultate
    rjecnik_frekvencija = {}
#2. Prolazimo kroz svaku riječ u primljenoj listi
    for rijec in lista_rijeci:
        if rijec in rjecnik_frekvencija:
            rjecnik_frekvencija[rijec] += 1
        else:
            rjecnik_frekvencija[rijec] = 1
    return rjecnik_frekvencija

def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in stop_words_lista:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik




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
         print(prociseni_tekst.__len__())

         #NOVI DIO - POZIVAMO NOVU FUNKCIJU
         print("brojim frekvenciju riječi...")
         broj_rijeci= broji_frekvenciju(prociseni_tekst)
         print("brojanje završeno!")

         #Ispisujemo rezultat da vidimo što smo dobili
         print("\n---Rječnik frekvencija riječi---")
         print(broj_rijeci)
         print("-" * 40)


         ociscene_frekvencije = ukloni_stop_words(broj_rijeci, STOP_WORDS)
         print("\n--- Očišćeni rječnik frekvencija riječi ---")
         print(ociscene_frekvencije)
         print("-" * 40)
        
    else:
         print("Program se prekida jer tekst nije učitan.")
     
