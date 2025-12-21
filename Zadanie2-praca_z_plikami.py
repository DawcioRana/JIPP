#Policz słowa w pliku
#Zadanie: Napisz program, który:

#odczytuje plik o nazwie story.txt

#liczy ile słów znajduje się w pliku ignoruj puste linie

#wyświetla wynik, np.: "Liczba słów: 42"

#Wskazówka: Użyj read() lub pętli po liniach; podziel tekst używając .split() aby uzyskać słowa.
with open("story.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

print(f"Liczba słów: {len(words)}")
