# **Zadanie J**: Anteny

## *Limit czasowy: 8s, limit pamięciowy: 512 MB*

___

## **Treść**

W tajnej bazie wojskowej testowana jest nowa technologia komunikacji radiowej. Na potrzeby
eksperymentu w obrębie bazy postawiono 𝑚 anten nadawczo-odbiorczych. Teren bazy jest
całkowicie płaski i ma z lotu ptaka kształt wielokąta wypukłego. Wzdłuż brzegu tego wielokąta
przebiega specjalny mur, który między innymi zabezpiecza fale radiowe przed podsłuchem.
Z powodu przebudowy architektury bazy konieczne będzie wyburzenie fragmentów muru
odpowiadającym pewnym dwu bokom wielokąta. To niestety wystawi testowaną technologię na
ryzyko podsłuchu: jeżeli można rozmieścić na zewnątrz bazy dwóch szpiegów w taki sposób,
by w linii prostej pomiędzy nimi znalazły się dwie anteny i by linii tej nie przedzielił żaden
fragment muru, to komunikację między tymi dwiema antenami można przechwycić. Rozważasz
różne scenariusze usunięcia dwu fragmentów muru. Twoim zadaniem jest wyznaczyć dla każdego
z tych scenariuszy, ile par anten będzie zagrożonych podsłuchem w tym scenariuszu.

___

___

Powyższy rysunek przedstawia przykładową bazę, której teren jest pięciokątem, i w obrębie
której znajdują się cztery anteny oznaczone krzyżykami. Liniami przerywanymi zaznaczono
wszystkie proste przechodzące przez pary różnych anten. Rysunek odpowiada pierwszemu
zestawowi danych z przykładowego wejścia przedstawionego w dalszej części treści.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 200 000). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera liczbę całkowitą 𝑛 (3 <= 𝑛 <= 10) – liczbę wierzchołków
wielokąta określającego teren bazy. Następne 𝑛 linii zawiera 𝑛 par liczb całkowitych – współrzędne kolejnych wierzchołków wielokąta zgodnie z ruchem wskazówek zegara. Wierzchołki numerujemy
od 0 zgodnie z ich kolejnością pojawiania się na wejściu. Kolejna linia zestawu zawiera
liczbę całkowitą 𝑚 (2 <= 𝑚 <= 50 000) – liczbę anten. Dalsza część zestawu składa się z 𝑚 linii,
każda zawierająca parę liczb całkowitych – są to współrzędne anten. W następnej linii znajduje
się liczba całkowita 𝑞 (1 <= 𝑞 <= 10) – liczba zapytań. Ostatnie 𝑞 linii zestawu zawiera 𝑞 par
liczb całkowitych (𝑎1, 𝑏1), . . . ,(𝑎𝑞, 𝑏𝑞) (0 <= 𝑎𝑖 < 𝑏𝑖 <= 𝑛 − 1), opisujących 𝑞 zapytań. Para (𝑎𝑖
, 𝑏𝑖)
oznacza zapytanie o liczbę nieuporządkowanych par różnych anten, takich że przechodząca przez
nie prosta przecina bok między wierzchołkami o numerach 𝑎𝑖 oraz 𝑎𝑖 + 1, a także bok między
wierzchołkami o numerach 𝑏𝑖 oraz (𝑏𝑖 + 1) mod 𝑛.

Wszystkie współrzędne są liczbami całkowitymi nieprzekraczającymi na moduł 10^9.
W obrębie zestawu danych, wszystkie pojawiające się punkty są różne i nie ma trzech
współliniowych. Między każdymi dwoma zestawami danych oraz przed pierwszym zestawem
znajduje się pusta linia.

Suma wartości 𝑚 we wszystkich zestawach danych nie przekracza 300 000.



## **Wyjście**

Dla każdego zestawu danych wypisz w osobnej linii odpowiedzi na kolejne zapytania,
oddzielając je spacjami.

### **Przykład:**

#### **Wejście**:

    2
    5
    0 0
    0 5
    3 7
    6 5
    6 0
    4
    1 2
    1 3
    5 2
    5 3
    3
    0 3
    1 4
    1 2
    4
    -1 -1
    -1 1
    2 1
    2 -1
    2
    0 0
    1 0
    6
    0 1
    0 2
    0 3
    1 2
    1 3
    2 3

#### **Wyjście**:

    4 1 0
    0 1 0 0 0 0