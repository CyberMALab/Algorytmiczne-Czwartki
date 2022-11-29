# **Zadanie I**: Henryk Portier i Promień Palindromiczny

## *Limit czasowy: 25s, limit pamięciowy: 512 MB*

___

## **Treść**

Młody czarodziej Henryk Portier otrzymał właśnie smutną wiadomość – odszedł nestor jego
rodu, Markus Radius Palindromus Black. Wujek Markus uchodził za dość ekscentrycznego, parał
się skomplikowaną magią binarną, był też niezwykle bogatym człowiekiem. Testament Blacka
przewiduje, że Henryk odziedziczy jego tajemniczy skarbiec. Aby jednak do niego wejść, musi
wypowiedzieć odpowiednie hasło 𝐻, które jest binarnym (złożonym ze znaków 0 i 1) słowem o
długości 𝑛. Wuj Black nie zdradził jednak Henrykowi hasła wprost – byłoby to zdecydowanie
nie w jego stylu. Zamiast tego, dla każdego 𝑥 = 1, 2, . . . , 𝑛 obliczył promień palindromiczny 𝑝𝑥
– największą możliwą liczbę całkowitą taką, że słowo 𝐻[𝑥 − 𝑝𝑥 .. 𝑥 + 𝑝𝑥] (o długości 2𝑝𝑥 + 1 i o
środku w 𝑥) istnieje i jest palindromem (czytane od przodu i od tyłu jest takie samo). Następnie
wysłał Henrykowi tylko ciąg 𝑝1, . . . , 𝑝𝑛. Na przykład, gdyby hasło było słowem 10111010, Henryk
otrzymałby ciąg (0, 1, 0, 3, 0, 1, 1, 0).

Henryk wolałby, żeby wuj Markus nie testował zza grobu jego umiejętności algorytmicznych.
Ale od czego ma przyjaciół? Znając ciąg przesłany w testamencie, znajdź wszystkie możliwe
hasła, które do niego pasują. Testament jest pożółkły i poplamiony – może się też niestety
zdarzyć, że coś zostało źle odczytane i rozwiązania w ogóle nie ma.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 200 000). Potem kolejno
podawane są zestawy w następującej postaci:

Opis jednego zestawu składa się z dwóch linii. Pierwsza linia zestawu zawiera liczbę 𝑛 –
długość hasła, a także ciągu przesłanego przez wuja Blacka (2 <= 𝑛 <= 1 000 000). Druga linia
zestawu zawiera 𝑛 liczb całkowitych 𝑝1, 𝑝2, . . . , 𝑝𝑛 (0 <= 𝑝𝑖 <= 𝑛) – promienie palindromiczne dla
kolejnych znaków hasła.

Suma długości ciągów we wszystkich zestawach danych nie przekracza 5 · 10^7.


## **Wyjście**

Dla każdego zestawu danych wypisz najpierw liczbę możliwych haseł 𝑘. Jeśli 𝑘 nie jest zerem,
to w kolejnych 𝑘 liniach wypisz możliwe rozwiązania – ciągi o długości 𝑛 złożone ze znaków 0 i
1 . Ciągi muszą być wypisane w porządku leksykograficznym.

Możesz założyć, że 𝑘 nie przekroczy 100.

### **Przykład:**

#### **Wejście**:

    1
    8
    0 1 0 3 0 1 1 0

#### **Wyjście**:

    4
    00010000
    01000101
    10111010
    11101111