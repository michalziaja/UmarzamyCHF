import pdfplumber
import re

search_phrase = """Jeżeli Kredytobiorca, mimo upływu okresu wypowiedzenia, nie ureguluje
należności, Bank w następnym dniu, po upływie terminu wypowiedzenia,
dokonuje przewalutowania całego wymagalnego zadłużenia na PLN, z
zastosowaniem aktualnego kursu sprzedaży dewiz, określanego przez Bank w
Tabeli Kusów. Poczynając od dnia przewalutowania Bank pobiera od
wymagalnego kapitału karne odsetki w wysokości 2-krotności
oprocentowania kredytów udzielanych w PLN (nie indeksowanych do waluty
obcej) przy zastosowaniu aktualnego z dnia przewalutowania wskaźnika
DBPLN oraz marży obowiązującej w dniu wypłaty kredytu lub jego pierwszej
transzy"""


search_phrase = re.sub(r'\s+', ' ', search_phrase).strip()

with pdfplumber.open('test.pdf') as pdf:

    for page in pdf.pages:
        # Wyodrębnij tekst
        text = page.extract_text()

  
        text = re.sub(r'\s+', ' ', text).strip()

  
        if search_phrase.lower() in text.lower():
            print(f"Znaleziono frazę '{search_phrase}' na stronie {page.page_number}.")