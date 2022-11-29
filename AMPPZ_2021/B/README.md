# **Zadanie B**: Babcia i pierogi

## *Limit czasowy: 15s, limit pamięciowy: 1024 MB*

___

## **Treść**

Babcia Bajtmiła postanowiła urządzić przyjęcie, na którym pochwali się swoimi
najznakomitszymi wyrobami kuchni garmażeryjnej – pierogami. Na przyjęciu będzie 𝑛 stanowisk,
zaś na 𝑖-tym z nich ma się znajdować talerz z dokładnie 𝑝𝑖 pierogami, przy czym wszystkie liczby
pierogów są różne. Zadanie wydawało się przekraczać możliwości jednej starszej pani, ale Bajtmiła
wykonała je błyskawicznie, przygotowując zgodnie z planem 𝑛 talerzy z 𝑝1, 𝑝2, . . . , 𝑝𝑛 pierogami.
Niestety, w pośpiechu pomyliła stanowiska i rozmieściła talerze w zupełnie innej kolejności.

Bajtmiła jest już porządnie zmęczona, a dodatkowo boi się całkiem pogubić w sytuacji. Nie
chce już ruszać samych talerzy, ale może przenosić pierogi z jednego stanowiska na inne tak,
żeby zamieniać wartości miejscami. Dokładniej, może w jednym ruchu wybrać dwa stanowiska,
na których znajduje się odpowiednio 𝑥 i 𝑦 pierogów, po czym przenieść dokładnie |𝑥 − 𝑦| między
nimi tak, aby na pierwszym było teraz 𝑦, a na drugim 𝑥. Każda taka operacja zajmie jej dokładnie
𝐶 + |𝑥 − 𝑦| sekund (𝐶 na znalezienie łyżki, 1 za każdy przeniesiony pieróg).

Przyjęcie już niedługo! Babcia nie pozwoli Ci dotknąć niczego w kuchni, ale jedno możesz
zrobić: wyznacz sekwencję zamian, która naprawi sytuację, w najkrótszym możliwym czasie
sprawiając, żeby na każdym stanowisku znalazła się właściwa liczba pierogów

## **Wejście**

Pierwsza linia wejścia zawiera liczbę zestawów danych 𝑧 (1 <= 𝑧 <= 1 000). Potem kolejno
podawane są zestawy w następującej postaci:

W pierwszej linii zestawu znajdują się dwie liczby całkowite 𝑛 oraz 𝐶 (1 <= 𝑛 <= 200 000,
1 <= 𝐶 <= 10^9
).

Następne 𝑛 linii zestawu zawiera opisy stanowisk. W 𝑖-tej linii podane są dwie liczby całkowite
𝑎𝑖 oraz 𝑝𝑖 (1 <= 𝑎𝑖
, 𝑝𝑖 <= 10^9
), które oznaczają odpowiednio aktualną oraz planowaną liczbę
pierogów na 𝑖-tym stanowisku.

W każdym zestawie liczby 𝑎𝑖 są różne. Wiadomo też, że zbiory {𝑎1, 𝑎2, ..., 𝑎𝑛} i {𝑝1, 𝑝2, ..., 𝑝𝑛}
są takie same.

Suma wartości 𝑛 we wszystkich zestawach nie przekracza 1 000 000.

## **Wyjście**

Dla każdego zestawu danych, w pierwszej linii wypisz dwie liczby całkowite 𝑆 oraz 𝐾 –
odpowiednio sumaryczny czas oraz liczbę operacji w Twoim rozwiązaniu.

Następne 𝐾 linii powinno opisywać kolejne operacje Twojego rozwiązania. W 𝑘-tej linii wypisz
dwie liczby 𝑥𝑘 oraz 𝑦𝑘 oznaczające, że 𝑘-ta operacja polega na przeniesieniu pierogów między
stanowiskami o numerach 𝑥𝑘 oraz 𝑦𝑘. Po wykonaniu wszystkich operacji, dla każdego 1 <= 𝑖 <= 𝑛,
na 𝑖-tym stanowisku musi się znajdować 𝑝𝑖 pierogów.

Jeżeli istnieje więcej niż jedna możliwa sekwencja zamian o sumarycznym koszcie równym 𝑆,
możesz wypisać dowolną z nich.


### **Przykład:**

#### **Wejście**:

    1
    4 2
    2 4
    3 2
    1 1
    4 3

#### **Wyjście**:

    6 2
    2 1
    4 1

___

## **Wyjaśnienie**

Na stanowiskach leżą kolejno 2, 3, 1 i 4 pierogi. Chcemy doprowadzić do sytuacji, w której
będzie to odpowiednio 4, 2, 1 i 3.

W pierwszym ruchu zamieniamy pierogi na stanowisku pierwszym i drugim. Koszt tej zamiany
to stała 𝐶 = 2 oraz różnica |3 − 2| = 1, czyli łącznie 3 sekundy. Po tej zamianie pierogi leżą w
kolejności (3, 2, 1, 4). W drugim ruchu zamieniamy pierogi na pierwszym i ostatnim stanowisku.
Koszt to 2+|4−3|, czyli znowu 3 sekundy. Teraz kolejność to (4, 2, 1, 3), czyli taka, jaką chcieliśmy
uzyskać. Łączny koszt zamian wynosi 6 sekund i jest minimalny możliwy.