# **Zadanie M**: Magiczne trójki

## *Limit czasowy: 20s, limit pamięciowy: 1024 MB*

___

## **Treść**

Siedzisz na egzaminie i zastanawiasz się, jak wyznaczyć medianę ciągu. Najwyższym
wysiłkiem przypominasz sobie, że mediana to element ciągu, który po posortowaniu go
niemalejąco zajmowałby środkową pozycję (jeśli długość ciągu jest parzysta, medianą
jest mniejszy z dwóch środkowych elementów). Egzamin polega na napisaniu pseudokodu
rozwiązania, po czym zasymulowaniu jego działania na przykładowym, podanym przez profesora,
ciągu wejściowym.

Mimo dziur w pamięci kojarzysz, że coś takiego pojawiło się na wykładzie. Niestety, z wykładu
pamiętasz tylko mgliste fragmenty (noce zarwane nad BajtStation i monotonny głos profesora
algorytmiki nie pomagały w skupieniu uwagi). Był jakiś magiczny algorytm... magiczne trójki?
Jakoś dzieli się ten ciąg, wywołuje rekurencyjnie, i potem łączy...?

Na bazie fragmentów, które udało Ci się zapamiętać, wymyśliłaś następujący algorytm:

    funkcja magiczneTrójki(ciąg)
        jeżeli długość ciągu jest nie większa niż 2 to
            zwróć najmniejszą wartość w ciągu
        w przeciwnym razie
            część_1, część_2, część_3 = podzielNaTrzyCzęści(ciąg)
            mediana_i = magiczneTrójki(część_i) dla i = 1, 2, 3
            zwróć medianę ciągu [mediana_1, mediana_2, mediana_3]

gdzie podzielNaTrzyCzęści dzieli ciąg na trzy spójne fragmenty o jak najbardziej zbliżonych
do siebie długościach. Konkretnie, kolejne fragmenty mają długości [s, s, s], [s + 1, s, s]
lub [s + 1, s + 1, s], w zależności od długości ciągu. Na przykład, ciąg [8, 2, 6, 6, 3,
5, 7, 1] podzieli się na [8, 2, 6], [6, 3, 5] i [7, 1].

Dopiero po wyjściu z egzaminu zdałaś sobie sprawę, że Twój algorytm nie jest aż tak
magiczny, bo nie zawsze działa. Może przynajmniej działał poprawnie dla ciągu z zadania, myślisz
z nadzieją... Niestety, Twoja pamięć w tej kwestii jest równie rozmyta co w przypadku samego
algorytmu: wprawdzie pamiętasz prawie wszystkie elementy ciągu profesora, ale niektórych
wartości nie jesteś pewna. Pamiętasz jedynie podane w treści zadania ograniczenie na wielkość
danych: wszystkie liczby w ciągu miały zawierać się w (domkniętym) przedziale [0, 𝑚 − 1].

Oblicz, na ile sposobów można wpisać nieznane Ci liczby tak, aby algorytm magiczneTrójki
dla otrzymanego ciągu zwracał jego prawdziwą medianę (zdefiniowaną powyżej). Ponieważ liczba
ta może być duża, wystarczy jeśli podasz jej resztę z dzielenia przez 10^9 + 7.

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧. Potem kolejno podawane są zestawy
w następującej postaci:

Pierwsza linia zestawu zawiera dwie liczby całkowite 𝑛, 𝑚 (𝑛 ⊗ 1, 1 <= 𝑚 <= 109
), oznaczające
długość ciągu testowego i ograniczenie na wartości jego elementów.

Druga linia zestawu zawiera ciąg testowy opisany przez 𝑛 liczb całkowitych z przedziału
[−1, 𝑚 − 1], gdzie wartości −1 oznaczają elementy o nieznanych wartościach.


## **Wyjście**

Dla każdego zestawu danych wypisz jedną liczbę całkowitą 𝑟 (0 <= 𝑟 < 109 + 7) – odpowiedź
na pytanie z treści zadania.

### **Przykład:**

#### **Wejście**:

    3
    3 10
    -1 -1 3
    4 50
    10 20 -1 40
    5 100
    -1 10 10 -1 20

#### **Wyjście**:

    100
    21
    1979
___

## **Wyjaśnienie**

W pierwszym teście algorytm magiczneTrójki zwraca poprawną medianę niezależnie od
wartości dwóch nieznanych elementów ciągu; odpowiedzią jest więc 102 = 100.

W drugim teście zwraca poprawną medianę tylko jeśli nieznana wartość jest nie większa niż
20, co daje 21 możliwości.

W trzecim teście zwraca niepoprawną medianę jeśli obie nieznane wartości są mniejsze niż
10, lub obie większe, co daje 1002 − (102 + 892
) = 1979 możliwości.