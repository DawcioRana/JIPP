# Zliczanie liczby samogłosek i spółgłosek w zadanym ciągu

# Utwórz zmienne "vowels" (samogłoski) i "consonants" (spółgłoski) i przypisz każdej z nich wartość 0

vowels = 0
consonants = 0

# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”
tekst = "Programowanie Pythona"   
for i in tekst:
    print(i)

# Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek w danym łańcuchu znaków
for i in tekst.lower():
    if i.isalpha():
        if i in "aeiouyąę":
            vowels += 1
        else:
            consonants += 1
    
        
# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków
print("Liczba samogłosek:", vowels)    
print("Liczba spółgłosek:", consonants)
