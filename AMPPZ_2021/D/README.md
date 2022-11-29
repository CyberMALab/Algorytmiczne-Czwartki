# **Zadanie D**: Dwuczęściowy mechanizm 

## *Limit czasowy: 10s, limit pamięciowy: 1024 MB*

___

## **Treść**

Maszyna Bytegate, najnowszy wynalazek Bajtazara, to mechanizm składający się z dwóch
części, których – cytując podekscytowanego Bajtazara – “po prostu nie da się rozdzielić!”. Jego
dwuletni syn Bajtuś za chwilę pokaże mu, jak bardzo się myli.

Początkowy stan Bytegate możemy opisać jako tablicę o rozmiarach 𝑛 × 𝑚, wypełnioną
znakami A, B oraz kropkami. Litery A oznaczają pierwszą część maszyny, litery B oznaczają
drugą część maszyny, zaś kropki oznaczają pustą przestrzeń. Przykładowy rysunek znajduje się
poniżej:

    B   B   A   A   .
    .   B   B   A   A
    A   .   B   B   A
    A   .   .   B   A
    A   A   A   A   A


Jest to dwuczęściowy mechanizm, dlatego na tablicy znajdzie się co najmniej jeden znak A
oraz co najmniej jeden znak B. Oprócz tego obydwie części maszyny są spójne, tzn. dla dowolnych
dwóch pól oznaczonych etykietą A istnieje pewna ścieżka łącząca te pola, w której każde kolejne
pole ma wspólny bok z poprzednim, a także każde pole na ścieżce ma etykietę A. W ten sam
sposób spójna jest część B.

Część A maszyny pozostawała nieruchoma, podczas gdy Bajtuś pchał część B w różnych
kierunkach. Jego zabawę możemy więc opisać jako sekwencję 𝑞 liter N, S, E, W (oznaczających
odpowiednio kierunek północny, południowy, wschodni i zachodni). Za każdym razem Bajtuś
pchał część B mechanizmu “do oporu” tj. do momentu, w którym dalsze jej przesunięcie
oznaczałoby nałożenie na siebie dwóch części maszyny. Mogło się zdarzyć, że Bajtuś był w stanie
przesuwać część B w nieskończoność – w takim przypadku powiemy, że udało mu się rozdzielić
obie części. Nie oznacza to jednak, że Bajtuś przestał w tym momencie szarpać mechanizmem.
Niemniej jednak uznajemy, że raz rozdzielone części maszyny pozostają w tym stanie do końca
zabawy Bajtusia.

Pomóż stwierdzić czy w trakcie zabawy Bajtuś rozdzielił obie części Bytegate.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 1 000). Potem kolejno
podawane są zestawy w następującej postaci:

W pierwszej linii zestawu znajdują się trzy liczby całkowite 𝑛, 𝑚, 𝑞 (1 <= 𝑛, 𝑚 <= 10,
1 <= 𝑞 <= 100). Następne 𝑛 linii wejścia opisuje początkowy stan maszyny. Każda z tych linii to
napis długości 𝑚 złożony ze znaków A, B oraz kropek. Obydwie części maszyny są niepuste oraz
spójne.

Ostatnia linia zestawu zawiera ciąg 𝑞 liter należących do zbioru {𝑁, 𝑆, 𝐸, 𝑊}, o znaczeniu
podanym w treści zadania.


## **Wyjście**

Dla każdego zestawu danych wypisz słowo TAK lub NIE oznaczające, czy Bajtusiowi udało się
rozdzielić od siebie dwie części maszyny.

### **Przykład:**

#### **Wejście**:

    3
    5 5 3
    BBAA.
    .BBAA
    A.BBA
    A..BA
    AAAAA
    WNW
    5 5 7
    BBAA.
    .BBAA
    A.BBA
    A..BA
    AAAAA
    WNWNSEN
    6 5 3
    .....
    .AAA.
    .A.A.
    .AB..
    .A.A.
    .AAA.
    SNE

#### **Wyjście**:

    NIE
    TAK
    NIE
___

## **Wyjaśnienie**

Kiedy Bajtuś zakończył zabawę maszynami z pierwszego i trzeciego zestawu, znajdowały się
one – odpowiednio – w następujących stanach:

    B   B   .   .   .   .   .
    .   B   B   .   A   A   .
    .   .   B   B   .   A   A
    .   .   A   B   .   .   A
    .   .   A   .   .   .   A
    .   .   A   A   A   A   A

    A   A   A
    A   B   A
    A   .   .
    A   .   A
    A   A   A

W drugim zestawie Bajtusiowi udało się rozdzielić obie części mechanizmu w czwartym ruchu