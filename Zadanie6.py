#### Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):     
   return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "You can't divide by zero!"
    return a / b

# Wyświetl listę operacji

print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")   

# Pozwól użytkownikowi wybrać żądane działanie na podstawie wyświetlonej listy poleceń
    
op = input("Please enter choice (a/ b/ c/ d): ")   

# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczby całkowitych   


# Logika do wykonywania określonej operacji za pomocą instrukcji IF -ELIF -ELSE.
if op not in ["a", "b", "c", "d"]:
    print("Invalid operation selected.")

else:
    numb1 = int(round(float(input("Enter first number: "))))
    numb2 = int(round(float(input("Enter second number: "))))

    if op == "a":
        print("Result:", add(numb1, numb2))
    elif op == "b":
        print("Result:", subtract(numb1, numb2))
    elif op == "c":
        print("Result:", multiply(numb1, numb2))
    elif op == "d":
        print("Result:", divide(numb1, numb2))

# Jeśli użytkownik wybierze operację, która nie jest dostępna, wyświetl komunikat o błędzie
