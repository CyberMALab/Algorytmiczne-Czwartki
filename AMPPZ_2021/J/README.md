# **Zadanie J**: Jadowie węże 

## *Limit czasowy: 15s, limit pamięciowy: 1024 MB*

___

## **Treść**

Plansza do gry Jadowite węże jest prostokątem o 𝑛 wierszach i 𝑚 kolumnach, podzielonym
na 𝑛 · 𝑚 jednostkowych pól. Każde pole może być puste, zablokowane lub zawierać siedlisko
jadowitych bądź niejadowitych węży. Gracz może odwrócić dowolną liczbę wybranych przez siebie
wierszy: wykonanie takiej operacji sprawia, że każde znajdujące się w danym wierszu siedlisko
jadowitych węży zamienia się w siedlisko węży niejadowitych, i vice versa. Analogicznie, gracz
może również odwrócić wybrane przez siebie kolumny. Jeżeli jakieś siedlisko zostanie odwrócone
dwukrotnie, powraca do swojego oryginalnego stanu. Po wykonaniu wszystkich tych akcji gracz
musi przejść z lewego górnego do prawego dolnego pola planszy, w każdym ruchu przechodząc o
jedno pole w prawo lub w dół. Ścieżka gracza nie może przechodzić przez pola zablokowane, ani
przez pola z jadowitymi wężami.

Twórcy gry zaimplementowali już 𝑧 proponowanych plansz. Konieczna jednak jest jeszcze
weryfikacja, które z nich da się w ogóle rozwiązać. Niestety, to zadanie zostało przydzielone
właśnie Tobie.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę plansz 𝑧 (1 <= 𝑧 <= 500). Opis każdej z nich jest
następującej postaci:

W pierwszej linii znajdują się dwie liczby całkowite 𝑛 oraz 𝑚 (2 <= 𝑛, 𝑚 <= 2 000).

Każda z kolejnych 𝑛 linii zawiera dokładnie 𝑚 znaków ., #, O (duża litera “o”) oraz @ (małpa),
oznaczających odpowiednio puste pole, zablokowane pole, pole z siedliskiem niejadowitych węży
oraz pole z siedliskiem jadowitych węży. Możesz założyć, że pierwszy znak pierwszej linii oraz
𝑚-ty znak 𝑛-tej linii są różne od #, tj. lewe górne ani prawe dolne pole nie są zablokowane.

Suma wartości 𝑛 oraz suma wartości 𝑚 we wszystkich zestawach nie przekraczają 15 000
każda.

## **Wyjście**

Dla każdego zestawu danych wypisz rozwiązanie w następującym formacie.

W pierwszej linii wypisz pojedynczy napis TAK lub NIE mówiący, czy daną planszę da się
rozwiązać.

Jeżeli Twoją odpowiedzią dla danego zestawu jest TAK, w następnych trzech liniach wypisz
kolejno:

 - Ciąg 𝑛 znaków T lub N, gdzie 𝑖-ty znak oznacza odpowiednio odwrócenie bądź nieodwrócenie
siedlisk znajdujących się w 𝑖-tym wierszu planszy;

 - Ciąg 𝑚 znaków T lub N, gdzie 𝑗-ty znak oznacza odpowiednio odwrócenie bądź
nieodwrócenie siedlisk znajdujących się w 𝑗-tej kolumnie planszy;

 - Ciąg 𝑛 + 𝑚 − 2 znaków P lub D, oznaczających że kolejne kroki ścieżki rozpoczynającej się
w lewym górnym polu planszy prowadzą odpowiednio w prawo bądź w dół. Opisana przez
Ciebie ścieżka musi prowadzić do prawego dolnego pola planszy i może używać jedynie
pustych pól oraz pól z siedliskami niejadowitych węży.

Jeśli istnieje wiele poprawnych rozwiązań, możesz wypisać dowolne z nich.


### **Przykład:**

#### **Wejście**:

    1
    4 5
    ..#..
    @@O@@
    ##@#O
    ..@.@

#### **Wyjście**:

    TAK
    NTNN
    NNTNT
    DPPDDPP

___

## **Wyjaśnienie**

Po odwróceniu wskazanych przez gracza wierszy i kolumn stan planszy przedstawia się
następująco:

    ..#..
    OOOO@
    ##O#@
    ..O.O

Wskazana przez gracza ścieżka używa jedynie pól pustych oraz pól, na których (po wykonaniu
wszystkich odwróceń) żyją węże niejadowite.
