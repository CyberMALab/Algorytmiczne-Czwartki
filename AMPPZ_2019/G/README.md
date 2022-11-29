# **Zadanie G**: Antykwariat

## *Limit czasowy: 7s, limit pamięciowy: 512 MB*

___

## **Treść**

Przeprowadzka do nowego miasta nigdy nie jest łatwa, a przeprowadzka do Krakowa potrafi
być szczególnie trudna. W tym mieście kultury i nauki nie sposób cieszyć się jakimkolwiek
szacunkiem bez posiadania w swoim lokum biblioteczki słusznych rozmiarów. Rynek nie znosi
próżni, a naprzeciw potrzebom przyjezdnych wychodzi znany krakoski antykwariat Książki Na
Metry.

Egzemplarze na wystawie ustawione są w dłuuuugim rzędzie, w przypadkowej kolejności, a
klient może zamówić dowolny spójny fragment książek, który już następnego dnia zostanie mu
dostarczony pod same drzwi. Ze względów logistycznych antykwariat nie pozwala kompletować
zamówienia z pojedynczych egzemplarzy rozrzuconych w różnych miejscach. Dla większości
klientów już taki wybór to i tak nadmiar luksusu – biorą po prostu pierwszy z brzegu odpowiednio
długi zestaw woluminów. Czasem jednak trafi się Klient Wybredny.

Klient Wybredny przed wizytą dokładnie wymierzył swoje półki i rzecz jasna zależy mu
na tym, żeby wszystkie zamówione książki mieściły się na wysokość, nie mogą być więc zbyt
wysokie. Co więcej, książki nie mogą być też za niskie, żeby nie sprawiały wrażenia, że
znalazły się na półce przez przypadek. Kiedy już Klient Wybredny zlokalizuje kilka fragmentów
wystawy, spełniających w całości jego wymagania, zaczyna dywagować, które obwoluty tworzą
najkorzystniejszy wzór kolorystyczny. Naturalnie, czym większy wybór, tym dłuższe dywagacje.

No właśnie, jak długo to jeszcze potrwa? Wczuj się w rolę zdesperowanego pracownika
krakowskiego antykwariatu w piątkowe popołudnie. Oblicz, ile spójnych fragmentów wystawy
spełnia wymagania poszczególnych Klientów Wybrednych, czyli zawiera wyłącznie książki w
pewnym podanym zakresie wysokości. Będziesz potrzebować szybkiego programu.

Wspominaliśmy już, że książki na wystawie ustawione są w “losowej” kolejności. Formalnie,
ciąg wysokości książek został wygenerowany przy pomocy poniższego programu dla pewnych
wartości parametrów 𝑁 ∈ {1, 2, . . . , 100 000} oraz 𝑀 = 10𝑞
, 𝑞 ∈ {1, 2, . . . , 6}.

    srand48(N + M);
    for (int i = 0; i < N; ++i)
        a[i] = 1 + lrand48() % M;

Do rozwiązania zadania nie jest wymagana znajomość szczegółów działania biblioteki
RAND48. Wystarczy założyć, że funkcja lrand48 zwraca 31-bitowe liczby całkowite nieujemne
“wylosowane” z rozkładu jednostajnego dyskretnego.


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 5). Potem kolejno podawane
są zestawy w następującej postaci:
Pierwsza linia zestawu zawiera liczbę książek 𝑛 oraz liczbę klientów 𝑘 (1 <= 𝑛 <= 200 000,
1 <= 𝑘 <= 500 000).

Druga linia zestawu zawiera 𝑛 liczb całkowitych dodatnich nie większych niż 1 000 000. Są to
wysokości kolejnych książek na wystawie.

Kolejne 𝑘 linii zawiera opisy zapytań. W 𝑖-tej spośród tych linii podane są dwie liczby
całkowite 𝑙𝑖
, ℎ𝑖 (1 <= 𝑙𝑖 <= ℎ𝑖 <= 1 000 000), oznaczające klienta szukającego książek nie niższych
niż 𝑙𝑖 oraz nie wyższych niż ℎ𝑖.

Łączna liczba książek we wszystkich zestawach danych nie przekracza 600 000, zaś łączna
liczba klientów we wszystkich zestawach danych nie przekracza 1 500 000.

## **Wyjście**

Dla każdego klienta wypisz w osobnej linii liczbę niepustych spójnych przedziałów, w których
wysokości wszystkich książek należą do podanego zakresu.

### **Przykład:**

#### **Wejście**:

    2
    10 3
    9 9 3 2 1 9 6 9 1 7
    1 13
    6 6
    2 9
    5 1
    66575 45720 67904 18764 35162
    20000 80000


#### **Wyjście**:

    55
    1
    17
    7