# **Zadanie E**: Epidemia 

## *Limit czasowy: 9s, limit pamięciowy: 1024 MB*

___

## **Treść**

Bajtocja zamknęła granice z powodu wykrycia u jej sąsiadów zakażeń nowym szczepem
bajtobakterii. Badania wskazują, że szczep ten nie tylko jest wysoce zaraźliwy, lecz również
nie powoduje żadnej reakcji układu immunologicznego Bajtocjan, przez co raz zarażona osoba
pozostanie zarażona – oraz będzie zarażać innych – dożywotnio (lub przynajmniej do czasu
wynalezienia skutecznego lekarstwa).

Aby nie dopuścić do rozprzestrzenienia się bajtobakterii, rząd Bajtocji wprowadził daleko
idące obostrzenia oraz uruchomił Narodowy System Inwigilacji, pozwalający monitorować
wszystkie kontakty społeczne w kraju. Zapowiedziano przy tym, że obostrzenia zostaną zniesione
dopiero wtedy, gdy pewnym będzie, że nikt oprócz osób przebywających na kwarantannie nie
jest zarażony bajtobakterią. Jako naczelnemu informatykowi Bajtocji, Tobie została powierzona
analiza danych z systemu inwigilacji i określenie, w którym momencie obostrzenia będą mogły
zostać uchylone.

Na terenie Bajtocji znajduje się 𝑛 osób, z których początkowo każda może być zarażona
bajtobakterią albo zdrowa. Po zamknięciu granic następuje ciąg 𝑘 zdarzeń, z których każde ma
jedną z następujących form:


 - Otrzymujesz z systemu inwigilacji informację, że pewna grupa osób spotyka się. Jeżeli
którakolwiek z nich była zarażona, to wszystkie stają się zarażone (i pozostaną już zarażone
do końca życia). Kontakt taki jest jedynym możliwym sposobem zarażenia się (wbrew
początkowym doniesieniom, dotykanie zakażonych powierzchni nie może spowodować
zarażenia się bajtobakterią).

 - Pewnej osobie zostaje wykonany test na obecność bajtobakterii i daje on wynik negatywny.

 - Pewnej osobie zostaje wykonany test na obecność bajtobakterii i daje on wynik pozytywny.
Osoba taka zostaje bezzwłocznie skierowana na bezterminową kwarantannę i nie będzie od
tego momentu uczestniczyć w żadnych kontaktach społecznych (może natomiast zdarzyć
się, że zostanie jej w przyszłości wykonany kolejny test 1
).

 - Otrzymujesz od ministra zdrowia Bajtocji zapytanie, czy zniesienie obostrzeń jest już
możliwe, to znaczy czy w oparciu o wszystkie zebrane do tej pory informacje da się
udowodnić, że nikt oprócz przebywających na kwarantannie nie może być zarażony. Jeśli
wciąż mogą istnieć osoby zarażone, musisz podać przykład takiej osoby, według wytycznych
Ministerstwa (opisanych w sekcji Wyjście).

Co ważne, Twój program musi działać online, to znaczy udzielać odpowiedzi bezpośrednio
po każdym zapytaniu ministra, przed wczytaniem kolejnych zapytań.


## **Wejście**

Właściwa interpretacja danych wejściowych zależeć będzie od aktualnej wartości zmiennej
shift. Na początku każdego zestawu danych wynosi ona 0, zaś jej kolejne wartości będą zależne
od udzielanych przez Twój program odpowiedzi. Taki opis wejścia ma za zadanie wymusić, aby
Twój program odpowiadał na każde z zapytań bezpośrednio po jego wczytaniu.

Funkcja dekodująca zdefiniowana jest w następujący sposób:

    decode (p) = ((p - 1 + shift) mod n) + 1

> 𝑝 jest liczbą całkowitą spełniającą 1 <= 𝑝 <= 𝑛, a mod to operacja reszty z dzielenia.

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 1 000). Potem kolejno
podawane są zestawy w następującej postaci:

