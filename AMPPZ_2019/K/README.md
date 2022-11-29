# **Zadanie K**: Duch

## *Limit czasowy: 10s, limit pamięciowy: 512 MB*

___

## **Treść**

Przyjechaliście na AMPPZ, w czasie wolnym chcieliście sobie zwiedzić zamek na Wawelu,
wchodzicie do komnaty...o nie, jesteście zamknięci! Pojawia się Duch i mówi, że wypuści Was
tylko jeśli poprawnie odpowiecie na jego pytania.

Na ścianie w komnacie wisi 𝑛 obrazów. Możemy myśleć o ścianie jako o płaszczyźnie z
kartezjańskim układem współrzędnych, a o obrazach jako o prostokątach o bokach równoległych
do osi. Dla każdego obrazu znacie jego wymiary i wiecie, gdzie się znajduje. W pewnym momencie,
nazwijmy ten moment chwilą 0, Duch zaczyna przemieszczać obrazy. Każdy potencjalnie w innym
kierunku i z inną prędkością, ale wszystkie ruchem jednostajnym prostoliniowym. Jako że jesteście
wyćwiczoną drużyną, dla każdego obrazu momentalnie zauważacie jego wektor prędkości.

Przedstawienie trwa przez jakiś czas, po czym Duch podda Was 𝑞 próbom. W każdej próbie
Duch poda dwie liczby 𝑙 oraz 𝑟 i poprosi, żebyście przypomnieli sobie wszystkie chwile pomiędzy
chwilą 𝑙 a chwilą 𝑟, i zastanowili się, czy w którejś z nich przypadkiem jakiś fragment ściany
nie był przykryty równocześnie przez wszystkie obrazy. Jeśli tak było, to jak duże było pole
powierzchni tego fragmentu? Ponieważ udzielenie odpowiedzi na to pytanie dla wszystkich chwil
𝑡 ∈ [𝑙, 𝑟] trwałoby nieskończenie długo – a tyle czasu nie mają nawet duchy – nasz Duch zadowoli
się, jeśli wykażecie się doskonałą pamięcią i podacie maksimum z wartości tego pola powierzchni
po wszystkich chwilach 𝑡 ∈ [𝑙, 𝑟]. Jeśli chcecie kiedyś wyjść z tej komnaty – lepiej, żebyście się nie
pomylili!


## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 4000). Potem kolejno
podawane są zestawy w następującej postaci:

Pierwsza linia zestawu zawiera liczbę obrazów 𝑛 (1 <= 𝑛 <= 100 000). Każda z kolejnych 𝑛
linii zawiera sześć liczb całkowitych 𝑥1, 𝑦1, 𝑥2, 𝑦2, 𝑣𝑥, 𝑣𝑦 (−1 000 000 <= 𝑥1 < 𝑥2 <= 1 000 000;
−1 000 000 <= 𝑦1 < 𝑦2 <= 1 000 000; −1 000 000 <= 𝑣𝑥, 𝑣𝑦 <= 1 000 000), gdzie (𝑥1, 𝑦1) to współrzędne
lewego dolnego rogu obrazu, (𝑥2, 𝑦2) to współrzędne jego prawego górnego rogu, a (𝑣𝑥, 𝑣𝑦) to
jego wektor prędkości. Formalnie oznacza to, że w chwili 𝑡 lewy dolny róg obrazu znajduje się w
punkcie (𝑥1 + 𝑡𝑣𝑥, 𝑦1 + 𝑡𝑣𝑦), a prawy górny w punkcie (𝑥2 + 𝑡𝑣𝑥, 𝑦2 + 𝑡𝑣𝑦).

Następna linia zestawu zawiera liczbę prób Ducha 𝑞 (1 <= 𝑞 <= 100 000). Każda z kolejnych 𝑞
linii zawiera dwie liczby rzeczywiste 𝑙, 𝑟 (0 <= 𝑙 <= 𝑟 <= 1 000 000), podane z co najwyżej 4 cyframi
po separatorze dziesiętnym i oznaczające, że Duch pyta o domknięty przedział czasowy [𝑙, 𝑟].

Łączna liczba obrazów we wszystkich zestawach danych nie przekracza 1 000 000.

Łączna liczba prób Ducha we wszystkich zestawach danych nie przekracza 1 000 000.

## **Wyjście**

Dla każdej próby w osobnej linii wypisz liczbę rzeczywistą – maksymalne pole, które osiąga
przecięcie wszystkich obrazów w danym przedziale czasowym. Aby odpowiedź została uznana za
poprawną wystarczy, by absolutny lub względny błąd nie przekraczał 10−6
. Innymi słowy, jeśli
Twój algorytm odpowie 𝑎, a poprawna odpowiedź to 𝑏, to wystarczy, by zachodziło |𝑎−𝑏|
max(1,𝑏) <=
10^−6.
Zauważ, że przecięcie może być puste. W takiej sytuacji należy wypisać 0 (±10^−6).

### **Przykład:**

#### **Wejście**:

    2
    2
    0 0 1 1 1 1
    1 1 2 2 -1 -1
    3
    0 0
    0.25 0.25
    0 2
    3
    0 0 1 1 2 2
    0 0 1 1 1 1
    1 1 2 2 -1 -1
    1
    0 2

#### **Wyjście**:

    0.000000000
    0.250000000
    1.000000000
    0.444444444