# Utwórz słownik filmów. Niech  kluczem będzie nazwa filmu, a parą wartości dwie liczby: kryteria wiekowe oraz liczba dostępnych biletów

movies = {"Finding Nemo":[5,2], "Moana":[6,3], "Batman":[18,5], "The Lion King":[10,4]}

# Utwórz pętlę, która będzie działać w nieskończoność
while True:
    
    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)
    movie = input("\nPodaj tytuł filmu: ").strip().title()
    
    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest odostępny w słowniku, kontynuuj
    if movie in movies:
        
        # Zapytaj użytkownika o wiek
        age = int(input("Podaj swój wiek: "))    
        
        # Sprawdź użytkownika pod kątem kwalifikowalności
    if movie in movies:      
            
            # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
        if age >= movies[movie][0]:
            
            # Sprawdzenie dostępności biletów
            if movies[movie][1] > 0:
                movies[movie][1] -= 1
                print("Rezerwacja udana!")
            else:
                print("Brak dostępnych biletów na ten film.")
        else:
            print("Nie spełniasz kryterium wiekowego.")
    else:
        print("Taki film nie istnieje w bazie.")        
            
                # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmiejsz pulę dostępnych miejsc o 1