W pierwszej linii znajdują się dwie liczby całkowite 𝑛 oraz 𝑘 (1 <= 𝑛 <= 500 000,
1 <= 𝑘 <= 1 000 000), oznaczające odpowiednio liczbę osób przebywających na terenie Bajtocji
oraz liczbę zdarzeń. Osoby ponumerowane są od 1 do 𝑛.

Kolejnych 𝑘 linii opisuje następujące po sobie zdarzenia. Mogą one być następującej postaci:

 - Litera K oraz liczba całkowita 𝑐 (2 <= 𝑐 <= 𝑛), po której następuje 𝑐 różnych liczb całkowitych
𝑝1, . . . , 𝑝𝑐 (1 <= 𝑝𝑖 <= 𝑛) – kontakt społeczny, w którym uczestniczy 𝑐 osób o indeksach
𝑑𝑒𝑐𝑜𝑑𝑒(𝑝1), . . . , 𝑑𝑒𝑐𝑜𝑑𝑒(𝑝𝑐).

 - Litera N oraz liczba całkowita 𝑝 (1 <= 𝑝 <= 𝑛) – osobie o indeksie 𝑑𝑒𝑐𝑜𝑑𝑒(𝑝) wykonany zostaje
test, który daje wynik negatywny.

 - Litera P oraz liczba całkowita 𝑝 (1 <= 𝑝 <= 𝑛) – osobie o indeksie 𝑑𝑒𝑐𝑜𝑑𝑒(𝑝) wykonany zostaje
test, który daje wynik pozytywny, zaś osoba ta trafia na kwarantannę. Możesz założyć, że
nie będzie ona od tego momentu uczestniczyć w żadnych kontaktach społecznych (zaś każdy
wykonany jej w przyszłości test oczywiście da również pozytywny wynik).

 - Litera Q oraz liczba całkowita 𝑝 (1 <= 𝑝 <= 𝑛) – zapytanie ministra zdrowia, w którym
wartością startową (patrz sekcja Wyjście) jest 𝑑𝑒𝑐𝑜𝑑𝑒(𝑝).


Sumy liczb 𝑛 oraz 𝑘 we wszystkich zestawach nie przekraczają, odpowiednio, 500 000 oraz
1 000 000. Suma liczb 𝑐 we wszystkich zapytaniach wszystkich zestawów nie przekracza 1 000 000.

## **Wyjście**

Dla każdego zestawu danych wypisz tyle linii, ile było w nim zapytań (zdarzeń typu Q).
Jeżeli w momencie otrzymania 𝑖-tego zapytania da się udowodnić, że nikt oprócz osób
przebywających na kwarantannie nie jest zarażony bajtobakterią, w 𝑖-tej linii wypisz pojedyncze
słowo TAK 2. Po takim zapytaniu, zmienna shift zmienia swoją wartość na 0.

W przeciwnym przypadku, w 𝑖-tej linii wypisz słowo NIE oraz identyfikator jednej osoby. Jeżeli
𝑑𝑒𝑐𝑜𝑑𝑒(𝑝) jest wartością startową tego zapytania, to musisz wypisać identyfikator **pierwszej osoby w ciągu** (𝑑𝑒𝑐𝑜𝑑𝑒(𝑝), 𝑑𝑒𝑐𝑜𝑑𝑒(𝑝) + 1, . . . , 𝑛, 1, 2, . . . , 𝑑𝑒𝑐𝑜𝑑𝑒(𝑝) − 1), która może być
zarażona bajtobakterią, a **nie przebywa na kwarantannie**. Wypisana liczba staje się nową
wartością zmiennej shift.

### **Uwagi**

 - Wartość zmiennej shift nie zmienia się przy wydarzeniach typu K, N oraz P.
 
 - Podane w danych wejściowych pozytywne i negatywne wyniki testów zawsze opisują wiarygodny scenariusz, tj. dla każdego zestawu danych istnieje co najmniej jeden możliwy zbiór osób początkowo zarażonych, dla którego podane dane nie zawierają sprzeczności

### **Przykład:**

#### **Wejście**:

    1
    6 14
    K 3 3 4 5
    K 2 6 5
    N 3
    Q 3
    P 1
    K 2 6 2
    P 6
    Q 4
    P 6
    K 2 1 3
    N 3
    Q 4
    N 2
    Q 1


#### **Wyjście**:

    NIE 5
    NIE 1
    TAK
    TAK

#### **Po zdekodowaniu, powyższy przykład wygląda następująco:**

    1
    6 14
    K 3 3 4 5
    K 2 6 5
    N 3
    Q 3
    P 6
    K 2 5 1
    P 5
    Q 3
    P 1
    K 2 2 4
    N 4
    Q 5
    N 2
    Q 1

___

## **Wyjaśnienie**

 - Przed pierwszym zapytaniem, osoby 3, 4 i 5 spotykają się, następnie osoby 5 i 6
spotykają się, po czym osoba 3 otrzymuje negatywny wynik testu. W momencie otrzymania
pierwszego zapytania, możemy w oparciu o dotychczas zebrane informacje wyprowadzić
następujące wnioski (poczynając od wartości startowej zapytania, czyli 3). Osoba 3 musi
być w tym momencie zdrowa (otrzymała ona właśnie negatywny wynik testu). Osoba 4
również musi być zdrowa (nie mogła ona być chora w momencie pierwszego spotkania, gdyż
zaraziłaby wtedy osoby 3 i 5, co stanowiłoby sprzeczność z uzyskanym później przez osobę
3 negatywnym wynikiem testu; od czasu tego spotkania osoba 4 nie mogła się zaś zarazić).
Osoba 5 może potencjalnie być zarażona (musiała być ona zdrowa w momencie spotkania z
osobami 3 i 4, jednak później spotkała się z osobą 6, której statusu zdrowotnego nie mamy
szans wywnioskować z zebranych informacji). Odpowiedzią dla zapytania jest więc NIE 5,
a zmienna shift przyjmuje wartość 5.

 - Następnie, osoba 6 otrzymuje pozytywny wynik testu, po czym osoby 1 i 5 spotykają się,
później zaś osoba 5 otrzymuje pozytywny wynik testu. W momencie otrzymania drugiego
zapytania, możemy w oparciu o dotychczas zebrane informacje wyprowadzić następujące
wnioski (poczynając od wartości startowej 3). Osoby 3 i 4 nadal muszą być zdrowe.
Osoby 5 i 6 przebywają na kwarantannie. Osoba 1 może być zarażona (co więcej, jesteśmy
nawet w stanie wywnioskować, że osoba 1 musi być w tym momencie zarażona, jednak
rozstrzygnięcie tego nie jest wymagane w zadaniu). Odpowiedzią dla zapytania jest więc
NIE 1, a zmienna shift przyjmuje wartość 1.
 - Następnie, osoba 1 otrzymuje pozytywny wynik testu, po czym osoby 2 i 4 spotykają się,
później zaś osoba 4 otrzymuje negatywny wynik testu. W momencie otrzymania trzeciego
zapytania, możemy w oparciu o dotychczas zebrane informacje wyprowadzić następujące
wnioski (zaczynając od wartości startowej 5). Osoby 5, 6 i 1 przebywają na kwarantannie.
Osoba 2 musi być zdrowa, z uwagi na otrzymany przez osobę 4 negatywny wynik testu.
Osoby 3 i 4 muszą być zdrowe. Odpowiedzią dla zapytania jest więc TAK, ponieważ można
udowodnić, że wszystkie osoby przebywające poza kwarantanną (2, 3 i 4) są zdrowe.
Zmienna shift przyjmuje wartość 0.
 - Po trzecim zapytaniu, osoba 2 otrzymuje negatywny wynik testu. Jak łatwo możesz
zauważyć, ta część wejścia nie ma de facto znaczenia: po pierwszej odpowiedzi TAK, epidemia
jest już opanowana i odpowiedź TAK musi powtarzać się do końca zestawu danych.